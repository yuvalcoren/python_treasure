import random


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
    """
    Function receives score, check if It can enter the top 10 scorers, if achieved, it is entered
    in top_score.txt which contains top 10 scorers. Firstly gets the file content,
     sorts it with lambda (by its integer score)
    then check if the worst score (most attempts) is better than users score. if user score is better,
    it is entered in, and the list is sorted once again (with the worst score getting out of table)
    :param score:
    :return:
    """
    with open('top_score.txt', mode='r+') as file:
        lst_score = file.readlines()
        lst_score = sorted(lst_score, key=lambda x: int(x.split()[1]))
        if len(lst_score) < 10:
            lst_score.append(f'{input("Enter name: ")} {score} \n')

        elif int(sorted(lst_score[-1].split())[0]) > score:
            del lst_score[-1]
            lst_score.append(f'{input("Well played, you entered to top scorers! Enter your name: ")} {score} \n')

        lst_score = sorted(lst_score, key=lambda x: int(x.split()[1]))
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

        print(f'Success! you hit the treasure in {score} moves!')
        top_score(score)


def main():
    create_treasure_file()
    start_game()


if __name__ == '__main__':
    main()
