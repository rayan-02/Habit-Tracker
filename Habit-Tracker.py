from datetime import datetime, timedelta

habits = {}

def current():
 for habit_name in habits:
    print(f"- {habit_name}: {len(habits[habit_name])} completions")

def new_habit():
    habit_name = input("Enter a Habit: ").title()
    if habit_name in habits:
        print("Habit already exists")
    else:
        habits[habit_name] = [] 
        print(f"{habit_name} added successfully")
        

def completed():
    now = datetime.now()
    date = str(now.date())
    habit_name = input("Enter a Habit: ").title()
    if habit_name not in habits:
        print("Habit does not Exists")
    else:
        if date in habits[habit_name]:
            print("Habit Already Completed today")
        else:
            habits[habit_name].append(date)
            print(f"{habit_name} marked completed for {date}")



def streak():
    for habit_name in habits:
        dates_list = habits[habit_name]
        if not dates_list:
            print(f"{habit_name}: No completions yet")
            continue
        date_objects = [datetime.strptime(d, "%Y-%m-%d").date() for d in sorted(dates_list)]

        longest_streak = 1
        temp_streak = 1
        for i in range(1, len(date_objects)):
            if (date_objects[i] - date_objects[i-1]).days == 1:
                temp_streak += 1
            else:
                temp_streak = 1
            if temp_streak > longest_streak:
                longest_streak = temp_streak

        temp_streak = 1
        for i in range(len(date_objects)-1, 0, -1):
            if (date_objects[i] - date_objects[i-1]).days == 1:
                temp_streak += 1
            else:
                break
        current_streak = temp_streak

        print(f"{habit_name}: Current Streak = {current_streak}, Longest Streak = {longest_streak}")


def delete():
    if not habits:
        print("No habits to delete.")
        return
    print("Your habits:", ', '.join(habits.keys()))
    habit_name = input("Enter the Habit to delete: ").strip().title()
    if habit_name not in habits:
        print("Habit does not exist")
    else:
        del habits[habit_name]
        print(f"{habit_name} deleted successfully")

def menu():
    print("1. Current Habits")
    print("2. Add a new habit")
    print("3. Mark habit completed for today")
    print("4. Show streaks")
    print("5. Delete Habit")
    print("6. Exit")


while True:
    menu()
    try:
        user_input = int(input("Select: "))
        if user_input == 1:
            current()
        elif user_input == 2:
            new_habit()
        elif user_input == 3:
            completed()
        elif user_input == 4:
            streak()
        elif user_input == 5:
            delete()
        elif user_input == 6:
            break
        
    except:
        print("Enter number b/w given range")
    
    

