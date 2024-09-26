#Dave.py
import os

def clear():
    if os.name == 'nt':  
        os.system('cls')
    else:
        os.system('clear')

print("----------------------")
print("Welcome to Quiz Game!")
print("----------------------")

while True:

    quiz = input("Are you ready? (y/n): ")

    if quiz.lower() == 'n' or quiz.lower() == 'no':
        print("----------------------")
        print("Bye bye bye")
        print("----------------------")
        quit()
    elif quiz.lower() == 'y' or quiz.lower() == 'yes':
        clear()
        print("----------------------")
        print("      Quiz Game!")
        print("----------------------")
    else:
        print("----------------------")
        print("Invalid input!")
        print("----------------------")
        quit()
#Question
    question = {
        "1. Who developed Python programming language?: ": "guido van rossum",
        "2. Who developed in HTML?: ": "tim berners lee",
        "3. Who developed C programming language?: ": "rennis ritchie",
        "4. Who developed C++ programming language?: ": "bjarne stroustrup",
        "5. Who developed in javascript?: ": "brendan eich"
    }
#Question
    score = 0

    for question, correct_answer in question.items():
        answer = input(question).lower()

        if answer == correct_answer:
            print("----------------------")
            print("Your Answer is Correct!")
            print("----------------------")
            score += 10
        else:
            print("----------------------")
            print(f"Wrong! (Answer is: {correct_answer})")
            print("----------------------")

    print("----------------------")
    print("Quiz Score:", score)
    print("----------------------")
    quit()
#Dave.py