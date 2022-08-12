# As a developer, I want to make at least three commits with descriptive messages.

# As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment selections in their own separate lists.
destination_space_list = ["Tomorrowland," Zagama Beach Saturn","Olduvai Ruins Mars"]
detination_water_list = ["Atlanis Underwater Theme Park," "Sea World"]

restaurant_space_list = ["Big Boy,"Carls Junior", "Pei Wei"]
restaurant_water_list = ["The Pearl Imporium,"Fishmongers,"Long John Silvers "]

restaurant_space_list = ["Big Boy,"Carls Junior", "Pei Wei"]
restaurant_water_list = ["The Pearl Imporium,"Fishmongers,"Long John Silvers "]

entertainment_space_list = ["Jet Pack rentals," "Hanging pools," "All ride daypass," "Trackless train tours"]
entertainment_water_list = ["mini sub tours," "All day ride pass," " Botanical gardens," "Trench Tours"]

# As a user, I want a destination to be randomly selected for my day trip.
from tkinter import Y
from tkinter.messagebox import YES


day_trip = input("Welcome to Total Recall Live Action Theme Parks. Where yould you like to go? Type Space or Sea to begin your daytrip!")

destination_space_list = ["Tomorrowland," Zagama Beach Saturn","Olduvai Ruins Mars"]
detination_water_list = ["Atlanis Underwater Theme Park," "Sea World"]
 if input = "space"
     item = random.choice(tuple(destination_space_list))
     print(item)
elif input = "water"
     item = random.choice(tuple(detination_water_list))
     print(item)
# As a user, I want a restaurant to be randomly selected for my day trip.

restaurant_space_list = ["Big Boy,"Carls Junior", "Pei Wei"]
restaurant_water_list = ["The Pearl Imporium,"Fishmongers,"Long John Silvers "]


# As a user, I want a mode of transportation to be randomly selected for my day trip.

transportation_space_list = ["SpaceXMercedes Rocket," "Space Shuttle, "Ark Stargate"]
transportation_water_list = ["MagLev Bullet train," "Vegas Submarines," "Torpedo Cruises"]

# As a user, I want a form of entertainment to be randomly selected for my day trip.

entertainment_space_list = ["Jet Pack rentals," "Hanging pools," "All ride daypass," "Trackless train tours"]
entertainment_water_list = ["mini sub tours," "All day ride pass," " Botanical gardens," "Trench Tours"]
# As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.
day_trip_confirmation =  input(" Would you like to confirm revervation? Type Y for Yes / N for No")
    if day_trip_confirmation = Y
        print("Great choice! You have selected the {destination_space_list}. Included in your day trip is the {entertainment_space_list} entertainment package You will travel in style via {transportation_space_list}. You will get a breakfast and lunch pass for one and dine at {}. ")

    else:
        print(day_trip)
# As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.
day_trip_complete = input("Do you wish to complete your reservation? Type Y for yes / N for No.")
# As a user, I want to display my completed trip in the console.

# As a developer, I want all of my functions to have a Single Responsibility. Res