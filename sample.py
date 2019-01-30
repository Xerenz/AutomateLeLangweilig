from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from jane import string_man
import pyautogui
import time

pyautogui.PAUSE = 1

driver = webdriver.Firefox()
x, y = 555, 178

driver.get('http://a-student.github.io/SvgToVectorDrawableConverter.Web/')

def the():
    string_man()
    elem = driver.find_element_by_tag_name('u')
    elem.click()
    time.sleep(0.25)
    print('moving...')
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(0.25)
    print('moving...')
    pyautogui.moveTo(1110, 747)
    pyautogui.click()
    print('moving...')

    element = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save to file')]"))
    )
    element.click()

    pyautogui.moveTo(504, 448)
    pyautogui.click()
    pyautogui.moveTo(914, 549)
    pyautogui.click()

    element = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Reset')]"))
    )
    element.click()


