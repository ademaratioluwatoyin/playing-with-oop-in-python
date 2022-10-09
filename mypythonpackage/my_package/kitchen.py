#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 15:26:09 2022

@author: user
"""

from room import Room

class Kitchen(Room):
    
    def __init__(self, length, breadth, purpose):
        Room.__init__(self, length, breadth)
        self.purpose = purpose