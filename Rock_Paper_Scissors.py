from os import error
import random

user_score=0
computer_score=0
name=input("\nEnter Your Name: ")
while True:
    chc=['rock','paper','scissor']
    computer_choice=random.choice(chc)
    user_choice=input("\nEnter rock, paper, or scissors (or 'exit' to quit): ".lower())
    if user_choice=='exit':
        break
    if user_choice not in ['rock','paper','scissor']:
        error("\nInvalid Input")
        continue
    if computer_choice==user_choice:
        print("\nTie")
    elif(user_choice == 'rock' and computer_choice == 'scissors') or \
        (user_choice == 'scissors' and computer_choice == 'paper') or \
        (user_choice == 'paper' and computer_choice == 'rock'):
        print("%sYou Win.."%name)
        user_score+=1
    else:
        print("Computer Win...")
        computer_score+=1
    print("\nScore -%s : %d, Computer: %d"%(name,user_score,computer_score))
    play_again = input("\nDo you want to play another round? (y/n): ").lower()
    if play_again != 'y':
        break
print("\nThanks for playing! %s Final Score - %s: %d, Computer: %d"%(name,name,user_score,computer_score))        
