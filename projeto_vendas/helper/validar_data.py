from datetime import datetime

def validar_data(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
        print("Data válida")
    except:
        print("Data inválida")