from libdw import pyrebase
import shutil
width = shutil.get_terminal_size((80, 20)).columns
screen_width = 156
def introduction(screen_width):
    print('=' * screen_width + "\n") 
    print("WELCOME TO THE RECYCLING QUIZ GAME".center(width)+"\n")
    
    print("an exciting and educational game designed especially for young eco warriors like you!".center(width))    
    print("Get ready to embark on a journey where you can showcase your knowledge about sustainability!".center(width))        
    print("The higher the level, the more points you can earn.".center(width) + "\n".center(width))
    print('=' * screen_width + "\n")

    user_input = input(" Press space to continue".center(width))
    if user_input.lower() != " ":
        print("Invalid Input... Press space to continue")
        print('=' * screen_width + "\n")
    
    


    print("""
        LEVEL 1 - Yes-No questions 
        LEVEL 2 - Muliple Choice Questions 
        LEVEL 3 - Open-Ended Questions """+ "\n")
          
    print("Type 'quit' if you want to force end the game. However, your progress won't be saved"+ "\n")
    print('-' * screen_width + "\n")

def login(final_score):
    username = input("Please key in your email: ")  # Example: ctd_is_the_best@ilovectd.com
    passw = input("Please type your password: ")    # Example: ctdctd
    dburl = "https://labexample-f5b6a-default-rtdb.asia-southeast1.firebasedatabase.app/"
    email = username
    password = passw 
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

    # Authenticate the user
    try:
        user = auth.sign_in_with_email_and_password(email, password)
    except:
        print("Authentication failed")
        return

    db = firebase.database()
    user = auth.refresh(user['refreshToken'])

    # Update the total score in the database
    score_key = f"users/{username.replace('.',',')}/score"  # Firebase keys cannot contain '.'
    db.child(score_key).set(final_score, user['idToken'])
    print("Your score has been updated in the database.")

    # Retrieve and display the updated score
    score = db.child(score_key).get(user['idToken']).val()
    print(f"Your total score is now: {score}")

print('-' * screen_width + "\n")
def select_level(levels): # choose different diffculty 
    
    while True:
        selected_level = input("Choose a level to play (e.g., Level 1): ").strip()
        if selected_level in levels:
            if selected_level == "Level 1":
                print("""
        INSTRUCTIONS
        For this Level, type 'yes' if you think the item is recyclable, and 'no' if not.""" + "\n")
            elif select_level == "Level 2":
                print("""
        INSTRUCTIONS
        For this level, choose the correct answer 'a,b,c,d'  """+"\n")
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
        print('-' * screen_width + "\n")
        print(f"\nSTARTING {selected_level}...")
        
        score = 0
        
        for item in quiz_items:
            user_guess = display_question(item, selected_level)
            if selected_level == "Level 1":
                correct_answer = quiz_items[item]
                give_feedback_Level_1(correct_answer, item)
                score, quit_game = check_answer(user_guess, correct_answer, score, score_multiplier, selected_level)


            elif selected_level == "Level 2":
                correct_answer = [option for option, (text, is_correct) in quiz_items[item].items() if is_correct][0]
                score, quit_game = check_answer(user_guess, correct_answer, score, score_multiplier, selected_level)
                give_feedback_Level_2(correct_answer , user_guess,item)

            
            if quit_game:
                return total_score  # If user wants to quit

     

        total_score += score
        print(f"You scored {score} points in {selected_level}.")
        print('' * screen_width + "\n")

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

def give_feedback_Level_1(correct_answer, item):
    explanation = "Recyclable" if correct_answer else "Not recyclable"
    print(f"The correct answer for '{item}' is: {explanation}.")
    print('-' * screen_width + "\n")
    # Here you can add more detailed explanations
    print()
def give_feedback_Level_2(correct_answer, user_guess, item):
    explanations = {
        "How many times can glass be recycled?": "Glass can be recycled indefinitely without losing quality.",
        "Why is it important to recycle?:": "Recycling helps save energy, reduces pollution, and conserves natural resources.",
        "How long does it take for a plastic bottle to decompose in a landfill?": "Plastic bottles can take up to 500 years to decompose in a landfill, causing environmental harm.",
        "What is composting?": "Composting is the process of turning organic waste into nutrient-rich soil.",
        "Which of these items can be reused?": "Cloth shopping bags can be reused, reducing the need for single-use plastic.",
        # Add explanations for other questions...
        
    }
    
    explanation = explanations.get(item, "No specific explanation available.")
    print(f"The correct answer for '{item}' is: {explanation}"+ "\n")
    print('-' * screen_width + "\n")
    # Here you can add more detailed explanations
    

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
                print("Oops! That's incorrect. The correct answer is "+ correct_answer)
                
        else:
            print("Invalid option selected!")

    return score, quit_game


levels = {
    "Level 1": { #TRUE-FALSE
        "Plastic bottle": True,
        "Styrofoam cup": False,
        "Food Waste" : False,
        "Cardboard": True,
        "Glass Jar" :True,
        "Paper": True,
        "Used pizza boxes":False,
        "Light bulbs":False,
        "Ceramics and porcelain":False,
        "Magazine":True
        

    },
    "Level 2": {
        "How many times can glass be recycled?": {
            "a": ("Indefintely", True),
            "b": ("10", False),
            "c": ("4", False),
            "d": ("1", False)
        },
        "Why is it important to recycle?:": {
            "a": ("It helps save energy", False),
            "b": ("It reduces pollution", False),
            "c": (" It conserves natural resources", False),
            "d": ("All of the above", True)
        },
        "How long does it take for a plastic bottle to decompose in a landfill?": {
            "a": ("5 years", False),
            "b": ("10 years", False),
            "c": ("50 years", False),
            "d": ("500 years", True)
        },
        "What is composting?": {
            "a": ("Throwing away plastic", False),
            "b": ("Turning organic waste into nutrient-rich soil", True),
            "c": (" Recycling used paper", False),
            "d": ("Donating old clothes", False)     
        },
        "Which of these items can be reused?": {
            "a": ("Single-use plastic water bottles", False),
            "b": (" Cloth shopping bags", True),
            "c": ("Styrofoam cups", False),
            "d": ("Plastic utensils", False)     
        }
    },
    
    "Level 3": { #OPEN-ENDED
        "q1": "correct ans",
        "question2": "correct answer",
        "question3": "correct answer",
        "question4": "correct answer"
    }
    # Add more levels as needed
}

if __name__ == "__main__":
    a = 0  
    introduction(width)
    final_score = main_game_loop(levels)
    login(final_score)
    print(f"\nYour total score is {final_score}.")
    print('=' * width + "\n")
    print("""
          
          THANK YOU FOR PLAYING!

          Remember, every small step in recycling helps our planet""" + "\n".center(width))
    print('=' * width)
