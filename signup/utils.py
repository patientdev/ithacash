import os, csv
from datetime import datetime

def CyclosCSV(inputs, csvfile):

	cyclos_fieldnames = ['name', 'username', 'email', 'password', 'creationdate', 'broker', 'images', 'address[identifier].name', 'address[identifier].line1', 'address[identifier].line2', 'adress[identifier].neighborhood', 'address[identifier].pobox', 'address[identifier].zip', 'address[identifier].city', 'address[identifier].region', 'address[identifier].country', 'address[identifier].private', 'mobile[identifier].name', 'mobile[identifier].number', 'mobile[identifier].private', 'landline[identifier].name', 'landline[identifier].number', 'landline[identifier].private',]

	# Create dict for Cyclos CSV and populate headings
	cyclos_input = {}
	cyclos_input.fromkeys(cyclos_fieldnames);

	# Map form input names to required Cyclos headings
	cyclos_input['name'] = inputs['company_name']
	cyclos_input['email'] = inputs['email']
	cyclos_input['username'] = inputs['login_name']
	cyclos_input['creationdate'] = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
	cyclos_input['address[identifier].line1'] = inputs['address_1']
	cyclos_input['address[identifier].line2'] = inputs['address_2']
	cyclos_input['address[identifier].city'] = inputs['city']
	cyclos_input['address[identifier].region'] = inputs['state']
	cyclos_input['address[identifier].zip'] = inputs['zip_code']
	cyclos_input['mobile[identifier].number'] = inputs['mobile_phone']
	cyclos_input['landline[identifier].number'] = inputs['landline_phone']

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

def IthacashCSV(inputs, csvfile):

	fieldnames = []

	# Let's keep the last 4 digits of the TIN in plain text
	inputs['tin_last_4'] = inputs['tin'][-4:]

	# Don't put the full TIN in at all
	inputs.pop('tin', None)

	for key in inputs.keys():
		fieldnames.append(key)

	if not os.path.isfile(csvfile):
		f = open(csvfile, 'a')
		writer = csv.DictWriter(f, fieldnames=fieldnames)

		writer.writeheader()

	else:
		f = open(csvfile, 'a')
		writer = csv.DictWriter(f, fieldnames=fieldnames)

	rows = {}
	rows.update(inputs.iteritems())

	writer.writerow(rows)
