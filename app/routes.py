from app import app
from app.forms import FormularioClima
from app.api import  ClimaPrevisao, ClimaAtual
from app.senhas import api_key
from flask import render_template, url_for, redirect, request
from datetime import datetime
from pytz import timezone

#Latitude e longitude da codade inicial (Timóteo-MG)
latitude = '-19.5845'
longitude = '-42.6444'

@app.route('/', methods=['GET','POST'])
def home():
  #Formulario de busca
  formulario = FormularioClima()

  #Carregamento dos dados atuais
  dados_atual = ClimaAtual(api_key).json_atuais(latitude, longitude)

  #Formata date e horas e altera o fuso horário - America/São Paulo
  data_hora_atual = datetime.fromtimestamp(float(dados_atual['dt']), tz=timezone('America/Sao_Paulo')).strftime('%d/%m/%Y %H:%M')
  hora_nascer_sol = datetime.fromtimestamp(float(dados_atual['sys']['sunrise']), tz=timezone('America/Sao_Paulo')).strftime('%H:%M')
  hora_por_sol = datetime.fromtimestamp(float(dados_atual['sys']['sunset']), tz=timezone('America/Sao_Paulo')).strftime('%H:%M')

  #Carregamento dos dados de previsao  
  dados_prev = ClimaPrevisao(api_key).json_prev(latitude, longitude)
  dados_prev = dados_prev['list'][0:7]


  #Busca os dados conforme valores preenchidos pelo usuario
  if request.method == 'POST':

    #Carregamento dos dados atuais
    dados_atual = ClimaAtual(api_key).json_atuais(formulario.latitude.data, formulario.longitude.data)

    #Formata data e horas e altera o fuso horário - America/São Paulo
    data_hora_atual = datetime.fromtimestamp(float(dados_atual['dt']), tz=timezone('America/Sao_Paulo')).strftime('%d/%m/%Y %H:%M')
    hora_nascer_sol = datetime.fromtimestamp(float(dados_atual['sys']['sunrise']), tz=timezone('America/Sao_Paulo')).strftime('%H:%M')
    hora_por_sol = datetime.fromtimestamp(float(dados_atual['sys']['sunset']), tz=timezone('America/Sao_Paulo')).strftime('%H:%M')

    #Carregamento dos dados de previsao 
    dados_prev = ClimaPrevisao(api_key)
    dados_prev = dados_prev.json_prev(formulario.latitude.data, formulario.longitude.data)
    dados_prev = dados_prev['list'][0:7]

  return render_template('index.html', formulario= formulario, dados_atual=dados_atual, data_hora_atual = data_hora_atual, hora_nascer_sol=hora_nascer_sol, hora_por_sol=hora_por_sol, dados_prev=dados_prev)