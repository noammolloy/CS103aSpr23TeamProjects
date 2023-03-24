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

def toDict(t):
        ''' t is a tuple (rowid,title, desc,completed)'''
        print('t='+str(t))
        todo = {'rowid':t[0], 'title':t[1], 'desc':t[2], 'completed':t[3]}
        return todo

class transaction():
    # Noam
    def __init__(self, filename):
        self.filename = filename
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions 
        (id INTEGER PRIMARY KEY, item# int, amount int, category text, date text, description text)''',())

    
    def show_transactions(self):
        ''' show all of the transactions in the transaction table '''
        return self.runQuery("SELECT * from transactions",())

    def add_transaction(self,item):
        ''' add a new transaction item to the transaction table '''
        return self.runQuery("INSERT INTO transactions VALUES (?,?,?,?,?,?)",item)

    def delete_transaction(self,rowid):
        ''' delete a transaction item from the transaction table '''
        return self.runQuery("DELETE FROM transactions WHERE rowid=?",(rowid,))

    # Sydney
    def summarize_transactions_by_date(self, date):
        ''' summarize transactions by date, using the date parameter passed in
         and returning a list of transactions that have that date. '''
        return self.runQuery("SELECT * from transactions WHERE date=?",(date,))
    
    # Sydney
    def summarize_transactions_by_month(self, month):
        ''' summarize transactions by month, using the month parameter passed in
         and returning a list of transactions that have that month. '''
        return self.runQuery("SELECT * from transactions WHERE month=?",(month,))
    
    # Sydney
    def summarize_transactions_by_year(self, year):
        ''' summarize transactions by year, using the year parameter passed in
         and returning a list of transactions that have that year.'''
        return self.runQuery("SELECT * from transactions WHERE year=?",(year,))
    
    # Sydney
    def summarize_transactions_by_category(self, category):
        ''' summarize transactions by category, using the category parameter passed in
         and returning a list of transactions that have that category. '''
        return self.runQuery("SELECT * from transactions WHERE category=?",(category,))

    def runQuery(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con= sqlite3.connect(self.filename)
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]

    

        


