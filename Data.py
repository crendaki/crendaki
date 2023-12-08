
def data_por_extenso(data):
    #remova as barras
    data= data.replace("/", "")
                       
    if not data.isdigit():
        return None
                        
    dia, mes, ano = data[:2], data[2:4], data[4:]

    meses ={
        "01": 'Janeiro',
        "02": 'Fevereiro',
        "03": 'Março',
        "04": 'Abril',
        "05": 'Maio',
        "06": 'Junho',
        "07": 'Julho',
        "08": 'Agosto',
        "09": 'Setembro',
        "10": 'Outubro',
        "11": 'Novembro',
        "12": 'Dezembro',
    }

    mes_por_extenso = meses.get(mes)

    if not mes_por_extenso:
            return None                     

    return F"{dia} de {mes_por_extenso} de {ano}"

resultado = data_por_extenso(input("Digite uma data no formato dd/mm/aaaa: "))
print(resultado)                                   






        