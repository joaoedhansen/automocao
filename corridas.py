import requests 
from bs4 import BeautifulSoup
import pandas as pd
import time

req = requests.get('https://speedhive.mylaps.com/livetiming/FD0F7C7ED42BEA92-2147484464/sessions/FD0F7C7ED42BEA92-2147484464-1073743280#all-results')
time.sleep(10)
#verificar se o servidor retorna o código 200 (200 = ok)
if req.status_code == 200:
    print('ok')
    content = req.content
    soup = BeautifulSoup(content, 'html.parser')
    #buscar a class "tab-content mt-3 shadow-sm"
    coluna = soup.find_all(class_='m-0 title')


    print(coluna)

    # for elementos in coluna:
    #     nome_coluna = 