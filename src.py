import os
import random
from unidecode import unidecode

from cesar import *

TEXTS = [
'Que o Natal encha seu coração de alegria e paz',
'Boas festas Muito amor e união para você e sua família.',
'Feliz Natal Que a magia renove sua esperança.',
'Paz amor e luz Que seu Natal seja especial.',
'Um Natal cheio de sorrisos e sonhos realizados',
'Que o espírito natalino esteja presente no seu lar.',
'Feliz Natal Que sua vida brilhe como as estrelas.',
'Amor e gratidão o verdadeiro espírito do Natal',
'Que este Natal traga saúde amor e felicidade',
'Um Natal abençoado com momentos inesquecíveis',
]

MAIRA = 'Maira'
DANIE = 'Daniel'
GABRI = 'Gabriel'
FEDIA = 'Felipe Dias'
FELEM = 'Felipe Leme'
MAGAL = 'Magali'
ANAPA = 'Ana Paula'
SERGI = 'Sergio'
GIOVA = 'Giovana'
LETIC = 'Leticia'
RAISS = 'Raissa'

names = [
    MAIRA,
    DANIE,
    GABRI,
    FEDIA,
    FELEM,
    MAGAL,
    ANAPA,
    SERGI,
    GIOVA,
    LETIC,
    RAISS
]

names_dic = {}

for name in names:
    names_dic[name] = {}

    names_dic[name]['exc'] = []
    names_dic[name]['exc'].append(name)

'''
Lista exclusão
'''

names_dic[MAIRA]['exc'].append(SERGI)
names_dic[SERGI]['exc'].append(MAIRA)

names_dic[MAGAL]['exc'].append(ANAPA)

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

    out = 'Deslocamento: '
    out += str(deslocamento) + '\n'
    out += cripto

    f = open(os.getcwd() + '/out/' + name + '.txt', "a")
    f.write(out)
    f.close()
    # print(cripto)
