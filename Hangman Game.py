import random
name=input("Enter Your Name : ")
print('''
WELCOME TO THE BLUE PEGASUS CREATIONS

HANGMAN GAME

INSTRUCTIONS:
GUESS THE LETTERS
USE SMALL ALPHABETS
YOU'LL GET 15 CHANCES IF THE GUESS IS CORRECT YOU'LL NOT LOSE A TURN
YOU'LL GET 3 TOPIC OPTIONS
CHOOSE ONLY 1 ''')
food=['pizza','burger','idli','dosa','vada','icecream','cake','donuts','pastry','biscuits','chocolates','toffe','cupcakes','cream','pancake','spaghetti','salad','milk','french fries','coffee','tea','milkshake','croissant','cookies','pie','pretzel','bagel','swissroll','pasta','macroni','omlette','sushi','noodles','dhokla','thepla','khandvi','samosa','khichdi','aamras','pyayasa','paratha','rice','sandwich','vadapav','dabeli','bhelpuri','panipuri','sevpuri']
travel=['airplane','bus','driving','tour','journey','backpack','departure','beach','trekking','train','holiday','vacation','roadtrip',]
clothes=['shirt','skirt','formals','denim','palazzo','outift','costume','garments','handkercheif','sweater','jacket','coat','socks','trackpants','vest','pajamas','underwear','bra','tights','nightwear','raincoat','tanktop','blouse','saree','lehenga','ghagra','stockings','tie','bow','hat','gloves','shawl','scarf','tshirt','tees','shorts','jeggings','frock','dress','gown','swimsuit','pants','uniform','blazers']                             
a=int(input("Enter 1 for food items, 2 for travel and 3 for clothing"))
print("THE GAME BEGINS ; ALL THE BEST ", name)                                                                                                                                                                                                                                                              
guesses = ''
turns = 15
if a==1:
    print("You selected food")
    word = random.choice(food)
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char)
            else:
                print("_")
                failed+=1
        if failed == 0:
            print('''YOU WIN !!
THE WORD IS ''',word)
            break
        guess = input("Enter a alphabet")
        guesses+=guess    
        if guess not in word:
            turns -=1
            print("You have", + turns, "more guesses")
            if turns==0:
                print("You lose")
                print("The word was",word)
elif a==2:
    print("You selected travel")
    word = random.choice(travel)
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char)
            else:
                print("_")
                failed+=1
        if failed == 0:
            print('''YOU WIN !!
THE WORD IS ''',word)
            break
        guess = input("Enter a alphabet")
        guesses+=guess    
        if guess not in word:
            turns -=1
            print("You have", + turns, "more guesses")
            if turns==0:
                print("You lose")
                print("The word was",word)
elif a==3:
    print("You selected clothing")
    word= random.choice(clothes)
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char)
            else:
                print("_")
                failed+=1
        if failed == 0:
            print('''YOU WIN !!
THE WORD IS''',word)
            break
        guess = input("Enter a alphabet")
        guesses+=guess    
        if guess not in word:
            turns -=1
            print("You have", + turns, "more guesses")
            if turns==0:
                print("You lose")
                print("The word was",word)
