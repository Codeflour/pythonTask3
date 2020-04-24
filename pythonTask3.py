#Welcome to your favorite guessing game!

def easy():
  secret_number=7
  guess_count=0
  guess_limit=6
  guess_remainder=(guess_limit-guess_count)
  guess_range= 10
  
  
    
  while guess_count<guess_limit:
   
    
    try:
      guess=int(input("Guess a number from 1-10: "))
      guess_count += 1
      
      if guess <= guess_range and guess >0:
  
     
        if guess==secret_number:
          print ("You got it right!")
          continueWelcome()
          break
     
        else:
          guess_remainder -= 1
          print("That was wrong")
          print( "You have "+str(guess_remainder)+" more guesses."  )
      
      else:
         print ("Your guess is out of range!")
   
   
    except ValueError:
      print ("Please, enter a number")
   
  
  print("Game Over")
  
  #easy()

def medium():
  secret_number=19
  guess_count=0
  guess_limit=4
  guess_remainder=(guess_limit-guess_count)
  guess_range= 20
  
  
    
  while guess_count<guess_limit:
   
    
    try:
      guess=int(input("Guess a number from 1-20: "))
      guess_count += 1
      
      if guess <= guess_range and guess >0:
  
     
        if guess==secret_number:
          print ("You got it right!")
          continueWelcome()
          break
     
        else:
          guess_remainder -= 1
          print("That was wrong")
          print( "You have "+str(guess_remainder)+" more guesses."  )
      
      else:
         print ("Your guess is out of range!")
   
   
    except ValueError:
      print ("Please, enter a number")
   
  
  print("Game Over")


#medium()


def hard():
  secret_number=35
  guess_count=0
  guess_limit=3
  guess_remainder=(guess_limit-guess_count)
  guess_range= 50
  
  
    
  while guess_count<guess_limit:
   
    
    try:
      guess=int(input("Guess a number from 1-50: "))
      guess_count += 1
      
      if guess <= guess_range and guess >0:
  
     
        if guess==secret_number:
          print ("You got it right!")
          continueWelcome()
          break
     
        else:
          guess_remainder -= 1
          print("That was wrong")
          print( "You have "+str(guess_remainder)+" more guesses."  )
      
      else:
         print ("Your guess is out of range!")
   
   
    except ValueError:
      print ("Please, enter a number")
   
  
  print("Game Over")
  
#hard()


#If the user finishes playing a level,and still to continue.

def continueWelcome():
  print ("""
You've finished the current level!
Choose another level:
    >Easy
    >Medium  
    >Hard 
    
 or quit
""")
  #level =""
  chosen_level = input().lower()
  levels = ["easy", "medium", "hard", "quit"]

  for level in levels:
    #print (level)
    if chosen_level == "easy":
      easy()
      break
      
    elif chosen_level == "medium":
      medium()
      break
      
    elif chosen_level == "hard":
      hard()
      break
      
    elif chosen_level == "quit":
      break
      #print("Game over!")
      
    else:
      print("Please, choose a valid level.")
      continueWelcome()
    




#The welcome function
def welcome():
  print ("""
Welcome to a guessing game!
Choose yourlevel:
    >Easy
    >Medium  
    >Hard

""")
  #level =""
  chosen_level = input().lower()
  levels = ["easy", "medium", "hard"]

  for level in levels:
    #print (level)
    if chosen_level == "easy":
      easy()
      break
      
    elif chosen_level == "medium":
      medium()
      break
      
    elif chosen_level == "hard":
      hard()
      break
    else:
      print("Please, choose a valid level.")
      welcome()
    


welcome()