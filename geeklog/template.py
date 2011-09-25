# -*- coding: utf-8 -*-
class Template():

    def __init__(self):
        self.vars = {}

    def add_var(self, name, value):
        self.vars[name] = value
