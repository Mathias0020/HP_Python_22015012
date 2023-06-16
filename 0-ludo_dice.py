import random
while True:
    choice=input ("would you like to roll the dice? toss or quit")
    if choice=='toss':
       user=random.randint(1,6)
       print ("you rolled a", user,"!")
       com=random.randint(1,6)
       print ("dealer rolled a", comp,"!")
       if user>comp:
          print ("you win")
       elif comp>user:
          print ("you loss")
       else:
          print ("it's a draw!")
    elif choice== 'quit'
          print("Thanks for playing!")
       break
    else:
          print ("Error. Please input 'toss' or 'quit,")
