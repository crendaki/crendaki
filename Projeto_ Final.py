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
        if event in (sg.Wib_closed, 'EXIT'):
         break
    window.close()                             
                                     
theme_dict= {'BACKGROUND': '#2b4750',
                'text': '#FFFFFF',
                'IMPUT': '#F2EF   