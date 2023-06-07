from datetime import date, datetime, timezone, timedelta
data_atual = date.today()
data_em_texo = data_atual.strftime('%d/%m/%Y')
data_e_hora_atuais = datetime.now()

print(data_atual)
print('{}/{}/{}'.format(data_atual.day, data_atual.month, data_atual.year))
print(data_em_texo)

print(data_e_hora_atuais)

data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%y %H:%M')
print(data_e_hora_em_texto)

data_hora_texto = '01/03/2018 12:30'
data_hora = datetime.strptime(data_hora_texto, '%d/%m/%Y %H:%M')
difereca = timedelta(hours=-3)
fuso_horario = timezone(difereca)

print (data_hora_texto)
print (data_hora)
print(difereca)
print(fuso_horario)

print('-------------------------------------------------------------------')

data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')

print(data_e_hora_sao_paulo_em_texto)