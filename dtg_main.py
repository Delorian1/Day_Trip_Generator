import random
from random import choice


# As a developer, I want to make at least three commits with descriptive messages.

# As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment selections in their own separate lists.

destination_space_list = ["Tomorrowland", "Zagama Beach Saturn", "Olduvai Ruins Mars"]
destination_sea_list = ["Atlanis Underwater Theme Park", "Carnival Day Cruise", "Sea World"]

restaurant_ordinary_list = ["Big Boy", "Carls Junior", "Pei Wei"]
restaurant_exotic_list = ["The Pearl Imporium", "Fishmongers", "Burger International"]

transportation_space_list = ["SpaceXMercedes Rocket", "Omni Space Shuttle", "Ark Stargate"]
transportation_water_list = ["MagLev Bullet train", "Vegas Submarines", "Torpedo Cruises"]

entertainment_space_list = ["Jet Pack rentals", "Hanging pools", "All ride daypass", "Trackless train sky tours"]
entertainment_sea_list = ["mini sub tours", "All day ride pass", " Botanical gardens", "Trench Tours"]

# As a user, I want a destination to be randomly selected for my day trip.
from multiprocessing.context import SpawnContext
from tkinter import Y
from tkinter.messagebox import YES

your_name = input("Please enter your name: ")
print('Hello ' + your_name + ' Welcome to the Total Recall Live Action ' + 'Theme Parks. Where would you like to go?')
    
day_trip_start = input("Type space or sea to begin your daytrip! ").lower()

destination_space_list = ["Tomorrowland", "Zagama Beach Saturn", "Olduvai Ruins Mars"]
detination_water_list = ["Atlanis Underwater Theme Park", "Carnival Day Cruise", "Sea World"]

if day_trip_start =="space":
    print(random.choice(destination_space_list))

# store choices as a variable

elif day_trip_start !="space":
    print(random.choice(destination_sea_list))

# As a user, I want a restaurant to randomly selected. 
restaurant_ordinary_list = ["Big Boy", "Carls Junior", "Pei Wei"]
restaurant_exotic_list = ["The Pearl Imporium", "Fishmongers", "Burger International"]

bk_lunch = input("Select a meal plan. Do you feel like the ordinary or exotic?: ").lower()

if bk_lunch == "space":
    print(random.choice(restaurant_ordinary_list) + " Excellent choice! Let's select your mode of transportation.")
  
elif bk_lunch != "space":
    print(random.choice(restaurant_exotic_list) + " Excellent choice! Let's select your mode of transportation.")


# # As a user, I want a mode of transportation to be randomly selected for my day trip.

transportation_space_list = ["SpaceX Mercedes Rocket ", "Omni Space Shuttle ", "Ark Stargate "]
transportation_water_list = ["MagLev Bullet train ", "Vegas Submarines ", "Torpedo Cruises "]

if day_trip_start  == "space":
    print(random.choice(transportation_space_list) + " Fantastic! You'll be traveling in style! Next up, entertainment. ")

elif day_trip_start != "space":
    print(random.choice(transportation_water_list) + " Fantastic! You'll be traveling in style! Next up, entertainment. ")

# # As a user, I want a form of entertainment to be randomly selected for my day trip.

entertainment_space_list = ["Jet Pack rentals ", "Hanging pools ", "All ride daypass ", "Trackless train sky tours "]
entertainment_water_list = ["mini sub tours ", "All day ride pass ", " Botanical gardens ", "Trench Tours "]

if bk_lunch  == "ordinary":
    print(random.choice(entertainment_space_list) + "Wow! Are you going to have a blast! Next, let's confirm your reservation.")

elif bk_lunch != "ordinary":
    print(random.choice(entertainment_water_list) + "Wow! Are you going to have a blast! Next, let's confirm your reservation.")


# As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.

play_again = input("Would you like to book your all-inclusive daytrip? Type yes or no: ").lower()
if play_again == "yes":
    print("Great, let's finalize and lock-in your reservation.") 

elif play_again != "yes":
     print("Sorry to see that the choices were not to your liking. Do you wish to try again? Type yes or no.")


def play_again(): 
    play_again = input("Do you wish to try again? Type yes or no: ") 
       
if play_again == "yes":
    return input("Please enter your name: ")
  
    
#  As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.

day_trip_confirmation=  input(" Would you like to finalize your revervation? Type yes to confirm: ").lower()

if day_trip_confirmation == "yes":
    print(" Your reservation is complete. Please see your reservation details below." + "Thank you for choosing Total Recall Live Action Theme Parks.")
    
# # # As a user, I want to display my completed trip in the console.

# def day_trip_confirmation():
#     if day_trip_start == "space":
#        print('Great choice! You have selected the' + random.choice().final_destination())

#     # elif day_trip_start != "space":
#     #      print('Great choice! You have selected the' + random.choice().final_destination_2())

# # As a developer, I want all of my functions to have a Single Responsibility. Rember each function should do just one thing!