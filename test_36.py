import pytest
import time
import math


links = ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1']


def get_feedback(url, browser):
    browser.get(url)
    answer = math.log(int(time.time()))
    browser.implicitly_wait(5)
    answer_input = browser.find_element_by_xpath("//textarea[@placeholder='Type your answer here...']")
    answer_input.send_keys(str(answer))

    # Отправляем заполненную форму
    button = browser.find_element_by_class_name("submit-submission")
    button.click()

    feedback = browser.find_element_by_xpath("//pre[@class='smart-hints__hint']")
    feedback_text = feedback.text
    return feedback_text


class TestLinks:

    @pytest.mark.parametrize('link', links)
    def test_get_feedback(self, link, browser):
        feedback = get_feedback(link, browser)
        assert feedback == "Correct!", "Feedback is different from expected"
