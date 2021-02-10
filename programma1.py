#programma 1
from __future__ import division
import sys
import codecs
import nltk
from nltk import FreqDist
from nltk import bigrams
from collections import Counter
import math
from nltk import text
import nltk, re, pprint
def main(file1,file2):#le variabili contrassegnate con '2' in posizione finale vengono utilizzate per l'analisi del secondo testo
    input = codecs.open(file1, "r", "utf-8")
    input2 = codecs.open(file2, "r", "utf-8")
    raw = input.read()
    raw2 = input2.read()
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    frasi = tokenizer.tokenize(raw)
    tokens = nltk.word_tokenize(raw)
    classiFreq = nltk.FreqDist(tokens)#estraggo le classi di frequenza per il testo 1
    frasi2 = tokenizer.tokenize(raw2)
    tokens2 = nltk.word_tokenize(raw2)
    classiFreq2 = nltk.FreqDist(tokens2)#estraggo le classi di frequenza per il testo 2
    pos = nltk.pos_tag(tokens)#analizza i token e le assegna un Part of speech tag
    pos2 = nltk.pos_tag(tokens2)
    tagFD = nltk.FreqDist(tag for (word, tag) in pos)#per ogni elemento in pos calcola le frequenze
    tagFD2 = nltk.FreqDist(tag for (word, tag) in pos2)#per ogni elemento in pos2 calcola le frequenze


    Verbi = 0
    Sostantivi = 0
    Verbi2 = 0
    Sostantivi2 = 0
    listaPOS = []
    listaPOS2 = []
    for j in pos:#ciclo sulla lista 'pos' per individuare i sostantivi  e i verbi
        listaPOS.append(j[1])
        if(j[1]=='NNP'):
            #print(j)
            Sostantivi = Sostantivi + 1
        elif(j[1]=='NN'):
            Sostantivi = Sostantivi + 1
        elif(j[1]=='NNPS'):
            Sostantivi = Sostantivi + 1
        elif(j[1]=='NNS'):
            Sostantivi = Sostantivi + 1
        elif(j[1]=='VBD'):
            Verbi = Verbi + 1
        elif(j[1]=='VBG'):
            Verbi = Verbi + 1
        elif(j[1]=='VBN'):
            Verbi = Verbi + 1
        elif(j[1]=='VBP'):
            Verbi = Verbi + 1
        elif(j[1]=='VBZ'):
            Verbi = Verbi + 1
    for j in pos2:#ciclo sulla lista 'pos2' per individuare i sostantivi  e i verbi
        listaPOS2.append(j[1])
        if(j[1]=='NNP'):
            #print(j)
            Sostantivi2 = Sostantivi2 + 1
        elif(j[1]=='NN'):
            Sostantivi2 = Sostantivi2 + 1
        elif(j[1]=='NNPS'):
            Sostantivi2 = Sostantivi2 + 1
        elif(j[1]=='NNS'):
            Sostantivi2 = Sostantivi2 + 1
        elif(j[1]=='VBD'):
            Verbi2 = Verbi2 + 1
        elif(j[1]=='VBG'):
            Verbi2 = Verbi2 + 1
        elif(j[1]=='VBN'):
            Verbi2 = Verbi2 + 1
        elif(j[1]=='VBP'):
            Verbi2 = Verbi2 + 1
        elif(j[1]=='VBZ'):
            Verbi2 = Verbi2 + 1
    h = 1000
    h2 = 1000
    while h <= len(tokens):#calcolo per porzioni incrementali di 1000 del testo: la distribuzione degli hapax e il vocabolario
        tk = tokens[:h]
        CF = FreqDist(tk)
        Voc = len(CF.keys())
        Hap = len(CF.hapaxes())
        DistHap = Hap/Voc
        print('Distribuzione hapax nel testo di token testo 1 per corpus lungo ', h)
        print(DistHap)
        print('Grandezza vocabolario testo 1 per corpus lungo ', h)
        print(Voc)
        h = h + 1000
    while h2 <= len(tokens2):
        tk2 = tokens2[:h]
        CF2 = FreqDist(tk2)
        Voc2 = len(CF2.keys())
        Hap2 = len(CF2.hapaxes())
        DistHap2 = Hap2/Voc2
        print('Distribuzione hapax nel testo di token testo 2 per corpus lungo', h2)
        print(DistHap2)
        print('Grandezza vocabolario testo 2 per corpus lungo', h)
        print(Voc2)
        h2 = h2 + 1000
    print('Numero totale di frasi testo 1\n', len(frasi),'\n')
    print('Numero totale di frasi testo 2\n', len(frasi2),'\n')
    if(len(frasi)>len(frasi2)):
        print('Il testo con il numero maggiore di frasi è il primo \n')
    else:
        print('Il testo con il numero maggiore di frasi è il secondo \n')
    print('Numero totale di token\n', len(tokens),'\n')
    print('Numero totale di token 2\n', len(tokens2),'\n')
    if(len(tokens)>len(tokens2)):
        print('Il testo con il numero maggiore di token è il primo \n')
    else:
        print('Il testo con il numero maggiore di token è il secondo \n')
    print('Lunghezza media delle frasi in termini di token testo 1\n', len(tokens)/len(frasi),'\n')
    print('Lunghezza media delle frasi in termini di token testo 2\n', len(tokens2)/len(frasi2),'\n')
    if(len(tokens)/len(frasi)>len(tokens2)/len(frasi2)):
        print('Il testo con la lunghezza media delle frasi è il primo\n')
    else:
        print('Il testo con la lunghezza media delle frasi è il secondo\n')
    print('Lunghezza media delle parole in termini di caratteri\n',len(raw)/len(tokens),'\n')
    print('Lunghezza media delle parole in termini di caratteri 2\n',len(raw2)/len(tokens2),'\n')
    if(len(raw)/len(tokens)>len(raw2)/len(tokens2)):
        print('Il testo con la lunghezza media delle parole è il primo\n')
    else:
        print('Il testo con la lunghezza media delle parole è il secondo\n')
    print('Grandezza vocabolario testo 1\n', len(classiFreq.keys()),'\n')
    print('Grandezza vocabolario testo 2\n', len(classiFreq2.keys()),'\n')
    if(len(classiFreq.keys())>len(classiFreq2.keys())):
        print('Il testo con il vocabolario più ampio è il primo\n')
    else:
        print('Il testo con il vocabolario più ampio è il secondo\n')
    if(len(classiFreq.hapaxes())>len(classiFreq2.hapaxes())):
        print('Il testo con hapax maggiori è il primo\n')
    else:
        print('Il testo con hapax maggiori è il secondo\n')
    print('10 PoS piu comuni testo 1')#10 pos piu comuni
    for elemn in tagFD.most_common(10):
        print('-',elemn[0],' : ',elemn[1])
    print('10 PoS piu comuni  testo 2')
    for elemn in tagFD2.most_common(10):
        print('-',elemn[0],' : ',elemn[1])
    print('Rapporto sostantivi e verbi testo 1\n',Sostantivi/Verbi,'\n')
    print('Rapporto sostantivi e verbi testo 2\n',Sostantivi2/Verbi2,'\n')



    big = list(bigrams(listaPOS))#estrae i bigrammi da listaPOS
    big2 = list(bigrams(listaPOS2))
    bigrUnici = Counter(big)#identifica i bigrammi senza ripetizioni
    bigrUnici2 = Counter(big2)
    bigrammiUnici = bigrUnici.keys()#estrae le chiavi bigrUnici
    bigrammiUnici2 = bigrUnici2.keys()
    ProbCond = {}
    ProbCond2 = {}
    dizProbCond = {}
    dizProbCond2 = {}
    dizForzAssoc = {}
    dizForzAssoc2 = {}
    for i in big:#ciclo sulla lista di bigrammi e identifico probabilità condizionata e LMI
        #prob condizionata
        fBig = big.count(i)#frequenza del bigramma
        fpos = listaPOS.count(i[0]) #frequenza della prima parola del bigramma
        vocabolario = len(classiFreq.keys())
        fposB = listaPOS.count(i[1])

        probabilitaCondizionata = fBig/fpos
        rapportoFposvoc = fpos/vocabolario
        probabilitaCongiunta = rapportoFposvoc*probabilitaCondizionata
        probB = fposB/vocabolario
        t = probabilitaCongiunta/(rapportoFposvoc*probB)
        LMI = fBig* math.log2(t)

        dizProbCond[i] = probabilitaCondizionata
        dizForzAssoc[i] = LMI

    for i in big2:
        #prob condizionata
        fBig = big2.count(i)#frequenza del bigramma
        fpos = listaPOS2.count(i[0]) #frequenza della prima parola del bigramma
        vocabolario = len(classiFreq2.keys())
        fposB = listaPOS2.count(i[1])

        probabilitaCondizionata = fBig/fpos
        rapportoFposvoc = fpos/vocabolario
        probabilitaCongiunta = rapportoFposvoc*probabilitaCondizionata
        probB = fposB/vocabolario
        t = probabilitaCongiunta/(rapportoFposvoc*probB)
        LMI = fBig* math.log2(t)

        dizProbCond2[i] = probabilitaCondizionata
        dizForzAssoc2[i] = LMI

    #prime dieci pos in ordine di probabilità condizionata
    sdo =  sorted(dizProbCond.items(), key=lambda x: x[1])#ordina in modo decrescente il dizionario in base al valore
    sdf = sdo[::-1]#inverte l'ordine di sdo
    print('10 Pos con probabilità condizionata massima\n\n')
    for ii in sdf[0:10]:
        print('-',ii[0],' : ',ii[1])
    sdo2 =  sorted(dizProbCond2.items(), key=lambda x: x[1])#ordina in modo decrescente il dizionario in base al valore
    sdf2 = sdo2[::-1]
    print('10 Pos con probabilità condizionata massima testo 2\n\n')
    for ii in sdf2[0:10]:
        print('-',ii[0],' : ',ii[1],'\n')
    #prime dieci pos in ordine di Local Mutual Information
    sdm =  sorted(dizForzAssoc.items(), key=lambda x: x[1])#ordina in modo decrescente il dizionario in base al valore
    sdn = sdm[::-1]
    print('10 PoS con forza associativa massima in termini di LMI\n\n')
    for ii in sdn[0:10]:
        print('-',ii[0],' : ',ii[1],'\n')
    sdm2 =  sorted(dizForzAssoc2.items(), key=lambda x: x[1])#ordina in modo decrescente il dizionario in base al valore
    sdn2 = sdm2[::-1]
    print('10 PoS con forza associativa massima in termini di LMI testo 2\n\n')
    for ii in sdn2[0:10]:
        print('-',ii[0],' : ',ii[1],'\n')


main(sys.argv[1], sys.argv[2])
