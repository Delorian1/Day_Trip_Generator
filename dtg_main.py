import random

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
    
day_trip_start = input("Type space or sea to begin your daytrip! ")

destination_space_list = ["Tomorrowland", "Zagama Beach Saturn", "Olduvai Ruins Mars"]
detination_water_list = ["Atlanis Underwater Theme Park", "Carnival Day Cruise", "Sea World"]

if day_trip_start =="space":
    print(random.choice(destination_space_list))

elif day_trip_start !="space":
    print(random.choice(destination_sea_list))

# As a user, I want a restaurant to randomly selected. 
restaurant_ordinary_list = ["Big Boy", "Carls Junior", "Pei Wei"]
restaurant_exotic_list = ["The Pearl Imporium", "Fishmongers", "Burger International"]

bk_lunch = input("Select a meal plan. Do you feel like the ordinary or exotic?: ")

if bk_lunch == "space":
    print(random.choice(restaurant_ordinary_list)+ " Excellent choice! Let's select your mode of transportation.")
  
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

day_trip_confirmation = input("Would you like to book your all-inclusive daytrip? Type y for yes, n for no: ")

day_trip_confirmation = YES
continue_daytrip = True

while day_trip_confirmation == True:
    if continue_daytrip == True:
       day_trip_confirmation = False
       print("Ok, let's finalize and lock-in your reservation.") 
    else: 
        print("We're sorry for the matches. If at first you don't succeed, try try again.")
        print(your_name_2)
    
# # As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.

day_trip_confirmation =  input(" Would you like to finalize your revervation? Type yes to confirm: ")

if day_trip_confirmation == "yes":
    print(" Your reservation is complete. Please see your reservation details below." + "Thank you for choosing Total Recall Live Action Theme Parks.")
    
# # # As a user, I want to display my completed trip in the console.

if day_trip_confirmation == "yes":
#     print('Great choice! You have selected the {destination_space_list}.\
#             Included in your day trip is the {entertainment_space_list}.\
#                 entertainment package. You will travel in style via {transportation_space_list}.\
#                     You will get a breakfast and lunch pass for one and dine at {}.')


# # # As a developer, I want all of my functions to have a Single Responsibility. Res