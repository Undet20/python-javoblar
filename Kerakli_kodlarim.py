# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 22:04:56 2024

@author: Acer
"""

def methods(klass):
    """class ichidagi metodlarni topuvchi funksiya"""
    return [method for method in dir(klass) if not method.startswith('__')]
