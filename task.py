print(r'''
*******************************************************************************

        )
       (  (              .^.
        \) )           .'.^.'.
         (/          .'.'---'.'.
        _\)_       .'.'-------'.'.
       (__)()    .'.'-,=======.-'.'.
       (_)__)  .'.'---|   |   |---'.'.
       (__)_),'.'-----|   |   |-----'.'.
       ()__.'.'-------|___|___|-------'.'.
       (_.'.'---------------------------'.'.
       .'.'-------------------------------'.'.
      """""|====..====.=======.====..====|"""""
       ()_)|    ||    |.-----.|    ||    |
       (_)_|    ||    ||     ||    ||    |
       (...|____||____||_____||____||____|
      (_)_(|----------| _____o|----------|
      (_)(_|----------||     ||----------|
      (__)(|----------||_____||----------|
      (_)(_|---------|"""""""""|---------|
      ()()(|--------|"""""""""""|--------|
Zot-wWUwwuw|wwWWwuu|"""""""""""""|uwuwuuW|wuwwuuwu
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("you are in the middle of the city at a crossroads.")

first_story = input("which way do you want to go?\n""Type 'left' or 'right'\n").lower()
if first_story == "left":
    second_story = input("Now you can see there are 2 shops in front of you,a fruit shop and a meat shop."
                         "\nWhich one do you want to go in?\nfruit shop or meat shop?\n").lower()
    if second_story == "meat shop":
        third_story = input("go inside and walk until you see there'are 3 elevators inside."
                            "\nOnly one elevator can going up!\nChoose elevator A , B , or C.\n").upper()
        if third_story == "A":
            print("Sorry, your elevator is broken, and you are stuck until security arrives tomorrow."
                  "\nYou got Panic Attack and Die!\nGame Over!")
        elif third_story == "B":
            print("Congrats you found a treasure!\nYou win!")
        elif third_story == "C":
            print ("Your elevator falls and you die!\nGame Over!")
        else:
            print("No!You Die!!\nGame Over!")
    elif second_story == "fruit shop":
        print("There was a thief in the shop, and you were shot dead by him.\nGame Over!")

    else:
        print("Wrong option dude2!")
elif first_story == "right":
    print("upssss..Sorry!you didn't look at the road so you got hit by a car.\nGame Over!\nMission Failed!")
else:
    print("Wrong option dude!")



