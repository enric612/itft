#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Coverage és una llibreria que permet fer un informe
# que ens diu quines linees no han sigut testejades.
# D'aquesta forma podem saber quins test falten per programar.
# Per poder utilitzar la llibreria prime la instalarem:
# $ pip install coverage

import coverage
# Indiquem que ha de monitorizar la aplicació dins de la carpeta app.
COV = coverage.coverage(branch=True, include='app/*')
COV.start()

# Busquem dins de la carpeta tests tots els test que hi han i els executem.
import unittest
suite = unittest.TestLoader().discover('tests')
unittest.TextTestRunner(verbosity=2).run(suite)

COV.stop()
COV.report()
