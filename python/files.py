# We can open files with python using the open() function

with open("welcome.txt") as text_file:
  text_data = text_file.read() # Use .read() to access the contents of the file

print(text_data)

# The .read(file, mode) method default second argument is "r" (read mode)

# .read() reads all the content in the document, to read by line we can use
# .readlines()

with open("how_many_lines.txt") as lines_doc:
  for line in lines_doc.readlines():
    print(line)

with open("just_the_first.txt") as first_line_doc:
  first_line = first_line_doc.readline()

print(first_line)

# We can write in a document using .write() and declaring the mode in read()

with open("bad_bands.txt", "w") as bad_bands_doc:
  bad_bands_doc.write("Music from TikTok sucks")

# We can also append text to the file using "append" mode, just adding "a" in open()

with open("cool_dogs.txt", "a") as cool_dogs_file:
  cool_dogs_file.write("Air Buddy\n") # Append mode appends the text for everytime the code is ran

# Files in python are external, so we use "with" to open and then close the file once we use it

with open('fun_file.txt') as close_this_file:
  setup = close_this_file.readline()
  punchline = close_this_file.readline() # file is closed once this is executed

# We can also read csv files

with open("logger.csv") as log_csv_file:
  print(log_csv_file.read())

# The best way to read csv files and accesing the data is using csv package

import csv

with open("cool_csv.csv") as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for row in cool_csv_dict:
    value = list(row.values())
    name = value[0]
    fact = value[2]
    print("Cool fact about {} is: {}".format(name, fact))

'''Fun fact, a csv file doesn't mean it's separated by a comma
it can be separated by diferent delimiters'''

import csv
 
with open('addresses.csv', newline='') as addresses_csv: # newLine is used in case there are \n characters
  address_reader = csv.DictReader(addresses_csv, delimiter=';') # delimiter is used to specify the delimiter on the file
  for row in address_reader:
    print(row['Address'])

import csv

with open("books.csv") as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter="@")
  isbn_list = [book.get("ISBN") for book in books_reader]

# We can also write new csv files programatically

access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

import csv

with open("logger.csv", "w") as logger_csv:
  log_writer = csv.DictWriter(logger_csv, fieldnames = fields)
  log_writer.writeheader()
  for item in access_log:
    log_writer.writerow(item)
  
# We can also open JSON files

import json

with open("message.json") as message_json:
  message = json.load(message_json)

print(message['text'])

# To write a json file we can do the following

data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

with open('data.json', 'w') as data_json:
   json.dump(data_payload, data_json)