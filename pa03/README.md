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