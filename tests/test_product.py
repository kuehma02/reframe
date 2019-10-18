import pandas as pd
import pytest
from reframe import Relation

def test_product_1():
    data_expected = {'animal_x': ['zebra','zebra','x-ray fish', 'x-ray fish'],
                'name': ['adam','adam','dina','dina'],
                'color': ['red','red','purple', 'purple'],
                'animal_y': ['zebra','x-ray fish', 'zebra','x-ray fish'],
                'age': [7, 678, 7, 678]}
    
    df_expected = pd.DataFrame(data=data_expected)
    r_expected = Relation(df_expected) 

    data_real_table1 = {'animal': ['zebra', 'x-ray fish'],
                'name': ['adam', 'dina'],
                'color': ['red', 'purple']}
    df_table1 = pd.DataFrame(data=data_real_table1)
    r_table1 = Relation(df_table1)
    
    data_real_table2 = {'animal': ['zebra', 'x-ray fish'],
                'age': [7, 678]}
    df_table2 = pd.DataFrame(data=data_real_table2)
    r_table2 = Relation(df_table2)
    
    r = r_table1.cartesian_product(r_table2)
    assert r.equals(r_expected)

def test_groupby_2():
    data_expected = {'student': ['amanda', 'sam', 'tony'],
                'classes': ['science', 'chinese', 'math'],
                'grade': ['A', 'A', 'A']}

    
    df_expected = pd.DataFrame(data=data_expected)
    r_expected = Relation(df_expected) 
    print(r_expected)


    data_real_table1 = {'student': ['amanda', 'sam', 'tony'],
                'classes': ['science', 'chinese', 'math']}
    df_table1 = pd.DataFrame(data=data_real_table1)
    r_table1 = Relation(df_table1)
    
    data_real_table2 = {'grade': ['A']}
    df_table2 = pd.DataFrame(data=data_real_table2)
    r_table2 = Relation(df_table2)
    
    r = r_table1.cartesian_product(r_table2)
    print(r)
    assert r.equals(r_expected)