import PySimpleGUI as sg

from generate_cod import get_cod
from message import send_message

validator = get_cod()
send_message(validator)

layout = [
  [
    sg.Text(
      'Digite o código de 6 dígitos recebido por SMS',
      background_color='#1D1C2D',
      text_color='#e3e3e3',
      font='"Roboto" 14', 
      size=(32, 0)
    )
  ],
  
  [
    sg.Input(
      key='code',
      background_color='#1D1C19',
      text_color='#e3e3e3',
      font='"Roboto" 14', 
      size=(32, 2)
    )
  ],
  
  [
    sg.Text(
      key='space',
      background_color='#1D1C2D',
      size=(0, 1)
    )
  ],
  
  [
    sg.Button(
      'Submeter',
      key='ok',
      button_color='#1D1C20',
      font='"Roboto" 14', 
      size=(10, 0)
    ),
    
    sg.Text(
      key='space',
      background_color='#1D1C2D',
      size=(8, 0)
    ),
    
     sg.Button(
      'Cancelar',
      key='error',
      button_color='#1D1C20',
      font='"Roboto" 14', 
      size=(10, 0)
    )
  ],
  
  [
      sg.Text(
      key='response',
      background_color='#1D1C2D',
      text_color='#e3e3e3',
      font='"Roboto" 14', 
      size=(32, 0)
    )
  ]
]

window = sg.Window(
  'Autentique-se',
  layout,
  background_color='#1D1C2D',
  size=(410, 300),
  location=(500, 150)
)

while True:
  events, values = window.read()
  if events == sg.WINDOW_CLOSED or events == 'error':
    break
  
  if events == 'ok':
    if str(validator) == values['code']:
      window['response'].update('Autenticado com sucesso.', text_color='#50fa7b')
      window.refresh()
    else:
      window['response'].update('Código incorreto. Tente novamente.', text_color='#ff5555')
