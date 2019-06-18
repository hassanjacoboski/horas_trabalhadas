# -*- coding: utf-8 -*-
import sys
from datetime import datetime, timedelta

class MissingArgumentError(ValueError):
    pass

agora = datetime.now()
# agora = datetime(2019,5,14,18,16)

dia = agora.day
mes = agora.month
ano = agora.year
data_hoje = agora.strftime('%Y-%m-%d ')

if len(sys.argv) < 2:
    raise MissingArgumentError('You need to pass at least one'+
                               ' HH:MM as arguments.')

argumentos = sys.argv[1:]

dt_entradas = []
dt_saidas = []
trabalhadas = None

formato = '%Y-%m-%d %H:%M'

for i in range(0, len(argumentos), 2):
    dt_entradas.append(datetime.strptime(data_hoje + str(argumentos[i]),
                       formato))

    try:
        dt_saidas.append(datetime.strptime(data_hoje + str(argumentos[i + 1]),
                         formato))
    except IndexError as e:
        dt_saidas.append(datetime.now())

    parcial = dt_saidas[-1] - dt_entradas[-1]

    if trabalhadas is None:
        trabalhadas = parcial
    else:
        trabalhadas += parcial

oito_horas = timedelta(seconds=(8 * 3600))

if trabalhadas > oito_horas:
    sobrando = trabalhadas - oito_horas
    msg = f'\nTrabalhadas: {trabalhadas}\nHoras extras: {sobrando}'
else:
    faltando = oito_horas - trabalhadas
    msg = f'\nTrabalhadas: {trabalhadas}\nHoras faltando: {faltando}'
    if (len(argumentos) % 2) > 0:
        msg += f'\nHorário previsto de saída: ' + \
               f'{(datetime.now() + faltando).strftime("%H:%M")}'

print(msg)