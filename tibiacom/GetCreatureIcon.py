import requests
import shutil
import pprint
import os

class GetCreatureIcon:
    basic_url = "https://static.tibia.com/images/library/"

    def __init__(self, name):
        self.name = name

    def get_icon(self):
        url = self.basic_url + self._convert_name()
        print(url + "\n")

        file_name = url.split("/")[-1]
        r = requests.get(url, stream = True)
         # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        if r.status_code == 200:
            r.raw.decode_content = True

            data_folder = os.path.join("icons")
            file_to_open = os.path.join(data_folder, file_name)
            print("folder: " + file_to_open + "\n")
            # Open a local file with wb ( write binary ) permission.
            with open(file_to_open, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
                
            print('Image sucessfully Downloaded: ',file_to_open)
        else:
            print('Image Couldn\'t be retreived')

    def _convert_name(self):
        return self.name.lower().replace(" ", "") + ".gif"
        

if __name__ == "__main__":
    creature_image = GetCreatureIcon("Acid Blob")
    creature_image.get_icon()