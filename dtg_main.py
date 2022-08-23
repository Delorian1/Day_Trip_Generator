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

#-------------------------------------------------------------------------------------------------------
# function that picks destination based on user shoice of sea or space

destination_space_list = ["Tomorrowland", "Zagama Beach Saturn", "Olduvai Ruins Mars"]
destination_sea_list = ["Atlanis Underwater Theme Park", "Carnival Day Cruise", "Sea World"]

def pick_destination():
    if day_trip_start == "space":
        random_destination = random.choice(destination_space_list)
        user_choice = input(f'You have selected {random_destination} our most popular destination out of our Space Odessey line up. Would you like to keep this? y or n ? ').lower()
        making_choice = True
        while making_choice == True:
            if user_choice == "y":
                print(f'{random_destination} has been confirmed. Meal selection is next')
                return random_destination
            elif user_choice == "n":              
                random_destination = random.choice(destination_space_list)
                user_choice = input(f'You have selected {random_destination} our most popular destination out of our Space Odessey line up. Would you like to keep this? y or n ? ').lower()    
# store choices as a variable  
    
    elif day_trip_start == "sea":
        random_destination = random.choice(destination_sea_list)
        user_choice = input(f'You have selected {random_destination} our most popular destination out of our Iliad line up. Would you like to keep this? y or n ? ').lower()
        making_choice = True

        while making_choice == True:
            if user_choice == "y":
                print(f'{random_destination} has been confirmed. Meal selection is next.')
                return random_destination
            elif user_choice == "n":
                random_destination = random.choice(destination_space_list)
                user_choice = input(f'You have selected {random_destination} our most popular destination out of our Iliad line up. Would you like to keep this? y or n ? ').lower()  

#function call and variable to save return
confirmed_destination = pick_destination()
# #--------------------------------------------------------------------------------------------------------
# # As a user, I want a restaurant to randomly selected. 

restaurant_space_list = ["Big Boy", "Carls Junior", "Pei Wei"]
restaurant_sea_list = ["The Pearl Imporium", "Fishmongers", "Burger International"]

bk_lunch = input("Breakfast and lunches are included on all daytrip packages. Please type space or sea to reserve your meal reservation: ").lower()
# function that picks destination based on user shoice of sea or space

def pick_restaurant():
    if bk_lunch == "space":
        random_restaurant = random.choice(restaurant_space_list)
        user_choice = input(f'Yum! You have selected {random_restaurant} for your meal package. Would you like to keep this? y or n ? ').lower()
        making_choice = True
        while making_choice == True:
            if user_choice == "y":
                print(f'{random_restaurant} has been confirmed. Lets select your mode of transportation.')
                return random_restaurant
            elif user_choice == "n":
                random_restaurant = random.choice(restaurant_space_list)
                user_choice = input(f'Yum! You have selected {random_restaurant} for your meal package. Would you like to keep this? y or n ? ').lower()
# # store choices as a variable  
    
    elif bk_lunch =="sea":
        random_restaurant = random.choice(restaurant_sea_list)
        user_choice = input(f'Yum! You have selected {random_restaurant} to dine at. Would you like to keep this? y or n ? ').lower()
        making_choice = True
        while making_choice == True:
            if user_choice == "y":
                print(f'{random_restaurant} has been confirmed. Lets select your mode of transportation.')
                return random_restaurant
            elif user_choice == "n":
                random_restaurant = random.choice(restaurant_sea_list)
                user_choice = input(f'Yum! You have selected {random_restaurant} to dine at. Would you like to keep this? y or n ? ').lower()
#function call and variable to save return
confirmed_meals = pick_restaurant()

#--------------------------------------------------------------------------------------------------------

# As a user, I want a mode of transportation to be randomly selected for my day trip.

# if day_trip_start  == "space":
#     print(random.choice(transportation_space_list) + " Fantastic! You'll be traveling in style! Next up, entertainment. ")

# elif day_trip_start != "space":
#     print(random.choice(transportation_sea_list) + " Fantastic! You'll be traveling in style! Next up, entertainment. ")

# # transportation_confirmation = input("Would you like to continue with selection? Type yes or no: ").lower()
transportation_space_list = ["SpaceX Mercedes Rocket ", "Omni Space Shuttle ", "Ark Stargate "]
transportation_sea_list = ["MagLev Bullet train ", "Vegas Submarines ", "Torpedo Cruises "]

transportation_start = input("You will leave from a predetermined port of call before traveling to your destination. Please type sea or space to begin: ").lower()

def pick_transportation():
    if transportation_start == "space":
        random_transportation = random.choice(transportation_space_list)
        user_choice = input(f'You have selected {random_transportation}. ' + "Fantastic! You'll be traveling in style using our state of the art travel systems! " + "Would you like to keep this? y or n ? ").lower()
        making_choice = True
        while making_choice == True:
            if user_choice == "y":
                print(f' {random_transportation} has been confirmed. Next up, entertainment.')
                return random_transportation
            elif user_choice == "n":
                random_transportation = random.choice(transportation_space_list)
                user_choice = input(f'You have selected {random_transportation}.' + "Fantastic! You'll be traveling in style using our state of the art travel systems!" + "Would you like to keep this? y or n ?").lower()   
# store choices as a variable  
    
    elif transportation_start == "sea":
        random_transportation = random.choice(transportation_sea_list)
        user_choice = input(f'You have selected {random_transportation}. ' + "Fantastic! You'll be traveling in style using our state of the art travel systems! " + "Would you like to keep this? y or n ? ").lower()
        making_choice = True
        while making_choice == True:
            if user_choice == "y":
                print(f'{random_transportation} has been confirmed. Next up, entertainment.')
                return random_transportation
            elif user_choice == "n":
                random_transportation = random.choice(transportation_sea_list)
                user_choice = input(f'You have selected {random_transportation}.' + "Fantastic! You'll be traveling in style using our state of the art travel systems!" + "Would you like to keep this? y or n ?").lower()

# #function call and variable to save return
confirmed_transportation = pick_transportation()

# #------------------------------------------------------------------------------
# # # As a user, I want a form of entertainment to be randomly selected for my day trip.

# entertainment_space_list = ["Jet Pack rentals ", "Hanging pools ", "All ride daypass ", "Trackless train sky tours "]
# entertainment_sea_list = ["Mini sub tours ", "All day ride pass ", "Botanical gardens ", "Trench Tours "]

# # if entertainment_start  == "space":
# #     print(random.choice(entertainment_space_list) + "Wow! You are going to love your entertainment package with free replay! Next, let's confirm your reservation.")

# # elif entertainment_start != "space":
# #     print(random.choice(entertainment_sea_list) + "Wow! Are you going to have a blast! Next, let's confirm your reservation.")

# # entertainment_confirmation =  input("Would you like to continue with selection? Type yes or no: ").lower()
# #-----------------------------------------------------------------------------------------------------------
entertainment_space_list = ["Jet Pack rentals ", "Hanging pools ", "All ride daypass ", "Trackless train sky tours "]
entertainment_sea_list = ["Mini sub tours ", "All day ride pass ", "Botanical gardens ", "Trench Tours "]

entertainment_start = input("Our entertainment packages are all complementary for new customers. Please type space or sea to reserve your entertainment package: ").lower()

def pick_entertainment():
    if entertainment_start =="space":
        random_entertainment = random.choice(entertainment_space_list)
        user_choice = input(f'You have selected {random_entertainment}. You are going to love your entertainment package with free replay! Would you like to keep this? y or n ? ').lower()
        making_choice = True
        while making_choice == True:
            if user_choice == "y":
                print(f'You have confirmed {random_entertainment}. Meal selection is next')
                return random_entertainment
            elif user_choice == "n":
                random_entertainment = random.choice(entertainment_space_list)
                user_choice = input(f'You have selected our {random_entertainment} package. You are going to love your entertainment package with free replay! Would you like to keep this? y or n ? ').lower()    
 # store choices as a variable  
    
    elif entertainment_start == "sea":
        random_entertainment = random.choice(entertainment_sea_list)
        user_choice = input(f'You have selected our {random_entertainment} package. You are going to love your entertainment package with free replay! Would you like to keep this? y or n ? ').lower()
        making_choice = True
        while making_choice == True:
            if user_choice == "y":
                print(f' {random_entertainment} package. You are going to love your entertainment package with free replay! Would you like to keep this? y or n ? ').lower() 
                return random_entertainment
            elif user_choice == "n":
                random_entertainment = random.choice(entertainment_space_list)
                user_choice = input(f'You have selected our {random_entertainment} package. You are going to love your entertainment package with free replay! Would you like to keep this? y or n ? ').lower()  

#function call and variable to save return
confirmed_entertainment = pick_entertainment()

# #-------------------------------------------------------------------------------------------------
# # `# As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.

# # day_trip_book = input("Would you like to book your all-inclusive daytrip? Type yes or no: ").lower()


# # #  As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.

# # day_trip_confirmation =  input("Would you like to finalize your revervation? Type yes to confirm: ").lower()

# #if day_trip_confirmation == "yes":
print(" Your reservation is complete. Please see your itenerary below." + "Thank you for choosing Total Recall Live Action Theme Parks.")
print(f'Thank you for confirming your choices.' + 'Destination {confirmed_destination}.' + 'Breakfast and lunch will be catered by {confirmed_meals}.' + 'Your transportation will be via {confirmed_transportation}.' + 'You have selected the {confirmed_entertainment} package.')


# As a user, I want to display my completed trip in the console.
#save itenerary
   

# def day_trip_confirmation():
#     if day_trip_start == "space":
#        print('Great choice! You have selected the' + random.choice().final_destination())

# elif day_trip_start != "space":
#      print('Great choice! You have selected the' + random.choice().final_destination_2())

# As a developer, I want all of my functions to have a Single Responsibility.Remember each function should do just one thing 