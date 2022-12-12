import sqlite3
 

conn = sqlite3.connect("baza.sqlite3")
# TODO: Tukaj moramo ustvarit bazo, če je še ni.

class Model:
    def dobi_vse_uporabnike(self):
        
        pass