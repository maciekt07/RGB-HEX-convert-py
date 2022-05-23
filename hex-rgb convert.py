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
    hex_kod = input("podaj kod hex: ")
    hex_kod = hex_kod.replace("#", "")
    print("hex",hex_kod, "to rgb format is:", tuple(int(hex_kod[i:i+2], 16) for i in (0, 2, 4)))
if (choice == "1"):
   choice1()
if (choice == "2"):
    choice2()
    