
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
words=['kala','rebka','sai','jhansi','ratna','malya','anusha','varsh','varshitha','jyothi','deepika']
chosen_word=random.choice(words)
l=[]
for i in range(len(chosen_word)):
    l.append('_')
print(l)
lives=6
game_over=False
while not game_over:
    guessed_letter=input("enter the guessed letter:").lower()
    if guessed_letter in l:
        print("You already guessed it!!")
    for i in range(len(chosen_word)):
        if guessed_letter==chosen_word[i]:
            l[i]=guessed_letter
    print(l)
    if guessed_letter not in chosen_word:
        lives-=1
        print(f"You guessed {guessed_letter}, that's not in the word. You lose a life.")
        if lives==0:
            game_over=True
            print("You lose!!!!😒")
    if '_' not in l:
        game_over=True
        print("You win!!!!😁")
    print(stages[lives])




