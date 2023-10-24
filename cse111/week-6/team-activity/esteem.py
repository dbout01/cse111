# Author - Dylan Butterfield, CSE111, 3:15PM Class

def main():
    print("""This program is an implementation of the Rosenberg")
    Self-Esteem Scale. This program will show you ten") statements that you could possibly apply to yourself.")
    Please rate how much you agree with each of the") statements by responding with one of these four letters

    D means you strongly disagree with the statement.
    d means you disagree with the statement.
    a means you agree with the statement.
    A means you strongly agree with the statement.""")

    #Ask all questions
    score = 0
    score += positive_question("1. I feel that I am a person of worth, at least on an equal plane with others.")
    score += positive_question("2. I feel that I have a number of good qualities.")
    score += negative_question("3. All in all, I am inclined to feel that I am a failure.")
    score += positive_question("4. I am able to do things as well as most other people.")
    score += negative_question("5. I feel I do not have much to be proud of.")
    score += positive_question("6. I take a positive attitude toward myself.")
    score += positive_question("7. On the whole, I am satisfied with myself.")
    score += negative_question("8. I wish I could have more respect for myself.")
    score += negative_question("9. I certainly feel useless at times.")
    score += negative_question("10. At times I think I am no good at all.")
    #Tell the user their score
    print()
    print(f"Your score is {score}.")
    print("A score below 15 may indicate problematic low self-esteem.")


#Display one statement & determine score for response & return (print)
def positive_question(question):
    """
    Parameters
        statement: The statement to show the user.
        pos_or_neg: Either the constant POSITIVE or NEGATIVE.
    Return: the score from the user's response to the statement.
    """
    print(question)
    answer = input("Enter D, d, a, or A: ")
    score = 0
    if answer == 'D':
        score = 0
    elif answer == 'd':
        score = 1
    elif answer == 'a':
        score = 2
    elif answer == 'A'.upper():
        score = 3
    return score

#Display one statement & get user's response & determine score for response & return (print)
def negative_question(question):
    """
    Parameters
        statement: The statement to show the user.
        pos_or_neg: Either the constant POSITIVE or NEGATIVE.
    Return: the score from the user's response to the statement.
    """
    print(question)
    answer = input("   Enter D, d, a, or A: ")
    score = 0
    if answer == 'D':
        score = 3
    elif answer == 'd':
        score = 2
    elif answer == 'a':
        score = 1
    elif answer == 'A'.upper():
        score = 0
    return score


# Executes file
if __name__ == "__main__":
    main()
