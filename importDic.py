import xml.etree.ElementTree as ET
import os, glob
from unidecode import unidecode

# Select the directory for the XML database
path = os.getcwd() + '/xmls'
allFiles = glob.glob(path+'/*.xml')
#

def word_comparator(): # Compare the received word from the input and the dictionary database
    no_accent_RecWord = unidecode(received_word).upper() # Clean input in unidecode
    noAccentDicWord = unidecode(dic_word).upper() # Clean database in unidecode
    if no_accent_RecWord == noAccentDicWord: 
        return print(dic_word, meaning) # Print the result (word and meaning) // * Grammatical class is missing

while True: # Loop search system
    received_word = str(input('Palavra: '))
    for fil in allFiles: # In allFiles
        root = ET.parse(fil).getroot() # Extracts root
        inside = root.findall('entry') # Search in <entry> tag in the xml file
        for c in inside:
            dic_word = c.find('form/orth').text # Get the word
            # grammar = c.find('sense/gramGrp') # Get the grammatical class // ** Missing code
            meaning = c.find('sense/def').text # Get the meaning from the dictionary
            word_comparator()
    if received_word == '0': # Input 0 to close the program
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


