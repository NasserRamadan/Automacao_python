import pyautogui
import time
import pandas

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=649, y=466)

pyautogui.write('nasserramadan22@gmail.com')
pyautogui.press("tab")
pyautogui.write('1234')
pyautogui.press("enter")

time.sleep(3)


tabela = pandas.read_csv("C:\Instensivão Python\Python POWERUP\produtos.csv")
print (tabela)

for linha in tabela.index:
    pyautogui.click(x=659, y=324)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
