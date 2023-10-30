file = open("dane.txt", "r")
numbers = list(map(str.strip, file.readlines()))
numbers = [item.split(" ") for item in numbers]
numbersn = [item for l in numbers for item in l]
numbersn = list(map(int, numbersn))

niggest = 255
whittest = 0
for i in numbersn:
    if i > whittest:
        whittest = i
    if i < niggest:
        niggest = i
print(niggest, whittest)
print(numbers[0])
chuj = len(numbers[0])
kurwa = 0
for column in numbers:
    for number in column:
        if column[(number)]
print(kurwa)
