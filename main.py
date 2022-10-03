from lib2to3.pgen2.token import EQUAL
import numpy as np
import pandas as pd
import matplotlib as plt
import csv
from IPython.display import HTML
from flask import Flask, render_template, send_file, make_response, url_for, Response

df = pd.DataFrame({'Name' : ['Adrian', 'Alain', 'Alec', 'Alcides', 'Bryan', 'Elien','Gabriel', 'Marco', 'Rudy'],
                   'Position' :['Midfielder','Defender','Forward','Midfielder','Forward','Defender','Defender','Midfielder','Forward'],
    
                   'Matches_Played': [13,26,13,26,13,27,25,19,27],
                   'W': [6,12,7,16,7,10,12,12,11],
                   'L': [7,14,6,10,6,15,13,7,16],
                   'Goals': [3,1,7,9,9,0,3,3,4],
                   'OG':[0,0,0,0,0,0,1,0,0],
                   'Assists': [1,2,0,11,3,2,7,2,4],
                   'Lost_Balls': [16,37,16,27,22,39,20,34,41],
                   'Recoveries': [16,27,14,19,19,30,45,18,24],
                   'Errors_Led_To_Goal': [0,0,0,0,0,0,0,0,0],
                   'Big_Chances_Missed': [0,1,0,1,1,0,1,0,4],
                   'Blocks': [3,10,8,2,2,18,3,1,6],
                   'Points': [0,0,0,0,0,0,0,0,0]},
                    index = [1,2,3,4,5,6,7,8,9])

goal_p = df.Goals*5
assist_p = df.Assists*3
recoveries_p = df.Recoveries*0.5
lballs_p = df.Lost_Balls*-0.5
wins_p = df.W*7.5
errors_p = df.Errors_Led_To_Goal*-5
comidas_p = df.Big_Chances_Missed*-1
blocks_p = df.Blocks*0.25
og_p = df.OG*-2.5

indicators = [goal_p, assist_p,recoveries_p,lballs_p,wins_p,errors_p,comidas_p, blocks_p, og_p]
df['Points'] = sum(indicators)
df['Points_Per_Game'] = df.Points/df.Matches_Played

pichichi = df.Goals.max()
df['Pichichi'] = df.loc[df['Goals'] >= pichichi, 'Name']


assists_l = df.Assists.max()
df['Assist_Leader'] = df.loc[df['Assists'] == assists_l, 'Name']

recoveries_l = df.Recoveries.max()
df['Recoveries_Leader'] = df.loc[df['Recoveries'] == recoveries_l, 'Name']

lb_l = df.Lost_Balls.max()
df['LB_Leader'] = df.loc[df['Lost_Balls'] == lb_l, 'Name']

df.to_csv(r"D:\Ranking_Football/Table.csv",index=False)

html = df.sort_values(['Points_Per_Game'], ignore_index = True,ascending = False).to_html(na_rep='')

text_file = open('index.html','w')
text_file.write(html)
text_file.close()

#<link rel="stylesheet" href="style.css">
#<header>Individual Stats</header>