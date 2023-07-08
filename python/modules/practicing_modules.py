# Normal import specifing the functions to import
from datetime import datetime
# Aliased import
from datetime import datetime as dtm
# Normal plain import
import random
# Importing a owned file
from python.strings.practice import color_count

current_time = datetime.now()
numbers_b = random.sample(range(1000), 12)

print(current_time)
print(numbers_b)

colors = ['red', 'blue', 'green']

print(colors.countcolor('red'))