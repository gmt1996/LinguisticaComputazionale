#programma2

import nltk
import sys
import codecs
from nltk.corpus import treebank
from nltk import FreqDist
from nltk import bigrams
from collections import Counter
from nltk import word_tokenize, pos_tag, ne_chunk
import re

def main(file):
    input = codecs.open(file, "r", "utf-8")
    raw = input.read()
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    frasi = tokenizer.tokenize(raw)
    listaPOS = []
    listaFrasiAnalizzare = []
    Person = []
    tokensTOT = []
    for i in frasi:
        tokens = nltk.word_tokenize(i)
        tokensTOT = tokensTOT + tokens
        a = pos_tag(tokens)#analizza i token e le assegna un Part of speech tag
        b = ne_chunk(a)#annota le Entità
        for nodo in b:
            NE = ''
            if hasattr(nodo,'label'):
                    for partNE in nodo.leaves():#nel caso l'entità fosse più di una parola la ricompongo con un for salvandola nella Stringa NE
                        NE = NE +' '+ partNE[0]
                    if(nodo.label() == 'PERSON'):#se l'etichetta del nodo è PERSON aggiungo alla Lista 'Person' La Stringa NE
                       Person.append(NE)
                       listaFrasiAnalizzare.append(i)#essendo quindi di interesse inserisco la frase nella Lista listaFrasiAnalizzare



    counta =  Counter(Person)#Conto le occorrenze in Person
    prima = counta.most_common(10)#estraggo da counta le dieci occorrenze più frequenti
    print('Dieci nomi di persona piu frequenti')
    for ii in prima:
        print('-', ii[0],': ',ii[1])
    for i in prima:#per ogni Nome presente in prima estraggo le informazioni richieste
        fraseLunga = 'v'
        fraseCorta = '''aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa


        aaaaaaaaaaaaaaaaaaaaaaaaaaaqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq'''
        mesi = []
        giorni = []
        date = []
        Luoghi = []
        Persone = []
        Sostantivi = []
        Verbi = []
        FraseProbAlta = 0
        listaFrasiPerNome = []
        fr = ''
        for j in listaFrasiAnalizzare:
            if(i[0] in j):
                listaFrasiPerNome.append(j)
                tokens = nltk.word_tokenize(j)
                if(len(j)>len(fraseLunga)):
                    fraseLunga = j
                if(len(j)<len(fraseCorta)):
                    fraseCorta = j
                #estraggo date mesi e giorni
                dat = re.findall(r'(:?\d*\d(st|nd|rd|th)\s(January|February|March|April|May|June|July|August|September|October|November|December)\s\d{2,4})', j)
                gio = re.findall(r'[Mm]onday|[Tt]uesday|[Ww]ednesday|[Tt]hursday|[Ff]riday|[Ss]aturday|[Ss]unday', j)
                lista = re.findall(r'[Jj]anuary|[Ff]ebruary|[Mm]arch|[Aa]pril|[Mm]ay|[Jj]une|[Jj]uly|[Aa]ugust|[Ss]eptember|[Oo]ctober|[Nn]ovenber|[Dd]ecember', j)
                if not(dat == []):
                    for ubb in dat:
                        date.append(ubb[0])
                if not(gio == []):
                    for u in gio:
                        giorni.append(u)
                if not(lista == []):
                    for ub in lista:
                        mesi.append(ub)
                #calcolo frase probabilità più alta con markov ordine 0
                if(len(tokens)>=8 and len(tokens)<=12):
                    probApp = 1
                    for tk in tokens:
                        probApp = probApp * (tokensTOT.count(tk)/len(tokensTOT))
                    if(probApp > FraseProbAlta) :#in caso positivo del condizionale assegno il valore aggiornato a FraseProbAlta e j 'la frase analizzata' alla stringa fr
                        FraseProbAlta = probApp
                        fr = j
                a = pos_tag(tokens)#analizza i token e le assegna un Part of speech tag
                b = ne_chunk(a)#annota le Entità
                for k in a:#ciclando nella lista contenente i token con il relativo Pos tag li divido in Sostantivi e Verbi
                    if(k[1]=='NNP' or k[1]=='NNPS'):
                        Sostantivi.append(k[0])
                    if(k[1]=='VBD' or k[1]=='VBG' or k[1]=='VBN' or k[1]=='VBP' or k[1]=='VBZ'):
                        Verbi.append(k[0])
                for nodo in b:#analizzo l'albero delle Entità e estraggo le Entità 'PERSON' e 'GPE'
                    NE = ''
                    if hasattr(nodo,'label'):
                            for partNE in nodo.leaves():#nel caso l'entità fosse più di una parola la ricompongo con un for salvandola nella Stringa NE
                                NE = NE +' '+ partNE[0]
                            if(nodo.label() == 'PERSON'):
                               Persone.append(NE)
                            if(nodo.label() == 'GPE'):
                               Luoghi.append(NE)

        print(Verbi)
        '''print('Lista frasi di' , i[0],' :')#per ogni Nome dei nomi più frequenti stampo tutte le frasi in cui esso compare
        for temp in listaFrasiPerNome:
            print('-', temp)
        Per = Counter(Persone)#Conto le occorrenze in Persone
        Luo = Counter(Luoghi)#Conto le occorrenze in Luoghi
        print('Persone piu frequenti di' , i[0],' :')
        for temp in Per.most_common(10):
            print('-', temp[0])
        print('Luoghi piu frequenti di' , i[0],' :')
        for temp in Luo.most_common(10):
            print('-', temp[0])
        tenSost = Counter(Sostantivi)#Conto le occorrenze in Sostantivi
        tenVer = Counter(Verbi)#Conto le occorrenze in verbi
        print('sostantivi piu frequenti di' , i[0],' :')
        for temp in tenSost.most_common(10):
            print('-', temp[0])
        print('Verbi piu frequenti di ' , i[0],' :', Verbi)
        for temp in tenVer.most_common(10):
            print('-', temp[0])
        print('Frase con probabilità piu alta di' , i[0],' :', fr)#fr la stringa che contiene la frase con probabilità più alta
        print('Date estratte per ' , i[0],' :')
        for temp in date:
            print('-', temp)
        print('Mesi estratti per' , i[0],' :')
        for temp in mesi:
            print('-', temp)
        print('Giorni estratti per' , i[0],' :')
        for temp in giorni:
            print('-', temp)
        print('Frase più lunga di ' , i[0],' :', fraseLunga)
        print('Frase più corta di' , i[0],' :', fraseCorta)
        print('\n\n')'''

print('\n\nTESTO1(Sherlock Holmes)\n\n')
main(sys.argv[1])
print('\n\nTESTO2(Dracula)\n\n')
main(sys.argv[2])
