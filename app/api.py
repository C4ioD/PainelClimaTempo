import requests


#Consulta Api clima atual com base na latitude e longitude
class ClimaAtual:
  
  def __init__(self, api_key):
    self.api_key = api_key
    self.idioma = 'pt_br'
    self.unidade = 'metric'


#Retorna os dados em formato Json
  def json_atuais(self, latitude, longitude):
    link = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={self.api_key}&lang={self.idioma}&units={self.unidade}'
    requisicao = requests.get(link)
    return requisicao.json()
  
#Consulta Api Previsao clima do dia seguinte com base na latitude e longitude
class ClimaPrevisao:
  
  def __init__(self, api_key):
    self.api_key = api_key
    self.idioma = 'pt_br'
    self.unidade = 'metric'

  #Retorna os dados  de previsao em formato Json
  def json_prev(self, latidude, longitude):
    link = f'https://api.openweathermap.org/data/2.5/forecast?lat={latidude}&lon={longitude}&appid={self.api_key}&lang={self.idioma}&units={self.unidade}'
    requisicao = requests.get(link)
    return requisicao.json()

  
