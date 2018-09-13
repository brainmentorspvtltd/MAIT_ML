import webbrowser as web
from datetime import datetime
import os, random

helloIntent = ['hi','hello','hey','hie']

while True:
    usermsg = input("Enter your message : ")

    if usermsg in helloIntent:
        print("Hello user")

    elif usermsg.startswith("open"):
        x = usermsg.split()[1]
        web.open("{}.com".format(x))

    elif usermsg == "time please": 
        currentTime = datetime.now().time()
        print("Time is",currentTime)

    elif usermsg == "play music":
        path = r'C:\Users\asus\Music'
        os.chdir(path)
        for root, folders, files in os.walk(path):
            file = random.choice(files)
            os.startfile(file)
        
    elif usermsg == "bye":
        print("Bye")
        break
    else:
        print("I don't understand")
