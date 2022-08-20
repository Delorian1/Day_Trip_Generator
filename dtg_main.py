import random
from random import choice





# As a developer, I want to make at least three commits with descriptive messages.

# As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment selections in their own separate lists.
# recall_1
destination_space_list = ["Tomorrowland", "Zagama Beach Saturn", "Olduvai Ruins Mars"]
restaurant_space_list = ["Big Boy", "Carls Junior", "Pei Wei"]
transportation_space_list = ["SpaceXMercedes Rocket", "Omni Space Shuttle", "Ark Stargate"]
entertainment_space_list = ["Jet Pack rentals", "Hanging pools", "All ride daypass", "Trackless train sky tours"]

# recall_2
destination_sea_list = ["Atlanis Underwater Theme Park", "Carnival Day Cruise", "Sea World"]
restaurant_sea_list = ["The Pearl Imporium", "Fishmongers", "Burger International"]
transportation_sea_list = ["MagLev Bullet train", "Vegas Submarines", "Torpedo Cruises"]
entertainment_sea_list = ["Mini sub tours", "All day ride pass", "Botanical gardens", "Trench Tours"]



# As a user, I want a destination to be randomly selected for my day trip.
from multiprocessing.context import SpawnContext
from tkinter.messagebox import YES


your_name = input("Please enter your name: ")

def sea_or_space():
    print('Hello ' + your_name + ' Welcome to the Total Recall Live Action ' + 'Theme Parks. Where would you like to go?')
    user_choice = input("Type space or sea to begin your daytrip! ").lower()
    return user_choice
day_trip_start = sea_or_space()

destination_space_list = ["Tomorrowland", "Zagama Beach Saturn", "Olduvai Ruins Mars"]
destination_sea_list = ["Atlanis Underwater Theme Park", "Carnival Day Cruise", "Sea World"]

# function that picks destination based on user shoice of sea or space

def pick_destination():
    if day_trip_start =="space":
        random_destination = random.choice(destination_space_list)
        user_choice = input(f'You have selected {random_destination} our most popular destination out of our Space Odessey line up. Would you like to keep this? y or n ?')
        making_choice == True
        while making_choice ==True:
            if user_choice == "y":
                print(f' {random_destination} has been confirmed. Meal selection is next')
                return random_destination
            elif user_choice =="n":
                random_destination = random.choice(destination_space_list)
                user_choice = input(f'You have selected {random_destination} our most popular destination out of our Space Odessey line up. Would you like to keep this? y or n ?')    
# store choices as a variable  
    
    elif day_trip_start =="sea":
        random_destination = random.choice(destination_sea_list)
        user_choice = input(f'You have selected {random_destination} our most popular destination out of our Space Odessey line up. Would you like to keep this? y or n ?')
        making_choice == True
        while making_choice ==True:
            if user_choice == "y":
                print(f' {random_destination} has been confirmed. Meal selection is next.')
                return random_destination
            elif user_choice =="n":
                random_destination = random.choice(destination_space_list)
                user_choice = input(f'You have selected {random_destination} our most popular destination out of our Space Odessey line up. Would you like to keep this? y or n ?')  

#function call and variable to save return
confirmed_destination = pick_destination()


# As a user, I want a restaurant to randomly selected. 
restaurant_space_list = ["Big Boy", "Carls Junior", "Pei Wei"]
restaurant_sea_list = ["The Pearl Imporium", "Fishmongers", "Burger International"]

bk_lunch = input("Next up meals. Breakfast and lunches are included on all daytrip packages. Please type space or sea to reserve your meal reservation: ").lower()
# function that picks destination based on user shoice of sea or space

def pick_restaurant():
    if bk_lunch =="space":
        random_restaurant = random.choice(restaurant_space_list)
        user_choice = input(f'Yum! You have selected {random_restaurant} to dine at. Would you like to keep this? y or n ?').lower()
        making_choice == True
        while making_choice ==True:
            if user_choice == "y":
                print(f' {random_restaurant} has been confirmed. Up next, transportation.')
                return random_restaurant
            elif user_choice =="n":
                random_restaurant = random.choice(restaurant_space_list)
                user_choice = input(f'Yum! You have selected {random_restaurant} to dine at. Would you like to keep this? y or n ?').lower()
# store choices as a variable  
    
    elif bk_lunch =="sea":
        random_restaurant = random.choice(restaurant_sea_list)
        user_choice = input(f'Yum! You have selected {random_restaurant} to dine at. Would you like to keep this? y or n ?').lower()
        making_choice == True
        while making_choice ==True:
            if user_choice == "y":
                print(f' {random_restaurant} has been confirmed. Up next, transportation.')
                return random_restaurant
            elif user_choice =="n":
                random_restaurant = random.choice(restaurant_sea_list)
                user_choice = input(f'Yum! You have selected {random_restaurant} to dine at. Would you like to keep this? y or n ?')
#function call and variable to save return
confirmed_meals = pick_restaurant()


if day_trip_start == "space":
    print(random.choice(restaurant_space_list) + " Excellent choice! Let's select your mode of transportation.")
  
elif day_trip_start != "space":
    print(random.choice(restaurant_sea_list) + " Excellent choice! Let's select your mode of transportation.")

bk_lunch_confirm = input("Would you like to continue with selection? Type yes or no: ").lower()

# As a user, I want a mode of transportation to be randomly selected for my day trip.

transportation_space_list = ["SpaceX Mercedes Rocket ", "Omni Space Shuttle ", "Ark Stargate "]
transportation_sea_list = ["MagLev Bullet train ", "Vegas Submarines ", "Torpedo Cruises "]

if day_trip_start  == "space":
    print(random.choice(transportation_space_list) + " Fantastic! You'll be traveling in style! Next up, entertainment. ")

elif day_trip_start != "space":
    print(random.choice(transportation_sea_list) + " Fantastic! You'll be traveling in style! Next up, entertainment. ")

transportation_confirmation = input("Would you like to continue with selection? Type yes or no: ").lower()

# # As a user, I want a form of entertainment to be randomly selected for my day trip.

entertainment_space_list = ["Jet Pack rentals ", "Hanging pools ", "All ride daypass ", "Trackless train sky tours "]
entertainment_sea_list = ["Mini sub tours ", "All day ride pass ", "Botanical gardens ", "Trench Tours "]

if day_trip_start  == "space":
    print(random.choice(entertainment_space_list) + "Wow! Are you going to have a blast! Next, let's confirm your reservation.")

elif day_trip_start != "space":
    print(random.choice(entertainment_sea_list) + "Wow! Are you going to have a blast! Next, let's confirm your reservation.")

entertainment_confirmation =  input("Would you like to continue with selection? Type yes or no: ").lower()

# As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.

day_trip_book = input("Would you like to book your all-inclusive daytrip? Type yes or no: ").lower()


#  As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.

day_trip_confirmation =  input("Would you like to finalize your revervation? Type yes to confirm: ").lower()

if day_trip_confirmation == "yes":
    print(" Your reservation is complete. Please see your reservation details below." + "Thank you for choosing Total Recall Live Action Theme Parks.")



# As a user, I want to display my completed trip in the console.
#save itenerary
   

# def day_trip_confirmation():
#     if day_trip_start == "space":
#        print('Great choice! You have selected the' + random.choice().final_destination())

# elif day_trip_start != "space":
#      print('Great choice! You have selected the' + random.choice().final_destination_2())

# As a developer, I want all of my functions to have a Single Responsibility.Remember each function should do just one thing 