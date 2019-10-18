import pandas as pd
import pytest
from reframe import Relation

def test_groupby_1():
    data_expected = {'animal': ['x-ray fish', 'yak', 'zebra'],
                    'count_name': [1,2,1]}
    
    df_expected = pd.DataFrame(data=data_expected)
    r_expected = Relation(df_expected) 

    data_real = {'animal': ['zebra', 'yak', 'yak', 'x-ray fish'],
                'name': ['adam', 'bob', 'charlie', 'dina']}
    df = pd.DataFrame(data=data_real)
    r = Relation(df)

    r = r.groupby(['animal']).count('name')
    assert r.equals(r_expected)

def test_groupby_2():
    data_expected = {'student': ['amanda', 'sam', 'sam', 'tony'],
                     'grade': ['A', 'A', 'C', 'B'],
                     'count_classes': [2,2,1,1]}

    
    df_expected = pd.DataFrame(data=data_expected)
    r_expected = Relation(df_expected) 
    print(r_expected)

    data_real = {'student': ['amanda', 'amanda', 'sam', 'sam', 'sam', 'tony'],
                'classes': ['math', 'science', 'math', 'science', 'chinese', 'math'],
                'grade': ['A', 'A', 'C', 'A', 'A', 'B']}
    df = pd.DataFrame(data=data_real)
    r = Relation(df)
    r = r.groupby(['student', 'grade']).count('classes')
    print(r)
    assert r.equals(r_expected)