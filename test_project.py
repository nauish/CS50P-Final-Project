from project import random_food, food_reader, food_filter_printer

def test_random_food():
    food_choice = food_reader()
    assert random_food(food_choice) in food_reader()
    assert random_food("Taiwanese")['name'] in ["Oyster omelette", "Braised pork rice", "Boba tea"]

#Test if food_reader function would read every food from the list
def test_food_reader():
    food = food_reader()
    assert len(food) == 8

#Test if food_filter_printer function would read only food in the category user specified, and if it would return full list if user has given a parameter that has no food
def test_food_filter_printer():
    foods = food_reader()
    filtered_foods = food_filter_printer(foods,"Taiwanese")
    assert len(filtered_foods) == 3
    filtered_foods_no = food_filter_printer(foods,"Japanese")
    assert len(filtered_foods_no) == 8

