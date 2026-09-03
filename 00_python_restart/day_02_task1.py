# no_of_rooms_occ = int(input("Number of rooms occupied: "))
# total_rev = 0

# for each_room in range(1, no_of_rooms_occ + 1):
#     price = float(input(f"Enter price for room no {each_room}: "))
#     total_rev += price

# food_rev = float(input("Food revenue: "))
# other_rev = float(input("Other revenue: "))

# print("Total revenue: ", total_rev + food_rev + other_rev)

def get_room_rev(no_of_rooms):
    """
    input no of rooms and sums up total and average room revenue
    """
    total_room_rev = 0
    for each_room_no in range(1, no_of_rooms+1):
            price = float(input(f"Enter price for room no {each_room_no}: "))
            total_room_rev += price
    print("\n")
    print("------------")
    # print("Total room revenue: ", total_room_rev)
    # print("Average room revenue: ", total_room_rev/ no_of_rooms)
    return total_room_rev

def get_food_revenue():

    """
      gets total food revenue
    """

    total_no_food_bills_generated = int(input("Enter total number of food bills generated: "))
    total_food_rev = 0
    walk_in_bills =int(input("Enter total number of walk in bills"))
    for tableno in range(1, walk_in_bills+1):
        amt = float(input(f"Please enter total amount for table number {tableno}:"))
        total_food_rev += amt
    room_food = int(input("Please enter number of rooms that ordered room service: "))
    for roomno in range(1, room_food+1):
            amt = float(input(f"Please enter total amount for room number {roomno}: "))
            total_food_rev += amt
    remaining_food = 0
    while walk_in_bills + room_food+ remaining_food != total_no_food_bills_generated:
        total_food_rev += float(input("please enter remaining food bill amount: "))
        remaining_food += 1

    return total_no_food_bills_generated, total_food_rev, room_food, walk_in_bills

def display(no_of_rooms, total_room_rev, total_no_food_bills_generated, total_food_rev, room_food, walk_in_bills):

     """
     Displays in detail information of revenue for the day
     """
     # display room information
     print("\n")
     print("------------")
     print("ROOM INFORMATION")
     print("------------")
     print(f"Total number of rooms: {no_of_rooms}")
     print(f"Total room revenue: {total_room_rev}")
     print(f"Average room revenue: {total_room_rev / no_of_rooms}")

     # display food information
     print("\n")
     print("------------")
     print("FOOD INFORMATION")
     print("------------")
     print(f"Total number of food bills today: {total_no_food_bills_generated}")
     print(f"Total amount of food: {total_food_rev}")
     print(f"Total number of walk in bills: {walk_in_bills}")
     print(f"Total number of room service bills: {room_food}")


      
print("Welcome to my application")
try:
    no_of_rooms = int(input("Please enter number of rooms occupied today: "))
    if no_of_rooms <= 0:
        raise ValueError("The number must be greater than zero!")
    
except ValueError:
    print("Invalid input. Please enter a valid number.")

else:
    total_room_rev = get_room_rev(no_of_rooms)
    total_no_food_bills_generated, total_food_rev, room_food, walk_in_bills = get_food_revenue()
    display(no_of_rooms, total_room_rev, total_no_food_bills_generated, total_food_rev, room_food, walk_in_bills)