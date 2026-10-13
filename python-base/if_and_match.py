if __name__ == '__main__':
    birth = input('birth: ')
    if int(birth) < 2000 | int(birth) >= 1990:
        print('00前')
    else:
        print('00后')

    score = 'B'
    match score:
        case 'A':
            print('score is A')
        case 'B' | 'E':
            print('score is B')
        case 'C':
            print('score is C')
        case 'D':
            print('score is D')