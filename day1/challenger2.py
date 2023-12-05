values = {'one': 1,
          'two': 2,
          'three': 3,
          'four': 4,
          'five': 5,
          'six': 6,
          'seven': 7,
          'eight': 8,
          'nine': 9}


def findWord(text):
    number = []
    for i, character in enumerate(text):
        if character.isalpha():
            for alpha_number, int_number in values.items():
                if text[i:i + len(alpha_number)] == alpha_number:
                    number.append(int_number)
        elif character.isdigit():
            number.append(int(character))
    return number


def getCode(str):
    getNumbers = findWord(str)
    return getNumbers[0] * 10 + getNumbers[len(getNumbers) - 1]


def sumCodes():
    sum = 0
    path = "./inputday1.txt"
    with open(path, 'r') as txt:
        for line in txt:
            sum += getCode(line)
    print(sum)
