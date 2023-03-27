Our app uses SQL to store and keep track of transactions with the following categories:
* item #: the row ID
* amount: amount of money 
* category: type of transaction
* date: date of transaction
* description: a description of the transaction

pylint transcript:
_______
transaction.py:

(base) Sydney@MacBook-Air-2 pa03 % pylint transaction.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)


_______
tracker.py:

(base) Sydney@MacBook-Air-2 pa03 % pylint tracker.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

____

pytest transcript:


(base) Sydney@MacBook-Air-2 pa03 % pytest -v
====================================================================== test session starts =======================================================================
platform darwin -- Python 3.9.13, pytest-7.1.2, pluggy-1.0.0 -- /Users/Sydney/opt/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/Sydney/Desktop/Brandeis Spring 2023/COSI 103A/CS103aSpr23TeamProjects/pa03
plugins: anyio-3.5.0
collected 8 items                                                                                                                                                

test_transaction.py::test_empty PASSED                                                                                                                     [ 12%]
test_transaction.py::test_show_transaction PASSED                                                                                                          [ 25%]
test_transaction.py::test_add_transaction PASSED                                                                                                           [ 37%]
test_transaction.py::test_delete_transaction PASSED                                                                                                        [ 50%]
test_transaction.py::test_summarize_transactions_by_date PASSED                                                                                            [ 62%]
test_transaction.py::test_summarize_transactions_by_month PASSED                                                                                           [ 75%]
test_transaction.py::test_summarize_transactions_by_year PASSED                                                                                            [ 87%]
test_transaction.py::test_summarize_transactions_by_category PASSED                                                                                        [100%]

======================================================================= 8 passed in 0.10s ========================================================================

PS C:\Users\noamm\OneDrive\Documents\Brandeis\Sophmore - spring\SWE\CS103aSpr23TeamProjects\pa03> python .\tracker.py
usage:
            quit
            show_transactions
            add_transaction <amount> <category> <YYYY-MM-DD> <description>
            delete_transaction <rowID>
            summarize_by_date <date>
            summarize_by_month <month>
            summarize_by_year <year>
            summarize_by_category <category>
            menu

command> add_transactions 100 cat1 2022-01-14 deposit
------------------------------------------------------------

command> add_transactions 200 cat1 2022-05-28 withdraw 
------------------------------------------------------------

command> add_transactions 150 cat2 2020-07-28 withdraw 
------------------------------------------------------------

command> add_transactions 1000 cat2 2021-01-14 deposit 
------------------------------------------------------------

------------------------------------------------------------

command> show_transactions
no tasks to print
------------------------------------------------------------

command> show_transactions
no tasks to print
------------------------------------------------------------

command> quit
PS C:\Users\noamm\OneDrive\Documents\Brandeis\Sophmore - spring\SWE\CS103aSpr23TeamProjects\pa03> python .\tracker.py
usage:
            quit
            show_transactions
            add_transaction <amount> <category> <YYYY-MM-DD> <description>
            delete_transaction <rowID>
            summarize_by_date <date>
            summarize_by_month <month>
            summarize_by_year <year>
            summarize_by_category <category>
            menu

command> add_transaction 100 cat1 2022-01-14 deposit  
------------------------------------------------------------

command> add_transaction 200 cat1 2022-05-28 withdraw  
------------------------------------------------------------

command> add_transaction 150 cat2 2020-07-28 withdraw  
------------------------------------------------------------

command> add_transaction 1000 cat2 2021-01-14 deposit  
------------------------------------------------------------

command> add_transaction 325 cat2 2021-05-03 withdraw  
------------------------------------------------------------

command> show_transactions


item #     amount     category   date            description
------------------------------------------------------------
1          100        cat1       2022-01-14      deposit
2          200        cat1       2022-05-28      withdraw
3          150        cat2       2020-07-28      withdraw
4          1000       cat2       2021-01-14      deposit
5          325        cat2       2021-05-03      withdraw
------------------------------------------------------------

command> delete_transaction 3
------------------------------------------------------------

command> show_transactions    


item #     amount     category   date            description
------------------------------------------------------------
1          100        cat1       2022-01-14      deposit
2          200        cat1       2022-05-28      withdraw
4          1000       cat2       2021-01-14      deposit
5          325        cat2       2021-05-03      withdraw
------------------------------------------------------------

command> summarize_by_date 2022-01-14


item #     amount     category   date            description
------------------------------------------------------------
1          100        cat1       2022-01-14      deposit
------------------------------------------------------------

command> summarize_by_month 05       


item #     amount     category   date            description
------------------------------------------------------------
2          200        cat1       2022-05-28      withdraw
5          325        cat2       2021-05-03      withdraw
------------------------------------------------------------

command> summarize_by_year 2022


item #     amount     category   date            description
------------------------------------------------------------
1          100        cat1       2022-01-14      deposit
2          200        cat1       2022-05-28      withdraw
------------------------------------------------------------

command> summarize_by_category cat2


item #     amount     category   date            description
------------------------------------------------------------
4          1000       cat2       2021-01-14      deposit
5          325        cat2       2021-05-03      withdraw
------------------------------------------------------------

command> menu
usage:
            quit
            show_transactions
            add_transaction <amount> <category> <YYYY-MM-DD> <description>
            delete_transaction <rowID>
            summarize_by_date <date>
            summarize_by_month <month>
            summarize_by_year <year>
            summarize_by_category <category>
            menu

------------------------------------------------------------

command> quit
PS C:\Users\noamm\OneDrive\Documents\Brandeis\Sophmore - spring\SWE\CS103aSpr23TeamProjects\pa03> 