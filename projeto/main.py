"""
Autor: Renan Kaic
github.com/Renanka
"""
import pyautogui
import webbrowser as web
from time import sleep
import pyperclip
from projeto.gerar_cpf import gerar_cpf

# Define o tempo da pause entre cada operação do pyautogui.
pyautogui.PAUSE = 1

# Caminho que leva ao gmail e o endereço de e-mail.
end = 'https://mail.google.com/mail/u/0/#inbox?compose=new'
email = 'email@email.com'

# Gera e formata o cpf.
cpf = gerar_cpf()
cpf_form = f'{str(cpf)[0:3]}.{str(cpf)[3:6]}.{str(cpf)[6:9]}-{str(cpf)[9:]}'

# Formatação da mensagem que sera enviada.
msg = f"""
Nome: FULANO DE TAL
CPF: {cpf_form}
"""
# Abre o navegador ou link (no navegador padrão do sistema).
web.open(end)
sleep(20)

# Passo-a-passo para enviar a mensagem eletrônica.
pyperclip.copy(email)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')
pyautogui.press('tab')
pyperclip.copy(msg)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 'enter')


