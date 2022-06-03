# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.




# The game starts here.

label start:
    $ days = 0
    $ stress = 0
    $ money = 500
    $ energy = 100

    "stories goes here"
    
    jump routines_menu

label routines_menu:
    $days += 1
    show screen info_Update

    menu :
        "Apa yang akan kamu lakukan hari ini?"

        "Bekerja":
            $ stress +=30
            $ energy -=30
            $ money += 300
        "Istirahat":
            $ stress -= 20
            $ energy += 80
            $ money -= 50
            if (energy>100):
                $energy = 100
            if (stress<0):
                $stress = 0
        "Pergi Rekreasi":
            $ money -= 500
            $ stress -= 90
            $ energy += 10
            if (energy>100):
                $energy = 100
            if (stress<0):
                $stress = 0

    jump endCheck

label endCheck:

    #3500 target money
    jump routines_menu
            

        
        
