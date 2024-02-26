import random

def guess_number_game():
    random_number = random.randint(1, 100)
    numbers = 0

    while True:
        user_input = input('숫자를 써주세요: ')

        if not user_input.isdigit():
            print('글자 말고 숫자만 써주세요!')
            continue

        user_input = int(user_input)

        if user_input < 1 or user_input > 100:
            print('1 ~ 100 사이의 숫자를 입력해주세요.')
            continue

        numbers += 1

        if user_input < random_number:
            print('up 입니다')
        elif user_input > random_number:
            print('down 입니다')
        else:
            print(f'정답입니다! {numbers}번만에 맞췄네요')
            break

if __name__ == '__main__':
    while True:
        guess_number_game()

        re_try = input('다시 하시겠습니까? (y/n): ')

        if not re_try.isdigit():
            print('y/n만 입력해주세요!')
        if re_try.lower() != 'y':
            print('게임을 종료합니다.')
            break
