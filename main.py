"""
piedra papel tijera
"""

from random import choice


def start():
    equivalences = {
        'piedra': 'tijera',
        'tijera': 'papel',
        'papel': 'piedra'
    }
    possible_choices = equivalences.keys()

    while True:
        system_selected = choice(list(possible_choices))
        print('System selected: {}'.format(system_selected))

        user_selected = input('Select a choice: [piedra|papel|tijera]')
        if user_selected not in possible_choices:
            print('Please select a correct choice')
            continue

        system_beats = equivalences[system_selected]
        user_beats = equivalences[user_selected]

        if system_beats == user_selected:
            print('YOU LOSE!!')
        elif user_beats == system_selected:
            print('YOU WIN!!!')
        else:
            print('TIE, NOBODY WINS!!!!')


if __name__ == '__main__':
    start()
