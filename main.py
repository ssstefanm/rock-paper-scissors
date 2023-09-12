import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
x = random.randint(0, 2)
y = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
values = [rock, paper, scissors]
if y == 0 :
  print (rock)
  print("Computer Chose: ")
  print(values[x])
  if x == 1:
    print("you lose")
  else:
    print("you win")
elif y == 1 :
  print (paper)
  print("Computer Chose: ")
  print(values[x])
  if x == 2:
    print("you lose")
  else:
    print("you win")
elif y == 2:
  print (scissors)
  print("Computer Chose: ")
  print(values[x])
  if x == 0:
    print("you lose")
  else:
    print("you win")
else:
    print("Invalid input. Please choose 0 for Rock, 1 for Paper, or 2 for Scissors.")
