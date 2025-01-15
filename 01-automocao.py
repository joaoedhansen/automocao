
import pyautogui
import time #biblioteca para realizar pausas em lugar especificos
import pandas

#configurar para cada comando possuir pausa de 1 segundo
pyautogui.PAUSE = 0.5 

#pyautogui.click() > clicar (X: >  Y: ⬇️)
#pyautogui.press() > pressionar uma tecla
#pyautogui.write() > escrever
#pyautogui.hotkey() > atalho de teclado
#pyautogui.scroll() > positivo = cima | negativo = baixo

#Passo 1: Abrir o sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.press("win") #apertar a tecla windows
pyautogui.write("chrome") #digitar "chrome"
pyautogui.press("enter") #apertar enter

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") #digitar a URL
pyautogui.press("enter") #pressionar enter

time.sleep(3) #pausa em um ponto em especifico

#Passo 2: Fazer o login

pyautogui.click(x=659, y=375) #selecionar primeiro grid de e-mail
pyautogui.write("joaoedhansen@gmail.com") #digital e-mail

pyautogui.press("tab") #proxímo grid de senha
pyautogui.write("tobias") #digitar senha

pyautogui.press("tab") #selecionar o botão "Logar"
pyautogui.press('enter') #entrar



#Passo 3: Importar a base de dados dos produtos

tabela = pandas.read_csv("01-produtos.csv")
print(tabela)

#Passo 4: Cadastrar 1 produto

for linha in tabela.index:
    time.sleep(1) #pausa em um ponto em especifico
    pyautogui.click(x=623, y=256) #clicar na caixa

    #codigo
    codigo = tabela.loc[linha , "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab") #proxíma caixa

    #marca
    marca = tabela.loc[linha , "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab") #proxíma caixa

    #tipo
    tipo = tabela.loc[linha , "tipo"]
    pyautogui.write(str(tipo)) 
    pyautogui.press("tab") #proxíma caixa

    #categoria
    categoria = tabela.loc[linha , "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab") #proxíma caixa

    #preco_unitario
    preco_unitario = tabela.loc[linha , "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab") #proxíma caixa

    #custo
    custo = tabela.loc[linha , "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab") #proxíma caixa

    #obs
    obs = str(tabela.loc[linha , "obs"])
    if obs != "nan": #se obs for diferente de "nan" (vazio), escreve
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter") #apertar o botão de enviar
    pyautogui.press("home") #voltar ao inicio da página
