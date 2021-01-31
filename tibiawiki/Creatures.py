class Creatures:
    creatures = None
    
    def __init__(self):
        self.creatures = []

    def list(self):
        if not self.creatures:
            self.creatures = [ "Charizard", "Pikachu" ]
        return self.creatures