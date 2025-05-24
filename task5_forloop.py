'''#1.Dice Roll Simulation
#simulate rolling a 6-sided die at least 20 times
''''''Count and print the following statistics: 
How many times you rolled a 6 
How many times you rolled a 1 
How many times you rolled two 6s in a row''''''

import random

rolls = []
roll_6_count = 0
roll_1_count = 0
double_6_count = 0

# Roll the die 20 times
for i in range(20):
    roll = random.randint(1, 6)
    rolls.append(roll)

    # Count 6s and 1s
    if roll == 6:
        roll_6_count += 1
    if roll == 1:
        roll_1_count += 1

# Count two 6s in a row
for i in range(1, len(rolls)):
    if rolls[i] == 6 and rolls[i-1] == 6:
        double_6_count += 1

# Results
print("Dice rolls:", rolls)
print("Number of times rolled a 6:", roll_6_count)
print("Number of times rolled a 1:", roll_1_count)
print("Number of times two 6s were rolled in a row:", double_6_count)
'''
#2.Jumping Jacks Workout Tracker
#you must do 100 jumping jacks,10 at a time
#After each set,ask:
'''Are you tired?" → If yes, ask "Do you want to skip remaining sets?"

    If yes → end the workout and show how many you completed

    If no → continue
    
    If you finish all 100 → print a success message'''

total_jumping_jacks = 100
completed = 0

for i in range(0, total_jumping_jacks, 10):
    completed += 10
    print(f"You completed {completed} jumping jacks.")

    tired = input("Are you tired? (yes/no): ").lower()
    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/no): ").lower()
        if skip in ["yes", "y"]:
            print(f"You completed a total of {completed} jumping jacks.")
            break
        else:
            print(f"{total_jumping_jacks - completed} jumping jacks remaining...")
    else:
        print(f"{total_jumping_jacks - completed} jumping jacks remaining...")

if completed == total_jumping_jacks:
    print("🎉 Congratulations! You completed the full workout.")
