import random, sys, csv

class Question:
    def __init__(self, question):
        self.question = question

    def yes_no_maybe(self):
        while True:
            answer = input(self.question)
            acceptable_answer = ["y", "n", "m"]
            if answer in acceptable_answer:
                return answer
            else:
                print("Please enter a valid answer.")

    def yes_no_question(self):
        while True:
            answer = input(self.question)
            acceptable_answer = ["y", "n"]
            if answer in acceptable_answer:
                return answer
            else:
                print("Please enter a valid answer.")

    def list_question(self, question_list):
        i = 1
        for question in question_list:
            print(f"{i}. {question}")
            i += 1
        while True:
            try:
                answer = int(input(self.question)) - 1
            except ValueError:
                print("Please enter a valid number.")
                continue
            if 0 <= answer <= len(question_list):
                return question_list[answer]
            else:
                print("Please enter a valid option.")

cuisine_style_list = [
    "Taiwanese",
    "Chinese",
    "Japanese",
    "Korean",
    "French",
    "English",
    "American",
    "Italian",
    "Spanish",
    "Vietnamese",
    "Thai",
    "Indian",
    "Other"]

#main() prints out the menu and forwards user input to other functions.
def main():
    welcome_msg = "##################################\nWelcome to What should I Eat? v0.1!\n##################################"
    options = [
        "Just tell me what to eat! (Randomly choose 1 from the list)",
        "Help me decide by comparing between food (Championship style)",
        "Randomly Choose 1 from the type of food you feel like eating",
        "Show all food from the list",
        "Add new food to the list",
        "Delete food from the list",
        "Set food in the list as favorite",
        "Set disliked food in the list",
        "Exit App",
    ]
    print(welcome_msg)
    while True:
        input("Press Enter to continue...")
        option = Question("Your selection: ").list_question(options)
        if option == options[0]:
            random_food()
        elif option == options[1]:
            food_championship()
        elif option == options[2]:
            food_filter_menu()
        elif option == options[3]:
            food_filter_printer(food_reader)
        elif option == options[4]:
            food_writer()
        elif option == options[5]:
            food_eraser()
        elif option == options[6]:
            set_favorite_food()
        elif option == options[7]:
            set_disliked_food()
        elif option == options[8]:
            sys.exit("Have a nice day!")
        else:
            print("Invalid input. Please press the number of the option you want to use.")

def random_food(cuisine_style=None, high_cal=None, cost=None, vegetarian=None, favorite=None, disliked=None):
    food = food_filter_printer(food_reader(), cuisine_style=cuisine_style, high_cal=high_cal, cost=cost, vegetarian=vegetarian, favorite=favorite, disliked=disliked)
    random_food_choice= random.choice(food)
    print(f"How about consider eating {str.lower(random_food_choice['name'])}?!")
    return random_food_choice

def food_championship():
    food = food_reader()
    #randomize the food list
    random.shuffle(food)
    #check if there is more than one food in the list
    while len(food) > 1:
        #take the first 2 food in the randomized list and store them into pair while popping them from the list
        pair = [food.pop(0), food.pop(0)]
        print("Which food do you prefer?")
        print(f"1. {pair[0]['name']}")
        print(f"2. {pair[1]['name']}")
        while True:
            try:
                choice = int(input("Enter your choice (1 or 2): "))
                if choice not in [1, 2]:
                    raise ValueError
                break
            except ValueError:
                print("Please type in only 1 or 2")
        #User choices start with 1, program starts with 0, so minus 1
        round_winner = pair[choice-1]
        #Add winner back to the back of the list
        food.append(round_winner)
    winner = food[0]
    print(f"The winner is: {str.lower(winner['name'])}.")
    return winner

def food_filter_menu():
        filter_list = [
        "Cuisine style",
        "High Calorie or not",
        "Expensive or cheap",
        "Vegetarian or not",
        "Favorite food",
        "Disliked food"
        ]
        filter=Question("What type of filter? ").list_question(filter_list)
        print(filter)
        if filter == filter_list[0]:
            cuisine = Question("What type of cuisine? ").list_question(cuisine_style_list)
            random_food(cuisine)
        elif filter == filter_list[1]:
            high = Question("Do you want to eat high calorie food? [y]yes/[n]no ").yes_no_question()
            random_food("",high)
        elif filter == filter_list[2]:
            cost = Question("Do you want to eat expensive food? [y]yes/[n]no ").yes_no_question()
            random_food("","",cost)
        elif filter == filter_list[3]:
            vegetarian = Question("Do you want to eat vegetarian food? [y]yes/[n]no ").yes_no_question()
            random_food("","","",vegetarian)
        elif filter == filter_list[4]:
            random_food("","","","","y")
        elif filter == filter_list[5]:
            random_food("","","","","","y")

#reads from food_list.csv and puts in in memory
def food_reader():
    food_list = []
    i = 1
    with open("food_list.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            food_list.append({"number":i,"name": row["name"], "cuisine_style": row["cuisine_style"], "high_cal": row["high_cal"], "cost": row["cost"],"vegetarian": row["vegetarian"], "note": row["note"], "favorite": row["favorite"], "disliked": row["disliked"]})
            i += 1
    return food_list

#reads from designated list and filtered by specific category and print out food list
def food_filter_printer(food, cuisine_style=None, high_cal=None, cost=None, vegetarian=None, favorite=None, disliked=None):
    unfiltered_food_list = food_reader()
    if cuisine_style is None and high_cal is None and cost is None and vegetarian is None and favorite is None and disliked is None:
        print("All food in the list:")
        for item in unfiltered_food_list:
            print(item["number"], item["name"])
        return unfiltered_food_list
    else:
        filtered_food_list = []
        if cuisine_style:
            for item in food:
                if item["cuisine_style"] in cuisine_style:
                    filtered_food_list.append(item)
        elif high_cal:
            for item in food:
                if item["high_cal"] in (high_cal, "m"):
                    filtered_food_list.append(item)
        elif cost:
            for item in food:
                if item["cost"] in (cost,"m"):
                    filtered_food_list.append(item)
        elif vegetarian:
            for item in food:
                if item["vegetarian"] in (vegetarian,"m"):
                    filtered_food_list.append(item)
        elif favorite:
            for item in food:
                if item["favorite"] in favorite:
                    filtered_food_list.append(item)
        elif disliked:
            for item in food:
                if item["disliked"] in disliked:
                    filtered_food_list.append(item)
        #if no food is added to the filtered_food_list
        if not filtered_food_list:
            print("No food in this category. Will use the full list instead.")
            for item in unfiltered_food_list:
                print(item["number"], item["name"])
            return unfiltered_food_list
        elif filtered_food_list:
            i = 1
            print("Food that match the criteria:")
            for item in filtered_food_list:
                print(i, item["name"])
                i += 1
            return filtered_food_list

#write user inputs to food_list.csv 
def food_writer():
    name = input("What's the name of the food? ").capitalize()
    while name == "":
        print("Please enter a food name.")
        name = input("What's the name of the food? ").capitalize()
    cuisine_style = Question("What is the food's cuisine style? ").list_question(cuisine_style_list)
    high_cal = Question("Is this food high calorie? ([y]yes/[n]no/[m]maybe) " ).yes_no_maybe()
    cost = Question("Is it expensive? ([y]yes/[n]no/[m]maybe) ").yes_no_maybe()
    vegetarian = Question("Is the food vegetarian? ([y]yes/[n]no/[m]maybe) ").yes_no_maybe()
    note = input("Additional note? ")
    favorite = "n"
    disliked = "n"
    with open("food_list.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "cuisine_style", "high_cal", "cost", "vegetarian", "note", "favorite", "disliked"],)
        writer.writerow({"name": name, "cuisine_style": cuisine_style, "high_cal": high_cal, "cost": cost, "vegetarian": vegetarian, "note": note, "favorite": favorite, "disliked": disliked})

#delete a food entry from food_list.csv
def food_eraser():
    food = food_filter_printer(food_reader())
    delete_number = input("Enter the number of the food you want to delete: ")
    #create an updated list
    updated_food = []
    for f in food:
        #copy the old entries to new list, if they don't have the number that is going to be deleted by the user
        if f["number"] != int(delete_number):
            updated_food.append(f)
    food = updated_food
    with open("food_list.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "cuisine_style", "high_cal", "cost", "vegetarian", "note", "favorite", "disliked"])
        writer.writeheader()
        for nf in food:
            writer.writerow({"name": nf["name"], "cuisine_style": nf["cuisine_style"], "high_cal": nf["high_cal"], "cost": nf["cost"], "vegetarian": nf["vegetarian"], "note": nf["note"], "favorite": nf["favorite"], "disliked": nf["disliked"]})

#set a food entry as favorite in food_list.csv
def set_favorite_food():
    food = food_filter_printer(food_reader())
    favorite_number = int(input("Enter food number that you would like to mark as your favorite: "))
    for item in food:
        if item["number"] == favorite_number:
            item["favorite"] = "y"
            if item["disliked"] == "y":
                item["disliked"] = "n"
    with open("food_list.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "cuisine_style", "high_cal", "cost", "vegetarian", "note", "favorite", "disliked"])
        writer.writeheader()
        for nf in food:
            writer.writerow({"name": nf["name"], "cuisine_style": nf["cuisine_style"], "high_cal": nf["high_cal"], "cost": nf["cost"], "vegetarian": nf["vegetarian"], "note": nf["note"], "favorite": nf["favorite"], "disliked": nf["disliked"]})

#set a food entry as disliked in food_list.csv
def set_disliked_food():
    food = food_filter_printer(food_reader())
    disliked_number = int(input("Enter food number that you don't like: "))
    for item in food:
        if item["number"] == disliked_number:
            item["disliked"] = "y"
            if item["favorite"] == "y":
                item["favorite"] = "n"
    with open("food_list.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "cuisine_style", "high_cal", "cost", "vegetarian", "note", "favorite", "disliked"])
        writer.writeheader()
        for nf in food:
            writer.writerow({"name": nf["name"], "cuisine_style": nf["cuisine_style"], "high_cal": nf["high_cal"], "cost": nf["cost"], "vegetarian": nf["vegetarian"], "note": nf["note"], "favorite": nf["favorite"], "disliked": nf["disliked"]})

if __name__ == "__main__":
    main()