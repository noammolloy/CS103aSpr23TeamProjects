''' tracker class'''
import sys
from transaction import Transaction

ts = Transaction('tracker.db')

#Jingyi
def print_usage():
    ''' print an explanation of how to use this command '''
    print('''usage:
            quit
            show_transactions
            add_transaction <amount> <category> <YYYY-MM-DD> <description> 
            delete_transaction <rowID>
            summarize_by_date <date>
            summarize_by_month <month>
            summarize_by_year <year>
            summarize_by_category <category>
            menu
            '''
            )
    #Noam
def print_transactions(_t_):
    ''' print the transaction items '''
    if len(_t_)==0:
        print('no tasks to print')
        return
    print('\n')
    print(f"{'item #':<10} {'amount':<10} {'category':<10} {'date':<15} {'description':<10}")
    print('-'*60)
    for item in _t_:
        values = tuple(item.values()) #(rowid,amount,category,date,desc)
        print(f"{values[0]:<10} {values[1]:<10} {values[2]:<10} {values[3]:<15} {values[4]:<10}")
    #Noam
def process_args(args):
    ''' process the command line arguments '''
    if args[0]=='quit':
        sys.exit()
    elif args[0]=='show_transactions':
        # show the transaction
        print_transactions(ts.show_transactions())
    elif args[0]=="add_transaction":
        # add a new transaction
        ts.add_transaction(args[1])
    elif args[0]=="delete_transaction":
        # delete a transaction
        ts.delete_transaction(args[1])
    elif args[0]=="summarize_by_date":
        # summarize transactions by date
        print_transactions(ts.summarize_transactions_by_date(args[1]))
    elif args[0]=="summarize_by_month":
        # summarize transactions by month
        print_transactions(ts.summarize_transactions_by_month(args[1]))
    elif args[0]=="summarize_by_year":
        # summarize transactions by year
        print_transactions(ts.summarize_transactions_by_year(args[1]))
    elif args[0]=="summarize_by_category":
        # summarize transactions by category
        print_transactions(ts.summarize_transactions_by_category(args[1]))
    elif args[0]=="menu":
        # show the menu
        print_usage()
#Jingyi
def toplevel():
    ''' read the command args and process them'''
    if len(sys.argv)==1:
        # they didn't pass any arguments,
        # so prompt for them in a loop
        print_usage()
        args = []
        while args!=['']:
            args = input("command> ").split(' ')
            if args[0]=='add_transaction':
                # join everything after the name as a string
                args = ['add_transaction', tuple(args[1:])]
            process_args(args)
            print('-'*60+'\n')
    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)
        print('-'*60+'\n')

toplevel()
