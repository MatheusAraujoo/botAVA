from selenium import webdriver
from webdriver_manager.chrome  import ChromeDriverManager
from selenium.webdriver import chrome 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pyautogui
from time import sleep


#Logando no AVA
def logar():
    #Full screen
    pyautogui.click(880,30)
    #usuário
    pyautogui.click(1257,385)
    pyautogui.typewrite("2301230027")
    #senha
    pyautogui.click(1248,481)
    pyautogui.typewrite("Dudumatheuscod7@")
    pyautogui.press("enter")
    return

#Encontrando as caixinhas vazias 
""" O find.elements já me retorna uma lista, então eu posso manipulá-lo como tal"""

def find_elements():
    global elements 
    elements = driver.find_elements(By.XPATH,"//*[@name='completionstate'][@value='1']")
    print(f"Existem {len(elements)} tarefas a serem feitas")
    return


#CHECAR OUTRA MATÉRIA

#somente o  find_element, no singular, possui o método .click(), o que faz total sentido.
def cursos():
        driver.find_element(By.XPATH,"//*[@data-key='mycourses']").click()
        #materias = driver.find_elements(By.XPATH,f"//*[@class='list-group-item list-group-item-action '][@data-key<{f}]") 
        c=625
        while c<940:
             c=c+1
             driver.find_elements(By.XPATH,f"//*[@class='list-group-item list-group-item-action '][@data-key<{c}]")
             if c%3==0 or c%7==0:
                  driver.find_element(By.XPATH,f"//*[@class='list-group-item list-group-item-action '][@data-key<{c}]").click()
                  

             
       
        
        

    

    
   


#MAIN
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
driver.get("http://ava.femass.edu.br/")




logar()
sleep(1)

#checagem das atividades
pyautogui.click(142,429)
pyautogui.click(134,469)

pyautogui.dragTo(900,418)
sleep(1)
pyautogui.scroll(-1000)

sleep(3)
find_elements()

cursos()
