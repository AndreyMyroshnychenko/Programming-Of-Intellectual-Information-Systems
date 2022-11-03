import chess
import chess.svg
from eval import getEval
from negamax import negamax
from negascout import negascout
from PVS import PVS
import sys

board = chess.Board()

INFINITY = 999999


def BestMove(depth, board, func):
    Moves = board.legal_moves
    bestMove = None

    maxScore = -INFINITY

    for move in Moves:
        board.push(move)

        if func == 'negamax':
            score = negamax(depth - 1, board)
        elif func == 'negascout':
            score = negascout(depth - 1, board, -INFINITY, INFINITY)
        elif func == 'PVS':
            score = PVS(depth - 1, board, -INFINITY, INFINITY)
        print(board)
        print('\na b c d e f g h')
        board.pop()
        if score >= maxScore:
            print('Новый лучший ход: ' + str(move.uci()) + '\nБаллы: ' + str(score))
            maxScore = score
            bestMove = move
    return bestMove

def main(argv):
    board = chess.Board()
    func = 'negamax'

    while 1:
        cpuMove = BestMove(1, board, func)
        print('Ход ІІ: ' + board.san(cpuMove))
        board.push(cpuMove)
        print(board)
        print('\na b c d e f g h')
        svg = chess.svg.board(board)
        with open('board.svg', 'w') as file:
            file.write(svg)

        move = input("Введите ход: ")
        if str(move) == 'баллы':
            print('Кол-во баллов: ' + str(getEval(board)))
            move = input("Введите ход: ")
        board.push_san(str(move))

if __name__ == "__main__":
   main(sys.argv[1:])