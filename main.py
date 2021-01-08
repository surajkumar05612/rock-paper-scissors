ock = '''
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
import random
print("Welcome to rock, paper & Scissors Game! ")
print("**************")
print("**************")

user_choice = int(input("Select your turn.... Type '1' for rock, '2' for paper, '3' for scissors  "))

if user_choice == 1:
  print(f"you choosed: Rock {rock}")
elif user_choice == 2:
  print(f"you choosed: Paper {paper}")
else:
  print(f"you choosed: Scissors {scissors}")

computer_choice = random.randint(1,3)

if computer_choice == 1:
  print(f"Computer choosed: Rock {rock}")
elif computer_choice == 2:
  print(f"Computer choosed: Paper {paper}")
else:
  print(f"Computer choosed: Scissors {scissors}")

if user_choice > 3 or user_choice < 1: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 1 and computer_choice == 3:
  print("You win!")
elif computer_choice == 1 and user_choice == 3:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")