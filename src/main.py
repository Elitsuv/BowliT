import random

def toss():
    print("Welcome to Bowl-it. Would you like to toss? (Y/N): ")
    response = input("Please enter: ").capitalize()

    if response == "Y" or "Yes":
        print("Let's toss!")
        
        user_choice = input("Choose Heads or Tails: ").capitalize()
        while user_choice not in ["Heads", "Tails"]:
            print("Invalid input. Please enter 'Heads' or 'Tails'.")
            user_choice = input("Choose Heads or Tails: ").capitalize()

        user_number = int(input("Choose a number between 1 and 6: "))
        robot_number = random.randint(1, 6)
        
        total = user_number + robot_number
        results = "Heads" if total % 2 != 0 else "Tails"
        print(f"The sum of numbers is: {total} ({'Odd' if total % 2 != 0 else 'Even'})")
        print(f"The toss result is: {results}")

        if user_choice == results:
            print("You win the toss!")
            return "user"
        else:
            print("Robot wins the toss!")
            return "robot"
    elif response == "N" or "no":
        print("Robot will toss.")
        robot_choice = random.choice(["Heads", "Tails"])
        print(f"Robot chose {robot_choice}")

        robot_number = random.randint(1, 6)
        user_number = int(input("Choose a number between 1 and 6: "))
        
        total = user_number + robot_number
        results = "Heads" if total % 2 != 0 else "Tails"
        print(f"The sum of numbers is: {total} ({'Odd' if total % 2 != 0 else 'Even'})")
        print(f"The toss result is: {results}")

        if robot_choice == results:
            print("Robot wins the toss!")
            return "robot"
        else:
            print("You win the toss!")
            return "user"
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")

def batting_innings(player, opponent):
    score = 0
    wickets = 0
    
    print(f"\n{player} is batting!")
    while wickets < 3:
        print(f"\n{player}'s Score: {score}, Wickets: {wickets}")
        
        user_run = int(input("Enter your run (0-6): "))
        while user_run < 0 or user_run > 6:
            print("Invalid input. Please enter a number between 0 and 6.")
            user_run = int(input("Enter your run (0-6): "))
        
        robot_run = random.randint(0, 6)
        print(f"{opponent} bowled {robot_run}")
        
        if user_run == robot_run:
            print("Out! Wicket fallen!")
            wickets += 1
        else:
            score += user_run
            print(f"{player} scored {user_run} runs!")
    
    print(f"{player}'s innings ended. Score: {score}, Wickets: {wickets}")
    return score

def bowling_innings(player, opponent):
    score = 0
    wickets = 0
    
    print(f"\n{player} is bowling!")
    while wickets < 3:
        print(f"\n{player}'s Bowling: Runs: {score}, Wickets: {wickets}")
        
        robot_run = random.randint(0, 6)
        print(f"{opponent} chose to play {robot_run}")
        score += robot_run
        
        user_run = int(input("Enter your run (0-6) to bowl out the batsman: "))
        while user_run < 0 or user_run > 6:
            print("Invalid input. Please enter a number between 0 and 6.")
            user_run = int(input("Enter your run (0-6) to bowl out the batsman: "))
        
        if robot_run == user_run:
            print("Wicket taken!")
            wickets += 1
    
    print(f"{player}'s bowling ended. Runs: {score}, Wickets: {wickets}")
    return score

def play_game():
    toss_winner = toss()
    
    if toss_winner == "user":
        choice = input("Do you want to Bat or Bowl (B/B): ").upper()
        while choice not in ["B", "B"]:
            print("Invalid choice. Please enter 'B' or 'B'.")
            choice = input("Do you want to Bat or Bowl (B/BB): ").upper()
        
        if choice == "B":
            user_score = batting_innings("You", "Robot")
            robot_score = bowling_innings("You", "Robot")
        else:
            user_score = bowling_innings("You", "Robot")
            robot_score = batting_innings("Robot", "You")
    else:
        print("Robot won the toss and chooses to Bat.")
        robot_score = batting_innings("Robot", "You")
        user_score = bowling_innings("You", "Robot")
    
    if user_score > robot_score:
        print(f"You win the match! Your score: {user_score}, Robot's score: {robot_score}")
    else:
        print(f"Robot wins the match! Robot's score: {robot_score}, Your score: {user_score}")

play_game()