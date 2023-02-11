#day tip generator
import random
def day_trip_generator():
    #list of destinations
    destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
    #list of restaurants
    restaurants = ["Chez Nous", "Burger King", "McDonalds", "Taco Bell", "KFC"]
    #list of modes of transportation
    transportation = ["car", "plane", "train", "bus", "bike"]
    #list of entertainment
    entertainment = ["movie", "concert", "museum", "zoo", "park"]
    #randomly select a destination, restaurant, mode of transportation, and form of entertainment
    destination = random.choice(destinations)
    restaurant = random.choice(restaurants)
    transportation = random.choice(transportation)
    entertainment = random.choice(entertainment)
    #print the results
    print("Your trip will be to " + destination + " and you will eat at " + restaurant + " and you will travel by " + transportation + " and you will visit a " + entertainment + "!")
    #ask the user if they are satisfied with the trip
    satisfied = input("Are you satisfied with your trip? (yes/no)")
    #if the user is satisfied, end the program
    if satisfied == "yes":
        print("Enjoy your trip!")
    #if the user is not satisfied, run the program again
    elif satisfied == "no":
        day_trip_generator()
    #if the user inputs something other than yes or no, end the program
    else:
        print("Invalid input. Please try again.")
day_trip_generator()    

  #end of program
