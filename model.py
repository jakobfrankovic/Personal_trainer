import sqlite3
import baza
#V modelu bo delal vse kar bo povezano z bazo.
conn = sqlite3.connect("baza.sqlite3") #connecti se na projekt
# TODO: Tukaj moramo ustvarit bazo, če je še ni.
baza.pripravi_vse(conn)

class Model:
    def dobi_vse_uporabnike(self):
        with conn:
            cur = conn.execute(""" 
            SELECT * FROM uporabnisko_ime
            """)
            return cur.fetchall()