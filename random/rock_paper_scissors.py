import random
import time

comp_score = 0
user_score = 0
allowed_moves = ["R", "P", "S"]

def compare(comp_mv, user_mv):
    if user_mv == comp_mv:
        print(f"You chose: {user_mv}\nThe Computer chose: {comp_mv}")
        time.sleep(0.7)
        print("Tied")
    elif (comp_mv == "R" and user_mv == "S") or (comp_mv == "P" and user_mv == "R") or (comp_mv == "S" and user_mv == "P"):
        print(f"You chose: {user_mv}\nThe Computer chose: {comp_mv}")
        time.sleep(0.7)
        print("Computer scores!")
        global comp_score
        comp_score += 1
    else:
        print(f"You chose: {user_mv}\nThe Computer chose: {comp_mv}")
        time.sleep(0.7)
        print("You score")
        global user_score
        user_score += 1
    time.sleep(1)
    print(f"Your score: {user_score}; Computer score: {comp_score}")

def iterate():
    comp_mv = random.choice(allowed_moves)
    user_mv = input("R for Rock, P for Paper, S for Scissors: ").upper()
    if user_mv in allowed_moves:
        compare(comp_mv, user_mv)
    else:
        print("Move not recognised")
        time.sleep(0.7)
        iterate()

while comp_score != 10 or user_score != 10:
    iterate()
    time.sleep(1)
