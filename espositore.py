class Espositore:
    def __init__(self, codice_univoco, nome, cognome):
        # inizializzazione degli attributi della classe Espositore
        self.__codice_univoco = codice_univoco
        self.__nome = nome
        self.__cognome = cognome

    @property
    def codice_univoco(self):                         #rende visualizzabile l'attributo codice_univoco
        return self.__codice_univoco

    def __eq__(self, other:object):                  #metodo che permette di eguagliare due oggetti
        return isinstance(other, Espositore) and self.__codice_univoco == other.__codice_univoco

    # permette la stampa degli oggetti Espositore
    def __str__(self):
        return f"{self.__codice_univoco} : {self.__nome} {self.__cognome}"

    # permette la stampa degli oggetti anche quando sono contenuti in una lista e viene stampata quest'ultima
    def __repr__(self):
        return self.__str__()