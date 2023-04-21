import random, sys, re, csv

#main() prints out the menu and forwards user input to other functions.
def main():
    welcome_msg = "##################################\nWelcome to the meal planner v0.1!\n##################################"
    options = [
        "[1]Just tell me what to eat! (Randomly choose 1 from the list)",
        "[2]Help me decide by comparing between food (Championship style)",
        "[3]Set what type of food you feel like eating",
        "[4]Set cuisine restriction",
        "[5]Show food list",
        "[6]Add new food to the list",
        "[7]Delete food from the list",
        "[0]Exit App",
    ]
    print(welcome_msg)
    for option in options:
        print(option)

    while True:
        option = input("Your selection: ")
        if option == "1":
            ...
            break
        elif option == "2":
            food_championship()
        elif option == "3":
            ...
        elif option == "4":
            ...
        elif option == "5":
            food_reader()
        elif option == "6":
            food_writer()
        elif option == "7":
            food_eraser()
        elif option == "0":
            sys.exit("Have a nice day!")
        else:
            print("Invalid input. Please press the number of the option you want to use.")

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


def favorite_food():
    ...

def bad_foood():
    ...

def food_writer():
    name = input("What's the name of the food? ")
    region = input("Where is the country where the food is originated? ")
    calorie_warning = input("Is this food high calorie?" )
    cost = input("Is it expensive? ")
    vegetarian = input("Is the food vegetarian? ")
    note = input("Additional note? ")
    with open("food_list.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "region", "calorie_warning", "cost", "vegetarian", "note"])
        writer.writerow({"name": name, "region": region, "calorie_warning": calorie_warning, "cost": cost, "vegetarian": vegetarian, "note": note})

def food_reader():
    food = []
    with open("food_list.csv", "r") as file:
        reader = csv.DictReader(file)
        for i, row in enumerate(reader, start=1):
            food.append({"number": i,"name": row["name"], "region": row["region"], "calorie_warning": row["calorie_warning"], "cost": row["cost"],"vegetarian": row["vegetarian"], "note": row["note"]})
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
        writer = csv.DictWriter(file, fieldnames=["name", "region", "calorie_warning", "cost", "vegetarian", "note"])
        writer.writeheader()
        for nf in food:
            writer.writerow({"name": nf["name"], "region": nf["region"], "calorie_warning": nf["calorie_warning"], "cost": nf["cost"], "vegetarian": nf["vegetarian"], "note": nf["note"]})

def generate_random_meal(restrictions, cuisine, budget):
    possible_meals = get_possible_meals(restrictions, cuisine, budget)
    if possible_meals:
        return random.choice(possible_meals)
    else:
        return "Sorry, there are no meals that match your criteria."

def get_possible_meals(restrictions, cuisine, budget):
    possible_meals = ["Asian stir fry", "Vegan burrito bowl", "Gluten-free spaghetti", "Meatloaf"]
    if restrictions:
        possible_meals = [meal for meal in possible_meals if restrictions.lower() in meal.lower()]
    if cuisine:
        possible_meals = [meal for meal in possible_meals if cuisine.lower() in meal.lower()]
    return [meal for meal in possible_meals if get_price(meal) <= budget]

def get_price(meal):
    prices = {"Asian stir fry": 8.99, "Vegan burrito bowl": 9.99, "Gluten-free spaghetti": 12.99, "Meatloaf": 7.99}
    return prices[meal]

main()