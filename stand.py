import espositore


class Stand:
    def __init__(self, codice_univoco, superficie, numero_padiglione, prezzo_base):
        #inizializzazione degli attributi della classe madre Stand
        self.__codice_univoco = codice_univoco
        self.__superficie = float(superficie)
        self.__numero_padiglione = int(numero_padiglione)
        self.__prezzo_base = float(prezzo_base)
        self.__disponibile = True
        self.__espositore = None

    @property
    def prezzo_base(self):                        #rende visualizzabile l'attributo prezzo_base
        return self.__prezzo_base

    @property
    def codice_univoco(self):                     #rende visualizzabile l'attributo codice_univoco
        return self.__codice_univoco

    @property
    def disponibile(self):                        #rende visualizzabile l'attributo disponibile
        return self.__disponibile

    @property
    def espositore(self):                         #rende visualizzabile l'attributo espositore
        return self.__espositore

    @property
    def tipologia(self):                          #permette di cambiare la tipologia dello stand
        return "Base"

    def assegnazione(self, espositore_interessato):
        self.__disponibile = False                          #lo stand non è più disponibile
        self.__espositore = espositore_interessato          #assegna un espositore allo stand

    #metodo per stampare informazioni comuni
    def info_comuni(self):
        return f"{self.__codice_univoco}: {self.tipologia} | {self.__superficie} mq - Padiglione {self.__numero_padiglione} - Prezzo {self.prezzo_base:.2f} euro"

    #metodo di stampa per stand base
    def __str__(self):
        if self.__disponibile:
            disponibilita = "Disponibile"
        else:
            disponibilita = f"Non disponibile, assegnato a {self.__espositore}"
        return f"{self.info_comuni()} - {disponibilita}"

    #permette la stampa degli oggetti anche quando sono contenuti in una lista e viene stampata quest'ultima
    def __repr__(self):
        return self.__str__()