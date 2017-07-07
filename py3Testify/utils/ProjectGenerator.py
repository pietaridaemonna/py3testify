#!/usr/bin/python3

import subprocess

print("Testify project generator")
print('================================================')
Choose_Item = input("Project name:")
print('proj name is '+Choose_Item)

sub1 = subprocess.call(["ssh", "pducai@80.159.247.194", "/dev/null"], stdout=subprocess.PIPE)
