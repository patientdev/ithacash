import os, csv
from datetime import datetime

def CSVify(dict, csvfile):

	cyclos_fieldnames = ['name', 'username', 'email', 'password', 'creationdate', 'broker', 'images', 'address[identifier].name', 'address[identifier].line1', 'address[identifier].line2', 'adress[identifier].neighborhood', 'address[identifier].pobox', 'address[identifier].zip', 'address[identifier].city', 'address[identifier].region', 'address[identifier].country', 'address[identifier].private', 'mobile[identifier].name', 'mobile[identifier].number', 'mobile[identifier].private', 'landline[identifier].name', 'landline[identifier].number', 'landline[identifier].private',]

	cyclos_input = {}
	cyclos_input.fromkeys(cyclos_fieldnames);

	cyclos_input['name'] = dict['company_name']
	cyclos_input['email'] = dict['email']
	cyclos_input['username'] = dict['login_name']
	cyclos_input['creationdate'] = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
	cyclos_input['address[identifier].line1'] = dict['address_1']
	cyclos_input['address[identifier].line2'] = dict['address_2']
	cyclos_input['address[identifier].city'] = dict['city']
	cyclos_input['address[identifier].region'] = dict['state']
	cyclos_input['address[identifier].zip'] = dict['zip_code']
	cyclos_input['mobile[identifier].number'] = dict['mobile_phone']
	cyclos_input['landline[identifier].number'] = dict['landline_phone']

	if not os.path.isfile(csvfile):
		f = open(csvfile, 'a')
		writer = csv.DictWriter(f, fieldnames=cyclos_fieldnames)

		writer.writeheader()

	else:
		f = open(csvfile, 'a')
		writer = csv.DictWriter(f, fieldnames=cyclos_fieldnames)

	rows = {}
	rows.update(cyclos_input.iteritems())

	writer.writerow(rows)
