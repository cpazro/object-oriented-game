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

    def __init__(self, escape_code, game_objects):
        self.escape_code = escape_code
        self.game_objects = game_objects

    def check_code(self, code):
        return self.escape_code == code
    
    def get_game_object_names(self):
        names = []
        for object in self.game_objects:
            names.append(object.name)
        return names