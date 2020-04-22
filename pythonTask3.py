print (input("""
Welcome to a guessing game!
Choose yourlevel:
    >Easy
    >Medium  
    >Hard

"""))

while input.lower != "easy" or input.lower !="medium" or input.lower !="hard":
  if input.lower == easy:
    easy()
    break
  else if input.lower == medium:
    medium()
    break
  else if input.lower === hard:
    hard()
    break
  else:
    print("Please, choose a valid level.")

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
    break
   
  else:
    guess_remainder -= 1
    print("That was wrong")
    print( "You have "+str(guess_remainder)+" more guesses."  )
print("Game Over")

#easy()

def medium():
secret_number=7
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
    break
   
  else:
    guess_remainder -= 1
    print("That was wrong")
    print( "You have "+str(guess_remainder)+" more guesses."  )
print("Game Over")

#medium()

def hard():
secret_number=7
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
    break
   
  else:
    guess_remainder -= 1
    print("That was wrong")
    print( "You have "+str(guess_remainder)+" more guesses."  )
print("Game Over")

#hard()