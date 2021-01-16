import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import numpy as np


host = 'smtp.gmail.com' #Mude de acordo com o seu host se não usar gmail
port = 587              #Enviadas com criptografia usam 465(não sei usar)
user = 'exemplo@gmail.com' #seu endereço de email
password = 'senha123' #senha do email
nome_remetente = 'Jacinto Pinto' # MUDE PARA O SEU NOME
assunto_mensagem = 'Impeachment 2021' #MUDE SE QUISER

# Criando objeto
print('Criando objeto servidor...')
server = smtplib.SMTP(host, port)
# Login com servidor
print('Login...')
server.ehlo()
server.starttls()
server.login(user, password)
nome, email = np.loadtxt('deputados.csv', delimiter=',', unpack=True, dtype='str')

for i in range(0, len(nome)):
    nome_destinatario = nome[i]
    email_destinatario = email[i]
    mensagem = """Prezado(a) Excelentíssimo(a) parlamentar {DESTINATARIO},

    Venho por meio desta carta pedir para que vossa senhoria se manifeste com relação ao impeachment do presidente em exercício, Jair Messias Bolsonaro.

    Acredito que não é necessário repetir, nesta carta, as diversas atrocidades ao nosso país e nossa população que o presidente em exercício tem sistematicamente empregado desde o começo do seu mandato.

    Dentre as inúmeras desumanidades, no entanto, se faz necessário reforçar o desastroso combate à pandemia de COVID-19, que assola o mundo e nosso país.

    Apenas para fins de ilustração da severidade e emergência do assunto, trago um dado de 15/01/2021: enquanto o mundo passava de dois milhões de mortos pelo COVID-19, o Brasil passava de 208 mil mortos. Em termos percentuais, o Brasil tem apenas 2,7% da população do planeta, mas tem 10% do total de mortes (ou seja, quatro vezes maior que a média).

    Infelizmente, os recentes pronunciamentos do presidente em exercício (e de seu ministro da saúde) sugerem que pouco está sendo feito para reverter a já desastrosa situação. O que pode ser, fatidicamente, observado pela ausência de apoio ao povo Manauara, que tem sido severamente impactado pela falta de recursos mínimos (como galões de oxigênio) para a operação de seus hospitais.

    A situação atual deixou de ser política e passou a ser de calamidade pública. Pelo exposto, como eleitor nortista que conta com o bom senso de seus representantes no congresso, peço para que vossa senhoria se manifeste publicamente, e o mais breve possível, favoravelmente ao processo de impeachment do presidente em exercício.

    Em saber que contarei com seu apoio, encerro aqui agradecendo os empenhos de vossa senhoria para reverter a dramática e sofrível situação em que o nosso povo se encontra.

    Sem mais para o momento,

    {REMETENTE}""".format(DESTINATARIO=str(nome_destinatario), REMETENTE=str(nome_remetente))

    print('Criando mensagem...')
    email_msg = MIMEMultipart()
    email_msg['From'] = user
    email_msg['To'] = email_destinatario
    email_msg['Subject'] = assunto_mensagem
    email_msg.attach(MIMEText(mensagem, 'plain'))

    print('Enviando mensagem...')
    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
    print('Mensagem enviada para {email_destinatario}'.format(email_destinatario=nome[i]))

server.quit()
