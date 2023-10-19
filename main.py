# Importando as bibliotecas
import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import time

# Criando o objeto da notificação
notification = ToastNotifier()

# Função que coleta dados de uma determinada url
def get_data(url):
    request = requests.get(url)

    return request.text


# Função que transforma minutos em segundos
def convert_min_sec(min):
    return min * 60

# Coletando dados da url que mostra o clima
html_data = get_data("https://weather.com/en-IN/weather/today/l/-23.53,-46.62")

# Convertendo em código HTML com o beautiful soup
soup = BeautifulSoup(html_data, 'html.parser')

# Encontrando os dados que queremos (Temperatura atual e chances de chuva)
current_temp = soup.findAll("span", class_="CurrentConditions--tempValue--MHmYY")
chances_rain = soup.findAll("span", class_="Column--precip--3JCDO")

# Transformando em strings
temp = (str(current_temp))
rain = (str(chances_rain))

# Formatando o texto da notificação
result = f"Temperatura Atual em São Paulo: {temp[82:-69]}ºC\n{rain[1589:-8]} de chance de chuva."

intervalo_notificacao = convert_min_sec(int(input("A cada quantos minutos deseja ser atualizado do clima? ")))


while True:
    notification.show_toast("Atualização do Clima", result, duration=10)
    time.sleep(intervalo_notificacao)
