# -*- coding: utf-8 -*-
"""
Created on Fri May 15 10:51:08 2015

@author: Alexis
"""

import pandas as pd

tab14 = read_2014()
# TODO: poser la question de pourquoi il y a des valeurs nulles
# TODO: pré-filtrer 
#tab14['Montant'] = tab14.groupby([u'Nom Attributaire', u'Nature du Marché', u'Tranche budgetaire']).transform(lambda x: x.fillna(x.mean()))

tab14 = tab14[tab14['Montant'].notnull()]
montant = tab14['Montant']
tab14.drop(['Tranche budgetaire', 'Attributaire est une PME'],
          axis=1, inplace=True)



total = montant.sum()
for col in tab14.columns.drop('Montant'):
    masse = tab14.groupby(col)['Montant'].sum()
    taux = masse*1000/total
    taux = taux.astype(int)
    
    n = 0
    while len(taux[taux > n]) > 15:
        n += 5
    a_afficher = taux[taux > n]
    print "variable " + col
    print "nombre de ligne avec taux superieur a ", n, len(a_afficher)
    print "qui font a elles toutes : ", sum(a_afficher)
    print a_afficher
    
    taux.plot(kind='pie')
    
## montant par date :
def vente_par_type_de_date(tab, par = 'dayofweek'):
    date = pd.DatetimeIndex(tab[u'date'])
    typde_de_date = getattr(date, par)
    sum = tab.groupby(typde_de_date)['Montant'].sum()
    count = tab.groupby(typde_de_date)['Montant'].count()
    mean = tab.groupby(typde_de_date)['Montant'].mean()
    
    data = pd.DataFrame({'somme': sum,
                         'nombre': count,
                         'moyenne': mean
                         })

#    data.index = labels
    return data


if __name__ == "__main__":
        
#    tab12 = read_2012()
#    data12 = vente_par_type_de_date(tab12)
#    tab13 = read_2013()
#    data13 = vente_par_type_de_date(tab13)
    tab14 = read_2014()
    data14 = vente_par_type_de_date(tab14)

    to_plot = data14[['moyenne', 'nombre']]
    to_plot['moyenne'] /= 1000
    plot = to_plot.plot()
    labels = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']

    data14 = vente_par_type_de_date(tab14, par='month')
#    data14 = vente_par_type_de_date(tab14[tab.Montant < 1e6], par='month')
    to_plot = data14[['somme', 'nombre']]
    to_plot['somme'] /= 1e6
    plot = to_plot.plot()

    
    
#
#par_date = tab14.groupby(u'Date de notification')['Montant'].sum()
#par_semaine = tab14.groupby(date.weekofyear)['Montant'].sum()
#par_semaine_count = tab14.groupby(date.weekofyear)['Montant'].count()
#par_mois_count = tab14.groupby(date.month)['Montant'].count()
#
#
#data = 100*data.divide(data.sum())
#data.plot()
#fig, axes = plt.subplots(nrows=1, ncols=3)
#fs = 10 # fontsize
#axes[0].plot(par_jour)
#axes[0].set_title('somme', fontsize=fs)
#axes[1].plot(par_jour_count)
#axes[1].set_title('nombre')
#axes[2].plot(par_jour_mean)
#axes[2].set_title('moyenne', fontsize=fs)
#
#
#montant_en_milliers = ((montant/1000).astype(int))
#mt = montant_en_milliers
#mt[mt > 1000] = 1000
#mt[mt < 100] .hist(bins=100)
#
#tab14.set_index(date, inplace=True)
#del tab14['date']
#tab14[u'Nature du Marché'].value_counts()