
# Robinson High School Adventure Game
# IT 140 Milestone - Room Movement and Item Collection

# A dictionary that connects each room to its available directions.
rooms = {
    "Outside Administration": {"east": "Administration Office"},
    "Administration Office": {"west": "Outside Administration",
                              "south": "Library"},
    "Library": {"north": "Administration Office",
                "south": "History Room"},
    "History Room": {"north": "Library",
                     "east": "Science Room"},
    "Science Room": {"west": "History Room",
                     "south": "English Room"},
    "English Room": {"north": "Science Room",
                     "east": "Shop Room"},
    "Shop Room": {"west": "English Room",
                  "south": "Math Room"},
    "Math Room": {"north": "Shop Room",
                  "west": "Cafeteria"},
    "Cafeteria": {"east": "Math Room"}
}

# Each room contains one item, except the starting room and cafeteria.
room_items = {
    "Administration Office": "map",
    "Library": "book",
    "History Room": "armor",
    "Science Room": "potion",
    "English Room": "spell",
    "Shop Room": "sword",
    "Math Room": "power boost"
}

# List of all seven items required to defeat Demon Joc.
required_items = [
    "map", "book", "armor", "potion",
    "spell", "sword", "power boost"
]

# Track the player's location and collected items.
current_room = "Outside Administration"
inventory = []

# Display the game introduction.
print("Welcome to Robinson High School!")
print("Demon Joc has taken over the cafeteria.")
print("Collect all seven items to defeat Demon Joc.")
print("Enter a direction, such as 'go east', to move.")
print("Enter 'get' followed by an item name to collect it.")
print("Enter 'exit' to quit the game.")

# Continue playing until the player exits or reaches the cafeteria.
while current_room not in ("Cafeteria", "exit"):

    print("\nYou are currently in:", current_room)

    # Show the available item, if there is one in this room.
    if current_room in room_items:
        item = room_items[current_room]

        if item not in inventory:
            print("You see a", item, "in this room.")
            print("Enter 'get", item, "' to collect it.")
        else:
            print("You have already collected the", item + ".")

    # Display available directions.
    print("Available directions:",
          ", ".join(rooms[current_room].keys()))

    command = input(
        "Enter your command (go direction, get item, or exit): "
    ).strip().lower()

    # Exit the game.
    if command == "exit":
        current_room = "exit"
        print("You have exited the game.")

    # Collect an item from the current room.
    elif command.startswith("get "):
        requested_item = command[4:].strip()

        if current_room in room_items:
            item = room_items[current_room]

            if requested_item == item:
                if item not in inventory:
                    inventory.append(item)
                    print("You collected the", item + "!")
                else:
                    print("You already collected the", item + ".")
            else:
                print("Invalid item. That item is not in this room.")
        else:
            print("There is no item to collect in this room.")

    # Handle movement commands such as "go north" or "north".
    elif command.startswith("go ") or command in (
        "north", "south", "east", "west"
    ):
        if command.startswith("go "):
            direction = command[3:].strip()
        else:
            direction = command

        # Check whether the direction is valid from this room.
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
            print("You moved", direction + ".")
            print("You are now in:", current_room)
        else:
            print("You cannot move in that direction from this room.")
            print("Please choose an available direction.")

    # Handle any command that is not recognized.
    else:
        print("Invalid command.")
        print("Enter a direction, 'get item', or 'exit'.")

# Check the outcome when the player reaches the cafeteria.
if current_room == "Cafeteria":
    print("\nYou have entered the Cafeteria!")
    print("Demon Joc is waiting for you!")

    if all(item in inventory for item in required_items):
        print("You collected all seven items!")
        print("You used your items to defeat Demon Joc!")
        print("Congratulations! You saved Robinson High School!")
    else:
        missing_items = [
            item for item in required_items if item not in inventory
        ]
        print("You did not collect all seven items.")
        print("Missing items:", ", ".join(missing_items))
        print("Demon Joc defeats you!")
        print("Game over.")

print("\nThank you for playing!")

