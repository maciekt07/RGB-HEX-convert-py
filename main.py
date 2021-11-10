import random
n = 0;
r = random.randint(0,255);
g = random.randint(0,255);
b = random.randint(0,255);
def rgb_to_hex(r, g, b):
  return ('{:X}{:X}{:X}').format(r, g, b);
solution = "#" + rgb_to_hex(r, g, b);
print("replace RGB to HEX game, use uppercase, author: github.com/maciekkoks");
print("RGB:", r, g, b);
input1 = input("Enter a hex code:");
if (input1 == solution): 
  print("the answer is correct!");
else: 
  print("the answer is not correct, the correct answer is:", solution);
input("press enter to exit");