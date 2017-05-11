# -*- coding: utf-8 -*-
"""
    Demo of the widget

    I haven't gotten these views working with tests.
"""
from collective.z3cform.datagridfield import DataGridField
from collective.z3cform.datagridfield import DataGridFieldFactory
from five import grok
from plone.directives import form
from z3c.form import field
from z3c.form.interfaces import DISPLAY_MODE
from z3c.form.interfaces import HIDDEN_MODE
from z3c.form.widget import FieldWidget
from zope import schema
from zope.interface import Interface


class Menu(grok.View):
    grok.context(Interface)
    grok.name('demo-collective.z3cform.datagrid-menu')
