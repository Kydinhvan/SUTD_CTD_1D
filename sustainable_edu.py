from libdw import pyrebase
def introduction():
    print("Welcome to the Recycling Quiz Game!")
    print("In this game, you'll need apply what you know about sustainabliy.")
    print("The higher the level, the more points you can earn.")
    print("Type 'quit' if you want to force end the game. However, your progress won't be saved")


def login(final_score):
    dburl = "https://labexample-f5b6a-default-rtdb.asia-southeast1.firebasedatabase.app/"
    apikey = "AIzaSyDvPsb9CRa-_a0RVt7CRuRpnKI38zMqDAM"
    authdomain = dburl.replace("https://", "")

    config = {
        "apiKey": apikey,
        "authDomain": authdomain,
        "databaseURL": dburl,
    }

    # Initialize Firebase
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    haveAccount = input("Do you have an account? (yes/no):").strip().lower()
    if haveAccount == "yes" or haveAccount == "y":
        email = input("Please key in your email: ")  # Example: ctd_is_the_best@ilovectd.com
        password = input("Please type your password: ")    # Example: ctdctd
    else:
        promptcreate = input("Would you like to create an account? (yes/no):").strip().lower()
        if promptcreate == "yes" or promptcreate == "y":
            email = input("Please key in your email: ")
            password = input("Please create your password: ")
            userCredentials = auth.create_user_with_email_and_password(email, password)
            print(userCredentials)

    # Authenticate the user
    try:
        user = auth.sign_in_with_email_and_password(email, password)
    except:
        print("Authentication failed")
        return

    db = firebase.database()
    user = auth.refresh(user['refreshToken'])

    score_key = f"users/{email.replace('.',',')}/score" # Firebase keys cannot contain '.'
    # Update the total score in the database 
    previous_score = db.child(score_key).get(user['idToken']).val()
    if final_score > previous_score:       
        db.child(score_key).set(final_score, user['idToken'])
        print("Your highscore has been updated in the database.")    # Retrieve and display the updated score
        return True
    else:
        print(f"Your highscore remains the same at {previous_score}") 




def select_level(levels): # choose different diffculty 
    print("\nAvailable Levels:")
    for level in levels:
        print(level)
    while True:
        selected_level = input("Choose a level to play (e.g., Level 1): ").strip()
        if selected_level in levels:
            if select_level == "Level 1":
                print("For this Level, type 'yes' if you think the item is recyclable, and 'no' if not.")
            elif select_level == "Level 2":
                print
            return selected_level
        else:
            print("Invalid level. Please choose a valid level.")

def main_game_loop(levels):
    total_score = 0
    while True:
        selected_level = select_level(levels)
        quiz_items = levels[selected_level]
        level_number = int(selected_level.split(" ")[-1])  # Assuming level format is "Level X"
        score_multiplier = level_number

        print(f"\nStarting {selected_level}...")
        score = 0
        for item in quiz_items:
            user_guess = display_question(item, selected_level)
            if selected_level == "Level 1":
                correct_answer = quiz_items[item]
            elif selected_level == "Level 2":
                correct_answer = [option for option, (text, is_correct) in quiz_items[item].items() if is_correct][0]

            score, quit_game = check_answer(user_guess, correct_answer, score, score_multiplier, selected_level)
            if quit_game:
                return total_score  # If user wants to quit

            give_feedback(correct_answer, item)

        total_score += score
        print(f"You scored {score} points in {selected_level}.")

        if input("\nDo you want to play another level? (yes/no): ").strip().lower() != "yes":
            break
    return total_score

def display_question(item,selected_level): 
    if selected_level == "Level 1":
        return input(f"Is a '{item}' recyclable? (yes/no): ").strip().lower()
    elif selected_level == "Level 2":
        # Displaying the multiple-choice question
        question = levels[selected_level][item]
        print(f"Question: {item}")
        for option in question:
            print(f"  {option}. {question[option][0]}")
        return input("Choose the correct option (a/b/c/d): ").strip().lower()

def give_feedback(correct_answer, item):
    explanation = "Recyclable" if correct_answer else "Not recyclable"
    print(f"The correct answer for '{item}' is: {explanation}.")
    # Here you can add more detailed explanations
    print()

def end_game_summary(score, total_items):
    print(f"Your final score is {score} out of {total_items}.")
    print("Thank you for playing! Remember, every small step in recycling helps our planet.")

def check_answer(user_guess, correct_answer, score, score_multiplier, level):
    quit_game = False

    if user_guess == "quit":
        quit_game = True
        return score, quit_game

    if level == "Level 1":
        if (user_guess == "yes" and correct_answer) or (user_guess == "no" and not correct_answer):
            print("Correct!")
            score += 1 * score_multiplier
        else:
            print("Incorrect!")
    elif level == "Level 2":
        if user_guess in ['a', 'b', 'c', 'd']:  # Check if the guess is a valid option
            if user_guess == correct_answer:
                print("Correct!")
                score += 1 * score_multiplier
            else:
                print("Incorrect!")
        else:
            print("Invalid option selected!")

    return score, quit_game


levels = {
    "Level 1": { #TRUE-FALSE
        "Plastic bottle": True,
        "Styrofoam cup": False,
    },
    "Level 2": {
        "question1": {
            "a": ("option1", True),
            "b": ("option2", False),
            "c": ("option3", False),
            "d": ("option4", False)
        },
        "question2": {
            "a": ("option1", True),
            "b": ("option2", False),
            "c": ("option3", False),
            "d": ("option4", False)
        },
        "question3": {
            "a": ("option1", True),
            "b": ("option2", False),
            "c": ("option3", False),
            "d": ("option4", False)
        }
    },
    "Level 3": { #OPEN-ENDED
        "question1": "correct answer",
        "question2": "correct answer",
        "question3": "correct answer",
        "question4": "correct answer"
    }
    # Add more levels as needed
}

if __name__ == "__main__":
    introduction()
    final_score = main_game_loop(levels)
    login(final_score)
    print(f"\nYour total score is {final_score}.")
    print("Thank you for playing! Remember, every small step in recycling helps our planet.")
