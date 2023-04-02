from flask import Flask, render_template
import chess
import chess.engine
import urllib.parse
import json

app = Flask(__name__)


# engine = chess.engine.SimpleEngine.popen_uci("./engine/stockfish-windows-2022-x86-64-avx2.exe")
# engine = chess.engine.SimpleEngine.popen_uci("./engine/OutOfStockFish.exe")


@app.route('/')
def home():  # put application's code here
    return render_template('home.html')

@app.route('/game')
def game():  # put application's code here
    return render_template('game.html')


@app.route('/engine/<path:fen>')
def get_engine_move(fen):
    engine = chess.engine.SimpleEngine.popen_uci("./engine/OutOfStockFish.exe")
    decoded_fen = urllib.parse.unquote(fen)
    board = chess.Board(decoded_fen)
    result = engine.play(board, chess.engine.Limit(time=3))
    engine.close()
    return json.dumps(result.move.uci())


if __name__ == '__main__':
    app.run()
