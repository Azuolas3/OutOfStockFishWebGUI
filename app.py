from flask import Flask, render_template
import chess
import chess.engine
import urllib.parse

app = Flask(__name__)


# engine = chess.engine.SimpleEngine.popen_uci("./engine/stockfish-windows-2022-x86-64-avx2.exe")
# engine = chess.engine.SimpleEngine.popen_uci("./engine/OutOfStockFish.exe")


@app.route('/')
def hello_world():  # put application's code here
    return render_template('home.html')


@app.route('/engine/<path:fen>')
def test_engine(fen):
    engine = chess.engine.SimpleEngine.popen_uci("./engine/OutOfStockFish.exe")
    decoded_fen = urllib.parse.unquote(fen)
    board = chess.Board(decoded_fen)
    result = engine.play(board, chess.engine.Limit(time=3))
    engine.close()
    return result.move.uci()


if __name__ == '__main__':
    app.run()
