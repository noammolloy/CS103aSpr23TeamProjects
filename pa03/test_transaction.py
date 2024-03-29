class test_transaction:
    '''
test_transaction runs a few tests on the transaction methods.
'''
from transaction import Transaction
import pytest

#Sydney
def test_empty():
    ts = Transaction('tracker.db')
    ts.reset()
    assert ts.show_transactions() == []
    assert ts.summarize_transactions_by_date('date') == []
    assert ts.summarize_transactions_by_month('month') == []
    assert ts.summarize_transactions_by_year('year') == []
    assert ts.summarize_transactions_by_category('category') == []

#Noam
def test_show_transaction():
    ts = Transaction('tracker.db')
    ts.reset()
    ts.add_transaction((100,'cat1','2022-01-14','deposit'))
    ts.add_transaction((200,'cat1','2022-05-28','withdraw'))
    ts.add_transaction((150,'cat2','2020-07-28','withdraw'))
    ts.add_transaction((1000,'cat2','2021-01-14','deposit'))
    ts.add_transaction((325,'cat2','2021-05-03','withdraw'))
    expected = [{'item #': 1, 'amount': 100, 'category': 'cat1', 'date': '2022-01-14', 'description': 'deposit'}, 
                {'item #': 2, 'amount': 200, 'category': 'cat1', 'date': '2022-05-28', 'description': 'withdraw'}, 
                {'item #': 3, 'amount': 150, 'category': 'cat2', 'date': '2020-07-28', 'description': 'withdraw'}, 
                {'item #': 4, 'amount': 1000, 'category': 'cat2', 'date': '2021-01-14', 'description': 'deposit'}, 
                {'item #': 5, 'amount': 325, 'category': 'cat2', 'date': '2021-05-03', 'description': 'withdraw'}]
    assert ts.show_transactions() == expected
    ts.reset()

#Noam
def test_add_transaction():
    ts = Transaction('tracker.db')
    ts.reset()
    ts.add_transaction((100,'cat1','2022-01-14','deposit'))
    ts.add_transaction((200,'cat1','2022-05-28','withdraw'))
    ts.add_transaction((150,'cat2','2020-07-28','withdraw'))
    ts.add_transaction((1000,'cat2','2021-01-14','deposit'))
    ts.add_transaction((325,'cat2','2021-05-03','withdraw'))
    # one row added
    expected = [{'item #': 1, 'amount': 100, 'category': 'cat1', 'date': '2022-01-14', 'description': 'deposit'}, 
                {'item #': 2, 'amount': 200, 'category': 'cat1', 'date': '2022-05-28', 'description': 'withdraw'}, 
                {'item #': 3, 'amount': 150, 'category': 'cat2', 'date': '2020-07-28', 'description': 'withdraw'}, 
                {'item #': 4, 'amount': 1000, 'category': 'cat2', 'date': '2021-01-14', 'description': 'deposit'}, 
                {'item #': 5, 'amount': 325, 'category': 'cat2', 'date': '2021-05-03', 'description': 'withdraw'},
                {'item #': 6, 'amount': 50, 'category': 'cat1', 'date': '2020-07-03', 'description': 'withdraw'}] # added row
    ts.add_transaction((50, 'cat1', '2020-07-03', 'withdraw'))
    assert ts.show_transactions() == expected
    ts.reset()

#Jingyi
def test_delete_transaction():
    ts = Transaction('tracker.db')
    ts.reset()
    ts.add_transaction((100,'cat1','2022-01-14','deposit'))
    ts.add_transaction((200,'cat1','2022-05-28','withdraw'))
    ts.add_transaction((150,'cat2','2020-07-28','withdraw'))
    ts.add_transaction((1000,'cat2','2021-01-14','deposit'))
    ts.add_transaction((325,'cat2','2021-05-03','withdraw'))
    # first row removed
    expected = [{'item #': 2, 'amount': 200, 'category': 'cat1', 'date': '2022-05-28', 'description': 'withdraw'}, 
                {'item #': 3, 'amount': 150, 'category': 'cat2', 'date': '2020-07-28', 'description': 'withdraw'}, 
                {'item #': 4, 'amount': 1000, 'category': 'cat2', 'date': '2021-01-14', 'description': 'deposit'}, 
                {'item #': 5, 'amount': 325, 'category': 'cat2', 'date': '2021-05-03', 'description': 'withdraw'}]
    ts.delete_transaction(1)
    assert ts.show_transactions() == expected
    ts.reset()

#Sydney
def test_summarize_transactions_by_date():
    ts = Transaction('tracker.db')
    ts.reset()
    ts.add_transaction((100,'cat1','2021-01-14','deposit'))
    ts.add_transaction((200,'cat1','2022-05-28','withdraw'))
    ts.add_transaction((150,'cat2','2020-07-28','withdraw'))
    ts.add_transaction((1000,'cat2','2021-01-14','deposit'))
    ts.add_transaction((325,'cat2','2021-05-03','withdraw'))
    expected = [{'item #': 1, 'amount': 100, 'category': 'cat1', 'date': '2021-01-14', 'description': 'deposit'}, 
                {'item #': 4, 'amount': 1000, 'category': 'cat2', 'date': '2021-01-14', 'description': 'deposit'}]
    assert ts.summarize_transactions_by_date('2021-01-14') == expected
    ts.reset()

#Sydney
def test_summarize_transactions_by_month():
    ts = Transaction('tracker.db')
    ts.reset()
    ts.add_transaction((100,'cat1','2022-01-14','deposit'))
    ts.add_transaction((200,'cat1','2022-05-28','withdraw'))
    ts.add_transaction((150,'cat2','2020-07-28','withdraw'))
    ts.add_transaction((1000,'cat2','2021-01-14','deposit'))
    ts.add_transaction((325,'cat2','2021-05-03','withdraw'))
    expected = [{'item #': 2, 'amount': 200, 'category': 'cat1', 'date': '2022-05-28', 'description': 'withdraw'}, 
                {'item #': 5, 'amount': 325, 'category': 'cat2', 'date': '2021-05-03', 'description': 'withdraw'}]
    assert ts.summarize_transactions_by_month('05') == expected
    ts.reset()

#Sydney
def test_summarize_transactions_by_year():
    ts = Transaction('tracker.db')
    ts.reset()
    ts.add_transaction((100,'cat1','2022-01-14','deposit'))
    ts.add_transaction((200,'cat1','2022-05-28','withdraw'))
    ts.add_transaction((150,'cat2','2020-07-28','withdraw'))
    ts.add_transaction((1000,'cat2','2021-01-14','deposit'))
    ts.add_transaction((325,'cat2','2021-05-03','withdraw'))
    expected = [{'item #': 1, 'amount': 100, 'category': 'cat1', 'date': '2022-01-14', 'description': 'deposit'}, 
                {'item #': 2, 'amount': 200, 'category': 'cat1', 'date': '2022-05-28', 'description': 'withdraw'}]
    assert ts.summarize_transactions_by_year('2022') == expected
    ts.reset()

#Jingyi
def test_summarize_transactions_by_category():
    ts = Transaction('tracker.db')
    ts.reset()
    ts.add_transaction((100,'cat1','2022-01-14','deposit'))
    ts.add_transaction((200,'cat1','2022-05-28','withdraw'))
    ts.add_transaction((150,'cat2','2020-07-28','withdraw'))
    ts.add_transaction((1000,'cat2','2021-01-14','deposit'))
    ts.add_transaction((325,'cat2','2021-05-03','withdraw'))
    expected = [{'item #': 1, 'amount': 100, 'category': 'cat1', 'date': '2022-01-14', 'description': 'deposit'}, 
                {'item #': 2, 'amount': 200, 'category': 'cat1', 'date': '2022-05-28', 'description': 'withdraw'}]
    assert ts.summarize_transactions_by_category('cat1') == expected
    ts.reset()

#Noam
if __name__=='__main__':
    test_show_transaction()
    test_add_transaction()
    test_delete_transaction()
    test_summarize_transactions_by_date()
    test_summarize_transactions_by_month()
    test_summarize_transactions_by_year()
    test_summarize_transactions_by_category()
