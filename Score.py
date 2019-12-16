from Utils import SCORES_FILE_NAME


def add_score(points):
    # update user current winning score
    content = ''
    try:
        # try to read the scores file
        file = open(SCORES_FILE_NAME, 'r+')
        content = file.read()
        file.seek(0)
    except FileNotFoundError:
        # create a new scores file
        file = open(SCORES_FILE_NAME, 'w')
    # get scores
    if len(content) > 0:
        try:
            score = int(content)
        except ValueError:
            score = 0
    else:
        score = 0
    # update scores
    score += points
    file.write(str(score))
    file.close()
    print('Current score is', score)

