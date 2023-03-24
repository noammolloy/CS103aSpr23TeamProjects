import sqlite3
import sys
from transaction import Transaction

ts = Transaction('tracker.db')

def print_usage():
    ''' print an explanation of how to use this command '''
    print('''usage:
            show transactions
            add transaction
            delete transaction
            summarize transactions by date
            summarize transactions by month
            summarize transactions by year
            summarize transactions by category
            print this menu
            '''
            )
    
def process_args(args):
    ''' process the command line arguments '''
    if args[0]=='add':
        # add a new todo item
        print("this is just here so no bug")

def toplevel():
    ''' read the command args and process them'''
    if len(sys.argv)==1:
        # they didn't pass any arguments, 
        # so prompt for them in a loop
        print_usage()
        args = []
        while args!=['']:
            args = input("command> ").split(' ')
            if args[0]=='add':
                # join everyting after the name as a string
                args = ['add',args[1]," ".join(args[2:])]
            process_args(args)
            print('-'*40+'\n'*3)
    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)
        print('-'*40+'\n'*3)