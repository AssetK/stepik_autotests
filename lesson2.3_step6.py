from selenium import webdriver

from selenium.webdriver.support.ui import Select

import os
import math
import time 

link = "http://sunInjuly.github.io/redirect_accept.html"  

try:
    browser = webdriver.Chrome()
    browser.get(link) 
    
    
    journey2 = browser.find_element_by_xpath("/html/body/form/div/div/button")
    journey2.click()

    new_window = browser.window_handles[1]

    browser.switch_to.window(new_window)

    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
