import random

def pc_selection():
    options = ('piedra', 'papel', 'tijera')
    sel = random.choice(options)
    print('El bot escogió ' + sel)
    return sel

def user_selection():
    options = ('piedra', 'papel', 'tijera')
    sel = input('Selecciona entre Piedra, Papel o Tijera => ').lower()
    
    if sel not in options:
        print('Selecciona una opción válida, no seas imbécil')

    print('El jugador escogió ' + sel)
    return sel

def game_rules(user_selection, pc_selection, user_wins, pc_wins):

    if user_selection == pc_selection:
        print('Es un empate')
    
    elif(user_selection == 'tijera'):
        if(pc_selection == 'papel'):
            print('La tijera le gana al papel')
            print('El jugador gana esta ronda')
            user_wins += 1
        else:
            print('La piedra le gana a la tijera')
            print('El bot gana esta ronda')
            pc_wins += 1
        
    elif(user_selection == 'papel'):
        if(pc_selection == 'piedra'):
            print('El papel le gana a la piedra')
            print('El jugador gana esta ronda')
            user_wins += 1
        else:
            print('La tijera le gana al papel')
            print('El bot gana esta ronda')
            pc_wins += 1
    
    elif(user_selection == 'piedra'):
        if(pc_selection == 'tijera'):
            print('La piedra le gana a la tijera')
            print('El jugador gana esta ronda')
            user_wins += 1
        else:
            print('El papel le gana a la piedra')
            print('El bot gana esta ronda')
            pc_wins += 1
    
    return user_wins, pc_wins



def winner(user_wins, pc_wins):

    if user_wins == 2:
        print('El jugador gana el juego')
        exit()

    if pc_wins == 2:
        print('El bot gana el juego')
        exit()


def run():
    user_wins = 0
    pc_wins = 0
    round = 1

    while True:

        print('*' * 10)
        print('ROUND ' + str(round))
        sel_user = user_selection()
        sel_pc = pc_selection()
        print('*' * 10)
        user_wins, pc_wins = (game_rules(sel_user, sel_pc, user_wins, pc_wins))

        round += 1

        print('*' * 10)
        print('MARCADOR')
        print('Jugador: ' + str(user_wins) + '/3')
        print('Bot: ' + str(pc_wins) + '/3')
        print('*' * 10)
        
        winner(user_wins, pc_wins)

if __name__ == '__main__':
    run()