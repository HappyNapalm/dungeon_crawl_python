from random import randint
while(True):

    stats=[0,1,2,3,4,5]

    i=0

    while(i<6):
        a=1
        j=0
        while(j<4):
            a = a+randint(1,6)
            if(a>8&a<18):
                j=j+1
        a = a-3    
        stats[i] = a
        i=i+1

    print("\nWhat is your race Adventurer?\n")
    race = input()
    race_parse = race.lowercase()
    if (race_parse == "human"):
        print("Str :",stats[0])
        print("Dex :",stats[1])
        print("Con :",stats[2])
        print("Int :",stats[3])
        print("Wis :",stats[4])
        print("Cha :",stats[5])
    elif (race_parse == "dwarf"):
        print("Str :",stats[0])
        print("Dex :",stats[1])
        print("Con :",stats[2]+2)
        print("Int :",stats[3])
        print("Wis :",stats[4])
        print("Cha :",stats[5]-2)
    elif (race_parse == "elf"):
        print("Str :",stats[0])
        print("Dex :",stats[1]+2)
        print("Con :",stats[2]-2)
        print("Int :",stats[3])
        print("Wis :",stats[4])
        print("Cha :",stats[5])
    elif (race_parse == "half-elf"):
        print("Str :",stats[0])
        print("Dex :",stats[1])
        print("Con :",stats[2])
        print("Int :",stats[3])
        print("Wis :",stats[4])
        print("Cha :",stats[5])
    elif (race_parse == "half-orc"):
        print("Str :",stats[0]+2)
        print("Dex :",stats[1])
        print("Con :",stats[2])
        print("Int :",stats[3]-2)
        print("Wis :",stats[4])
        print("Cha :",stats[5]-2)
    elif (race_parse == "halfling"):
        print("Str :",stats[0]-2)
        print("Dex :",stats[1]+2)
        print("Con :",stats[2])
        print("Int :",stats[3])
        print("Wis :",stats[4])
        print("Cha :",stats[5])
    elif (race == "gnome"):
        print("Str :",stats[0]-2)
        print("Dex :",stats[1]+2)
        print("Con :",stats[2])
        print("Int :",stats[3])
        print("Wis :",stats[4])
        print("Cha :",stats[5])
    else:
        print("Speak up Champion!")
