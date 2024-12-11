import os
import random
import re
from unidecode import unidecode

from cesar import *

MODE = '[AMIGO SECRETO]'

# PUT MESSAGES HERE, THE MORE THE BETTER
TEXTS = [
'Que o Natal encha seu coração de alegria e paz',
'Boas festas Muito amor e união para você e sua família.',
]

# PUT THE NAMES HERE
MAIRA = 'Maira'
DANIE = 'Daniel'
MAGAL = 'Magali'
ANAPA = 'Ana Paula'
SERGI = 'Sergio'

# THE SAME NAMES MUST BE IN THE ARRAY BELOW
names = [
    MAIRA,
    DANIE,
    MAGAL,
    ANAPA,
    SERGI,
]


# EXCLUDING LIST
names_dic = {}

for name in names:
    names_dic[name] = {}

    names_dic[name]['exc'] = []
    names_dic[name]['exc'].append(name)

names_dic[MAIRA]['exc'].append(SERGI)
names_dic[SERGI]['exc'].append(MAIRA)

names_dic[MAGAL]['exc'].append(ANAPA)

#SHUFLE
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

# CRIPTO AND SAVE IT
for target in sorteio:
    text = TEXTS[random.randint(0, len(TEXTS)-1)]
    text_len = len(text)

    name = names[sorteio.index(target)]
    rand_pos = random.randint(1, text_len-1)

    inserted = unidecode(text[0:rand_pos] + ' ' + target + ' ' + text[rand_pos:text_len])
    deslocamento = random.randint(2,5)

    cripto = cifra_cesar(inserted, -deslocamento).lower()
    cripto = re.sub(' +', ' ', cripto)

    out = MODE + '\n'
    out += 'Deslocamento: '
    out += str(deslocamento) + '\n'
    out += cripto
    # out += '\n'+inserted

    f = open(os.getcwd() + '/out/' + name + '.txt', "a")
    f.write(out)
    f.close()
