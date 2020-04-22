secret_number=7
guess_count=0
guess_limit=3
guess_remainder=(guess_limit-guess_count)
#easy
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