# -*- coding: utf-8 -*-
"""
Created on Thu May 14 13:59:12 2015

@author: Alexis
"""

import os
import pandas as pd


path = "M:\data\marches_publics"

# TODO
#def read_2011():
#    file = os.path.join(path, "Liste_marches_conclus_2012.xls")
#    tab = pd.read_csv(file, sep=';')
#    return tab


def read_2012():
    file = os.path.join(path, "Liste_marches_conclus_2012.xls")
    tab = pd.read_excel(file, parse_cols=12)
    date = pd.DatetimeIndex(tab[u'Date de notification'], dayfirst=True)
    tab['date'] = date
    tab.rename(columns= {u'Montant du marché si renseigné': 'Montant'},
               inplace=True)
    tab['Montant'].astype(float)
    return tab


def read_2013():
    file = os.path.join(path, "Liste_marches_conclus_2013.xls")
    tab = pd.read_excel(file, parse_cols=12)
    date = pd.DatetimeIndex(tab[u'Date de notification'], dayfirst=True)
    tab['date'] = date
    tab['Montant'].replace('307461maximum', '307461', inplace=True)
    tab['Montant'].replace("125000H,T", '125000', inplace=True)
    tab['Montant'] = tab['Montant'].astype(float)
    return tab


def read_2014():
    file = os.path.join(path, "PLACE_Export_Marches_ETALAB_2014.xls")
    tab = pd.read_excel(file, parse_cols=12)
    date = pd.DatetimeIndex(tab[u'Date de notification'], dayfirst=True)
    tab['date'] = date
    return tab
    
if __name__ == "__main__":
    tab = read_2014()
    tab.to_csv('marches_conclus_2014.csv', sep=';')
