# String Manipulation

string.title() = Capitalizes each initial letter in a word inside the string

string.upper() = Uppercases each word inside the string

string.lower() = Lowercases each word inside the string

.find("word") = Search of a word or character inside a string and returns the index where is located, if you search for a word for example "hello" it would return the index in "h"

"string".format(variable = variable, variable2 = variable 1, variable 1 = variable 2) = Makes code more legible it helps you assign a variable to a string without the need of concatenation ("string" + "string" + "string")

.split("character") = Takes a string and breaks it onto a list, the delimiter will be the character inside the method the character is not included in the list

"character".join(list_variable) = Joins a list into a string, for this method you must first specify the joining character for example " " for a empty space, then inside the method you must call the variable with the list

.strip() = Strip lets you "strip" characters from the corners of a string, if the method is called with no arguments then it strips the empty spaces at the corners of the string, if you call it with an argument, the argument inside the method is stripped from the corners of the string, you can also use concatenated calls of this method (e.g .strip(":").strip()) <- This would strip the ":" first and then the empty spaces