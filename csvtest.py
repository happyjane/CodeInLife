import csv
with open('eggs.csv', 'wb') as csvfile:
    #spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter = csv.writer(csvfile, dialect='excel')
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
