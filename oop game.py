# Declaring a class
class GameObject:
    name = ""
    appearance = ""
    feel = ""
    smell = ""

    # Initializer
    def __init__(self, name, appearance, feel, smell):
        self.name = name
        self.appearance = appearance
        self.feel = feel
        self.smell = smell

    # Return string describing object appearance
    def look(self):
        return f"You look at the {self.name}. {self.appearance}\n"
    # Return string describing object feel 
    def touch(self):
        return f"You touch the {self.name}. {self.feel}\n"
    # Return string describing smell
    def sniff(self):
        return f"You sniff the {self.name}. {self.smell}\n"
    
class Room:

    escape_code = 0
    game_objects = []

    # set up an instance of a Room with escape_code and game_objects
    def __init__(self, escape_code, game_objects):
        self.escape_code = escape_code
        self.game_objects = game_objects

    # return true if code matches the escape_code and false otherwise
    def check_code(self, code):
        return self.escape_code == code
    
    # return a list of the names of game_objects
    def get_game_object_names(self):
        names = []
        for object in self.game_objects:
            names.append(object.name)
        return names

class Game:

    def __init__(self):
        self.attempts = 0
        objects = self.create_objects()
        self.room = Room(731, objects)

    def create_objects(self):
        return [          
            GameObject(
            "Sweater",
            "It's a blue sweater that had the number 12 switched on it.",
            "Someone has unstitched the second number, leaving only the 1.",
            "The sweater smells of laundry detergent."),
          GameObject(
            "Chair", 
            "It's a wooden chair with only 3 legs.",
            "Someone had deliberately snapped off one of the legs.",
            "It smells like old wood."),
          GameObject(
            "Journal",
            "The final entry states that time should be hours then minutes then seconds (H-M-S).",
            "The cover is worn and several pages are missing.",
            "It smells like musty leather."),
          GameObject(
            "Bowl of soup", 
            "It appears to be tomato soup.",
            "It has cooled down to room temperature.",
            "You detect 7 different herbs and spices."),
          GameObject(
            "Clock", 
            "The hour hand is pointing towards the soup, the minute hand towards the chair, and the second hand towards the sweater.",
            "The battery compartment is open and empty.",
            "It smells of plastic."),
        ]

    def take_turn(self):
        prompt = self.get_room_prompt()
        selection = input(prompt)
        print(selection)

    def get_room_prompt(self):
        prompt = "Enter the 3 digit lock code or choose an item to interact with:\n"
        names = self.room.get_game_object_names()
        index = 1 
        for name in names:
            prompt += f"{index}. {name}\n"
            index += 1
        return prompt

game = Game()
game.take_turn()