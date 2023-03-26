class test_transaction:
    '''
test_transaction runs a few tests on the transaction methods.
'''
from transaction import Transaction
import pytest

ts = Transaction('tracker.db')
ts.add_transaction((100,'cat1','2022-1-14','deposit'))
ts.add_transaction((200,'cat1','2022-5-28','withdraw'))
ts.add_transaction((150,'cat2','2020-7-28','withdraw'))
ts.add_transaction((1000,'cat2','2021-1-14','deposit'))
ts.add_transaction((325,'cat2','2021-5-3','withdraw'))

def test_empty():
    ts = Transaction('tracker.db')
    assert ts.show_transactions() == None
    assert ts.add_transaction('item#', 'amount', 'category', 'date', 'description') == None
    assert ts.delete_transaction('rowID') == None
    assert ts.summarize_transactions_by_date('date') == None
    assert ts.summarize_transactions_by_month('month') == None
    assert ts.summarize_transactions_by_year('year') == None
    assert ts.summarize_transactions_by_category('category') == None
    assert ts.menu() == None


def my_testing():
    print(ts.show_transactions())

def test_show_transaction():
    assert ts.show_transactions() == None

def test_add_transaction():
    assert ts.add_transaction('item#', 'amount', 'category', 'date', 'description') == None

def test_delete_transaction():
    assert ts.delete_transaction('rowid') == None

def test_summarize_transactions_by_date():
    assert ts.summarize_transactions_by_date('date') == None

def test_summarize_transactions_by_month():
    assert ts.summarize_transactions_by_month('month') == None

def test_summarize_transactions_by_year():
    assert ts.summarize_transactions_by_year('year') == None

def test_summarize_transactions_by_category():
    assert ts.summarize_transactions_by_category('category') == None


if __name__=='__main__':
    my_testing()
    ts.reset()
    # test_show_transaction()
    # test_add_transaction()
    # test_delete_transaction()
    # test_summarize_transactions_by_date()
    # test_summarize_transactions_by_month()
    # test_summarize_transactions_by_year()
    # test_summarize_transactions_by_category()
