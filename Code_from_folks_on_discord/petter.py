import random

from Code_from_folks_on_discord.eleven import Player, clear_screen


class HumanPlayer(Player):
    def get_move(self):
        clear_screen()
        print(self.board, self.score)

        while True:
            direction = input('Enter a move: ')
            is_valid = self.board.is_valid_direction(direction.lower())
            if is_valid:
                return direction
            print("Invalid input!")

    def play(self):
        player_won = super().play()
        if player_won:
            print('You won')
        else:
            print('Game over')
        print(self.board, self.score)


class ComputerPlayer(Player):
    def get_move(self):
        return random.choice(self.board.valid_moves())


class ComputerPlayer2(ComputerPlayer):
    def get_move(self):
        moves = {}
        for move in self.board.valid_moves():
            _, point = self.board.calculate_move(move)
            moves[point] = move
        best_move_scores = [m for m in moves if m == max(moves)]
        if len(best_move_scores) > 1:
            return moves[best_move_scores[random.randint(len(best_move_scores))]]
        return moves[best_move_scores[0]]


if __name__ == "__main__":
    # import spyobject.SPyObject as SPY
    from spyobject import SPyObject as SPY

    # Assign our tested class to a variable
    player_obj = ComputerPlayer2()
    # Call our spy on that object assigned to the variable
    SPY(player_obj, globals()).obj_info()
    # used the .get_move() method to return its output to another variable
    move = player_obj.get_move()
    # now spy that variable to see what it has returned
    SPY(move, globals()).obj_info()
    print(SPY(player_obj, globals()).attributes)
