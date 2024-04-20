from  selenium import webdriver
driver = webdriver.Firefox() # acessa o navagador atravez do driver
driver.get("https://ri.magazineluiza.com.br/") # o metodo get vai passar a url do site q vamos acessar
driver.find_element('xpath','/html/body/form/main/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/a[3]/i' ).click() # é passado o path do elemento q estamos buscando