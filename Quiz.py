# Python Quize Game

# questions= ("which is your favourite color: ",
#             "which is your favourite food: ",
#             "which is your favourite subject: ",
#             "which is your favourite fruit: ",
#             "which is your favourite place: ")

# Questions and options for the quiz
questions = (
    "How many continents are there on Earth?",
    "Who was the first man to walk on the Moon?",
    "Which is the only mammal that lays eggs?",
    "How many zeroes are there in 1 million?",
    "Who is the richest person in the world?"
)

options = (
    ("A. 20", "B. 10", "C. 15", "D. 7"),
    ("A. Neil Armstrong", "B. Barack Obama", "C. George Bush", "D. George Washington"),
    ("A. Bat", "B. Kangaroo", "C. Dolphin", "D. Platypus"),
    ("A. 6", "B. 5", "C. 4", "D. 7"),
    ("A. Mark Zuckerberg", "B. Bill Gates", "C. Elon Musk", "D. Jeff Bezos")
)

answers = ("D", "A", "D", "A", "C")

guesses = []  # List to store user's guesses
score = 0  # Keep track of the user's score
question_no = 0  # Keep track of the question number

# Loop through each question
for question in questions:
    print("------------------------")
    print(question)
    # Print options for the current question
    for option in options[question_no]:
        print(option)
    
    # Get user's guess
    guess = input("Enter(A, B, C, D): ").upper()
    guesses.append(guess)
    
    # Check if the guess is correct
    if guess == answers[question_no]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_no]} is the correct answer")
    
    # Increment the question number after each question
    question_no += 1

# Show final score
print("------------------------")
print(f"Your final score is: {score}/{len(questions)}")
