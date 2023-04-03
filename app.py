from flask import Flask, render_template
import chess
import chess.engine
import urllib.parse
import json

app = Flask(__name__)


# engine = chess.engine.SimpleEngine.popen_uci("./engine/stockfish-windows-2022-x86-64-avx2.exe")
# engine = chess.engine.SimpleEngine.popen_uci("./engine/OutOfStockFish.exe")

@app.route('/')
def game():
    return render_template('game.html')


@app.route('/engine/<path:fen>/<int:thinking_time>')
def get_engine_move(fen, thinking_time):
    engine = chess.engine.SimpleEngine.popen_uci("./engine/OutOfStockFish.exe")
    decoded_fen = urllib.parse.unquote(fen)
    board = chess.Board(decoded_fen)
    result = engine.play(board, chess.engine.Limit(time=thinking_time))
    engine.close()
    return json.dumps(result.move.uci())


if __name__ == '__main__':
    app.run()
