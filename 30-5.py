import random
from bisect import bisect


def create_treasure_file():
    """
    This function opens a file, in the following pattern : 0-9 numbers with
    random amount of digits, for each digit. then string TREASURE then 9-0 with random
    amount of digits.
    :return:
    none
    """
    with open('find_treasure.txt', mode='w') as file:
        for i in range(0, 10):
            rnd = (random.randint(1, 20))
            file.write(str(i) * rnd)
        file.write('TREASURE')
        for i in range(9, -1, -1):
            rnd = (random.randint(1, 20))
            file.write(str(i) * rnd)


def top_score(score):
    with open('top_score.txt', mode='r+') as file:
        file.seek(0)
        lst_score = file.readlines()
        lst_score = sorted(lst_score, key=lambda x: int(x.split()[1]))
        if len(lst_score) < 10:
            lst_score.append(f'{input("Enter name: ")} {score} \n')

        elif int(sorted(lst_score[-1].split())[0]) > score:
            del lst_score[0]
            lst_score.append(f'{input("Well played, you entered to top scorers! Enter your name: ")} {score} \n')

        lst_score = sorted(lst_score, key=lambda x: int(x.split()[1]))
        print(lst_score)
        file.seek(0)
        file.writelines(lst_score)


def start_game():
    with open('find_treasure.txt', mode='r') as file:
        score = 0
        file_cont = file.read()
        file.seek(0)
        while True:
            choice = int(input('Where do you want to move? [1 - forward, 2 - backward]: '))
            if choice == 1:
                choice = int(input('How many characters forward? '))
                file.seek(file.tell() + choice)
            elif choice == 2:
                choice = int(input('How many characters backward? '))
                file.seek(file.tell() - choice)
            else:
                print('Enter 1 for forward or 2 for backwards.')
                continue
            score += 1
            print(f'You hit: {file_cont[file.tell()]}')
            if not file_cont[file.tell()].isdigit():
                break

        print('Success! you hit the treasure')
        top_score(score)


def main():
    create_treasure_file()
    start_game()


if __name__ == '__main__':
    main()