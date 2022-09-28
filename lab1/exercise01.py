def str2dict(str) :
    dict = {}

    for i in str :
        if (i not in dict.keys()):
            dict[i] = str.count(i)

    return dict

def str2dict_plus(str):
    punc = '!"#$%&\'()*+, -./:;<=>?@[\]^_`{|}~'
    str = str.lower()

    for character in punc:
        str = str.replace(character, '')

    dict = str2dict(str)

    return dict

def histogram(str):
    dict = str2dict_plus(str)

    for letter in dict:
        print(f'{letter} ', end='')
        num = dict[letter]
        for i in range(num):
            print('*', end='')
        print()

def main():
    histogram(',S\'/.,.$%&$@#MimmlLLE')

if __name__ == '__main__':
    main()