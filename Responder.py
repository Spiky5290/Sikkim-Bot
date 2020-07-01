from Speech import*
from Speaker import*
import pandas as pd
import time
import re

data = pd.read_excel("Sikkim.xlsx")


def trial(name):
    ma = data[name]
    ma = dict(ma)
    ma = [*ma.values()]
    if name == "Distance from Delhi by Car(km)":
        pa = data["Main_Attractions"]
        pa = dict(pa)
        pa = [*pa.values()]
        voice_assist("The distance is as follows  :~")
        for i in ma:
            for j in pa:
                voice_assist(j)
                print(j, end=" :: ")
                pa.remove(j)
                break
            voice_assist(i)
    else:
        for i in ma:
            voice_assist(i)
    print()


def gretting():
    voice_assist("Hello, How May i Help You")


def request_error():
    voice_assist("Sorry! I don't have any info about your Query")


def get_attractions():
    name = "Main_Attractions"
    voice_assist("Main Attractions of Sikkim are :~ ")
    trial(name)


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
    voice_assist("My name is Maly")
    voice_assist("How may i assist You")


def get_info(place):
    for index, rows in data.iterrows():
        my_list = [rows.Main_Attractions, rows.Information]
        if place == my_list[0]:
            voice_assist(my_list[1])


def help():
    voice_assist("You may Ask Me Questions Like:~ ")
    print('''              1)What are the Main Attractions of Sikkim ?
              2)What is Your Name ?
              3)What is The distance of Various PLaces of Sikkim From Delhi ?
              4)What is the Special Dishes Of Sikkim ?
              ''')


def main():
    voice_assist("Hi! My name is Maly")
    help()
    time.sleep(5)


    TOTAL_PATTERNS = {
        re.compile("[\w\s]+ name"): get_name,
        re.compile("hello"): gretting,
        re.compile("help"): help,
        re.compile("hi"): gretting,
        re.compile("[\w\s]+ main attractions [\w\s]"): get_attractions,
        re.compile("[\w\s]+ number [\w\s]+ attractions"): get_noofattractions,
        re.compile("[\w\s]+ dishes [\w\s]"): get_cuisine,
        re.compile("[\w\s]+ distance [\w\s]"): get_distance
    }

    PLACE_PATTERS = {
        re.compile("[\w\s]+ information "): lambda place:get_info(place),
    }

    End_Phrase = "stop"

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

        for pattern, func in PLACE_PATTERS.items():
            if pattern.match(text1):
                words = text1.split(" ")
                places = dict(data["Main_Attractions"])
                places = [*places.values()]
                for place in places:
                    for i in words:
                        words.append(i.capitalize())
                        words.remove(i)
                    if place in words:
                        result = get_info(place)
                    break

        if result is not None:
            voice_assist(result)

        if End_Phrase in text1:
            voice_assist("Thank You! Bye")
            break


main()
