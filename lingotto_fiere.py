from stand import Stand
from standPrese import StandPrese
from standPremium import StandPremium
from espositore import Espositore
from operator import attrgetter

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.__stand = []
        self.__espositori = []

    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):                                     #rende leggibile l'attributo nome
        return self.__nome

    @nome.setter
    def nome(self, nuovo_nome):                         #rende modificabile l'attributo nome
        self.__nome = nuovo_nome

    @property
    def stand(self):                                   #rende leggibile l'attributo stand
        return self.__stand

    @property
    def espositori(self):                              #rende leggibile l'attributo espositori
        return self.__espositori

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        self.__stand.clear()                            #elimina dalla lista gli elementi presenti
        self.__espositori.clear()

        try:
            file = open(file_path,"r")                  #apertura file
            for line in file:                           #lettura riga per riga del file
                line = line.strip()                     #ripulisce la riga dai caratteri in eccesso

                if line == "":                          #nel caso in cui una riga fosse vuota, passa avanti
                    continue

                dati = line.split(",")                  #trasforma ogni riga del file in una lista
                if dati[0][0] == "S":                   #controlla che il primo carattere del codice sia una S
                    if len(dati) == 4:                  #controlla se ogni stand ha 4 informazioni o meno
                        self.__stand.append(Stand(dati[0], dati[1], dati[2], dati[3]))
                    else:
                        if dati[4].isdigit():           #se lo stand non ha 4 informazioni, controlla se la quinta è un numero
                            self.__stand.append(StandPrese(dati[0], dati[1], dati[2], dati[3], dati[4]))
                        else:
                            self.__stand.append(StandPremium(dati[0], dati[1], dati[2], dati[3], dati[4]))

                else:                                   #se la prima lettera del codice non è la S si tratta di un espositore
                    self.__espositori.append(Espositore(dati[0], dati[1], dati[2]))

            file.close()                                #chiusura file

        except FileNotFoundError:                       #se il file non viene trovato viene scatenata l'eccezione
            raise FileNotFoundError("Il file CSV non è stato trovato.")

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        stand_interessato = None                        #lo stand che si vuole assegnare non è ancora stato trovato
        espositore_interessato = None                   #l'espositore che si vuole assegnare non è ancora stato trovato

        for s in self.__stand:
            if s.codice_univoco == codice_stand:        #viene cercato lo stand che si vuole assegnare
                stand_interessato = s
                if not stand_interessato.disponibile:   #se lo stand viene trovato si controlla che sia disponibile
                    raise Exception("Stand non disponibile")  #se non è disponibile viene scatenata un'eccezione

        if stand_interessato is None:                   #se lo stand non viene trovato viene scatenata un'eccezione
            raise Exception("Stand non trovato")

        for e in self.__espositori:
            if e.codice_univoco == codice_espositore:   #viene cercato l'espositore che si vuole assegnare
                espositore_interessato = e
                for s in self.__stand:
                    if s.espositore == espositore_interessato:   #se l'espositore viene trovato si controlla che non sia già assegnato
                        raise Exception("Espositore occupato")   #se è già assegnato a un altro stand viene scatenata un'eccezione

        if espositore_interessato is None:              #se l'espositore non viene trovato viene scatenata un'assegnazione
            raise Exception("Espositore non trovato")

        stand_interessato.assegnazione(espositore_interessato)   #se nessuna eccezione viene scatenata l'espositore viene assegnato allo stand

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        for e in self.__espositori:              #si controlla per ogni espositore se è assegnato a uno stand
            es = e
            for s in self.__stand:
                if e == s.espositore:
                    es = f"{e} - Assegnato allo stand {s.codice_univoco}"    #se assegnato viene stampato il codice dello stand a cui è assegnato
                    break
            print(es)         #se non è assegnato viene stampato solo l'espositore

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        return sorted(self.__stand, key=attrgetter('prezzo_base'))         #tutti gli stand vengono ordinati per prezzo
