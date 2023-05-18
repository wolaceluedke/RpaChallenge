from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd

# Atribuição de Variáveis
site = "http://rpachallenge.com/"
arquivo = 'challenge.xlsx'
df_registros = pd.read_excel(arquivo)

# Configurar o Service
service = Service('C:\drivers\chromedriver.exe')

# Configurar o ChromeDriver com o Service
driver = webdriver.Chrome(service=service)
print("Iniciando nosso robô\n")
print("Acessando site")
driver.get(site)

print('Inicia')
botao = driver.find_element(By.XPATH, "//button[@class='waves-effect col s12 m12 l12 btn-large uiColorButton']")
botao.click()
time.sleep(2)

for i, r in df_registros.iterrows():        
    role = r['Role in Company']
    email = r['Email']
    first_name = r['First Name']
    last_name = r['Last Name']
    phone = r['Phone Number']
    company = r['Company Name']
    address = r['Address']

    print(first_name)
    
    #LOGIN
    print("roteiro de escreita")
    textbox = driver.find_element_by_xpath("//input[@ng-reflect-name='labelRole']")
    textbox.clear()
    textbox.send_keys(role)
   

    print("email")
    textbox = driver.find_element_by_xpath("//input[@ng-reflect-name='labelEmail']")
    textbox.clear()
    textbox.send_keys(email)
    #time.sleep(0.5)

    print("nome")
    textbox = driver.find_element_by_xpath("//input[@ng-reflect-name='labelFirstName']")
    textbox.clear()
    textbox.send_keys(first_name)
    

    print("sobre-nome")
    textbox = driver.find_element_by_xpath("//input[@ng-reflect-name='labelLastName']")
    textbox.clear()
    textbox.send_keys(last_name)
    

    print("telefone")
    textbox = driver.find_element_by_xpath("//input[@ng-reflect-name='labelPhone']")
    textbox.clear()
    textbox.send_keys(phone)
    

    print("endereço")
    textbox = driver.find_element_by_xpath("//input[@ng-reflect-name='labelAddress']")
    textbox.clear()
    textbox.send_keys(address)
    

    print("empresa")
    textbox = driver.find_element_by_xpath("//input[@ng-reflect-name='labelCompanyName']")
    textbox.clear()
    textbox.send_keys(company)
    

    print('enviar')
    botao = driver.find_element_by_xpath("//input[@type='submit']")
    botao.click()
    time.sleep(0.5)

print('Processo finalizado')
