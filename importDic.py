import xml.etree.ElementTree as ET
import os, glob
from unidecode import unidecode
from tkinter import *


def back_end():  # Search word in database when click in "Pesquisar"

    def word_comparator():  # Compare the received word from the input and the dictionary database
        no_accent_rec_word = unidecode(received_word).upper()  # Clean input in unicode
        no_accent_dic_word = unidecode(dic_word).upper()  # Clean database in unicode
        if no_accent_rec_word == no_accent_dic_word:
            return dic_word, meaning  # Print the result (word and meaning) // * Grammatical class is missing

    # Select the directory for the XML database
    path = os.getcwd() + '/xmls'
    all_files = glob.glob(path + '/*.xml')
    received_word = word_entry.get()

    for fil in all_files:  # In allFiles
        root = ET.parse(fil).getroot()  # Extracts root
        inside = root.findall('entry')  # Search in <entry> tag in the xml file
        for c in inside:
            dic_word = c.find('form/orth').text  # Get the word
            # grammar = c.find('sense/gramGrp') # Get the grammatical class // ** Missing code
            meaning = c.find('sense/def').text  # Get the meaning from the dictionary
            if word_comparator():
                result_label['text'] = dic_word, meaning


#
rootwind = Tk()
rootwind.title('Dicionário Open Source')
#
word_entry = Entry(rootwind)
search_button = Button(rootwind, text='Pesquisar', command=back_end)
quit_button = Button(rootwind, text='Fechar', command=rootwind.destroy)
result_label = Label(rootwind, text='Nada')
#
rootwind.grid_rowconfigure(0, weight=1)
rootwind.grid_rowconfigure(3, weight=1)
rootwind.grid_columnconfigure(0, weight=1)
rootwind.grid_columnconfigure(3, weight=1)
#
word_entry.grid(row=1, column=1, columnspan=2)
search_button.grid(row=2, column=1)
quit_button.grid(row=2, column=2)
result_label.grid(row=3, column=1, columnspan=2)
#
rootwind.geometry('300x300+200+200')
rootwind.mainloop()






               




















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


