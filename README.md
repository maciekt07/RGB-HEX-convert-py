# RGB-to-HEX-Game
![preview](https://raw.githubusercontent.com/maciekkoks/RGB-to-HEX-Game-py/main/preview1.png)
```py
import random
r = random.randint(0,255);
g = random.randint(0,255);
b = random.randint(0,255);
solution = '%02x%02x%02x' % (r, g, b);
print("replace RGB to HEX game, author: github.com/maciekkoks");
print("RGB:", r, g, b);
input1 = input("Enter a hex code: #");
if (input1 == solution or input1 == solution.upper()): 
  print("the answer is correct!");
else: 
  print("the answer is not correct, the correct answer is:", solution);
input("press enter to exit");

```
