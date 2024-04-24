from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
# faz com que nao precise baixar um driver  pois ele chama um q é compativel com a versao do  navegador
servico = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service = servico)


def _cadastrar(nomeUser, emailUser):
    driver.get('https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_C0aj3FjN5e0') #passa a url do site q vai ser acessado
    driver.find_element('xpath','//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input').send_keys(nomeUser)
    driver.find_element('xpath','//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input').send_keys(emailUser)
    driver.find_element('xpath','//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/button/span/b').click()
