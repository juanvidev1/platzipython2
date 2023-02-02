import random

"""
EN - This is a classic game of rock, paper and scissors. Here we are going to explain the game, how it is 
divided into functions and how each function is working. Rock, paper amd scissors is a game where you can choose
between three options (rock, paper, or scissors) and each option has a strength over other and a weakness with
the other option, just like this:
    --> Rock beats Scissors
    --> Scissors beat Paper
    --> Paper beats Rock

This game is organized in 5 functions: one main function to run the game, two for the selection of the players
and two extra functions to develop the game logic and the winner:
    Funcs 1 and 2 --> Gets the selection of the player and the computer
    Func 3 --> It has the main game logic where the selections from the player and the bot are taken and decides
    who wins the round
    Func 4 --> This function checks when there's a game winner and finishes the game.
    Func 5 --> Main function. This function runs the rest of the functions and the game logic itself 

ES - Este es un clásico juego de piedra, papel y tijeras. Aquí explicaremos un poco el juego, como se dividió en
funciones y cómo está trabajando cada función. Piedra, papel y tijeras es un juego donde puede elegir entre tres
opciones (piedra, papel y tijera) y cada opción tiene una fortaleza frente a otra de las opciones y una debilidad
frente a la opción restante, justo así:
    --> Piedra le gana a Tijeras
    --> Tijeras le gana a Papel
    --> Papel le gana a Piedra

Este juego está organizado en 5 funciones: una función principal para correr el juego, dos para la selección
de los jugadores y dos más para la lógica central del juego y definir al ganador:
    Funciones 1 y 2 --> Obtienen las selecciones del usuario y del computador
    Función 3 --> Tiene la lógica central del juego donde se toman las selecciones del jugador y del pc y se
    decide quién es el ganador de la ronda
    Función 4 --> Esta función verifica cuando haya un ganador y finaliza el juego
    Función 5 --> La función principal. Esta función corre el resto de funciones y la lógica del juego como tal
    
    Advertencia: La documentación de las funciones quedará en inglés, como debe usarse en los entornos 
    profesionales
"""

def pc_selection():
    """
    options --> A tuple with the three options of the game (rock, paper and scissors)
    sel --> A random selection for the computer from the options tuple
    return sel --> It returns the selection made by the bot
    """
    options = ('piedra', 'papel', 'tijera')
    sel = random.choice(options)
    print('El bot escogió ' + sel)
    return sel

def user_selection():
    """
    options --> A tuple with the three options of the game (rock, paper and scissors)
    sel --> An input for the selection of the user from the options tuple
    return sel --> It returns the selection made by the bot
    """
    options = ('piedra', 'papel', 'tijera')
    sel = input('Selecciona entre Piedra, Papel o Tijera => ').lower()
    
    "This checks that the option sent by the user is a valid option from the tuple options"
    if sel not in options:
        print('Selecciona una opción válida, no seas imbécil')

    print('El jugador escogió ' + sel)
    return sel

def game_rules(user_selection, pc_selection, user_wins, pc_wins):

    """
    This function checks who is the round winner based on the selection
    
    Parameters
    ------------
    user_selection: string
        It receives a string that contains the user selection from the user
    pc_selection: string
        It receives a string that contains the computer selection
    user_wins: int
        It receives an integer containing the number of wins of the user
    pc_wins: int
        It receives an integer containing the number of wins of the computer

    return user_wins, pc_wins
    -------------
    int
        Returns the number of wins from the user and the number of wins of the computer so they can be used
        in the winner function
    """

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
    """
    This function checks the game winner checking the number of round-wins of the user and the computer and
    finishing the game when one of the player gets 2 wins

    Parameters
    ------------
    user_wins: int
        It receives an integer containing the number of the user wins
    pc_wins: int
        It receives an integer containing the number of the computer wins

    """

    if user_wins == 2:
        print('El jugador gana el juego')
        exit()

    if pc_wins == 2:
        print('El bot gana el juego')
        exit()


def run():
    """
    This is the main function that runs all the game itself making calls to the functions above and showing the
    static frame for the game
    """
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