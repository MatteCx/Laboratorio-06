from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        lista_strumento = []
        cnx = get_connection()
        cursore = cnx.cursor()
        query = ("SELECT * "
                 "FROM strumento")
        cursore.execute(query)
        for el in cursore:
            disp = True if el[-1] == 1 else False
            lista_strumento.append(Strumento(codice = el[0], tipo = el[1], marca = el[2], anno_acquisto = int(el[3]), valore = float(el[4]), disponibile = disp))
        return lista_strumento

    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        lista_strumento_filtrata = []
        cnx = get_connection()
        cursore = cnx.cursor()
        query = (f"""select *
                 from strumento s 
                 where s.tipo like '{tipo}'""")
        cursore.execute(query)
        for el in cursore:
            disp = True if el[-1] == 1 else False
            lista_strumento_filtrata.append(Strumento(codice = el[0], tipo = el[1], marca = el[2], anno_acquisto = int(el[3]), valore = float(el[4]), disponibile = disp))
        return lista_strumento_filtrata
