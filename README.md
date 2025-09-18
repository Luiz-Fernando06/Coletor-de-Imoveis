# 🏠 Coletor de Imóveis Martinelli

Este projeto é um web scraper que coleta automaticamente informações de imóveis do site Imóveis Martinelli
 e salva os dados em uma planilha Excel.

O programa extrai:

💲 Preço do imóvel

🔗 Link do anúncio

📅 Data da coleta

Ele foi feito em Python usando Selenium e openpyxl, e pode ser empacotado como um executável (.exe) para entregar ao cliente sem necessidade de Python instalado.

⚙️ Como funciona

Abre a página do site de imóveis usando Selenium.

Coleta preços e links de todos os anúncios disponíveis na página.

Armazena os dados em uma planilha Excel (imoveis.xlsx), criando a planilha se ainda não existir.

Salva a data da coleta junto com cada registro.

Fecha o navegador automaticamente após a coleta.

🛠 Tecnologias usadas

Python
 → Linguagem principal

Selenium
 → Automação do navegador

webdriver-manager
 → Baixa automaticamente o ChromeDriver correto

openpyxl
 → Manipulação de arquivos Excel

datetime
 → Captura a data atual

os
 → Gerencia caminhos e diretórios

 ▶️ Como usar
1. Instale as dependências
pip install selenium webdriver-manager openpyxl

2. Rode o script Python
python app.py

3. (Opcional) Transformar em .exe para entrega
python -m PyInstaller --onefile --noconsole app.py


O executável será gerado na pasta dist/.

O arquivo Excel será criado na mesma pasta do .exe.

🎯 Objetivo

Projeto desenvolvido para automatizar a coleta de dados de imóveis, facilitando análises de preços e links de anúncios sem precisar acessar manualmente o site.

📂 Saída

O programa gera automaticamente o arquivo:

imoveis.xlsx
