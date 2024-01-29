import PySimpleGui as sg
from datetime import date
import random
import requests
import locale as l
import mysql.connector as mysql

def banco():
      nome = values['-nome-']
      email = values['-email-']
      telefone = values ['-telefone-']
 
 try:
    conexao = mysql.connect(
      host="127.0.0.1",
      user= "root", 
      password = "root",
      database ="dbpython"
    )    

    print("Conexão realizada com sucesso.")
    cursor = conexao.cursor()

    sql = "INSERT INTO contatos(nome, email, telefone) VALUES(%s, %s, %s)"
    vals =(nome, email, telefone)
    cursor.execute(sql, vals)
    conexao.commit()
    print("Salvo com sucesso")

 except mysql.Error as e:
    print(e.msg)

def grafico():
    BAR_WIDTH = 50
    BAR_SPACING = 75
    EDGE_OFFSET = 3
    GRAPH_SIZE = DATA_SIZE = (300, 400)

    sg.theme('Dashboard')
    layout = [[sg.text('Grafico de barras com PYSimpleGUI')],
              [sg.Graph(graph_size, (0,0), DATA_SIZE, K='-GRAPH-')],
              [sg.button('OK'), sg.T('Click para ver mais dados'), sg.Exit()]] 
    window = sg.window('Grafico de barras', layout, finalize =True)

    while true:
        graph.erase()
        for i in range(7):
            graph_value = random.randint(0, graph_SIZE[1])
            graph.draw_rectangle(top_left=(i * bar_spacing + edge_offset + bar_width, 0),
                             bottom_right= (i * BAR_SPACING + EDGE_OFFSET + BAR_WIDTH, 0),
                             fill_color = sg.theme_button_color()[1])
            graph.draw_text(text = graph_value, location =(i * BAR_SPACING + EDGE_OFFSET + 25, graph_value + 10))

        event, values =window.read()
        if event in (sg.Win_closed, 'Exit'):
          break
    window.close()                             
                                     
theme_dict= {'BACKGROUND': '#2b4750',
                'text': '#FFFFFF',
                'IMPUT': '#F2EFE8,   
                'Text_Input: #000000',
                'SCROLL': '#F2EFE8',
                'BUTTON': ('#000000', '#C2D4D8'),
                'PROGRESS': ('#FFFFFF', '#C7D5E0'),
                'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH':0}
sg.LOOK_AND_FEEL_TABLE ['Dashboard'] = theme_dict
sg.theme('Dashboard')
BORDER_COLOR = '#C7D5E0'
DARK_HEADER_COLOR = '#1B2838'
BPAD_TOP = ((20,20), (20, 10))
BPAD_LEFT = ((20,10), (0, 10))
BPAD_LEFT_INSIDE = (0, 10)
BPAD_RIGHT + ((10, 20), (10, 20))

l.setlocale(l.LC_TIME, "pt")
data_atual = date.today()
data_em_texto = data_atual.strftime("%d de %B de %Y").title()
top_banner = [[sg.Text('Dashboard'+''*64, font='Any 20', background_color= DARK_HEADER_COLOR),
               sg.Text(data_em_texto, font='Any 20', background_color)]]   

API_KEY ="7753eeffac2836bdb825e03be43f51"
cidade ="Brasilia"
link =f"https://api.openweathermap.org/data2.5/weather?q={cidade}&appid={API_KEY}&lang+pt_br"
requisicao = requests.get(link)
requisicao_dic =reuisicao.json()
descricao= requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] - 273.15
top = [[sg.Text(f"Temperatura em Brasilia {temperatura:.2f}"C", size=(50, 1),justification = 'c', pad = BPAD_TOP, font='Any 20')],
            [sg.T(f'{i*25}-{i*34}') for i in range(7), ]
                                     
      

