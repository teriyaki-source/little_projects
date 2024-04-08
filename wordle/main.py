import random
import os

# define colours for output
blank = "\U00002800"
green = "\U0001F7E9"
white = "\U00002B1C"
yellow = "\U0001F7E8"

def get_data():
  f = open("./wordle-La.txt", "r")
  can_be = f.readlines()
  for i in range(len(can_be)):
    can_be[i] = can_be[i].strip()
  f.close()   

  f = open("./wordle-Ta.txt", "r")
  can_guess = f.readlines()
  for i in range(len(can_guess)):
    can_guess[i] = can_guess[i].strip()
  f.close()
  answer = can_be[random.randint(0,len(can_be)-1)]
  library = can_be + can_guess
  return can_be, can_guess, answer, library

def clean():
  # For Windows
  if os.name == 'nt':
    _ = os.system('cls')
  
  # For macOS and Linux
  else:
    _ = os.system('clear')

def print_board(attempt, guesses, states):
  clean()
  if len(attempt) != 5:
    print("Needs to be a 5 letter word!")
  elif attempt not in library:
    print("Not in the word list")
  for i in range(len(guesses)):
    for j in range(len(guesses[i])):
      print("{0: <2.5}".format(guesses[i][j]),end ="")
    print()
    if states[i][0] == "-":
      for j in range(len(states[i])):
        print("{0: <2}".format(states[i][j]),end = "")
      print()
    else:
      print(states[i])

def check_word(answer, attempt):
  result = [white, white, white, white, white]
  return check_double_letter(result, answer, attempt)

def check_double_letter(result, answer,attempt):
  for i in range(len(attempt)):
    no_attempt = attempt.count(attempt[i])
    no_answer = answer.count(attempt[i])
    if no_attempt <= no_answer:
      if attempt[i] in answer:
        if attempt[i] == answer[i]:
          result[i] = green
        else:
          result[i] = yellow
      else:
        result[i] = white
    else:
      if attempt[i] == answer[i]:
        result[i] = green
      else:
        result[i] = white
  return "".join(result)

guesses =   ["-----"]*6
states =    ["-----"]*6

count = 0
attempt = ""

can_be, can_guess, answer, library = get_data()

# print(answer)
# game start

print("** Bootleg Wordle **")
print("By Luke, for Chiara")
print("Game Begin:")

# for i in guesses:
#   print(i)

while count < 6:
  count += 1
  attempt = input("Guess: ")
  while len(attempt) != 5 or attempt not in library:
    print_board(attempt, guesses, states)
    attempt = input("Guess: ")
  guesses[count-1] = attempt
  states[count-1] = check_word(answer, attempt)
  print_board(attempt, guesses, states)
  if attempt == answer:
    break

if attempt == answer:
  print("Victory! The word was '{str:s}'.".format(str = answer))
  print("Bootleg Wordle in {num:d}".format(num = count))
else:
  print("Better luck next time")