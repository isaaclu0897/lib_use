#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 17:30:50 2018

@author: wei
"""

class Node(object):
    
    # define the Props of the node
    def __init__(self):
        self.p = 20
        self.t = None
        self.h = None
        self.s = None
        self.d = None
        self.q = None
        self.over = None
    @property
    def p(self):
        return self._p*100
    @p.setter
    def p(self, value):
        self._p = value/100
        return self._p
    def pp(self):
        return self._p

a = Node()
print(a.p)
a.p = 30
print(a.p)
print(a.pp())
    
     

    