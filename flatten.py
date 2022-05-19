# -*- coding: utf-8 -*-
"""
Created on Fri May 13 17:04:13 2022
@author: Mario Ponce
"""

import json
import sys

def solution(s: str) -> str:
    """Flattens a dictionary into a list of dictionaries.

    Args:
        s (str): contains a json-format dictonay.

    Returns:
        str that contains a list of dictionaries.
    """

    # Convert 's' into a dict 'd'
    try:
        d = json.loads(s)
    except:
        # When there is an error in the string, we abort the flattening process
        print('Impossible to convert into a dict. Please, check your input.')
        sys.exit(0)
    # Call the flatten function, with the already converted dict as parameter
    return(str(flatten(d)))

def flatten_gen(d:dict, k_0:str = '') -> iter:
    """Generates an iterator that contains key-value tuples from a dictionary

    Args:
        d (dict): could contains dict, list or str.
        k_0 (str): key in the original dict in which d is a value (default '').

    Returns:
        iter contains key-value tuples.
    """
    # Let's check each key-value pair contained in d
    for k, v in d.items():
        # Generating a key from previous keys
        k_1 =  k_0 + '.' + k if k_0 else k
        # when the value is a dictionary
        if isinstance(v, dict):
            # recursive strategy
            yield from flatten_gen(v, k_1)
        # when the value is a list.
        elif isinstance(v, list):
            i = 0
            for e in v:
                # when there is free element
                if isinstance(e, str):
                    # recursive strategy
                    yield from flatten_gen({k_1+'['+str(i)+']':e})
                else:
                    # recursive strategy
                    yield from flatten_gen(e, k_1+'['+str(i)+']')
                i += 1
        else:
            # final excution of the recursive strategy
            yield k_1, v

def flatten(d:dict) -> str:
    """Processes an iterator of tuples into a list of dictionaries.

    Args:
        d (dict): dict that could contains dict, list or str.

    Returns:
        list of dictionaries that contains str as value.
    """

    # ld : list of dictionaries
    try:
        ld = [{i[0]:i[1]} for i in list(flatten_gen(d))]
    except:
        # When there is an error in the string, we abort the flattening process
        print('Imput should be a dictionary. Please, check your input.')
        sys.exit(1)
    return(ld)
