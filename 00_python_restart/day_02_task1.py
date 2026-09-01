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
    print("Total room revenue: ", total_room_rev)
    print("Average room revenue: ", total_room_rev/ no_of_rooms)

def get_food_revenue():
    """
      gets total food revenue
    """
    total_no_food_bills_generated = int(input("Enter total number of food bills generated: "))
    total_food_rev = 0

    while total_no_food_bills_generated != 0:
        walk_in_dining = int(input("Please enter number of walk in guest for food: "))
        for walk in range(1, walk_in_dining+1):
            total_food_rev += float(input(f"Total Amount for walk in guest on table no {walk}: "))
        total_no_food_bills_generated -= walk_in_dining

        print("\n")
        print("------------")

        room_food = int(input("Please enter number of rooms that ordered room service: "))
        for room_no in range(1, room_food+1):
            total_food_rev += float(input(f"Total Amount for room number {room_no}"))
        total_no_food_bills_generated -= room_food

        print("\n")
        print("------------")

        if total_no_food_bills_generated != 0:
             print("Enter correc information")
        else:
             print("Total food revenue: ", total_food_rev)





      
print("Welcome to my application")
# get_room_rev(int(input("Please enter number of rooms occupied today: ")))
get_food_revenue()