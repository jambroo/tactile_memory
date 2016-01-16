import os

class colors:
  WRONG = '\033[91m'
  OK = '\033[0m'

print("What are you trying to remember?")
target = input()

def attempt():
  os.system('clear')

  print("Try:")
  attempt = input()

  if attempt != target:
    print("Wrong:")
    for i in range(0, len(target)):
      tChar = target[i]
      aChar = ""
      if len(attempt) > i:
        aChar = attempt[i]
      if tChar == aChar:
        print(tChar, end="")
      else:
        print(colors.WRONG + tChar, end="")
      print(colors.OK, end="")
    print("")
  else:
    print(":)")
  input()

while True:
  attempt()


