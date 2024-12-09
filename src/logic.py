import random

def toss():
    print("Welcome to bowl-it. Would you like to toss? (Y/N): ")
    response = input("Please enter: ").capitalize()
    if response == "Y":
        print("Let's toss!")

        user_choice = input("Choose Heads or Tails: ").capitalize()

        while True:
            try:
                user_number = int(input("Choose a number between 1 and 6: "))
                if 1 <= user_number <= 6:
                    break
                else:
                    print("Please enter a number between 1 and 6.")
            except ValueError:
                print("Invalid input. Enter a valid number between 1 and 6.")

        robot_number = random.randint(1, 6)
        print(f"Robot chose: {robot_number}")

        total = user_number + robot_number
        toss_result = "Heads" if total % 2 != 0 else "Tails"
        print(f"The sum of numbers is: {total} ({'Odd' if total % 2 != 0 else 'Even'})")
        print(f"The toss result is: {toss_result}")

        if user_choice == toss_result:
            print("You win the toss!")
        else:
            print("Robot wins the toss!")
    else:
        print(":(")

toss()
