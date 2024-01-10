import pyautogui
import pandas 
from time import sleep

# comando basicos do pyautogui
# clicar -> pyautogui.click
# escrever -> pyautogui.write
# apertar tecla -> pyautogui.press
# aoertar para atalhos obs:ctrl+ c-> pyautogui.hotkey
# scroll/rolar tela -> pyautogui.scroll


# acessar o chrome

pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# acessar o sistema
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
sleep(3)

#login
pyautogui.click(x=763, y=408)
pyautogui.write('botafogo@gmail.com')
pyautogui.press('tab')
pyautogui.write('852369741')
pyautogui.press('tab')
pyautogui.press('enter')

# cadastro de produtos 
tabela = pandas.read_csv('produtos.csv')


for linha in tabela.index:
    # codigo
    pyautogui.click(x=743, y=293)
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press('tab')

    # marca
    pyautogui.write(str(tabela.loc[linha,'marca']))
    pyautogui.press('tab')

    # tipo
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')

    # categoria
    pyautogui.write(str(tabela.loc[linha,'categoria']))
    pyautogui.press('tab')

    # preco
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))    
    pyautogui.press('tab')

    #custo
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    #obs
    obs = tabela.loc[linha,'obs']
    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha, 'obs']))
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(2000)



