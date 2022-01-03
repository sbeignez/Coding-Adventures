import random
from snake_utils import *
from snake_game_session import Snake, Apple

class GameEngine():

    def __init__(self, game):
        self.game = game

    def is_game_over(self, session):
        moves_possible = [ Direction.add(session.snake.head(), d) for d in Direction.all_dirs()]
        game_over = not any([ self.is_valid_move(session, move) for move in moves_possible])
        return game_over

    def is_valid_action(self, session, action):
        return self.is_valid_move(session, Direction.add(session.snake.head(), action))

    def is_valid_move(self, session, block):
        return self.is_valid_move_board(session, block) and self.is_valid_move_snake(session, block)

    def is_valid_move_board(self, session, block):
        return block[0] >= 1 and block[0] <= session.board.cols and block[1] >= 1 and block[1] <= session.board.rows

    def is_valid_move_snake(self, session, block):
        return block not in session.snake.body



    def init_snake(self, session):
        """ Rules to initialize the snake. Options:
        # 1. Random
        # 2. Head in center, Tail upward
        """

        snake_body = [ ((session.board.cols+1)//2, (session.board.rows+1)//2 + 2 - i) for i in range(3) ]
        # print("Engine.init_snake()", snake_body)
        session.snake = Snake(snake_body)



    def create_apple(self, session):
        """ Create new apple randomly
        Exclude cells with snake body
        """

        if session.snake.len() == session.board.rows * session.board.cols:
            return None
        cells = { (c,r) for r in range(1, session.board.rows) for c in range(1, session.board.cols + 1) } - set(session.snake.body) 
        
        if len(cells) != 0:
            apple = Apple(* random.choice(tuple(cells)))
            session.apple = apple
        else:
            print("Engine.create_apple(): error")

        # print("Engine.create_apple()", apple)
        


    def next_state(self, session, action):

        direction = action

        new_head = Direction.add(session.snake.head(), direction)
        
        if self.is_valid_move(session, new_head): # No COLLISION BOARD BODERS and BODY

            # MOVE
            is_apple = new_head == session.apple.cell()

            session.snake.move_to(new_head, is_apple)
            session.steps += 1

            if is_apple:
                self.game.engine.create_apple(session)
                session.score += 1
            

            # EAT APPLE
            if :
                if session.snake.len() == session.board.rows * session.board.cols:
                    print("WIN")
                    return 3 # game_won
                session.snake.grow()
                

            return "game_on"

        else:
            if self.is_game_over(session.board):
                return "game_over"
            else:
                # invalid move. Retry. (for Human agent)
                return "game_paused"
