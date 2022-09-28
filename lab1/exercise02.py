import os

def count_people(file):
    people = 0
    names = set()
    with open(file, 'r') as file:
        for line in file:
            if {line}.issubset(names) == False:
                names.add(line)
                people += 1

    return people


def main():
    result = count_people('lab1/data01.txt')
    print(result)
    result = count_people('lab1/people_1.txt')
    print(result)
    result = count_people('lab1/people_2.txt')
    print(result)
    result = count_people('lab1/people_3.txt')
    print(result)

if __name__ == '__main__':
    main()