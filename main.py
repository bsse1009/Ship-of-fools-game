from playroom import PlayRoom
from shipoffoolsgame import ShipOfFoolsGame
from player import Player


if __name__ =="__main__":
    """
        The main loop of the game
        create a playroom
        create a game instances
        create player instances 
        add game and players in playroom
        loop the game until the game finished
    """
    room = PlayRoom()
    game = ShipOfFoolsGame(21)
    room.set_game(game)
    player1 = Player()
    player1.set_name("Player 1")
    player2 = Player()
    player2.set_name("Player 2")
    room.add_player(player1)
    room.add_player(player2)
    room.reset_scores()
    while not room.game_finished():
        room.play_round()
        room.print_scores()
    room.print_winner()