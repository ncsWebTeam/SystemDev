import mysql.connector

class MySQL:
    def __init__(self, **dns):
        self.dns = dns
        self.dbh = None

    def _open(self):
        self.dbh = mysql.connector.MySQLConnection(**self.dns)

    def _close(self):
        self.dbh.close()

    def query(self, sql, args=None):
        self._open()
        if args != None:
            cursor = self.dbh.cursor()
            cursor.execute(sql, args)
        else:
            cursor = self.dbh.cursor()
            cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        self._close()
        return data
    
    def upQuery(self, sql, args):
        self._open()
        try:
            cursor = self.dbh.cursor()
            data = cursor.execute(sql, args)
            self.dbh.commit()
        except:
            data = None
            self.dbh.rollback()
        cursor.close()
        self._close()
        return data
