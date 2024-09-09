# This is to test pycodestyle

# list to hold even and odd numbers
even_no = []
odd_no = []

# loop through the numbers 2 to 50
for a in range(2, 51):
    if a % 2 == 0:
        even_no.append(a)
    else:
        odd_no.append(a)
print("Even numbers: ", even_no)
print("Odd numbers: ", odd_no)
