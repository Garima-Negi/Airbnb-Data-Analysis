from __future__ import unicode_literals
from langdetect import detect
import csv

#This snippet is used to remove newline characters 
file_open = open('/Users/arjun/Downloads/AirBnb/Test/reviews_Boston.csv','w')
writer = csv.writer(file_open, delimiter=',', quoting=csv.QUOTE_MINIMAL)
with open('/Users/arjun/Downloads/AirBnb/Test/reviews.csv', 'rU',encoding='latin1') as myfile:
    filtered = (line.replace('\r', '').replace('\n','') for line in myfile)
    for row in csv.reader(filtered):
        writer.writerow(row)

file_open = open('/Users/arjun/Zeppelin/AirBnb/Test/listings_filtered_Boston.csv','w')
writer_price = csv.writer(file_open, delimiter=',')
with open('/Users/arjun/Zeppelin/AirBnb/Test/listings_Boston.csv', 'rU',encoding='latin-1') as myfile:
    reader = csv.reader(myfile)
    for row in reader:
        try:
            if row[6] == '':
                row[6] = 0
            writer.writerow(row)
        except Exception as e:
            print(e)
            pass

file_open = open('/Users/arjun/Downloads/AirBnb/Test/reviews_filtered_Boston.csv','w')
writer_lang = csv.writer(file_open, delimiter=',')
with open('/Users/arjun/Downloads/AirBnb/Test/reviews_Boston.csv', 'r',encoding='latin-1') as myfile:
    reader = csv.reader(myfile)
    for row in reader:
        try:
            lang = detect(row[5])
            if lang=='en':
                writer.writerow(row)
        except Exception as e:
            print(e)
            pass
