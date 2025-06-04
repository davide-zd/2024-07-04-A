from database.DB_connect import DBConnect
from model.avvistamento import Avvistamento
from model.state import State
from model.sighting import Sighting


class DAO():
    def __init__(self):
        pass

    # metodo per prendere tutti gli anni dal database (serve per caricare il dropdown)
    @staticmethod
    def getAllYear():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct(year(s.`datetime`)) anno
                    from sighting s 
                    order by year(s.`datetime`) desc"""
        cursor.execute(query)

        for row in cursor:
            result.append(row["anno"])
        cursor.close()
        conn.close()
        return result

    # metodo per prendere le forme in base all'anno scelto
    @staticmethod
    def getShape(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct(s.shape) shape
                    from sighting s 
                    where year(s.`datetime`) = %s 
                        and s.shape != ""
                    order by s.shape"""
        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(row["shape"])
        cursor.close()
        conn.close()
        return result

    # metodo per prendere i nodi (avvistamenti)
    @staticmethod
    def getNodes(anno, shape):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select s.id id, s.`datetime` data, s.state stato, s.city citta
                    from sighting s 
                    where year(s.`datetime`) = %s
                        and s.shape = %s"""
        cursor.execute(query, (anno, shape))

        for row in cursor:
            result.append(Avvistamento(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdges(anno, shape):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)

        query = """select s1.id nodo1, s2.id nodo2, s1.`datetime` data1, s2.`datetime` data2
                    from sighting s1, sighting s2
                    where year(s1.`datetime`) = year(s2.`datetime`) 
                        and year(s1.`datetime`) = %s
                        and s1.`datetime` != s2.`datetime`
                        and s1.shape = s2.shape
                        and s1.shape = %s
                        and s1.state = s2.state
                        and s1.id > s2.id"""
        cursor.execute(query, (anno, shape))

        for row in cursor:
            result.append((row["nodo1"], row["nodo2"], row["data1"], row["data2"]))
        cursor.close()
        conn.close()
        return result