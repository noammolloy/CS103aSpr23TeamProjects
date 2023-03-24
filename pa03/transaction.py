'''imports SQL functions'''
import sqlite3

def to_dict(dict_t):
    ''' t is a dictionary of the transaction table'''
    transaction_dict = {'rowid':dict_t[0], 'item#':dict_t[1],
                   'amount':dict_t[2], 'category':dict_t[3],
                   'date':dict_t[4], 'description':dict_t[5]}
    return transaction_dict
class Transaction():
    '''list of SQL commands that the user can indirectly call'''
    # Noam
    def __init__(self, filename):
        self.filename = filename
        self.run_query('''CREATE TABLE IF NOT EXISTS transactions
        (item# int, amount int,
        category text, date text, description text)''',())
    def show_transactions(self):
        ''' show all of the transactions in the transaction table '''
        return self.run_query("SELECT * from transactions",())
    def add_transaction(self,item):
        ''' add a new transaction item to the transaction table '''
        return self.run_query("INSERT INTO transactions VALUES (?,?,?,?,?)",item)
    def delete_transaction(self,rowid):
        ''' delete a transaction item from the transaction table '''
        return self.run_query("DELETE FROM transactions WHERE rowid=?",(rowid,))
    # Sydney
    def summarize_transactions_by_date(self, date):
        ''' summarize transactions by date, using the date parameter passed in
         and returning a list of transactions that have that date. '''
        return self.run_query("SELECT * from transactions WHERE date=?",(date,))
    # Sydney
    def summarize_transactions_by_month(self, month):
        ''' summarize transactions by month, using the month parameter passed in
         and returning a list of transactions that have that month. '''
        return self.run_query("SELECT * from transactions WHERE month=?",(month,))
    # Sydney
    def summarize_transactions_by_year(self, year):
        ''' summarize transactions by year, using the year parameter passed in
         and returning a list of transactions that have that year.'''
        return self.run_query("SELECT * from transactions WHERE year=?",(year,))
    # Sydney
    def summarize_transactions_by_category(self, category):
        ''' summarize transactions by category, using the category parameter passed in
         and returning a list of transactions that have that category. '''
        return self.run_query("SELECT * from transactions WHERE category=?",(category,))
    def run_query(self,query,tuple_list):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con= sqlite3.connect(self.filename)
        cur = con.cursor()
        cur.execute(query,tuple_list)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [to_dict(dict_t) for dict_t in tuples]
    