from database.DB_connect import DBConnect
from model.canzone import Canzone


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllGenres():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            select *
            from genre g 
                """
        cursor.execute(query, )
        result = []
        for row in cursor:
            result.append((row["GenreId"], row["Name"]))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodes(genere):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            select TrackId, Name, Bytes,  Milliseconds
            from track t
            where t.GenreId = %s
            order by Name
        """
        cursor.execute(query, (genere, ))
        result = []
        for row in cursor:
            result.append(Canzone(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges(genere, idMap):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            select t1.TrackId as t1, t2.TrackId as t2, abs(t2.Milliseconds - t1.Milliseconds) as durata
            from track t1, track t2
            where t1.TrackId < t2.TrackId and t1.MediaTypeId = t2.MediaTypeId
                and t1.GenreId = t2.GenreId and t2.GenreId = %s
                """
        cursor.execute(query, (genere, ))
        result = []
        for row in cursor:
            c1 = idMap[row["t1"]]
            c2 = idMap[row["t2"]]
            result.append((c1, c2, row["durata"]))
        cursor.close()
        conn.close()
        return result
