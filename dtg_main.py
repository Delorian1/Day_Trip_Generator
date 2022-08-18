import random
from random import choice





# As a developer, I want to make at least three commits with descriptive messages.

# As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment selections in their own separate lists.
destination_space_list = ["Tomorrowland", "Zagama Beach Saturn", "Olduvai Ruins Mars"]
destination_sea_list = ["Atlanis Underwater Theme Park", "Carnival Day Cruise", "Sea World"]

restaurant_space_list = ["Big Boy", "Carls Junior", "Pei Wei"]
restaurant_sea_list = ["The Pearl Imporium", "Fishmongers", "Burger International"]

transportation_space_list = ["SpaceXMercedes Rocket", "Omni Space Shuttle", "Ark Stargate"]
transportation_sea_list = ["MagLev Bullet train", "Vegas Submarines", "Torpedo Cruises"]

entertainment_space_list = ["Jet Pack rentals", "Hanging pools", "All ride daypass", "Trackless train sky tours"]
entertainment_sea_list = ["Mini sub tours", "All day ride pass", "Botanical gardens", "Trench Tours"]



# As a user, I want a destination to be randomly selected for my day trip.
from multiprocessing.context import SpawnContext
from tkinter.messagebox import YES


your_name = input("Please enter your name: ")

print('Hello ' + your_name + ' Welcome to the Total Recall Live Action ' + 'Theme Parks. Where would you like to go?')
    
day_trip_start = input("Type space or sea to begin your daytrip! ").lower()

destination_space_list = ["Tomorrowland", "Zagama Beach Saturn", "Olduvai Ruins Mars"]
destination_sea_list = ["Atlanis Underwater Theme Park", "Carnival Day Cruise", "Sea World"]


if day_trip_start =="space":
    print(random.choice(destination_space_list))

# store choices as a variable

elif day_trip_start !="space":
    print(random.choice(destination_sea_list))

day_trip_confirm = input("Would you like to continue with selection? Type yes or no: ").lower()


# As a user, I want a restaurant to randomly selected. 
restaurant_space_list = ["Big Boy", "Carls Junior", "Pei Wei"]
restaurant_sea_list = ["The Pearl Imporium", "Fishmongers", "Burger International"]

bk_lunch = input("Would you like the space or sea menu? Type space or sea: ").lower()

if bk_lunch == "space":
    print(random.choice(restaurant_space_list) + " Excellent choice! Let's select your mode of transportation.")
  
elif bk_lunch != "space":
    print(random.choice(restaurant_sea_list) + " Excellent choice! Let's select your mode of transportation.")

bk_lunch_confirm = input("Would you like to continue with selection? Type yes or no: ").lower()

# while bk_lunch_confirm == "yes"
#     continue

# elif bk_lunch_confirm == "yes"
 


# As a user, I want a mode of transportation to be randomly selected for my day trip.

transportation_space_list = ["SpaceX Mercedes Rocket ", "Omni Space Shuttle ", "Ark Stargate "]
transportation_sea_list = ["MagLev Bullet train ", "Vegas Submarines ", "Torpedo Cruises "]

if day_trip_start  == "space":
    print(random.choice(transportation_space_list) + " Fantastic! You'll be traveling in style! Next up, entertainment. ")

elif day_trip_start != "space":
    print(random.choice(transportation_sea_list) + " Fantastic! You'll be traveling in style! Next up, entertainment. ")

# transportation_confirmation = input("Would you like to continue with selection? Type yes or no: ").lower()

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

def calc:
    return restart()
def restart():
    while True:
        again =  input("Would you like to book your all-inclusive daytrip? Type yes or no: ")
        if again not in {"yes", "no"}:
            print ("Please enter valid option





#  As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.

day_trip_confirmation =  input("Would you like to finalize your revervation? Type yes to confirm: ").lower()

if day_trip_confirmation == "yes":
    print(" Your reservation is complete. Please see your reservation details below." + "Thank you for choosing Total Recall Live Action Theme Parks.")


choice_destination_space_list = choice(destination_space_list)
choice_destination_sea_list = choice(destination_sea_list)

choice_restaurant_space_list = choice(restaurant_space_list)
choice_restaurant_sea_list = choice(restaurant_sea_list)

choice_transportation_space_list = choice(transportation_space_list)
choice_transportation_sea_list = choice(transportation_sea_list)

choice_entertainment_space_list = choice(entertainment_space_list)
choice_entertainment_sea_list = choice(entertainment_sea_list)




print("You have chosen "+ "Destination:" + choice(destination_space_list) or choice(destination_sea_list))
print("You will dine in style at " + "Dining: " + choice(restaurant_ordinary_list) or choice(restaurant_exotic_list))
print("You will picked up at the port of call and taken to your destination via " + "Transportation" + choice(transportation_space_list) or choice(transportation_water_list))
print("Your all inclusive daytrip will include an entertainment package: " + "Entertanment" + choice(entertainment_space_list) or choice(entertainment_sea_list))
print("Thank you for booking your daytrip with Total Recall Live Action Theme Parks where we make your dreams a reality!")


# As a user, I want to display my completed trip in the console.
#save itenerary
   

# def day_trip_confirmation():
#     if day_trip_start == "space":
#        print('Great choice! You have selected the' + random.choice().final_destination())

# elif day_trip_start != "space":
#      print('Great choice! You have selected the' + random.choice().final_destination_2())

# As a developer, I want all of my functions to have a Single Responsibility.Remember each function should do just one thing