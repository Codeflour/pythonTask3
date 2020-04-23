#Welcome to your favorite guessing game!

def easy():
  secret_number=7
  guess_count=0
  guess_limit=6
  guess_remainder=(guess_limit-guess_count)

  while guess_count<guess_limit:
    guess=int(input("Guess: "))
    guess_count += 1
  
    #if guess != int:
     # print ("Please, enter a number!")
    if guess==secret_number:
      print ("You got it right!")
      welcome()
      break
     
    else:
      guess_remainder -= 1
      print("That was wrong")
      print( "You have "+str(guess_remainder)+" more guesses."  )
    
  
  print("Game Over")
  
  #easy()

def medium():
  secret_number=19
  guess_count=0
  guess_limit=4
  guess_remainder=(guess_limit-guess_count)
  while guess_count<guess_limit:
    guess=int(input("Guess: "))
    guess_count += 1
  
    #if guess != int:
     # print ("Please, enter a number!")
    if guess==secret_number:
      print ("You got it right!")
      welcome()
      break
   
    else:
      guess_remainder -= 1
      print("That was wrong")
      print( "You have "+str(guess_remainder)+" more guesses."  )
  print("Game Over")

#medium()

def hard():
  secret_number=35
  guess_count=0
  guess_limit=3
  guess_remainder=(guess_limit-guess_count)
  while guess_count<guess_limit:
    guess=int(input("Guess: "))
    guess_count += 1
  
    #if guess != int:
     # print ("Please, enter a number!")
    if guess==secret_number:
      print ("You got it right!")
      welcome()
      break
   
    else:
      guess_remainder -= 1
      print("That was wrong")
      print( "You have "+str(guess_remainder)+" more guesses."  )
  print("Game Over")

#hard()

def welcome():
  print ("""
Welcome to a guessing game!
Choose yourlevel:
    >Easy
    >Medium  
    >Hard

""")
  #level =""
  level = input().lower()
  levels = ["easy", "medium", "hard"]

  for lvl in levels:
    #print (level)
    if level == "easy":
      easy()
      break
      
    elif level == "medium":
      medium()
      break
      
    elif level == "hard":
      hard()
      break
    else:
      print("Please, choose a valid level.")
      welcome()
    


welcome()