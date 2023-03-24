class test_transaction:
    '''
test_transaction runs a few tests on the transaction methods.
'''
from transaction import transaction
import pytest

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

def test_with_data():
    ts = transaction('tracker.db')
    assert ts.add_transaction('item#', 'amount', 'category', 'date', 'description') == None
    assert ts.show_transactions() == None
    assert ts.delete_transaction('rowID') == None
    assert ts.summarize_transactions_by_date('date') == None
    assert ts.summarize_transactions_by_month('month') == None
    assert ts.summarize_transactions_by_year('year') == None
    assert ts.summarize_transactions_by_category('category') == None
    assert ts.menu() == None

# def test_quit():
#     with pytest.raises(SystemExit):
#         quit()

# def test_show_transaction():
#     ts = transaction('tracker.db')
#     assert ts.show_transactions() == None

# def test_add_transaction():
#     ts = transaction('tracker.db')
#     assert ts.add_transaction('item#', 'amount', 'category', 'date', 'description') == None

# def test_delete_transaction():
#     ts = transaction('tracker.db')
#     assert ts.delete_transaction('rowID') == None

# def test_summarize_transactions_by_date():
#     ts = transaction('tracker.db')
#     assert ts.summarize_transactions_by_date('date') == None

# def test_summarize_transactions_by_month():
#     ts = transaction('tracker.db')
#     assert ts.summarize_transactions_by_month('month') == None

# def test_summarize_transactions_by_year():
#     ts = transaction('tracker.db')
#     assert ts.summarize_transactions_by_year('year') == None

# def test_summarize_transactions_by_category():
#     ts = transaction('tracker.db')
#     assert ts.summarize_transactions_by_category('category') == None

# def test_menu():
#     ts = transaction('tracker.db')
#     assert ts.menu() == None

if __name__=='__main__':
    # test_quit()
    # test_show_transaction()
    # test_add_transaction()
    # test_delete_transaction()
    # test_summarize_transactions_by_date()
    # test_summarize_transactions_by_month()
    # test_summarize_transactions_by_year()
    # test_summarize_transactions_by_category()
    # test_menu()