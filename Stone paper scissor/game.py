import random

def get_random():
    return random.choice(["Stone", "Paper", "Scissors"]).capitalize()

def get_user_choice():
    user_choice=input("Enter your choice (Stone/Paper/Scissors): ").capitalize()
    while user_choice not in ["Stone", "Paper", "Scissors"]:
        user_choice =input(" Invalid choice. Please Re-Enter your choice (Stone/Paper/Scissors): ").capitalize()
    return user_choice


def  get_result(user_choice, computer_choice):
    if user_choice==computer_choice:
        return "It's a tie"
    elif (user_choice=="Stone" and computer_choice=="Scissors") or \
         (user_choice=="Paper" and computer_choice=="Stone") or\
         (user_choice=="Scissors" and computer_choice=="Paper"):
        return  "You win"
    else:
        return "Computer wins"

def get_score(result,user_score,computer_score):
    
    if result=="You win":
        user_score +=1    
    elif result=="Computer wins":
        computer_score +=1
    print(f"Your Score: {user_score}")
    print(f"Computer Score: {computer_score}")
    return user_score,computer_score

def game():
    user_score = 0
    computer_score=0    
    print("Welcome to Stone Paper Scissors Game")    
    while user_score<10 and computer_score<10:
        
        user_choice=get_user_choice()
        print(f"User Choice: {user_choice}")
        computer_choice= get_random()
        print(f"Computer choose: {computer_choice}")
        result=get_result(user_choice,computer_choice)
        user_score , computer_score = get_score(result,user_score,computer_score)
        print(result)

    # Option to play again or quit
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
    else:
        game()

if __name__ == "__main__":
    game()


