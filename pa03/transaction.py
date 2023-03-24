# import sqlite3

# class Transaction:
#      def __init__(self, filename) -> None:
#          con= sqlite3.connect(filename)
#          cur = con.cursor()
#          cur.execute("CREATE TABLE IF NOT EXISTS transactions (id INTEGER PRIMARY KEY, item# int, amount int, category text, date text, description text)")
#          con.commit()
#          con.close()

import sqlite3
import os

class transaction():
    # Noam
    def __init__(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions 
        (id INTEGER PRIMARY KEY, item# int, amount int, category text, date text, description text)''',())
    
    def selectActive(self):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        return self.runQuery("SELECT rowid,* from todo where completed=0",())

    def selectAll(self):
        ''' return all of the tasks as a list of dicts.'''
        return self.runQuery("SELECT rowid,* from todo",())

    def selectCompleted(self):
        ''' return all of the completed tasks as a list of dicts.'''
        return self.runQuery("SELECT rowid,* from todo where completed=1",())

    def add_transaction(self,item):
        ''' create a transaction item and add it to the transaction table '''
        return self.runQuery("INSERT INTO todo (item) VALUES (?)",(item,))

    def delete_transaction(self,rowid):
        ''' delete a transaction item '''
        return self.runQuery("DELETE FROM todo WHERE rowid=(?)",(rowid,))

    def setComplete(self,rowid):
        ''' mark a todo item as completed '''
        return self.runQuery("UPDATE todo SET completed=1 WHERE rowid=(?)",(rowid,))

    def runQuery(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con= sqlite3.connect(os.getenv('HOME')+'/todo.db')
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()

    

        


