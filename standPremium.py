from stand import Stand

class StandPremium (Stand):
    #inizializzazione degli attributi della classe figlia StandPremium
    def __init__(self, codice_univoco, superficie, numero_padiglione, prezzo_base, posizione):
        super().__init__(codice_univoco, superficie, numero_padiglione, prezzo_base)
        self.__posizione = posizione

    @property
    def prezzo_base(self):                            #modifica l'attributo prezzo_base della classe Stand
        return super().prezzo_base * 1.30

    @property
    def tipologia(self):                    #modifica la tipologia dello stand
        return "Premium"

    # metodo di stampa per la classe figlia
    def __str__(self):
        if self.disponibile:
            disponibilita = "Disponibile"
        else:
            disponibilita = f"Non disponibile, assegnato a {self.espositore}"
        return f"{super().info_comuni()} - Posizione: {self.__posizione} - {disponibilita}"

    # permette la stampa degli oggetti anche quando sono contenuti in una lista e viene stampata quest'ultima
    def __repr__(self):
        return f"{super().__repr__()} - Posizione: {self.__posizione}"