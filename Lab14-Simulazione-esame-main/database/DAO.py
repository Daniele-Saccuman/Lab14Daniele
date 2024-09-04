from database.DB_connect import DBConnect
from model.Gene import Gene


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllGenes():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select * from genes"""

        cursor.execute(query)

        for row in cursor:
            result.append(Gene(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllChromosomes():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct Chromosome 
                        from genes g 
                        where g.Chromosome > 0 """
        cursor.execute(query)

        for row in cursor:
            result.append(row["Chromosome"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnectedGenes():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select g1.Chromosome as cr1, g2.Chromosome as cr2, g1.GeneID as g1, g2.GeneID as g2, i.Expression_Corr as corr
                    from interactions i, genes g1, genes g2
                    where i.GeneID1 <> i.GeneID2 
                    and i.GeneID1 = g1.GeneID
                    and i.GeneID2 = g2.GeneID
                    and g2.Chromosome <> g1.Chromosome
                    and g2.Chromosome > 0
                    and g1.Chromosome > 0
                    group by g1.GeneID, g2.GeneID"""

        cursor.execute(query)

        for row in cursor:
            result.append((row['cr1'], row['cr2'], row['g1'], row['g2'], row['corr']))

        cursor.close()
        conn.close()
        return result