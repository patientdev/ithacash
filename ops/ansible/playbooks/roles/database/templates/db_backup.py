import os
import datetime
import subprocess
import requests
from requests_oauthlib import OAuth1
import hashlib

if __name__ == "__main__":
    dump_and_encrypt()
    upload_to_egnyte()


def dump_and_encrypt():
    db_name = 'ithacash'
    db_port = '5432'
    db_host = 'localhost'
    db_user = 'ithacash_db_user'
    db_pass = open('/ithacash/staging/ithacash_dev/settings/secrets/PRODUCTION_DB_PASSWORD', 'r').read()

    today = datetime.datetime.now().strftime('%Y_%m_%d')

    output_filename = '/root/ithacash_db_dump_%s.enc' % today

    pg_dump = subprocess.Popen(['pg_dump', '-h', db_host, '-p', db_port, '-U', db_user, db_name], stdout=subprocess.PIPE)
    openssl = subprocess.Popen(['openssl', 'aes-256-cbc', '-pass', 'file:/root/db_enc_pass.txt', '-out', output_filename], stdin=pg_dump.stdout, stdout=subprocess.PIPE)
    openssl.communicate()[0]


def decrypt():
    today = datetime.datetime.now().strftime('%Y_%m_%d')

    input_filename = 'ithacash_db_dump_%s.enc' % today
    output_filename = 'ithacash_db_dump_%s.txt' % today

    subprocess.call(['openssl', 'aes-256-cbc', '-d', '-pass', 'file:/root/db_enc_pass.txt', '-in', input_filename, '-out', output_filename])


def authenticate_egnyte():
    egnyte_api_key = 'rxfzs54zc6zrsxr2e9myxkn7'
    egnyte_user = 'shane@ithacash.com'
    egnyte_pass = 'Igltt4t5!'

    payload = {
        'client_id': egnyte_api_key,
        'username': egnyte_user,
        'password': egnyte_pass,
        'grant_type': 'password'
    }

    r = requests.post('https://ithacash.egnyte.com/puboauth/token', data=payload)
    response = r.json()

    return response['access_token']


def generate_hash():

    today = datetime.datetime.now().strftime('%Y_%m_%d')
    db_backup = open('/root/ithacash_db_dump_%s.enc' % today, 'rb')

    backup_sha512_hash = hashlib.sha512()
    with db_backup as afile:
        buf = afile.read(65536)
        while len(buf) > 0:
            backup_sha512_hash.update(buf)
            buf = afile.read(65536)

    return backup_sha512_hash.hexdigest()


def upload_to_egnyte():

    egnyte_token = authenticate_egnyte()
    backup_hash = generate_hash()
    today = datetime.datetime.now().strftime('%Y_%m_%d')
    filepath = '/IT/Backups/Database/ithacash_db_dump_%s.enc' % today
    backup_file = {'file': open('/root/ithacash_db_dump_%s.enc' % today, 'rb')}

    r = requests.post('https://ithacash.egnyte.com/pubapi/v1/fs-content/Shared%s' % filepath, files=backup_file, headers={'Authorization': 'Bearer %s' % egnyte_token})
    response = r.json()

    if response['checksum'] != backup_hash:
        print "%s: %s" % (datetime.now(), response)

    else:
        os.remove('/root/ithacash_db_dump_%s.enc' % today)
        print "%s: %s" % (datetime.now(), response)
