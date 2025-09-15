import random
import time
import json

def main():
	scores=load_score()
	print(f"Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou have 5 chances to guess the correct number.")
	print(f"\n")
	
	while True:
		print(f"🏁The scores are:🏁")
		for level,score in scores.items():
			if score is None:
				score="Not yet"
			print(f"{level} : {score}")
		chances=0
		print(f"\nPlease select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)")
		print(f"\n")
		option=input("Enter your choice:")
		print(f"\n")
		if option=="1":
			level_name="Easy"
			chances=10
		elif option=="2":
			level_name="Medium"
			chances=5
		elif option=="3":
			level_name="Hard"
			chances=3
		else:
			print(f"Invalid Input")
			continue
		print(f"Great! You have selected the {level_name} difficulty level.\nLet's start the game!")
		print(f"\n")
		
		found_number=False
		attemps=0
		computer_choice=random.randrange(1,100)
		
		start=time.time()
		while found_number==False and chances>0:
			try:
				user_input=input("Enter your guess:")
				if user_input in ["hint","h"]:
					print( get_hint(computer_choice))
					continue
				elif user_input in ["quit","q"]:
					print("👍🏻Thank you for your participation.Good Bye!! 👍🏻")
					return
				user_guessing=int(user_input)
			except ValueError:
				print("Please enter a valid number or 'hint' ")
				continue
			if user_guessing>computer_choice:
				attemps=attemps+1
				chances=chances-1
				print(f"Incorrect! The number is less than {user_guessing}.")
			elif user_guessing<computer_choice:
				attemps=attemps+1
				chances=chances-1
				print(f"Incorrect! The number is greater than {user_guessing}.")
			else:
				attemps=attemps+1
				found_number=True
				
		end=time.time()
		timer=round(end-start,2)
		if found_number==True:
			print(f"\n")
			print(f"Congratulations! You guessed the correct number in {attemps} attempts in {timer} seconds.")
			if scores[level_name] is None or attemps<scores[level_name]:
				print(f"New high score for {level_name}")
				scores[level_name]=attemps
				save_score(scores)
		else:
			print(f"\n")
			print(f"Sorry, you lost ! The number was: {computer_choice}")
			print(f"\n")
			
				
		continu=input("Do you want to continue? (y/n): ").lower()
		if continu=="yes" or continu=="y":
			continue
		elif continu=="no" or continu=="n":
			print(f"👍🏻Thank you for your participation.Good Bye!! 👍🏻")
			break

#Build get_hint function 
def get_hint(secret_number):
	hint_type=random.choice(["parity","divisibility_3","divisibility_5","range"])
	if hint_type=="parity":
		return "Even number" if secret_number %2==0 else "Odd number"
	elif hint_type=="divisibility_3":
		return "divisible by 3" if secret_number %3==0 else "Not divisible by 3"
	elif hint_type=="divisibility_5":
		return "divisible by 5" if secret_number %5==0 else "Not divisible by 5"
	elif hint_type=="range":
		low=max(1,secret_number-10)
		high=min(100,secret_number+10)
		return f"The number is between {low} and {high}"

#Manage scores
#load the score
def load_score():
	try:
		with open("scores.json","r") as file:
			scores=json.load(file)
			return scores
	except (FileNotFoundError,json.JSONDecodeError):
		scores={"Easy":None,"Medium":None,"Hard":None}
		return scores
#save the score
def save_score(scores):
	with open("scores.json","w") as file:
		json.dump(scores,file)
if __name__=="__main__":
	main()	