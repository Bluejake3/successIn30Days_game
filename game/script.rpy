# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.




# The game starts here.

label start:
    $ days = 0
    $ stress = 0
    $ money = 500
    $ energy = 100
    scene city with fade

    "Setelah mencari pekerjaan, akhirnya kamu mendapat sebuah pekerjaan yang kamu impikan"

    "Dengan dukungan dari orang tua, kamu menatap kehidupan baru yang lebih berat dari kehidupan kuliah"

    menu:
        "Apakah kau membutuhkan tutorial cara bermain?"
        "Ya":
            "Setiap hari, kamu akan diberikan 3 opsi kegiatan"
            "Opsi pertama adalah bekerja. Opsi ini akan menambah uangmu, tetapi mengonsumsi energi dan menambah stress"
            "Opsi istirahat berfungsi untuk memulihkan energimu dan mengurangi sedikit stress dengan menggunakan sedikit uang"
            "Opsi terakhir adalah Pergi Rekreasi. Opsi ini mengurangi stress secara signifikan dan memulihkan sedikit energi dengan menggunakan sejumlah uang"
            "Hati-hati dalam memilih agar seluruh kondisimu seimbang"
        "Tidak":
            "Baik, mari kita bermain"
        
    
    jump routines_menu

label routines_menu:
    $days += 1
    show screen info_Update
    
    scene bedroom with dissolve
    menu :
        "Apa yang akan kamu lakukan hari ini?"

        "Bekerja":
            scene office with dissolve
            $ stress +=30
            $ energy -=30
            $ money += 300
            "Kamu bekerja seperti biasa dan kamu menerima gaji untuk hari itu"
            "Uang +300, Stress +30, Energi -30"
        "Istirahat":
            $ stress -= 20
            $ energy += 80
            $ money -= 50
            if (energy>100):
                $energy = 100
            if (stress<0):
                $stress = 0
            "Kamu beristirahat satu hari"
            "Energi +80, Uang -50, Stress -20"
        "Pergi Rekreasi":
            scene mall with dissolve
            $ money -= 500
            $ stress -= 90
            $ energy += 20
            if (energy>100):
                $energy = 100
            if (stress<0):
                $stress = 0
            "Kamu pergi liburan dan melupakan tekanan dalam pekerjaan walau untuk sementara"
            "Stress -90, Energi +20, Uang -500"

    jump endCheck

label endCheck:

    if(days >= 30):
        if(money >=3000):
            if(stress <50):
                jump kayaBahagia
            else:
                jump kayaMenderita
        else:
            if(stress < 50):
                jump bahagia 
            else:
                jump menderita
    elif(money < 0):
        jump miskin
    elif (stress >= 100):
        jump gila 
    elif(energy <= 0):
        scene bedroom with dissolve
        "Kamu terlalu lelah sehingga kamu jatuh sakit. Kamu memanggil dokter dan memutuskan untuk beristirahat untuk 5 hari"
        $ days += 5
        $ energy = 20
        $ money -= 300


    jump routines_menu
            

        
        
