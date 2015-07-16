import os, csv

def CSVify(dict, csvfile):
	
	fieldnames = []

	for key in dict.keys():
		fieldnames.append(key)
	
	if not os.path.isfile(csvfile):
		f = open(csvfile, 'a')
		writer = csv.DictWriter(f, fieldnames=fieldnames)

		writer.writeheader()

	else:
		f = open(csvfile, 'a')
		writer = csv.DictWriter(f, fieldnames=fieldnames)

	rows = {}
	rows.update(dict.iteritems())

	writer.writerow(rows)