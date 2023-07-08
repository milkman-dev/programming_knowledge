# Takes a list of numbers named nums as a parameter and returns the count of how many numbers in the list are divisible by 10
def divisible_by_ten(num):
  count = 0
  for number in num:
    if number % 10 == 0:
      count += 1
  return count

print(divisible_by_ten([20, 25, 30, 35, 40]))

# Takes a list of strings named names as a parameter and returns a new list containing the greetings
def add_greetings(names):
  greet = ["Hello, {}".format(name) for name in names]
  return greet

print(add_greetings(["Owen", "Max", "Sophie"]))

# I dont even know what i wanted to do, but it deletes the first elements until a odd number is found
def delete_starting_evens(my_list):
  index = 0
  while index < len(my_list) and my_list[index] % 2 == 0:
    my_list.pop(index)
  return my_list

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

# Creates a new list w/ every element from my_list that has an odd index
def odd_indices(my_list):
  new_list = [num for num in my_list if my_list.index(num) % 2 != 0]
  return new_list

print(odd_indices([4, 3, 7, 10, 11, -2]))

# Takes two lists as parameters named bases and powers and returns a new list containing every number in bases raised to every number in powers
def exponents(bases, powers):
  return [base ** power for base in bases for power in powers]

print(exponents([2, 3, 4], [1, 2, 3]))