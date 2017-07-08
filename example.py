#!/usr/bin/python3


from py3Testify.core import TestPlan, TestSuite, TestCase
from json import JSONEncoder
import json

import colors
print(colors.red('this is red'))
print(colors.green('this is green'))

tsp = TestPlan('new testplan1', 'some descr')

sut = TestSuite('ping_suite')
sut2 = TestSuite('echo_suite')

st1 = TestCase('st1')
st2 = TestCase('st2')
st3 = TestCase('st3')


sut.add_test_case(st1)
sut2.add_test_case(st2)
sut2.add_test_case(st3)

tsp.add_test_suite(sut)
tsp.add_test_suite(sut2)


print(tsp)






