import random
import string
def hangman():
    words=['google','maggie','crockery','icecream','drawing','laptop','notebook']
    new_word=random.choice(words)
    turns=10
    guessmade=""
    letter=set(string.ascii_lowercase)
    choose=string.ascii_lowercase


    while len(new_word)>0:
        main_word=''
        for letters in new_word:
            if letters in guessmade:
                main_word+=letters
            else:
                main_word+="_"
        if main_word==new_word:
            print(main_word)
            print("you won!!!")
            break
        print("guess the word",main_word)
        print(choose)
        guess=input("guess the letter from alphabets:-")
        if guess in main_word:
            print("you already guessed",guess)
        if guess in letter:
            guessmade+=guess        
        else:
            print("enter valid characters")
            guess=input("guess the letter:-")
        
        if guess not in new_word:
            turns-=1
            if turns==9:
                print("9 turns left!!!")
                print('''________________
                                        
                                        
                                        
                                |
                                |
                             ___|____
                                        ''')
            if turns==8:
                print("8 turns left!!!")
                print('''________________
                                        
                        O       
                                        
                                |
                                |
                             ___|____
                                        ''')
            if turns==7:
                print("7 turns left!!!")
                print('''________________
                                        
                        O       
                        |       
                                |
                                |
                             ___|____
                                        ''')
            if turns==6:
                print("6 turns left!!!")
                print('''________________
                                        
                        O       
                        |       
                       /        |
                                |
                             ___|____
                                        ''')
            if turns==5:
                print("5 turns left!!!")
                print('''________________
                                        
                        O       
                        |       
                       / \      |
                                |
                             ___|____
                                        ''')
            if turns==4:
                print("4 turns left!!!")
                print('''________________
                                        
                        O       
                       \|       
                       / \      |
                                |
                             ___|____
                                        ''')
            if turns==3:
                print("3 turns left!!!")
                print('''________________
                                        
                        O       
                       \|/      |
                       / \      |
                                |
                             ___|____
                                        ''')
            if turns==2:
                print("2 turns left!!!")
                print('''________________
                        ---------
                                 
                        O       |
                       \|/      |
                       / \      |
                                |
                             ___|____
                                        ''')
            if turns==1:
                print("only 1 turn is left!!!")
                print('''________________
                        ---------
                                |
                        O       |
                       \|/      |
                       / \      |
                                |
                             ___|____
                                        ''')
            if turns==0:
                print("you loose")
                print("you let a good man die")
                print('''________________
                        ---------
                        |       |
                        O       |
                       /|\      |
                       / \      |
                                |
                             ___|____
                                        ''')
                break   
name=input("enter your name:-")
print("Welcome",name,"!")
print("try to guess the word in less than 10 attempts")
hangman()