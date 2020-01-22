import os

SCORES_FILE_NAME = 'Scores.txt'
ERROR_MESSAGE = 'Something went wrong..'
WEBDRIVER_EXEC_PATH = 'C:/Temp/chromedriver.exe'
HOST_IP = '0.0.0.0'
HOST_PORT = '5000'
DOCKER_IP = '192.168.99.103'
DOCKER_PORT = '8777'


def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')
