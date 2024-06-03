"""Module docstring"""


# imports
# CONSTANTS

def score_menu():
    print("Welcome to the Score program!")
    score = get_valid_score()
    while True:
     Print(("\nMenu:"))
     Print("(G)et a valid score")
     print("(P)rint result")
     print("(S)how stars")
     print("(Q)uit")
     choice = input("Choose an option: ").upper()
     if choice == 'G'
         score= get_vaild_score
     elif choice =='P'
         result = evaluate_score(score)
         print(f"Result: {result}")
     elif choice == 'S'
          show_stars(score)
     elif choice == 'Q':
            print("Farewell!")
            break
        else:
            print("Invalid choice. Please try again.")

            def get_valid_score():
                while True:
                    try:
                        score = float(input("Enter a valid score (0-100): "))
                        if 0 <= score <= 100:
                            return score
                        else:
                            print("Score must be between 0 and 100. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

            def evaluate_score(score):
                if score < 0 or score > 100:
                    return "Invalid score"
                elif score >= 90:
                    return "Excellent"
                elif score >= 50:
                    return "Passable"
                else:
                    return "Bad"

            def show_stars(score):
                print('*' * int(score))
