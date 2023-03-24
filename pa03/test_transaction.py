class test_transaction:
    '''
test_transaction runs a few tests on the transaction methods.
'''
from transaction import transaction
import pytest

ts = transaction('tracker.db')
ts.add_transaction((1,100,'cat1','1-14-2022','deposit'))
ts.add_transaction((2,200,'cat1','5-28-2022','withdraw'))
ts.add_transaction((3,150,'cat2','7-28-2020','withdraw'))
ts.add_transaction((4,1000,'cat2','1-14-2021','deposit'))
ts.add_transaction((5,325,'cat2','5-3-2021','withdraw'))

def test_empty():
    ts = transaction('tracker.db')
    assert ts.show_transactions() == None
    assert ts.add_transaction('item#', 'amount', 'category', 'date', 'description') == None
    assert ts.delete_transaction('rowID') == None
    assert ts.summarize_transactions_by_date('date') == None
    assert ts.summarize_transactions_by_month('month') == None
    assert ts.summarize_transactions_by_year('year') == None
    assert ts.summarize_transactions_by_category('category') == None
    assert ts.menu() == None



def test_quit():
    with pytest.raises(SystemExit):
        quit()

def test_show_transaction():
    assert ts.show_transactions() == None

def test_add_transaction():
    assert ts.add_transaction('item#', 'amount', 'category', 'date', 'description') == None

def test_delete_transaction():
    assert ts.delete_transaction('rowID') == None

def test_summarize_transactions_by_date():
    assert ts.summarize_transactions_by_date('date') == None

def test_summarize_transactions_by_month():
    assert ts.summarize_transactions_by_month('month') == None

def test_summarize_transactions_by_year():
    assert ts.summarize_transactions_by_year('year') == None

def test_summarize_transactions_by_category():
    assert ts.summarize_transactions_by_category('category') == None

def test_menu():
    assert ts.menu() == None

if __name__=='__main__':
    test_quit()
    test_show_transaction()
    test_add_transaction()
    test_delete_transaction()
    test_summarize_transactions_by_date()
    test_summarize_transactions_by_month()
    test_summarize_transactions_by_year()
    test_summarize_transactions_by_category()
    test_menu()