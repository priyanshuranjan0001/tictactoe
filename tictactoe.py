#game start

gameStarterText = "This Is A Tic Tack Toe Game \nIf You And Your Partner Are Ready\nPress Enter To Start The Game : ) "
gameStarterInput = input(gameStarterText)
gameStarterInput = None
#symbol assinment
symbol1 = "x"
symbol2 = "o"


player1SymbolSelection = input("Player 1 Please Select Your Symbol [x or o]")

player2SymbolSelection = None



    
if (player1SymbolSelection == symbol1):
    player2SymbolSelection = symbol2
    
        
elif player1SymbolSelection == symbol2:
    player2SymbolSelection = symbol1
        
else :
    print("Player 1 Please Select from [x or o]")
#symbol assingment complete  


#position assignment
position1 = 1
position2 = 2
position3 = 3
position4 = 4
position5 = 5
position6 = 6
position7 = 7
position8 = 8
position9 = 9
player1Position=None
player2Position=None
player1Status=None
player2Status=None






#grid design
line1="{}|{}|{}"
line2="{}|{}|{}"
line3="{}|{}|{}"


# instructions
def gridPrint():
    print("              ",line1.format(position1,position2,position3))
    print("              ",line2.format(position4,position5,position6))
    print("              ",line3.format(position7,position8,position9))

gridPrint()

print("press The Respective Key To Occupy The Position\n Don't override positions")

gameStarterText = "Press Enter To Start The Game : ) "
gameStarterInput = input(gameStarterText)
gameStarterInput = None

userRequest = True
while userRequest :
    
    
    player1Position = int(input("Player 1 Your Turn "))
   
    
    if player1Position ==  position1:
        position1=player1SymbolSelection

    elif player1Position == position2:
        position2=player1SymbolSelection

    elif player1Position == position3:
        position3=player1SymbolSelection


    elif player1Position == position4:
        position4=player1SymbolSelection

    elif player1Position == position5:
        position5=player1SymbolSelection

    elif player1Position == position6:
        position6=player1SymbolSelection

    elif player1Position == position7:
        position7=player1SymbolSelection


    elif player1Position == position8:
        position8=player1SymbolSelection

    elif player1Position == position9:
        position9=player1SymbolSelection


    gridPrint()

   

                 

    
    
    

    player2Position = int(input("Player2 Your Turn"))


    
    if player2Position ==  position1:
        position1=player2SymbolSelection

    elif player2Position == position2:
        position2=player2SymbolSelection

    elif player2Position == position3:
         position3=player2SymbolSelection


    elif player2Position == position4:
        position4=player2SymbolSelection

    elif player2Position == position5:
        position5=player2SymbolSelection

    elif player2Position == position6:
        position6=player2SymbolSelection

    elif player2Position == position7:
        position7=player2SymbolSelection


    elif player2Position == position8:
        position8=player2SymbolSelection

    elif player2Position == position9:
        position9=player2SymbolSelection

    gridPrint()


           
    
    









