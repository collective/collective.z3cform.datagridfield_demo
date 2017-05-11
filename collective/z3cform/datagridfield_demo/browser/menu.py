# -*- coding: utf-8 -*-
"""
    Demo of the widget

    I haven't gotten these views working with tests.
"""
from five import grok
from zope.interface import Interface


class Menu(grok.View):
    grok.context(Interface)
    grok.name('demo-collective.z3cform.datagrid-menu')
