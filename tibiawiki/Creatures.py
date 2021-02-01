import requests

class Creatures:
    creatures = None
    get_creatures_uri = "https://tibiawiki.dev/api/creatures/"

    def list(self):
        if not self.creatures:
            self._list_creatures()
        return self.creatures
    
    def _list_creatures(self):
        response = requests.get(self.get_creatures_uri)
        self.creatures = response.json()

if __name__ == "__main__":
    creature = Creatures()
    creature_list = creature.list()
    