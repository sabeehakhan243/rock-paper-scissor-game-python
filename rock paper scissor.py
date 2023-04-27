
player_name = input("= Please enter your name : ")
print("\n\n  ----->> Welcome to my very simple Rock paper scissors game <<-----\n\n			----->>", player_name, ":D <<-----\n\n")
while True:
    while True:
        t = [1, 2, 3]
        import random
        computer_pick = random.choice(t)
        while True:
            player_pick = input("= Please choose your play? \n\n 1.Rock \n\n 2.Paper \n\n 3.Scissors \n\n = Put the number of your choice here, Please: ")
            try:
                int(player_pick)
                if int(player_pick) < 0 or int(player_pick) > 3:
                    print("\n\n  ----->> Please choose from the available choices! <<-----\n\n")
                else:
                    break
            except:
                print("\n\n  ----->> Please type a number <<-----\n\n")
        if int(player_pick) == 1 and computer_pick == 1:
            print("\n=", player_name, "chose: Rock \n\n = computer chose: Rock \n\n\n  ----->> Draw <<-----\n")
            
        elif int(player_pick) == 2 and computer_pick == 2:
            print("\n=", player_name, "chose: Paper \n\n = computer chose: Paper \n\n\n  ----->> Draw <<-----\n")
            
        elif int(player_pick) == 3 and computer_pick == 3:
            print("\n=", player_name, "chose: Scissors \n\n = computer chose: Scissors \n\n\n  ----->> Draw <<-----\n")
            
        elif int(player_pick) == 1 and computer_pick == 2:
            print("\n=", player_name, "chose: Rock \n\n = Computer chose: Paper \n\n = Paper covers Rock \n\n\n  ----->> Computer Wins <<-----\n")
            break
        elif int(player_pick) == 2 and computer_pick == 1:
            print("\n=", player_name, "chose: Paper \n\n = computer chose: Rock \n\n = paper covers rock \n\n\n  " "----->>", player_name, " Wins <<-----\n")
            break
        elif int(player_pick) == 1 and computer_pick == 3:
            print("\n=", player_name, "choice: Rock \n\n = computer choice: Secissors \n\n = Rock crushes Scissors \n\n\n  " "----->>", player_name, " Wins <<-----\n")
            break
        elif int(player_pick) == 3 and computer_pick == 1:
            print("\n=", player_name, "choice: Secissors \n\n = computer choice: Rock \n\n = Rock crushes Scissors \n\n\n  ----->> Computer Wins <<-----\n")
            break
        elif int(player_pick) == 2 and computer_pick == 3:
            print("\n=", player_name, "choice: Paper \n\n = computer choice: Secissors \n\n = Scissors cuts Paper \n\n\n  ----->> Computer Wins <<-----\n")
            break
        elif int(player_pick) == 3 and computer_pick == 2:
            print("\n=", player_name, "choice: Secissors \n\n = computer choice: Paper \n\n = Scissors cuts Paper \n\n\n  " "----->>", player_name, " Wins <<-----\n")
            break
    play_again = input("\n= Wanna play again? \n\n 1.Yes, please. \n\n 2.No, I want some rest.\n\n Put your choice here, Please: ")
    try:
        int(play_again)
        if int(play_again) == 1:
            print("\n  ----->> Right away :D <<-----\n\n")
        elif int(play_again) == 2:
            break
        else:
            print("\n  ----->> I will cosider it as yes! :P <<-----\n\n")
    except:
        print("\n  ----->> I will cosider it as yes! :P <<-----\n\n")
print("\n----->> thanks for playing! <<-----\n\n")
