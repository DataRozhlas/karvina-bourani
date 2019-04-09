#%%
import requests
import pandas as pd
import json

#%%
d = pd.read_csv('bourani.csv', sep='\t', encoding='utf-8')
d = list(d.to_dict(orient='index').values())

#%%
for addr in d:
    r = requests.get('http://ags.cuzk.cz/arcgis/rest/services/RUIAN/Vyhledavaci_sluzba_nad_daty_RUIAN/MapServer/exts/GeocodeSOE/tables/1/findAddressCandidates?SingleLine=' + addr['ulice'] + ' ' + str(addr['cislo']) + ', Karviná&outSR=4326&maxLocations=&outFields=&searchExtent=&f=pjson')
    try:
        addr.update({
            'x': r.json()['candidates'][0]['location']['x'], 
            'y': r.json()['candidates'][0]['location']['y']
            })
    except:
        print(addr['ulice'] + ' ' + str(addr['cislo']))

#%%
d

#%%
