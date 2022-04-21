import folium
import array as arr
import pandas as pd
import numpy as np
import os
import json

m = folium.Map(location=[8.8932, 76.6141], zoom_start=12)      
print('Do you want to create marker : (YES/NO)')
g = input('').upper() 
if g == 'YES':
    print('how many: ')
    n =input('')
    result_t = []
    name_t = [None]*len(n)
    lon_t=[None]*len(n)
    lat_t=[None]*len(n)
    for i in range(0,int(n)):
        t=i
        print("enter name: ")
        name_t.insert(t,input(""))
        tooltip="hey its me"
        print('enter longitude: ')
        lon_t.insert(t,float(input('')))
        print('enter latitude: ')
        lat_t.insert(t,float(input('')))
        print(lon_t,name_t)
        folium.Marker(location=[lon_t[t], lat_t[t]],
            Popup='<strong>Location One</strong>',
            tooltip=tooltip).add_to(m)
        name_t.append(t)
        lon_t.append(t)
        lat_t.append(t)
        result_t.append(t) 
       
else:
    pass 
def edit_marker():
    print('which marker do you want to edit: ')  
    e=int(input(''))
    lon_t.pop(e)
    lat_t.pop(e)
    name_t.pop(e)
    lon_t.insert(e,float(input('')))
    lat_t.insert(e,float(input('')))
    name_t.insert(e,input(''))  
edit_marker()  
print(name_t)
print(lat_t)
print(lon_t)
         
m.save('Application.html')