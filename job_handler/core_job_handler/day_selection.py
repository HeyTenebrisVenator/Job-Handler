#!/usr/bin/python3

import datetime
import time
def Configure_day():
    try:
        dia = input('Qual dia você gostaria de programar  >>  ')
        if int(dia) < 10 and '0' not in dia:
            dia = f'0{dia}'
        if int(dia) > 31:
            print('Não coloque o dia maior do que 32')
            quit()
        mes = input('Qual mês você gostaria de programar  >>  ')
        if int(mes) < 10 and '0' not in mes:
            mes = f'0{mes}'
        if int(mes) > 12:
            print('O mês não pode ser maior do que 12')
            quit()
        ano = int(input('Qual ano você gostaria de programar  >>  '))
        if ano < int(datetime.datetime.today().year):
            print('Não pode colocar o ano menor do que ' + str(datetime.datetime.today().year))
            quit()
        text = input('O que gostaria de escrever  >>  ')
    except:
        print('Erro ao configurar a data')
        quit()


    data_configurada = f'{ano}-{mes}-{dia}'
    try:
        open(f'/usr/bin/job_handler/core_job_handler/Data_Saved/{data_configurada}', 'a').write(f'{text}\n')
    except:
        print('Data não configurada')
        quit()