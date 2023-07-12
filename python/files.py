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