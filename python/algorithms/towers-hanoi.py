from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks

stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks = [
  left_stack,
  middle_stack,
  right_stack
]

#Set up the Game

num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3\n"))

for disk in range(num_disks, 0 , -1):
  left_stack.push(disk)

num_optimal_moves = (2**num_disks) - 1
print(f"\nThe fastest you can solve this game is in {num_optimal_moves} moves")

#Get User Input

def get_input():
  choices = [letter.get_name()[0] for letter in stacks]

  while True:
    for i in range(len(stacks)):
      print(f"Enter {choices[i]} for {stacks[i].get_name()}")
    user_input = input("")
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]


#Play the Game

num_user_moves = 0

while right_stack.get_size() != num_disks:
  print("\n\n\n...Current Stacks...")
  for stack in stacks:
    stack.print_items()
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    if from_stack.is_empty():
      print("\n\nThe stack you're retrieving the disk from is empty")
    elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print("\n\nInvalid move. Try again (idk what happened)")
  
print(f"\n\nYou completed the game in {num_user_moves} moves, and the optimal number of moves is {num_optimal_moves}")