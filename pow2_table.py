n = int(input("Введите число n: "))
otvet = ""
while n !=0:
    otvet += f"2**{n}, DEC = {2**n}, BIN = {bin(2**n)[2:]}, HEX = {hex(2**n)[2:]}\t\n"
    n -=1
print(otvet)

