from flask import Flask
from Utils import ERROR_MESSAGE, SCORES_FILE_NAME

app = Flask(__name__)


def get_score():
    # function to read the user current score
    try:
        scores = open(SCORES_FILE_NAME, "r")
        score = int(scores.readline())
        scores.close()
        return score
    except ValueError:
        # file contains unknown data format
        return -1
    except FileNotFoundError:
        # no scores yet
        return -1


@app.route('/')
def score_server():
    # get the score and show it on http://localhost:8080/
    score = get_score()
    if score < 1:
        return """
        <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
        <body>
            <h1><div id="score" style="color:red">{0}</div></h1>
        </body>
        </html>
        """.format(ERROR_MESSAGE)
    return """
    <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>The score is <div id="score">{0}</div></h1>
        </body>
    </html>""".format(score)


if __name__ == '__main__':
    app.run(host='localhost', debug=True, threaded=True, port=8080)
