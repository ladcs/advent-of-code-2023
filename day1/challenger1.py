def numbers(text):
    number = []
    for character in text:
        if character.isdigit():
            number.append(int(character))
    return number


def getCode(str):
    getNumbers = numbers(str)
    return getNumbers[0] * 10 + getNumbers[len(getNumbers) - 1]


def sumCodes():
    sum = 0
    path = "./inputday1.txt"
    with open(path, 'r') as txt:
        for line in txt:
            sum += getCode(line)
    print(sum)
