# What should I Eat?
## Video Demo:  <URL HERE>
## Description:
### Why I designed the app:
I have always had troubles when it comes to figuring out what to eat with my friends and coworkers, and using online tools can be too much of a hassle too since I have to type in potential options each time, and it most likely just randomly select 1. Therefore, I wanted to create a project that solves just that! This program is designed to help users decide what to eat for their next meal. It provides several potential options for the user to choose from.

### Features:
1. Randomly choose 1 food from the list (**random_food()** function): This is the simpliest option. Should the user created the list through the in-program option beforehand, the program will list out all potential food options except disliked items from the list and will randomly picks one for the user. 
2. Help users decide by comparing two food (**food_championship()** function): This one is one of the more intersting features. This function will randomly shuffle all food from the list and list 2 foods for users to pick. The winner will be re-added to the list and the loser will be dropped. This is a bit similiar to winning a championship.
3. Randomly Choose 1 from the type of food you feel like eating (**food_filter_menu()** and **food_filter_printer()**): This can help if the user have created too much food entries. It lets user choose from a variety of filters like cuisine syle, high calorie or low calorie food, expensive or cheap food, etc. 
4. Show all food from the list (**food_reader()**): This let user see what have they put in the list.
5. Add new food to the list (**food_writer()**): This function will ask the user a series of question, and add the food into the list. I tried to make it easy and fast food the user to add new food.
6. Delete food from the list (**food_eraser()**): This will return the number and the name of the foods and let user delete the food from the csv file.
7. Set food in the list as favorite(or disliked) (**set_favorite_food()** and **set_disliked_food()**): This will let the user mark their favorite or disliked food. I made it so that this 2 options are mutually exclusive (i.e. if a food is marked favorite, the disliked status will automatically removed). 

### How to use:
Just run the download project.py and food_list.csv and place them in the same folder and run it. You can then add, remove food from the, and use the features to find the food you want to eat. Bon appetit!

### Thank you:
I would like to express my sincere gratitude to Sophy, Elcent, Tim, Tom, and everyone who has encouraged me to learn programming. I wouldn't have thought of this idea if we hadn't gone through great troubles figuring out what to eat. Thank you! 