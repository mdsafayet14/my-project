import random
import time


def ask_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2

    question = f"{num1} {operator} {num2}"
    return question, correct_answer


def play_game():
    score = 0
    total_questions = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be asked 5 random math questions.\n")

    for i in range(total_questions):
        question, answer = ask_question()
        print(f"Q{i+1}: What is {question}?")
        while True:
            try:
                user_input = int(input("Your answer: "))
                break
            except ValueError:
                print("❌ Please enter a valid number!")

        if user_input == answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer was {answer}\n")

        time.sleep(1)

    print("Quiz Over!")
    print(f"Your final score is {score} out of {total_questions}.\n")


if __name__ == "__main__":
    play_game()
