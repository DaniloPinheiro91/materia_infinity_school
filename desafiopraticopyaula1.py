competidores = (
    ('EquipeA', [110,80,95,70]),
    ('EquipeB', [80,100,85,75]),
    ('EquipeC', [110,80,90,85]),
    )
medias = []
for equipes, pontuacoes in competidores:
    print(F'{equipes}: {pontuacoes}\n')
    media = sum(pontuacoes)/len(pontuacoes)
    medias.append((equipes, media))

medias.sort(key=lambda x: x[1], reverse=True)
print(f'A media das equipes do maior para o menor é: {medias}\n')

classificacao = medias
contador = 1
for item in classificacao:
    print(f'posição {contador}: {item}')
    contador +=1
