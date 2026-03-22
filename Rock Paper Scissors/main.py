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
#Store images into array
game_display = [rock, paper, scissors]

#Player logic. Get input and return images.
playerChoice = int(input("What do you choose?\nType 0 for Rock, type 1 for Paper, or type 2 for Scissors\n"))
#Win and lose conditions
if playerChoice >= 3 or playerChoice < 0:
    print("You typed an invalid number, you lose!")
    print(game_display[playerChoice])
else:
    #Computer logic. Generate random numbers 0-2. Then return images.
    computerChoice = random.randint(0, 2)
    print("Computer chose: ")
    print(game_display[computerChoice])



if playerChoice == 0 and computerChoice == 2:
     print("You Win!")
elif computerChoice > playerChoice:
    print("You Lose!")
elif computerChoice == 0 and playerChoice == 2:
    print("You lose!")
elif playerChoice > computerChoice:
     print("You Win!")
elif computerChoice == playerChoice:
     print("Stalemate!")
