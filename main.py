print('''
      __                                                      
     /  l                                                     
   .'   :               __.....__..._  ____                   
  /  /   \          _.-"        "-.  ""    "-.                
 (`-: .---:    .--.'          _....J.         "-.             
  """y     \,.'    \  __..--""       `+""--.     `.           
    :     .'/    .-"""-. _.            `.   "-.    `._.._     
    ;  _.'.'  .-j       `.               \     "-.   "-._`.   
    :    / .-" :          \  `-.          `-      "-.      \  
     ;  /.'    ;          :;               ."        \      `,
     :_:/      ::\        ;:     (        /   .-"   .')      ;
       ;-"      ; "-.    /  ;           .^. .'    .' /    .-" 
      /     .-  :    `. '.  : .- / __.-j.'.'   .-"  /.---'    
     /  /      `,\.  .'   "":'  /-"   .'       \__.'          
    :  :         ,\""       ; .'    .'      .-""              
   _J  ;         ; `.      /.'    _/    \.-"                  
  /  "-:        /"--.b-..-'     .'       ;                    
 /     /  ""-..'            .--'.-'/  ,  :                    
:`.   :     / : bug         `-i" ,',_:  _ \                   
:  \  '._  :__;             .'.-"; ; ; j `.l                  
 \  \          "-._         `"  :_/ :_/                       
  `.;\             "-._                                       
    :_"-._             "-.                                    
      `.  l "-.     )     `.                                  
        ""^--""^-. :        \                                 
                  ";         \                                
                  :           `._                             
                  ; /    \ `._   ""---.                       
                 / /   _      `.--.__.'                       
                : :   / ;  :".  \                             
                ; ;  :  :  ;  `. `.                           
               /  ;  :   ; :    `. `.                         
              /  /:  ;   :  ;     "-'                         
             :_.' ;  ;    ; :                                 
                 /  /     :_l                                 
                 `-'                                          

               _     _                                 
              (_)   | |                                
     ___ _ __  _  __| | ___ _ __ _ __ ___   __ _ _ __  
    / __| '_ \| |/ _` |/ _ \ '__| '_ ` _ \ / _` | '_ \ 
    \__ \ |_) | | (_| |  __/ |  | | | | | | (_| | | | |
    |___/ .__/|_|\__,_|\___|_|  |_| |_| |_|\__,_|_| |_|
        | |                                            
        |_|  

''')

print("Welcome to New York City!")
print("Your mission is to help save Spider-Man!")

first_turn = input("You\'re driving down the street, and need to turn \"right\" or \"left\". Which way do you want to go?\n").lower()
if first_turn == "left":
  second_turn = input("You get to the lobby inside the building. Do you \"enter\" the elevator or take the \"stairs\"?\n").lower()
  if second_turn == "stairs":
    third_turn = input("You walk inside the room and encounter 3 doors. \"Red\", \"yellow\", and \"blue\". Which color door do you choose?\n").lower()
    if third_turn == "red":
      print("The Sinister Six were waiting inside for you. Game Over.")
    elif third_turn == "yellow":
      print("The door led to an open elevator shaft, which you fell down. Game Over.")
    elif third_turn == "blue":
      print("You found Spidey!. You won!")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You waited for the elevator, and Spidey perished. Game Over.")
else:
  print("You fell into a hole. Game Over.")