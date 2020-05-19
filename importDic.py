import xml.etree.ElementTree as ET
import os, glob

# Seleciona o caminho dos arquivos XML
path = os.getcwd() + '/xmls'
allFiles = glob.glob(path+'/*.xml')


while True: # Repete o sistema de busca.
    ppp = str(input('Palavra: '))
    for fil in allFiles: # Em allFiles
        root = ET.parse(fil).getroot() # Extrai root  
        inside = root.findall('entry') # Pesquisa a tag primária do arquivo
        for c in inside:
            palavra = c.find('form/orth').text # Retorna a Palavra
            # gramar = c.find('sense/gramGrp') # Retorna Classe Gramatical
            sig = c.find('sense/def').text # Retorna o significado da palavra
            if ppp == palavra:
                print(palavra, sig) # Printa a palavra com o(s) seu(s) significado(s).
    if ppp == '0': # Caso o usuário digita 0 o programa finaliza.
        print('Fim do programa.')
        break                




















    # for entry in root:
    #     gotWord = False
    #     gotGram = False
    #     for sub in entry:
    #         if sub.tag == 'form':
    #             try:
    #                 word = sub.find('orth').text
    #                 gotWord = True
    #             except AttributeError:
    #                 pass
    #         elif sub.tag == 'sense':
    #             try:
    #                 gram = sub.find('gramGrp').text
    #                 gotGram = True
    #             except AttributeError:
    #                 pass  
    #         if gotWord and gotGram:
    #             dic_pt_br[word.lower()] = gram.lower()
    #             break 


