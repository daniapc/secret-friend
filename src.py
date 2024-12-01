import os
import random
from unidecode import unidecode

from cesar import *

MODE = '[INIMIGO SECRETO]'

TEXTS = [
'O Natal chegou e com ele as brigas familiares.',
'Mais um Natal mais dívidas no cartão Feliz?',
'Clima natalino paz na ceia guerra nos grupos.',
'É Natal Hora de ouvir as mesmas piadas ruins.',
'Natal falsos abraços e promessas que não duram.',
'Presentes caros afetos baratos Feliz Natal!',
'Ceia farta mas o coração segue vazio.',
'Natal luzes brilhantes contas ainda mais altas.',
'Alegria de Natal Só até abrir a fatura.',
'Família reunida Que comece o show de indiretas!',
]

MAIRA = 'Maira'
DANIE = 'Daniel'
FELEM = 'Felipe Leme'
ANAPA = 'Ana Paula'
LETIC = 'Leticia'
RAISS = 'Raissa'
SAMUE = 'Samuel'

names = [
    MAIRA,
    DANIE,
    FELEM,
    ANAPA,
    LETIC,
    RAISS,
    SAMUE
]

names_dic = {}

for name in names:
    names_dic[name] = {}

    names_dic[name]['exc'] = []
    names_dic[name]['exc'].append(name)

'''
Embaralha
'''
success = False
sorteio = []

while not(success):

    success = True

    sorteio = names.copy()
    random.shuffle(sorteio)

    for target in sorteio:
        name = names[sorteio.index(target)]

        if (target in names_dic[name]['exc']):
            success = False
            break

for target in sorteio:
    text = TEXTS[random.randint(0, len(TEXTS)-1)]
    text_len = len(text)

    name = names[sorteio.index(target)]
    rand_pos = random.randint(1, text_len-1)

    inserted = unidecode(text[0:rand_pos] + target + text[rand_pos:text_len])
    deslocamento = random.randint(2,5)

    cripto = cifra_cesar(inserted, -deslocamento).lower()

    out = MODE + '\n'
    out += 'Deslocamento: '
    out += str(deslocamento) + '\n'
    out += cripto

    f = open(os.getcwd() + '/out/' + name + '.txt', "a")
    f.write(out)
    f.close()
    # print(cripto)
