"""Module docstring"""


# imports
# CONSTANTS

def score():
    score = float(input("Enter score:"))
    result = evaluate_score(score)
    print(result)

    random_score = random.uniform(0, 100)
    random_result = evaluate_score(random_score)
    print(f"Random score: {random_score:.2f} - {random_result}")

def evaluate_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"



