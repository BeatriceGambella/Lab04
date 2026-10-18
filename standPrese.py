from stand import Stand

class StandPrese (Stand):
    #inizializzazione degli attributi della classe figlia StandPrese
    def __init__(self, codice_univoco, superficie, numero_padiglione, prezzo_base, prese):
        super().__init__(codice_univoco, superficie, numero_padiglione, prezzo_base)
        self.__prese = int(prese)

    @property
    def prezzo_base(self):                                      #modifica l'attributo prezzo_base della classe Stand
        return super().prezzo_base * (1 + 0.07 * self.__prese)

    @property
    def tipologia(self):               #modifica la tipologia dello Stand
        return "Prese Extra"

    #metodo di stampa per la classe figlia
    def __str__(self):
        if self.disponibile:
            disponibilita = "Disponibile"
        else:
            disponibilita = f"Non disponibile, assegnato a {self.espositore}"
        return f"{super().info_comuni()} - Prese aggiuntive: {self.__prese} - {disponibilita}"

    # permette la stampa degli oggetti anche quando sono contenuti in una lista e viene stampata quest'ultima
    def __repr__(self):
        return f"{super().__repr__()} - Prese aggiuntive: {self.__prese}"