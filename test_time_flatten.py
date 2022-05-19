# -*- coding: utf-8 -*-
"""
Created on Fri May 13 17:10:33 2022
@author: Mario Ponce
"""

import argparse
import flatten as ft
import timeit

def parsing():
    """Catches the arguments in the comand line.

    Returns:
        args: argparse.Namespace
    """
    parser = argparse.ArgumentParser(description='Compute time to execute the fattle script.')
    parser.add_argument('-d','--default',
                    help ='Evaluate some defualt cases.',
                    action = 'store_true')
    parser.add_argument('-j','--json',
                    type = str,
                    help ='Dictionary in json format.')
    parser.add_argument('-l', '--loops',
                    type = int,
                    help='Number of loops to execute.')

    args = parser.parse_args()

    return args

def check_time(instance:str, loops:int):
    """Evaluates the time performance of the function 'solution'.

    Args:
        instance (str): dictionary in a json format.
        loops (int): number of times to execute.
    """
    t = timeit.timeit(stmt=ft.solution(instance), number=loops)
    print("For the  intance: \n")
    print(instance, "\n")
    print("    + Mean exceute time:", t)
    print("    + Number of loops excuted:", loops)
    print("\n","-"*80)

if __name__ == "__main__":

    args = parsing()

    if args.loops:
        loops = args.loops
    else:
        loops = 100000

    if args.default:
        instances = ["""{"a": "aa"}""",
        """{"a": ["aa"]}""",
        """{"a": ["aa", "ab"]}""",
        """{"b": {"bb1": "d", "bb2": "d2"}}""",
        """{"a": "aa",\n "b": {"bb1": "d","bb2": "d2"},\n "c": [{"cc1": "d"},{"cc1": "d2","cc2": [{"e": "f"}]}],\n "g": ["h", "i"], "gg": ["h", "i"]}"""
        ]

        for instance in instances:
            check_time(instance, loops)

    if args.json:
            check_time(args.json, loops)
