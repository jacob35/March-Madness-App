# StreamLit App

# imports
import pandas as pd
import streamlit as st 
#import plotly.express as px


# import data
df_team_all = pd.read_excel('sportsref_download_Advanced_More.xls', sheet_name='Data')            # Get Team Names (All)
df_team = pd.read_excel('sportsref_download_Advanced_More.xls', sheet_name='Seeds')               # Get Team Names & Seeds
df_team_ratings = pd.read_excel('sportsref_download_Ratings.xls')                                 # Get Team Offensive and Defensive Ratings
df_seed_data = pd.read_excel('sportsref_download_Advanced_More.xls', sheet_name='Seed Data')      # Get Seed Data
df_seed_stats = pd.read_excel('sportsref_download_Advanced_More.xls', sheet_name='Seed Stats')    # Get Seed Stats
df_team_basic = pd.read_excel('sportsref_download_Basic.xls')                                     # Get Team FT% and 3P%

data_seed_1 = df_seed_data['Seed_1'].values     # Higher Seed Numbers (first round)
data_seed_per = df_seed_data['Win %'].values    # Hihgher seed win % (first round)

# Rounds
Rounds = ['1st Round', '2nd Round', 'Sweet 16', 'Elite 8', 'Final Four', 'Championship']

# Title for app
st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color: blue;'>March Madness Tool (2023)</h1>", unsafe_allow_html=True)

# Header for choosing your team
teams = df_team['School'].values
seeds = df_team['Seed'].values

st.header('Choose Your Teams')

col1, col2, col3 = st.columns(3)

with col1:
    # Higher Seed
    team_1 = st.selectbox('Choose your first team - higher seed', df_team['School'])
    for i in range(len(teams)):
        if team_1 == teams[i]:
            seed_1 = seeds[i]
with col2:
    team_2 = st.selectbox('Choose your second team - lower seed', df_team['School'])
    for i in range(len(teams)):
        if team_2 == teams[i]:
            seed_2 = seeds[i]
with col3:
    # Chooose the round
    choose_round = st.selectbox('Choose the round ', Rounds)

# Data
st.header('Data About Teams')
team_1_new = team_1
team_2_new = team_2
team_1_new += '\xa0NCAA'  # Able to search on df_team_all
team_2_new += '\xa0NCAA'  # Able to search on df_team_all
df_team_1 = df_team_all[df_team_all['School'] == team_1_new].reset_index(drop=True)
df_team_2 = df_team_all[df_team_all['School'] == team_2_new].reset_index(drop=True)

# Get FT% and 3P%
df_team_1_basic = df_team_basic[df_team_basic['School'] == team_1_new].reset_index(drop=True)
df_team_2_basic = df_team_basic[df_team_basic['School'] == team_2_new].reset_index(drop=True)

df_team_1_data_basic = df_team_1_basic[['FT%','3P%']]
df_team_2_data_basic = df_team_2_basic[['FT%','3P%']]

# Get the Offensive and Defensive Rankings
df_team_ratings['Off. Rank'] = df_team_ratings['ORtg'].rank(ascending=False)
df_team_ratings['Def. Rank'] = df_team_ratings['DRtg'].rank()
df_team_ratings['Net Rank'] = df_team_ratings['NRtg'].rank(ascending=False)

df_team_1_ratings = df_team_ratings[df_team_ratings['School'] == team_1].reset_index(drop=True)
df_team_2_ratings = df_team_ratings[df_team_ratings['School'] == team_2].reset_index(drop=True)

df_team_1_append = df_team_1_ratings[['Off. Rank', 'Def. Rank', 'Net Rank']]
df_team_2_append = df_team_2_ratings[['Off. Rank', 'Def. Rank', 'Net Rank']]

# Combine all DataFrames
df_team_1_data = df_team_1[['SRS','eFG%','TRB%','TOV%','Pace']]
df_team_1_data_appended = pd.concat([df_team_1_append, df_team_1_data, df_team_1_data_basic], axis=1)
df_1_seed_name = pd.DataFrame({'School':[team_1],'Seed':[seed_1]})
df1 = pd.concat([df_1_seed_name, df_team_1_data_appended], axis=1)
df1.index = range(1,len(df1)+1)

df_team_2_data = df_team_2[['SRS','eFG%','TRB%','TOV%','Pace']]
df_team_2_data_appended = pd.concat([df_team_2_append, df_team_2_data, df_team_2_data_basic], axis=1)
df_2_seed_name = pd.DataFrame({'School':[team_2],'Seed':[seed_2]})
df2 = pd.concat([df_2_seed_name, df_team_2_data_appended], axis=1)

df_1 = df1.append(df2, ignore_index=True)
df_1.index = range(1,len(df_1)+1)

# Combine Team 1 and Team 2 Dataframe and format
df_all = df_1.style.highlight_max(color='orange',axis=0,subset=['SRS','eFG%','TRB%','Pace','FT%','3P%']).highlight_min(color='#90ee90',axis=0,subset=\
    ['Seed','Off. Rank','Def. Rank', 'Net Rank','TOV%']).format({'Off. Rank':'{0:,.0f}','Def. Rank':'{0:,.0f}',\
        'Net Rank':'{0:,.0f}','SRS':'{0:,.2f}','Pace':'{0:,.1f}','eFG%':'{:.1%}','TRB%':'{0:,.1f}','TOV%':'{0:,.1f}','FT%':'{:.1%}','3P%':'{:.1%}'})

st.write(':orange[Orange] = Max value (applied to SRS, eFG%, TRB%, Pace, FT%, and 3P%)')
st.write(':green[Light Green] = Min value (applied to Seed, Off. Rank, Def. Rank, Net Rank, and TOV%)')
st.dataframe(df_all)
st.write('Statistic definitions at bottom of the page')

# Definition of Team Stats
Stats = ['Off. Rank', 'Def. Rank', 'Net Rank','SRS','eFG%','TRB%','TOV%','Pace','FT%','3P%']
Definitions = ['Offensive Efficiency Rank (1=best, 363=worst)','Defffensive Efficiency Rank (1=best, 363=worst)','Net Rank (1=best, 363=worst)',\
    'Simple Rating System - Rating that takes into account average point differential and strength of schedule. The rating is denominated in points above/below average, where zero is the average (higher number is better).', \
    'Effective Field Goal Percentage - Field goal % that adjusts for 3s being worth more than 2s','Total rebound %',\
        'Turnover % - An estimate of turnovers per 100 plays',\
            'Estimate of possesions per 40 minutes (Higher # = plays quick with a lot of possessions, Lower # = the team slows the game down)','Free throw %','Three point %']
df_def = pd.DataFrame(list(zip(Stats,Definitions)), columns = ['Stats', 'Definitions'])
df_def.index = range(1,len(df_def)+1)

# Seed Data/Stats
st.header('Seed Data/Stats')

# Highlighting the background of the cell

def color_coding_1st_round(row):
    return ['background-color:yellow']* len(row) if row.Seed_1 == seed_1 else ['background-color:white'] * len(row)

def color_coding_all(row):
    value = row.loc['Seed']
    if seed_1 != seed_2:
        if value == seed_1:
            color = 'lightblue'
        elif value == seed_2:
            color = 'lightgreen'
        else:
            color = 'white'
    else:
        if value == seed_1:
            color = 'lightblue'
        else:
            color = 'white'
    return ['background-color: {}'.format(color) for r in row]


# 1 Round winner %
if choose_round == '1st Round':
    st.write('__1st Round Higher Seed Win Percentage__')
    df_seed_data.index = range(1,len(df_seed_data)+1)
    d2 = dict.fromkeys(df_seed_data.select_dtypes('float').columns, "{:.1%}")
    df_color_1st_round = df_seed_data.style.apply(color_coding_1st_round, axis=1).format(d2)
    st.dataframe(df_color_1st_round)

# Seed Odds
st.write('__Odds to advance to the next round__', "(Ex: The 1 seed has a 99.3% odd of advancing to the 2nd Round)")
st.write(':blue[Light Blue] = ', team_1)
st.write(':green[Light Green] = ', team_2)
df_seed_stats.index = range(1,len(df_seed_stats)+1)
d3 = dict.fromkeys(df_seed_stats.select_dtypes('float').columns, "{:.1%}")
df_color_all= df_seed_stats.style.apply(color_coding_all, axis=1).format(d3)
st.table(df_color_all)

# Printing Stat Definitions
st.header('Statistic Definitions')
st.table(df_def)