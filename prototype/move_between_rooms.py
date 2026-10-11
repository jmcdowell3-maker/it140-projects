
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
