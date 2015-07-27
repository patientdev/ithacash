import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'PRODUCTION_DB_PASSWORD'), 'r') as password_file:
    PRODUCTION_DATABASE_PASSWORD = password_file.read()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8*y7hv3wq()sdas$$&0CCyhr4tn*^&5asd06ASD)FHi234wuv[]|77856'
MANDRILL_API_KEY = 'ly2C9WtldCUoGnSY3IvfnQ'
