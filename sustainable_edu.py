from libdw import pyrebase
from time  import sleep
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

    user_input = input(" Press enter to continue".center(width))
    print('=' * screen_width + "\n")
    print("""
        LEVEL 1 - Yes-No questions 
        LEVEL 2 - Muliple Choice Questions 
        LEVEL 3 - Open-Ended Questions """+ "\n")
          
    print("Type 'quit' if you want to force end the game. However, your progress won't be saved"+ "\n")
    print('-' * screen_width + "\n")

def login(final_score):
    password = "ctdctd"
    # username = input("Please key in your email: ")  # Example: ctd_is_the_best@ilovectd.com
    # passw = input("Please type your password: ")    # Example: ctdctd
    dburl = "https://labexample-f5b6a-default-rtdb.asia-southeast1.firebasedatabase.app/"
    # email = username
    # password = passw 
    apikey = "AIzaSyDvPsb9CRa-_a0RVt7CRuRpnKI38zMqDAM"
    authdomain = dburl.replace("https://", "")
    secret_key = '"-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCiTLKeL0KcvWDz\nFC4iDtKPD4OiMOuhfolZjtiWrl5faKrNVKrajuO8FOVYGb8G53xV6fm46GXy0kWH\ngO3MpJn/e+2ZCcmfGnntvLm3pBUoDRSM5tUsKPWQQooU6uqjvGMV3DGVJGrktgcx\n+yOIiRulwwrp1iQKUzGDLZdADyTQs+z4EvZr3jQZ0BSSbTdkIBbkqjLPmdViTVPj\nlKWbOrqw34YTCYNw+2U3E6QrgyX2OhgsBlm7paI9nREOLNOTE5ZIvF4PYvckRESL\nTceGwbzXYxdUQMogmJwyGbv1F7aSlo2YZnjeXqB+U4yhPeZTURe9NbrPbdqIYCU7\n5SSshiDHAgMBAAECggEAS9NOfgXxdp4pvddXSFUpfWoPo0Z8x8oA7IUG3rsfXy7c\n4aplWk/4yOXwUm1Q6K5c0hzKrV9yRfSERG7xarMaOZkSI/ZFKt6pSW9rSwdPVRNr\nXvr3bDbEp33W2jf4oL/CgTOLPLUzdaAvk2PUMZVxA8wwfJgt5V8B2loB+I06s4Al\nbPKp5m9TxbtRhAFqKlOt6MXn3+RitDNW8IeitvJQ2iK8h1V+p2hMEChNlUBD0ivu\nE1RCAHu+Adko99kYfrlBmaekqJACv6RKpYB24hJoyalGhDnvIYluBSVYgqWMgCH9\nGFR7R+hTv9HrGbsCfk6Bl3YcMh4W4VxzuR4jevE6KQKBgQDYmZnI7j4gfTwhEKld\ndIZVGWP+w7VaMQYeZJcLK3OqqfXGYNkp0Or8SI5uNB92tJJTzVLGvLUuVykecfQG\ni5AyE4F7U8dfhUscErUhVNi9bR/iwF0JYROcj7euEAyncaJjZ3iafchZnYx3mwyo\nkWF+xgZVGqIuOYUa4J+Ug/cEeQKBgQC/0n5SKk1hfUHMbNE3AhNQpDNqPVyz3/i+\nkAEqy9cAEg2mPqT4BkCMYN2uJoedfoAHkJWWyzy76H/9L9E9PCOihdxu+UGCOmt8\n05ZxX9JoVyDAqDyI8oRFTBQB8muUuQgFKohLbQ+HxTfyho+327zjoAD1jw1F7sTK\njsJ5mqR/PwKBgQCmDnx8M0qmFd03bFKsN12VeHXVJ62ti9ApFO1HvvRabxriD/Xt\nvSGqcOXhT0yf8SgN32gKvToaYPBBSxPOwMi324R1THGZpdNDnoQHHclc0ICVkuzA\n+A/VA8nKRLuu08uvcfBgYPZs3gCG4fP+eBbK3n6UWGrmDWsig/tUHSgP4QKBgGMa\nWh8TMeVTNGJsOe7kiJwaKWITD8jyxu2VMrUsmQi1Sw3/wXVOrZyZEw69Y0VQLM87\nuL0uhVNDvJRPVxf+8R4vcIJ5Doo8qnnUSx6J9gfoM8i1YokSWpn+wzt6RnCQ4/7f\nSYlGcEah8tS/BpNj2IP1j2lOnfnqcQuBlCIFbkU7AoGAXQNW4VuSrFWE2mL2HnJU\n3k0h4Pe/wcaZj2JsslzdS+8qaBnGoyJ5VEH5KGvj3MPq4amhuLCeVVfPxxq2BsXv\nVccJ5dvdNIQ9vzSff4046sY7LzJ/nrnEJXmWoFAQYyCpo9LeP8Dku1IZq+9dKEaF\nM0CqvmCBLGZ/iIazzDtubtQ=\n-----END PRIVATE KEY-----\n"'

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
            #print(userCredentials)
        else:
            print("Logging in as Guest User...")
            sleep(1)
            email = "guestuser@game.com" # Example: ctd_is_the_best@ilovectd.com
            password =  "ctdctd"  # Example: ctdctd

    # Authenticate the user
    try:
        user = auth.sign_in_with_email_and_password(email, password)
    except:
        print("Authentication failed...")
        return

    db = firebase.database()
    user = auth.refresh(user['refreshToken'])
    
    score_key = f"users/{email.replace('.',',')}/score"  # Firebase keys cannot contain '.'
    previous_score = db.child(score_key).get(user['idToken']).val()
    
    if email !="guestuser@game.com":
        if previous_score is None:
            db.child(score_key).set(final_score, user['idToken'])
            score = db.child(score_key).get(user['idToken']).val()
            print(f'Welcome to the Recycling Quiz Game and Congratulation on getting {score} point on your first try!')
        elif previous_score < final_score:
            # Update the total score in the database
            db.child(score_key).set(final_score, user['idToken'])

            # Retrieve and display the updated score
            score = db.child(score_key).get(user['idToken']).val()
            print(f"New high score {score} achieved! You're on fire! 🔥🎉")
        else:
            score = db.child(score_key).get(user['idToken']).val()
            print (f"Keep pushing, you're {score-final_score} away from your high score! Don't give up! 👍🎮")


    # LEaderboard
    
    # users = db.child("users").get().val()
    leaderboard = []
    users = [
    "ctd_is_the_best@ilovectd.com",
    "deb123@hello.com",
    "guestuser@game.com",
    "jana123@sutd.suck"
]
    for email in users:
        try:
            # Authenticate each user
            user = auth.sign_in_with_email_and_password(email, password)
            auth.refresh(user['refreshToken'])

            # Retrieve the score
            score_key = f"users/{email.replace('.',',')}/score"
            score = db.child(score_key).get(user['idToken']).val()

            if score is not None:
                leaderboard.append((email[:5], score))

        except Exception as e:
            print(f"Failed to retrieve score for {email}: {e}")

    # Sort the leaderboard
    leaderboard.sort(key=lambda x: x[1], reverse=True)

    # Display the leaderboard
    print("🏆 Leaderboard 🏆".center(width))
    line = "-" * 30
    print(line.center(width))
    for rank, (user, score) in enumerate(leaderboard[:5], start=1):
        user_display = user.split('@')[0]  # Display only the part before '@' in the email
        print(f"{rank:2}. {user_display:15} Score: {score}".center(width))

        print(line.center(width))
        # print(f"Showing top {5} entries".center(width))
        
    

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
        sleep(1)
        
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

            elif selected_level == "Level 3":
                correct_answer = levels[selected_level][item]
                score, quit_game = check_answer(user_guess, correct_answer, score, score_multiplier, selected_level)
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
    
    elif selected_level == "Level 3":
        question = levels["Level 3"][item]
        print(f"Question: {item}")
        lvl3_ans= input("Enter your answer:").strip().lower()
        return lvl3_ans.strip().lower()

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
    elif level == "Level 3":
        for i in levels["Level 3"]:
            if user_guess == correct_answer:
                print("Correct!")
                score += 1 * score_multiplier
                break
        else:
            print("Incorrect!")

    return score, quit_game


levels = {
    "Level 1": { #TRUE-FALSE
        "Plastic bottle": True,
        "Styrofoam cup": False,
        "Cardboard": True,
        "Glass Jar" :True,
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
    

    "Level 3": {
        "What is the term for using water to separate materials that sink from those that float in the recycling process?": "hydrocyclone separation",
        "Name a common household item that can be recycled into fiber for making new clothing.": "plastic bottles",
        "What is the term for decomposing organic waste, like food scraps and yard waste, into a soil conditioner?": "composting",
        "Why is it important to rinse containers before recycling them?": "to remove food residue and prevent contamination."   
    }
    # Add more levels as needed
}

if __name__ == "__main__":
    a = 0  
    introduction(width)
    final_score = main_game_loop(levels)
    login(final_score)
    print('=' * width + "\n")
    print(f"Your final score is {final_score}.".center(width))
    message = "THANK YOU FOR PLAYING!\n\nRemember, every small step in recycling helps our planet"
    for lineee in message.split('\n'):
        print(lineee.center(width))
    print('=' * width)
