from Speech import *
from Speaker import *
import pandas as pd
import time
import re

data = pd.read_excel("Sikkim.xlsx")
ending = 1
pa = data["Main_Attractions"]

def trial(name):
    global pa
    ma = data[name]
    ma = dict(ma)
    ma = [*ma.values()]
    print(ma)
    if name == "Distance from Delhi by Car(km)":
        pa = dict(pa)
        pa = [*pa.values()]
        voice_assist("The distance is as follows", ":~")
        for i in ma:
            for j in pa:
                voice_assist(j, ":- ")
                pa.remove(j)
                break
            voice_assist(i + "km")


def gretting():
    voice_assist("Hello, How May i Help You")


def get_attractions():
    voice_assist("Main Attractions of Sikkim are", ":~")
    for i in pa:
        voice_assist(i)


def get_distance():
    name = "Distance from Delhi by Car(km)"
    data[name] = data[name].astype('str')
    trial(name)


def get_cuisine():
    name = "Cuisine"
    voice_assist(data.iloc[0, 1])


def get_noofattractions():
    no = str(len(data["Main_Attractions"]))
    return no


def get_name():
    voice_assist("My name is Macy")
    voice_assist("How may i assist You")


def get_info(place):
    for index, rows in data.iterrows():
        my_list = {rows.Main_Attractions: rows.Information}
        if place.title() in my_list:
            voice_assist(my_list[place.title()])


def help():
    voice_assist("You may Ask Me Questions Like", ":~")
    print('''              1)What are the Main Attractions of Sikkim ?
              2)What is Your Name ?
              3)What is The distance of Various PLaces of Sikkim From Delhi ?
              4)What are the Special Dishes Of Sikkim ?
              5)To know about a Tourist Destination just say it's Name(e.g Gangtok)
              ''')


def main():
    global ending, text1
    voice_assist("Hi! My name is Macy")
    help()
    time.sleep(3)

    TOTAL_PATTERNS = {
        re.compile("[\w\s]+ name"): get_name,
        re.compile("hello"): gretting,
        re.compile("help"): help,
        re.compile("hi"): gretting,
        re.compile("[\w\s]+ main attractions [\w\s]"): get_attractions,
        re.compile("main attractions + [\w\s]"): get_attractions,
        re.compile("[\w\s]+ number [\w\s]+ attractions"): get_noofattractions,
        re.compile("[\w\s]+ dishes [\w\s]"): get_cuisine,
        re.compile("[\w\s]+ distance [\w\s]"): get_distance,
    }


    End_Phrase = ["quit", "stop", "end", "dismiss"]

    while True:
        voice_assist("Listening... ")
        text1 = get_audio()
        result = None

        for pattern, func in TOTAL_PATTERNS.items():
            if pattern.match(text1):
                try:
                    result = func()
                except TypeError:
                    pass
                break

        words = text1.lower()
        places = dict(data["Main_Attractions"])
        places = [*places.values()]
        for place in places:
            place = place.lower()
            if place == words:
                get_info(place)
                break

        if result is not None:
            voice_assist(result)

        for end in End_Phrase:
            if re.search(end, text1):
                voice_assist("Thank You! Bye")
                ending = 0
                break

        if ending == 0:
            break


main()

"""        for pattern, func in PLACE_PATTERS.items():
            if pattern.match(text1):
                words = text1.split(" ")
                places = dict(data["Main_Attractions"])
                places = [*places.values()]
                for place in places:
                    '''for i in words:
                        words.append(i.title())
                        words.remove(i)'''
                    place.lower()
                    if place in words:
                        result = get_info(place)
                    break"""