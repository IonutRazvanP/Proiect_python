import time
import datetime
         

def verificare_ore_lucrate():
    orelucrate=[
        {
        "zi":"01.02.2022",
        "nr_ore":5
        },
        {
        "zi":"02.02.2022",
        "nr_ore":9
        },
        {
        "zi":"03.02.2022",
        "nr_ore":8
        },
        {
        "zi":"04.02.2022",
        "nr_ore":10
        }
    ]
    ore=[]
    for element in orelucrate:
        if(element["nr_ore"]<8): 
            ore.append(element)
    if(len(ore)>0):
        text=""
        for element in ore:
            text+="Angajatul dvs a lucrat "+str(element["nr_ore"])+" ore in data de "+element["zi"]
        print(text)
        #trimite_emal("Angajatul nu a lucreat destu",text)
verificare_ore_lucrate()


ArulatVerificarea=0
def inregistrare_angajati():
    while True:
        if(datetime.datetime.now().hour==22):
            if(ArulatVerificarea==0):
                print ("e ora 22")
                ArulatVerificarea+=1
        else:
            ArulatVerificarea=0
            time.sleep(5)


inregistrare_angajati()
         