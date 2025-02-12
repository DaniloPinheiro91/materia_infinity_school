from datetime import datetime

#captura a hora atual e transforma em uma lista de numeros inteiros
def horario_atual ():
    horario = datetime.now()
    hora_minuto = horario.strftime('%H:%M')
    hora_minuto = list(map(int, hora_minuto.split(":")))
    return hora_minuto
# imprime uma divisão -=-=-=-=-=-=...
def imprime_linha():
    print('-='*30)

hora_atual = horario_atual()

imprime_linha()
if hora_atual[0] >= 0 and hora_atual[0] < 12:
    print(f'{hora_atual[0]}:{hora_atual[1]} Bom dia!')
elif hora_atual[0] >= 12 and hora_atual[0] < 18:
    print( f'{hora_atual[0]}:{hora_atual[1]}Boa Tarde!')
else:
    print(f'{hora_atual[0]}:{hora_atual[1]} Boa noite! ')
imprime_linha()