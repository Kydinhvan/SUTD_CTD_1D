def introduction():
    print("Welcome to the Recycling Quiz Game!")
    print("In this game, you'll guess whether certain items are recyclable.")
    print("The higher the level, the more points you can earn.")
    print("Type 'yes' if you think the item is recyclable, and 'no' if not.")

def select_level(levels): # choose different diffculty 
    print("\nAvailable Levels:")
    for level in levels:
        print(level)
    while True:
        selected_level = input("Choose a level to play (e.g., Level 1): ").strip()
        if selected_level in levels:
            return selected_level
        else:
            print("Invalid level. Please choose a valid level.")

def main_game_loop(levels): # we modify this as we add more features to the game 
    total_score = 0
    while True:
        selected_level = select_level(levels)
        quiz_items = levels[selected_level]
        level_number = int(selected_level.split(" ")[-1])  # Assuming level format is "Level X"
        score_multiplier = level_number  # More points for higher levels

        print(f"\nStarting {selected_level}...")
        score = 0
        for item in quiz_items:
            user_guess = display_question(item)
            correct_answer = quiz_items[item]
            score = check_answer(user_guess, correct_answer, score, score_multiplier)
            if score == "quit":
                end_game_summary(0, 0)
                raise SystemExit
            give_feedback(correct_answer, item)
        total_score += score
        print(f"You scored {score} points in {selected_level}.")

        if input("\nDo you want to play another level? (yes/no): ").strip().lower() != "yes":
            break

    return total_score

def display_question(item): 
    return input(f"Is a '{item}' recyclable? (yes/no/quit): ").strip().lower()

def give_feedback(correct_answer, item):
    explanation = "Recyclable" if correct_answer else "Not recyclable"
    print(f"The correct answer for '{item}' is: {explanation}.")
    # Here you can add more detailed explanations
    print()

def end_game_summary(score, total_items):
    print(f"Your final score is {score} out of {total_items}.")
    print("Thank you for playing! Remember, every small step in recycling helps our planet.")

def check_answer(user_guess, correct_answer, score, score_multiplier):
    if (user_guess == "yes" and correct_answer) or (user_guess == "no" and not correct_answer):
        print("Correct!")
        return score + (1 * score_multiplier)
    elif(user_guess== "quit" ):
        return "quit"
    else:
        print("Incorrect!")
        return score

levels = {
    "Level 1": {
        "Plastic bottle": True,
        "Styrofoam cup": False,
    },
    "Level 2": {
        "Glass jar": True,
        "Used pizza box with grease": False,
    },
    # Add more levels as needed
}

if __name__ == "__main__":
    a =0
    introduction()
    final_score = main_game_loop(levels)
    print(f"\nYour total score is {final_score}.")
    print("Thank you for playing! Remember, every small step in recycling helps our planet.")
