from database.DB_connect import DBConnect
from model.country import Country


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getNodes(anno):
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT co.StateAbb, co.CCode, co.StateNme 
                from contiguity c, country co
                where c.`year` <= %s
                and c.state1no = co.CCode 
                group by c.state1no ORDER BY StateAbb"""
            cursor.execute(query,(anno,))
            for row in cursor:
                res.append((Country(**row)))

            cursor.close()
            cnx.close()
        return res

    @staticmethod
    def getEdges(anno,idMap):
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select state1no as id1, state2no as id2
                    from contiguity 
                    where contiguity.conttype=1 
                    and contiguity.year <= %s"""
            cursor.execute(query,(anno,))
            for row in cursor:
                res.append((idMap[row["id1"]],idMap[row["id2"]]))

            cursor.close()
            cnx.close()
        return res
