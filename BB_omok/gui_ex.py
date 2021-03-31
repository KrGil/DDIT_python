from ursina import *
import numpy as np
from tensorflow.keras.models import load_model
from gomoku import Board, Gomoku
from conda.common._logic import FALSE

model = load_model('models/20201213_202430.h5')

w, h = 20, 20
board = Board(w=w, h=h)
game = Gomoku(board=board)

# cpu turn
input = game.board.board.copy()
input[(input != 1) & (input != 0)] = -1
input[(input == 1) & (input != 0)] = 1
input = np.expand_dims(input, axis=(0, -1)).astype(np.float32)

output = model.predict(input).squeeze()
output = output.reshape((20, 20))
output_y, output_x = np.unravel_index(np.argmax(output), output.shape)

