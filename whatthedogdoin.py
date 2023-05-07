import random
import time
import json
from PIL import Image
from playsound import playsound


# img = Image.open("WHAT THE DOG DOIN.jpg")

# img.show()

minsec = 2
maxsec = 20

print("WHAT THE DOG DOIN LOADED")


try:
  with open("config.json", "r") as f:
    data = json.loads(f.read())
    
    minsec = data["minsec"]
    maxsec = data["maxsec"]
except Exception as e:
  print("ERROR: " + e)


# thread = threading.Thread(target=settings)
# thread.start()

while True:
  playsound("audio.mp3", False)
  img = Image.open("WHAT THE DOG DOIN.jpg")
  img.show()
  time.sleep(random.randint(minsec, maxsec))