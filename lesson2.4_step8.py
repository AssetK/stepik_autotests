from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import os
import math
import time 

link = "http://sunInjuly.github.io/explicit_wait2.html"  

try:
    browser = webdriver.Chrome()
        
    browser.get(link) 
    
    
    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    
    book = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "book"))
            ) 
    book.click()

        
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(y)

    
    submit = WebDriverWait(browser, 7).until(EC.element_to_be_clickable((By.ID, "solve"))
            )
    
    #button = browser.find_element_by_css_selector("button.btn")
    submit.click()

    
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
