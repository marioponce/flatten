# -*- coding: utf-8 -*-
"""
Created on Fri May 13 17:05:55 2022
@author: Mario Ponce
"""

import flatten as ft
import pytest

@pytest.mark.parametrize("able_to_flatten, expected_result", [
    ("""{"a": "aa"}""", "[{'a': 'aa'}]"),
    ("""{"a": ["aa"]}""", "[{'a[0]': 'aa'}]"),
    ("""{"a": ["aa", "ab"]}""", "[{'a[0]': 'aa'}, {'a[1]': 'ab'}]"),
    ("""{"b": {"bb1": "d", "bb2": "d2"}}""",
     "[{'b.bb1': 'd'}, {'b.bb2': 'd2'}]"),
    ("""{"a": "aa", "b": {"bb1": "d","bb2": "d2"},"c": [{"cc1": "d"},{"cc1": "d2","cc2": [{"e": "f"}]}], "g": ["h", "i"], "gg": ["h", "i"]}""",
     "[{'a': 'aa'}, {'b.bb1': 'd'}, {'b.bb2': 'd2'}, {'c[0].cc1': 'd'}, {'c[1].cc1': 'd2'}, {'c[1].cc2[0].e': 'f'}, {'g[0]': 'h'}, {'g[1]': 'i'}, {'gg[0]': 'h'}, {'gg[1]': 'i'}]")
])

def test_able_to_flatten(able_to_flatten, expected_result):
    assert ft.solution(able_to_flatten) == expected_result

@pytest.mark.parametrize("not_able_to_flatten_0", [
    ("""{a": "aa"}"""),
    ("""{"a": ("aa")}""",),
    ("""{4: ["aa", "ab"]}""")
])

def test_exit_0(not_able_to_flatten_0):
    with pytest.raises(SystemExit) as exc:
        ft.solution(not_able_to_flatten_0)
    assert exc.value.code == 0

@pytest.mark.parametrize("not_able_to_flatten_1", [
    ("""["aa", "ab"]"""),
    ("""3""")
])

def test_exit_1(not_able_to_flatten_1):
    with pytest.raises(SystemExit) as exc:
        ft.solution(not_able_to_flatten_1)
    assert exc.value.code == 1
