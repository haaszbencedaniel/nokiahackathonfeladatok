from pathlib import Path

def is_magic_num(number):

    string = str(number)

    return string == string[::-1]


def next_magic_num(n):

    next_number = n + 1

    string = str(next_number)

    length = len(string)

    half = string[:(length + 1) // 2]

    mirrored = int(half + half[:length // 2][::-1])

    if mirrored > n:

        return mirrored

    half_inc = str(int(half) + 1)

    if len(half_inc) > len(half):

        return int("1" + "0" * length + "1")

    return int(half_inc + half_inc[:length // 2][::-1])


def main():
    data = Path("input.txt").read_text(encoding="utf-8")

    for line in data.splitlines():

        line = line.strip()

        number = eval(line.replace("^", "**"))

        print(next_magic_num(number))


if __name__ == "__main__":
    main()
