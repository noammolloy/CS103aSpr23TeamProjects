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
            add_transaction <item#> <amount> <category> <date> <description> 
            delete_transaction <rowID>
            summarize_by_date <date>
            summarize_by_month <month>
            summarize_by_year <year>
            summarize_by_category <category>
            menu
            '''
            )
def process_args(args):
    ''' process the command line arguments '''
    if args[0]=='quit':
        sys.exit()
    elif args[0]=='show_transaction':
        # show the transaction
        Transaction.show_transactions()
    elif args[0]=="add_transaction":
        # add a new transaction
        Transaction.add_transaction(args[1])
    elif args[0]=="delete_transaction":
        # delete a transaction
        Transaction.delete_transaction(args[1])
    elif args[0]=="summarize_by_date":
        # summarize transactions by date
        Transaction.summarize_transactions_by_date(args[1])
    elif args[0]=="summarize_by_month":
        # summarize transactions by month
        Transaction.summarize_transactions_by_month(args[1])
    elif args[0]=="summarize_by_year":
        # summarize transactions by year
        Transaction.summarize_transactions_by_year(args[1])
    elif args[0]=="summarize_by_category":
        # summarize transactions by category
        Transaction.summarize_transactions_by_category(args[1])
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
            print('-'*40+'\n'*3)
    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)
        print('-'*40+'\n'*3)
