
#======<<Input>>========================================
import random as r
import time
cstreak = 0
hstreak = 0
user = "Mango"

freshset=input("Set a password to access the arcade: ")
Egypt1 = freshset
#=====------------=======================================














def login():
    
    def resetpassword():
            global Egypt1
            print(r"""
---------------------------------------
           ___  __________________
  / _ \/ __/ __/ __/_  __/
 / , _/ _/_\ \/ _/  / /   
/_/|_/___/___/___/ /_/
---------------------------------------""")
            time.sleep(2)
            print("")
            time.sleep(1)
            Egypt=str(input("Enter your new password: "))
            Egypt1=str(input("Enter your password again to verify: "))
            while Egypt != Egypt1:
                print("Passwords do not match. Please try again.")
                time.sleep(2)
                Egypt=str(input("Enter your new password: "))
                Egypt1=str(input("Enter your password again to verify: "))
            print("Verified. Changing passwords and returning to the login screen...")
            time.sleep(0.5)
            loginschema(Egypt1)

        

    def loginschema(base=freshset):
        global user
        time.sleep(0.5)
        print(r"""
~=—~=—~=—~=—~=—~=—~=—~=—~=—~=—~=—~=—~=—~=—~=—~=—~
  .---.       ,-----.      .-_'''-.  .-./`) ,---.   .--. 
  | ,_|     .'  .-,  '.   '_( )_   \ \ .-.')|    \  |  | 
,-./  )    / ,-.|  \ _ \ |(_ o _)|  '/ `-' \|  ,  \ |  | 
\  '_ '`) ;  \  '_ /  | :. (_,_)/___| `-'`"`|  |\_ \|  | 
 > (_)  ) |  _`,/ \ _/  ||  |  .-----..---. |  _( )_\  | 
(  .  .-' : (  '\_/ \   ;'  \  '-   .'|   | | (_ o _)  | 
 `-'`-'|___\ `"/  \  ) /  \  `-'`   | |   | |  (_,_)\  | 
  |        \'. \_/``".'    \        / |   | |  |    |  | 
  `--------`  '-----'       `'-...-'  '---' '--'    '--'
  Username: ____________
  Password: ____________
~=—~=—~=—~=—~=—~=—~=—~=—~=—~=—~=—~=—~=—~=—~=—~=—~
""")
        time.sleep(0.5)
        print("")
        time.sleep(0.5)
        Username=(str(input("Please enter your username. ")))
        user = Username
        Password=(str(input("Please enter password. ")))
        cap=0
        if Password == base:
            print("Access granted. The Interface will boot up shortly...")
            interface(Username)
        else:
            while Password != base and cap <= 5:
                cap += 1
                Password=(str(input("Incorrect Password. Please Try Again. ")))
            if Password == base:
                print("Access granted. The Interface will boot up shortly...")
                interface(Username)                
            while Password != base and 5 < cap <= 10:
                cap += 1
                print("Too many requests. Please wait 10 seconds before trying again.")
                time.sleep(10)
                Password=(str(input("Please try enter the password again: ")))
                if Password == base:
                    print("Access granted. The Interface will boot up shortly...")
                    interface(Username)
            while Password != base and cap > 10:
                Resetter=(str(input('Entered too many incorrect requests. Enter "A1B2C3" to reset password')))
                while Resetter != "A1B2C3":
                    time.sleep(5)
                    Resetter=(str(input('Entered too many incorrect requests. Enter "A1B2C3" to reset password. ')))
                    if Resetter =="A1B2C3":  
                        resetpassword()
	
    print(r"""	
=================================================
     _    ____   ____    _    ____  _____ 
    / \  |  _ \ / ___|  / \  |  _ \| ____|
   / _ \ | |_) | |     / _ \ | | | |  _|  
  / ___ \|  _ <| |___ / ___ \| |_| | |___ 
 /_/   \_\_| \_\\____/_/   \_\____/|_____|
 
 ================================================
 Login (1) | forgot password? (2)
 ------------------------------------------------""")
    time.sleep(0.2)
    print("")
    time.sleep(0.3)
    Choice=input("Enter password to access the machine (1)! If forgotten password, press 2: ")
    if Choice =="1":
        loginschema(Egypt1)
    elif Choice =="2":
        resetpassword()
            
                          
    else:
        while Choice != "1" and Choice != "2":
            print(" ")
            time.sleep(0.5)
            Choice=input("""Incorrect entering method, or invalid selection. Please either:
1) press 1 to enter password, or 2) If forgotten password, press 2 to reset: """)
            if Choice =="1":
                loginschema(Egypt1)
            elif Choice =="2":
                resetpassword()

































def interface(borrowUser="Mango"):
    time.sleep(1)
    print(r"""
 ----------------------------------------------------------------
                  .-'''-.                                         
             '   _    \                                       
   .       /   /` '.   \  __  __   ___         __.....__      
 .'|      .   |     \  ' |  |/  `.'   `.   .-''         '.    
<  |      |   '      |  '|   .-.  .-.   ' /     .-''"'-.  `.  
 | |      \    \     / / |  |  |  |  |  |/     /________\   \ 
 | | .'''-.`.   ` ..' /  |  |  |  |  |  ||                  | 
 | |/.'''. \  '-...-'`   |  |  |  |  |  |\    .-------------' 
 |  /    | |             |  |  |  |  |  | \    '-.____...---. 
 | |     | |             |__|  |__|  |__|  `.             .'  
 | |     | |                                 `''-...... -'    
 | '.    | '.                                                 
 '---'   '---'
 ----------------------------------------------------------------
 Select game: [1] Cups | [2] Coming soon! | [X] Logout""")
    choice2 = input(f"Welcome back, {borrowUser}! Please select one of our available games to play, or type 'X' to logout! :)  ")
    choice2 = choice2.upper()
    while choice2.upper != "X" and choice2 != "1":
        time.sleep(0.05)
        print("")
        print(choice2)
        time.sleep(0.05)
        choice2 = input("Unfortunately we only have the cups game available at this time. Please enter another number, remembering only positive integers are valid: ")
    if choice2 == 'X':
        print("Signing out, please wait...")
        time.sleep(5)
        print("Successfully signed out. Returning to startup screen..")
        time.sleep(1.5)
        login()
    elif int(choice2) == 1:
        print("Understood! Loading the cup game....")
        time.sleep(1)
        cup_intro()

































def cup_intro():
    time.sleep(0.3)
    print(r"""
~=—~=—~=—~=—~=—~=—~=—~=—~=—~=—~=—~=—~=—~=—~=—~=—~~=—~=—~=—~=—~=—~=—~=—~=

                 |       _,.----.                  _ __     ,-,--.  
    _______      |   .' .' -   \ .--.-. .-.-. .-`.' ,`. ,-.'-  _\       
  /\       \     |  /==/  ,  ,-'/==/ -|/=/  |/==/, -   Y==/_ ,_.'       
 /()\   ()  \    |  |==|-   |  .|==| ,||=| -|==| _ .=. \==\  \          
/    \_______\   |  |==|_   `-' \==|- | =/  |==| , '=',|\==\ -\         
\    /()     /   |  |==|   _  , |==|,  \/ - |==|-  '..' _\==\ ,\       
 \()/   ()  /    |  \==\.       /==|-   ,   /==|,  |   /==/\/ _ |       
  \/_____()/     |   `-.`.___.-'/==/ , _  .'/==/ - |   \==\ - , /
                 |              `--`..---'  `--`---'    `--`---'
                 
~=—~=—~=—~=—~=—~=—~=—~=—~=—~=—~=—~=—~=—~=—~=—~=—~~=—~=—~=—~=—~=—~=—~=—~=""")
    time.sleep(0.5)
    print("Welcome to the cup game! This is a game of chance, where you must guess what cup my ball is under. Once you are down to the last cup, you lose!")
    time.sleep(1)
    print("Highest streak:",hstreak)
    time.sleep(0.08)
    print("Current streak:",cstreak)
    time.sleep(0.5)
    ncup=int(input("How many cups do you want to play with this round? Press 0 if you want the default: "))
    if ncup == 0:
        cup_game()
    while ncup < 0:
        ncup=int(input("Cup number must be positive, please try again: "))
    while ncup == 1:
        ncup=int(input("Invalid cup number. Cup number must be greater than one, please try again: "))
    cup_game(ncup)











def cup_looper(result):
    print("")
    time.sleep(0.5)
    if result:
        redo=input(f"Congrats on winning! Press 1 to play again, or press any other key to go back to home. Your current streak is {cstreak}, and your highest streak is {hstreak}. ")
        if redo =="1":
                 cup_intro()
        else:
                interface(user)
    if not result:
        if cstreak > hstreak:
            redo=input(f"Better luck next time! Your new highest streak is {cstreak}. Press 1 to play again, or press any other key to go back to home. ")
            if redo =="1":
                    cup_intro()
            else:
                    interface(user)
        elif cstreak <= hstreak:
            redo=input("Better luck next time! Press 1 to play again, or press any other key to go back to home. ")
            if redo =="1":
                    cup_intro()
            else:
                    interface(user)










def cup_game(cups=3):
    global cstreak,hstreak
    time.sleep(0.8)
    print("""


""")
    display = ""
    dCollect = ""
    ball = r.randint(1, cups)
    for i in range (1,cups-1):
        dCollect += str(i) + "-"
        display += str ( i)+", "
    display += f"{cups-1} or {cups}"    
    dCollect += str(cups-1) + "-" + str(cups)
    dList=dCollect.split("-")
    
    y = int(input(f"Enter your guess, ({display}): "))
    while y > cups:
        y=int(input(f"The number of cups you selected was {cups}, try again. Choose from ({display}): ")) 
    while str(y) not in dList:
        y=int(input(f"Try again, you have already guessed this cup. Choose from ({display}): "))
    if y == ball:
        print("You guessed right! Well done!")
        cstreak += 1
        if cstreak > hstreak:
            hstreak = cstreak
        cup_looper(True)

            
    while y != ball:
        if len(dList) ==3:
            z = y
            y = ball
        while y > cups:
            print("")
            y=int(input(f"The number of cups you selected was {cups}, try again. Choose from ({display}): ")) 
        while str(y) not in dList:
            print("")
            y=int(input(f"Try again, you have already guessed this cup. Choose from ({display}): "))

            
        while len(dList) > 3:
            while y > cups:
                print("")
                y=int(input(f"The number of cups you selected was {cups}, try again. Choose from ({display}): ")) 
            while str(y) not in dList:
                print("")
                y=int(input(f"Try again, you have already guessed this cup. Choose from ({display}): "))            
            dList.remove(str(y))
            display = ""            
            for i in range (1,len(dList)-1):
                display += dList[i-1]+", "
            display += f"{dList[-2]} or {dList[-1]}"
            print("")
            y=int(input(f"You guessed wrong! Have one more try. Enter your guess, ({display}): "))
            if y == ball:
                print("")
                print("You guessed right! Well done!")
                cstreak+= 1
                if cstreak > hstreak:
                    hstreak = cstreak
                cup_looper(True)




            
    dList.remove(str(z))
    display = f"{dList[0]} or {dList[1]}"             
    y=int(input(f"You guessed wrong! Have one, FINAL try. Enter your guess, ({display}): "))
    while y > cups:
        y=int(input(f"The number of cups you selected was {cups}, try again. Choose from ({display}): ")) 
    while str(y) not in dList:
        y=int(input(f"Try again, you have already guessed this cup. Choose from ({display}): "))    
    if y != ball:
            print(f"You guessed wrong! The ball was in cup number {ball}... Better luck next time!")
            cstreak=0
            cup_looper(False)
    elif y == ball:
        print("You guessed right! Well done!")
        cstreak+= 1
        if cstreak > hstreak:
            hstreak = cstreak
        cup_looper(True)


                                 


#======<<Output>>========================================
login()
#=====------------=======================================
                

 
                                          
