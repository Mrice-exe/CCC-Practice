txt = input("")

sad = txt.count(":-(")
happy = txt.count(":-)")
if sad + happy == 0:
    print("none")
if happy == sad and sad + happy != 0:
    print("unsure")
if happy > sad:
    print("happy")
if sad > happy:
    print("sad")
