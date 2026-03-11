

if __name__ == '__main__':

    # print without a line break using this function
    # print('🌷', end='')

    # i'm using these emojis - 💕 🥀

    print('')
    print('solid')
    for i in range(11):
        for j in range(11):
            print('💕', end='')
        print('')

    print('')
    print('horizontal')
    for i in range(11):
        for j in range(11):
            if i % 2 == 0:
                print('💕', end='')
            else:
                print('🥀', end='')
        print('')

    print('')
    print('vertical')
    for i in range(11):
        for j in range(11):
            if j % 2 == 0:
                print('💕', end='')
            else:
                print('🥀', end='')
        print('')

    print('')
    print('diagonal')
    for i in range(11):
        for j in range(11):
            if i % 2 == 0 and j % 2 == 0:
                print('💕', end='')
            elif i % 2 == 1 and j % 2 == 1:
                print('💕', end='')
            else:
                print('🥀', end='')
        print('')

    print('')
    print('plaid')
    for i in range(11):
        for j in range(11):
            if j % 2 == 0 and i % 2 == 0:
                print('💕', end='')
            else:
                print('🥀', end='')
        print('')