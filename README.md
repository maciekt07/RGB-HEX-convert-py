# RGB-HEX-convert-py
Simple RGB-HEX converter with guessing game made in python

## hex-rgb convert.py
```py
print("1. convert rgb to hex format")
print("2. convert hex to rgb format")
choice = input(":")
def choice1(): # rgb to hex
  r = int(input("R: "))
  g = int(input("G: "))
  b = int(input("B: "))
  wynik = '#%02x%02x%02x' % (r, g, b);
  print("rgb", r, g, b, "to hex format is:", wynik) 
def choice2(): # hex to rgb
    hex_code = input("enter hexcode: ")
    hex_code = hex_code.replace("#", "")
    print("hex",hex_code, "to rgb format is:", tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4)))
if (choice == "1"):
   choice1()
if (choice == "2"):
    choice2()
```
## rgb-hex-guessing-game.py
```py
import random
r = random.randint(0,255);
g = random.randint(0,255);
b = random.randint(0,255);
solution = '#%02x%02x%02x' % (r, g, b);
print("replace RGB to HEX game, author: github.com/maciekkoks");
print("RGB:", r, g, b);
input1 = input("Enter a hex code:");
if (input1 == solution or input1 == solution.upper()): 
  print("the answer is correct!");
else: 
  print("the answer is not correct, the correct answer is:" ,solution);
input("press enter to exit");

```
