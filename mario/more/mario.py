from cs50 import get_int

# Asks for user input until it receives a valid one
while True:
    height = get_int("Height: ")
    if height > 0:
        if height < 9:
            break

# prints a pyramid of hashes
for i in range(1, height + 1):
     print(" " * (height - i), end="")
     print("#" * i, end="  ")
     print("#" * i)