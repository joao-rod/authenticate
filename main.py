from random import randint
from message import send_message

cod = randint(100000, 999999)
send_message(cod)
num = int(input('Digite o código recebido por SMS.'))
if num == cod:
  print('Autenticado com sucesso.')
else:
  print('Ocorreu um erro...')