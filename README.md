# Dicionário pt-BR
### *Project in progress*

Brazilian portuguese dictionary project usind the xml database from [dicionário-aberto](https://dicionario-aberto.net/).
The code is supposed to first run in IDLE then in a GUI with tkinter.

Librarys:
```
import xml.etree.ElementTree as ET
import os
import glob
from unidecode import unidecode
from tkinter import *
``` 
- [x] Read all XML database files;
- [x] Recognize words with different typing (accents, lower/upper cases);
- [ ] Return all information (word, grammatical class, meaning) with legible formatting;
- [x] Create a GUI with tkinter
- [ ] Optimize tkinter GUI

*About the coder:
I'm a begginer in coding, python is my first language and this is my first project. So if you see something strange, just tell me, i'll be glad to take constructive critics.
email: ricardorkaito@gmail.com*
