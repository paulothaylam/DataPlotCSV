from csvChart import split_values, open_csv_file, get_file_names
import pytest

def test_split_data():
    t_data = {
        "fieldnames": ['pizza', 'orders'],
        "values": [
            {"pizza":'Pepperoni', "orders": '100'},
            {"pizza":'Broccoli', "orders":'30'}
        ]
    }

    assert split_values(t_data) == (['Pepperoni', 'Broccoli'], ['100', '30'])

    t_data["values"].pop()
    assert split_values(t_data) == (['Pepperoni'], ['100'])

    t_data['fieldnames'][1] = 'number'
    assert split_values(t_data) == (['Pepperoni'], [None])

def test_errors():
    with pytest.raises(FileNotFoundError):
        open_csv_file('-@$#') # Putting special characters in filename to invalid them

def test_getter_sys_argv():
    assert get_file_names([]) == [None, None]
    assert get_file_names(['archive']) == ['archive', None]
    assert get_file_names(['archive', 'orderList']) == ['archive', 'orderList']