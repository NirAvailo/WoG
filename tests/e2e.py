import sys

from selenium import webdriver, common

from Utils import WEBDRIVER_EXEC_PATH, DOCKER_IP, DOCKER_PORT

driver = webdriver.Chrome(executable_path=WEBDRIVER_EXEC_PATH)
driver.implicitly_wait(3)


def test_scores_service(app_url):
    try:
        driver.get(app_url)
        score_element = driver.find_element_by_css_selector("div#score")
        score = int(score_element.text)
        return not (score < 0 or score > 1000)
    except common.exceptions.NoSuchElementException:
        return False
    except AttributeError:
        return False
    except ValueError:
        return False
    finally:
        driver.close()


def main_function():
    sys.exit(0 if test_scores_service('http://' + DOCKER_IP + ':' + DOCKER_PORT + '/') else -1)


if __name__ == '__main__':
    main_function()
