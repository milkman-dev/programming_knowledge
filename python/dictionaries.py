''' Dictionaries are like lists but for each item
there is a key and a value, keys can only be unhashable
and values can be any data type'''

# Declaring an empty dictionary

new_dictionary = {}

# Dictionary with item (String) and value (String)

new_dictionary = {"item": "value"}

# Dictionary with different data type as a value

new_dictionary = {"item": {"new_item": "new_value"}}
new_dictionary = {"item": [1, 2, 3, 4, 5]}

# Add a single item to a dictionary

new_dictionary["new_item"] = "new_value"

# Add multiple items to a dictionary

new_dictionary.update({"item1": "value1", "item2": "value2", "item3": "value3"})

# Overwrite an item value

new_dictionary["item"] = "new_value"

inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20}
 
inventory["invisible knife"] = 40
inventory["mithril shield"] = 25

# Just as list comprehensions there are dictionary comprehensions (Cool!)

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)

drinks_to_caffeine = {item: value for item, value in zipped_drinks}
drinks_to_caffeine = {drinks[item]: caffeine[item] for item in range(len(drinks))}
drinks_to_caffeine = {item: value for item, value in zip(drinks, caffeine)}

# Practicing how Spotify may work with dict:

# ---

# 2 Lists

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# Make a dict with dict comprehension

plays = {item: value for item, value in zip(songs, playcounts)}

# o.o

print(plays)

# Add new song

plays["Purple Haze"] = 1

# I listened to more songs from Aretha Franklin

plays["Respect"] = 94

# New dict

library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library)

# ---

# Access values by key in a dict

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements["earth"])
print(zodiac_elements["fire"])

# .get() method dict.get(key, default_value(if not found))

print(".get() example")

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)

print(tc_id)

print(user_ids.get("superStackSmash", 100000))

# Removing items from a dict using .pop(item, default value(if not exist))
# and adding that item value to a variable, if not exist add default value

print(".pop() example")

vailable_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}

health_points = 20

health_points += available_items.pop("stamina grains", 0)

health_points += available_items.pop("power stew", 0)

health_points += available_items.pop("mystic bread", 0)

print(available_items, health_points)

# .keys() method worksd to give the keys of a dictionary

print(".keys() example")

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()

print(users)
print(lessons)

# .values() method works to give the values of a dictionary