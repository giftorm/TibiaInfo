import requests

class Creatures:
    creatures = None
    
    def __init__(self):

    def list(self):
        if not self.creatures:
            self._list_creatures()
        return self.creatures
    
    def _list_creatures(self):
        self.creatures = requests.get