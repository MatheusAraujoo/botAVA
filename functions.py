from selenium import webdriver
from webdriver_manager.chrome  import ChromeDriverManager
from selenium.webdriver import chrome 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pyautogui as bot
from time import sleep


#ESTRUTURA PARA O FUNCIONAMENTO 
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
driver.get("http://ava.femass.edu.br/")



#LOGANDO NO AVA 
def logar():
    #Full screen
    bot.click(880,30)
    #usuário
    bot.click(1257,385)
    bot.typewrite("2301230027")
    #senha
    bot.click(1248,481)
    bot.typewrite("Dudumatheuscod7@")
    bot.press("enter")
    return

#ENCIONTRANDO AS CAIXINHAS VAZIAS 
""" O find.exercises já me retorna uma lista, então eu posso manipulá-lo como tal"""

def find_exercises():
    global elements 
    elements = driver.find_elements(By.XPATH,"//*[@name='completionstate'][@value='1']")
    print(f"Existem {len(elements)} tarefas a serem feitas")
    return


#CHECANDO AS TAREFAS NOS CURSOS
def check_cursos():
    #MEUS CURSOS
    bot.click(100,429)
    #PRIMEIRO CURSO
    bot.click(123,470)
    sleep(2)
    find_exercises()
    bot.click(103,622)
    sleep(2)
    #SEGUNDO CURSO
    bot.click(123,730)
    sleep(2)
    find_exercises()
    bot.click(103,622)
    sleep(2)
    #TERCEIRA CURSO
    bot.click(120,779)
    sleep(2)
    find_exercises()
    bot.click(103,622)
    sleep(2)
    #QUARTO CURSO 
    bot.click(141,852)
    sleep(2)
    find_exercises()
    bot.click(103,622)
    sleep(2)
    #QUINTO CURSO 
    bot.click(148,923)
    sleep(2)
    find_exercises()
    bot.click(103,622)
    sleep(2)
    #SEXTO CURSO
    bot.click(141,995)
    sleep(2)
    find_exercises()

   
    return
    
 #TENTANDO CRIAR UM LAÇO PARA PERCORRER E CLICAR NOS ELEMENTOS DA LISTA
 #PROBLEMAS: O MOUSEINFO NÃO RECONHECE O PONTO E A LISTA NÃO ACEITA A VIRGULA COMO PARTE DO ELEMENTO
"""
    pos = [103.619]
    n=0
    # O range(len()) corrigiu o erro
    for n in range(len(pos)):
        print(pos[n])
        c = pos[n]
        
        bot.click(c)
"""

   
    