# -*- coding:utf-8 -*-
s1='姓名：聂朝刚'
s2='学号：1403050114'
s3='班级：通风1班'

import math

T = 273
P = 1.0e-2
p = 1.24e-2
NA = 6.022e23
K = 1.38e-23
n = P/K*T
m = p/n
M = m*NA
print 'n=',n,'m=',m

M = (P*K*T*NA)/p

print 'M=',M