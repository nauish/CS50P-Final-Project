import random, sys, csv

class Question:
    def __init__(self, question):
        self.question = question

    def yes_no_question(self):
        while True:
            answer = input(self.question)
            acceptable_answer = ["y", "n", "m"]
            if answer in acceptable_answer:
                return answer
            else:
                print("Please enter a valid answer.")

    def list_question(self, question_list):
        for i, question in enumerate(question_list):
            print(f"{i + 1}. {question}")
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
    welcome_msg = "##################################\nWelcome to the meal planner v0.1!\n##################################"
    options = [
        "Just tell me what to eat! (Randomly choose 1 from the list)",
        "Help me decide by comparing between food (Championship style)",
        "Set what type of food you feel like eating",
        "Set cuisine restriction",
        "Show food list",
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
            break
        elif option == options[2]:
            filter_list = [
            "Cuisine style",
            "High Calorie or not",
            "Expensive or cheap",
            "Vegetarian or not",
            ]
            filter=Question("What type of filter? ").list_question(filter_list)
            print(filter)
            if filter == filter_list[0]:
                cuisine=Question("What type of cuisine? ").list_question(cuisine_style_list)
                food_reader(cuisine)
            elif filter == filter_list[1]:
                high_cal=Question("Do you want to eat high calorie food? [y]Yes/[n]No ").yes_no_question()
                print(high_cal)
                food_reader(high_cal)
        elif option == options[3]:
            ...
        elif option == options[4]:
            food_reader()
        elif option == options[5]:
            food_writer()
        elif option == options[6]:
            food_eraser()
        elif option == options[7]:
            set_favorite_food()
        elif option == options[8]:
            set_disliked_food()
        elif option == "0":
            sys.exit("Have a nice day!")
        else:
            print("Invalid input. Please press the number of the option you want to use.")
def random_food():
    random_food = random.choice(food_reader())
    print(f"You should eat {random_food['name']}!")

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
    print(f"The winner is: {winner['name']}.")
    return winner

def food_writer():
    name = input("What's the name of the food? ")
    while not name:
        print("Please enter a food name.")
        name = input("What's the name of the food? ")
    cuisine_style = Question("What is the food's cuisine style? ").list_question(cuisine_style_list)
    high_cal = Question("Is this food high calorie? ([y]yes/[n]no/[m]maybe) " ).yes_no_question()
    cost = Question("Is it expensive? ([y]yes/[n]no/[m]maybe) ").yes_no_question()
    vegetarian = Question("Is the food vegetarian? ([y]yes/[n]no/[m]maybe) ").yes_no_question()
    note = input("Additional note? ")
    favorite = "n"
    disliked = "n"
    with open("food_list.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "cuisine_style", "high_cal", "cost", "vegetarian", "note", "favorite", "disliked"],)
        writer.writerow({"name": name, "cuisine_style": cuisine_style, "high_cal": high_cal, "cost": cost, "vegetarian": vegetarian, "note": note, "favorite": favorite, "disliked": disliked})

def food_reader(cuisine_style=None, high_cal=None, cost=None, vegetarian=None):
    food = []
    with open("food_list.csv", "r") as file:
        reader = csv.DictReader(file)
        for i, row in enumerate(reader, start=1):
            food.append({"number": i,"name": row["name"], "cuisine_style": row["cuisine_style"], "high_cal": row["high_cal"], "cost": row["cost"],"vegetarian": row["vegetarian"], "note": row["note"]})
    filtered_food = []
    if cuisine_style:
        for item in food:
            if item["cuisine_style"] in cuisine_style:
                filtered_food.append(item)
                food = filtered_food
    elif high_cal:
        for item in food:
            if item["high_cal"] in high_cal:
                filtered_food.append(item)
                food = filtered_food
    elif cost:
        for item in food:
            if item["cost"] in cost:
                filtered_food.append(item)
                food = filtered_food
    elif vegetarian:
        for item in food:
            if item["vegetarian"] in vegetarian:
                filtered_food.append(item)
                food = filtered_food
    print("All food in the list:")
    for item in food:
        print(item["number"], item["name"])
    return food     

def food_eraser():
    food = food_reader()
    delete_number = input("Enter the number of the food you want to delete: ")
    #create an updated list
    updated_food = []
    for f in food:
        #copy the old entries to new list, if they don't have the number that is going to be deleted by the user
        if f["number"] != int(delete_number):
            updated_food.append(f)
    food = updated_food
    with open("food_list.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "cuisine_style", "high_cal", "cost", "vegetarian", "note"])
        writer.writeheader()
        for nf in food:
            writer.writerow({"name": nf["name"], "cuisine_style": nf["cuisine_style"], "high_cal": nf["high_cal"], "cost": nf["cost"], "vegetarian": nf["vegetarian"], "note": nf["note"]})

def set_favorite_food():
    food = food_reader()
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

def set_disliked_food():
    food = food_reader()
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

main()