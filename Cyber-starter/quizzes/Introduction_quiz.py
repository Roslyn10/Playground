#!/usr/bin/python3
# Questions, options, answers for the quiz
questions = (
    "What is the internet?",
    "What is the main difference between the internet and the World Wide Web?",
    "What are the different types of internet connections?",
    "What is an IP address?",
    "What is a server used for?"
)
options = (
    ("A. A global network of computers", "B. A website that contains information", "C. The World Wide Web", "D. A collection of websites we want to view"),
    ("A. The internet is a global network that connects computers, and the web is a collection of information accessed through this network", 
     "B. The World Wide Web is the internet itself"),
    ("A. Dial-up", "B. DSL", "C. Cable", "D. Fiber", "E. Cellular"),
    ("A. A unique identifier for a device connected to the internet", "B. A number used by websites to store data", 
     "C. The location of a computer's data on the internet", "D. A code that encrypts information on the web"),
    ("A. To store and deliver data (like websites) to users on the internet", "B. To access the World Wide Web", 
     "C. To control the entire internet", "D. To store users' personal information")
)
answers = ("A", "A", "A, B, C, D", "A", "A")
guesses = []
score = 0
for question_num in range(len(questions)):
    print("----------------------")
    print(questions[question_num])
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!! :)")
    else:
        print("INCORRECT!! :(")
        print(f"{answers[question_num]} is the correct answer")
print(f"Your final score is {score}/{len(questions)}")
