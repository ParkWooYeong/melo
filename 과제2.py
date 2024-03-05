import random

def get_you_choice():
    choice = input('가위, 바위, 보 중 하나를 선택하시오: ').lower()
    if choice == 'rock':
        return '바위'
    elif choice == 'paper':
        return '보'
    elif choice == 'scissors':
        return '가위'
    return choice

def get_computer_choice():
    computer_choices = ['가위', '바위', '보']
    return random.choice(computer_choices)
def decide(you_choice, computer_choice):
    if you_choice == computer_choice:
        return '무승부 이오!'
    elif (you_choice == '가위' and computer_choice == '보') or \
            (you_choice == '바위' and computer_choice == '가위') or \
            (you_choice == '보' and computer_choice == '바위'):
        return '당신이 이겼소!'
    elif (you_choice == 'scissors' and computer_choice == '보') or \
             (you_choice == 'rock' and computer_choice == '가위') or \
             (you_choice == 'paper' and computer_choice == '바위'):
        return '당신이 이겼소!'
    else:
        return '당신이 졌소!'

def game_start():
    win_count = 0
    lose_count = 0
    draw_count = 0

    while True:
        user_choice = get_you_choice()
        computer_choice = get_computer_choice()

        print(f'Player: {user_choice}')
        print(f'Computer: {computer_choice}')

        result = decide(user_choice, computer_choice)
        print(result)

        if '승리' in result:
            win_count += 1
        elif '패배' in result:
            lose_count += 1
        else:
            draw_count += 1
    while True:
            get_you_choice():
        
        re_try = input('다시 하겠소? (y/n): ')
        
    while True:
        
        if re_try.lower() != 'y':
            print('게임을 이만 끝내오.좋은 하루 되시오')
            print(f'총 게임 횟수: {win_count + lose_count + draw_count}')
            print(f'승리 횟수: {win_count}')
            print(f'패배 횟수: {lose_count}')
            print(f'무승부 횟수: {draw_count}')
            break
        elif re_try.lower() != 'n':
            print('게임을 다시 시작하오.')
if __name__ == '__main__':
    game_start()
