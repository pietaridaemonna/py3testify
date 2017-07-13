#!/usr/bin/python3


from py3Testify.core import TestPlan, TestSuite, TestCase, TestStep

import colors


stp1 = TestStep('step1', 'shell', 'uname -a')
stp2 = TestStep('step1', 'shell', 'cat /proc/cpuinfo')

st1 = TestCase('st1','dessdkjf')
st2 = TestCase('st2','dessdkjf')
st3 = TestCase('st3','dessdkjf')

st1.add_test_step(stp1)
st1.add_test_step(stp2)
st2.add_test_step(stp2)

sut = TestSuite('ping_suite','lets ping something')
sut2 = TestSuite('echo_suite','echo hello world')

sut.add_test_case(st1)
sut2.add_test_case(st2)
sut2.add_test_case(st3)

tsp = TestPlan('new testplan1', 'some descr')

tsp.add_test_suite(sut)
tsp.add_test_suite(sut2)

print(colors.red('printing test plan'))
print(tsp)






