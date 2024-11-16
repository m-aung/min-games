from wordsBank import words
import random

def runHangman(words:list):
  word = random.choice(words)
  display = ['_' for _ in word] # convert the letters to _
  attemptsLeft = 6
  
  while attemptsLeft > 0 and '_' in display:
    print('\n', ' '.join(display))
    guess = input('Guess a letter: ').lower()
    if guess in word:
      for index, letter in enumerate(word):
        if letter == guess:
          # reveal the letter
          display[index] = guess 
    else:
      print('The letter is not in the word. Please try again.')
      attemptsLeft -= 1
  if '_' not in word:
    print ('Victory!!! 🎉🎉🎉')
    print(' '.join(word))
  else:
    print('you ran out of attempts. the word was: ',word)
    print('Game Over!!!😔😔😔')

runHangman(words)
