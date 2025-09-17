# Bibliotecas necessarias
from selenium import webdriver  # Abrir a página
from selenium.webdriver.common.by import By # Seleciona todos os elementos especificos que eu quero
from datetime import datetime  # Pega data atual
import openpyxl

# 1 entrar: https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&id_cidade%5B%5D=129&finalidade=&dormitorio=&garagem=&vmi=&vma=&ordem=4
driver = webdriver.Chrome()
driver.get("https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&id_cidade%5B%5D=129&finalidade=&dormitorio=&garagem=&vmi=&vma=&ordem=4")

# 2 inserir preço, link da casa, data dentro de uma planilha que eu criei
# 3 anotar os preços, links das casas e datas de cada um dos anuncios daquela página
precos = driver.find_elements(By.XPATH, "//div[@class='card-valores']/div")
links = driver.find_elements(By.XPATH, "//a[@class='carousel-cell']")

planilha_imoveis = openpyxl.load_workbook(r"C:\Users\eluiz\Downloads\imoveis.xlsx")
pagina_imoveis = planilha_imoveis['precos']

for preco, link in zip(precos, links):
    preco_limpo = preco.text.strip(' ')
    link_pronto = link.get_attribute('href')
    data_atual = datetime.now().strftime('%d/%m/%Y')
    pagina_imoveis.append([preco_limpo, link_pronto, data_atual])

planilha_imoveis.save('imoveis.xlsx')
