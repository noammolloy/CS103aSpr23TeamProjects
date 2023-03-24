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
    def __init__(self, filename):
        self.filename = filename
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions 
        (id INTEGER PRIMARY KEY, item# int, amount int, category text, date text, description text)''',())

    def show_transactions(self):
        ''' show all of the transactions in the transaction table '''
        return self.runQuery("SELECT rowid,* from transactions",())

    def add_transaction(self,item):
        ''' add a new transaction item to the transaction table '''
        return self.runQuery("INSERT INTO transactions VALUES (?,?,?,?,?,?)",item)

    def delete_transaction(self,rowid):
        ''' delete a transaction item from the transaction table '''
        return self.runQuery("DELETE FROM transactions WHERE rowid=?",(rowid,))

    def summarize_transactions_by_date(self,rowid):
        ''' summarize transactions by date '''
        return self.runQuery("SELECT rowid,* from transactions",())
    
    def summarize_transactions_by_month(self,rowid):
        ''' summarize transactions by month '''
        return self.runQuery("SELECT rowid,* from transactions",())
    
    def summarize_transactions_by_year(self,rowid):
        ''' summarize transactions by year '''
        return self.runQuery("SELECT rowid,* from transactions",())
    
    def summarize_transactions_by_category(self,rowid):
        ''' summarize transactions by category '''
        return self.runQuery("SELECT rowid,* from transactions",())

    def runQuery(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con= sqlite3.connect(self.filename)
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()

    

        


