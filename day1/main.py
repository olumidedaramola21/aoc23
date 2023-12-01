digits1 = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9"
]

digits2 = digits1 + [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

digits2_map: dict[str, int] = {
    "1": 1,
    "one": 1,
    "2": 2,
    "two": 2,
    "3": 3,
    "three": 3,
    "4": 4,
    "four": 4,
    "5": 5,
    "five": 5,
    "6": 6,
    "six": 6,
    "7": 7,
    "seven": 7,
    "8": 8,
    "eight": 8,
    "9": 9,
    "nine": 9
}

def read() -> list[str]:
    with open("input.txt") as f:
        lines = f.readlines()
        return lines

def solve1():
    lines = read()

    rv = 0
    digit_set = set(digits1)
    for line in lines:
        for c in line:
            if c in digit_set:
                rv += int(c) * 10
                break
        
        for c in reversed(line):
             if c in digits1:
                rv += int(c)
                break

    return rv

if __name__ ==  "__main__":
    rs = solve1()
    print(rs)