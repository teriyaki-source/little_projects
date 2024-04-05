import random
import os

def clean():
  # For Windows
  if os.name == 'nt':
    _ = os.system('cls')
  
  # For macOS and Linux
  else:
    _ = os.system('clear')

def print_board(guesses, states):
  clean()
  for i in range(len(guesses)):
    print(guesses[i])
    print(states[i])

def check_word(answer, attempt):
  # todo: make check more robsut to account for double letters out of order/guessing doubles when 
  # not required. e.g. answer is ghost, guessing goops returns y~yn~ but should be ynyn~
  result = ["x","x","x","x","x"]
  for i in range(len(attempt)):
    if attempt[i] in answer[i:]:
      if attempt[i] == answer[i]:
        result[i] = "y"
      else:
        result[i] = "~"
    else:
      result[i] = "x"
  result = ''.join(result)
  return result

guesses = ["-----","-----","-----","-----","-----","-----"]
states = ["xxxxx","xxxxx","xxxxx","xxxxx","xxxxx","xxxxx"]
count = 0
attempt = ""
f = open("wordle-La.txt", "r")
can_be = f.readlines()
for i in range(len(can_be)):
  can_be[i] = can_be[i].strip()
f.close()   

f = open("wordle-Ta.txt", "r")
can_guess = f.readlines()
for i in range(len(can_guess)):
  can_guess[i] = can_guess[i].strip()
f.close()
answer = can_be[random.randint(0,len(can_be)-1)]
library = can_be + can_guess


# print(answer)
# game start

print("** Bootleg Wordle **")
print("By Luke, for Chiara")
print("Game Begin:")
for i in guesses:
  print(i)

while count < 6:
  count += 1
  attempt = input("Guess: ")
  while len(attempt) != 5 or attempt not in library:
    if len(attempt) != 5:
      print("Needs to be a 5 letter word!")
    elif attempt not in library:
      print("Not in the word list")
    print_board(guesses, states)
    attempt = input("Guess: ")
  guesses[count-1] = attempt
  states[count-1] = check_word(answer, attempt)
  print_board(guesses, states)
  if attempt == answer:
    break

if attempt == answer:
  print("Victory!")
  print("Bootleg Wordle in {num:d}".format(num = count))
else:
  print("Better luck next time")