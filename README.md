# Overview
March ranks among my favorite times of the year! I love this season because 68 of the best college basketball teams compete in a single-elimination tournament to crown a champion. The single-elimination format creates opportunities for thrilling upsets, where lesser-known schools suddenly topple top-ranked teams. Grit, stamina, and a bit of luck for 40 minutes are all a team needs to pull off these awe-inspiring victories.

Along with this incredible tournament comes the March Madness bracket challenge, a chance to earn bragging rights and prove superior college basketball knowledge to friends and family. Given the tournament's unpredictability and frequent upsets, choosing the right team often comes down to luck. I've noticed a pattern when friends or family pick an improbable upset—they say, "I knew this upset was coming because of X statistic." Whether that statistic actually mattered or luck played the larger role, those claims pushed me to rely less on gut feelings and more on data when making picks. That’s why I built an app to visualize key statistics and provide a data-driven approach to filling out brackets.

Links to the March Madness Streamlit Apps: 
1. [2023-2024 Regular Season Data](https://march-madness-app-2024.streamlit.app/)
2. [2022-2023 Regular Season Data](https://jacob35-march-madness-app-app-lt3kow.streamlit.app/)

These app allows for you to do the following:
1. Look at head to head matchups with key statistics.
2. Group teams according to their defensive and offensive efficiency rankings.
3. See historical seed statistics.

These apps utilizes data from sports-reference.com. These apps utilize pandas to clean, manipulate, and analyze the data. These apps use Streamlit for all front end features. 
- [Python Script](https://github.com/jacob35/March-Madness-App/blob/main/2024/App.py)
- [GitHub Repository](https://github.com/jacob35/March-Madness-App/tree/main)

## Research & Key App Features
Prior to creating the app, I did thorough research to understand what statistics I wanted to see. One key to having a successful bracket is to make sure you pick the correct final four teams. Generally, you get more points on your bracket if you pick the correct team in later rounds. Thus, being able to pick a champion or the final four teams has a huge impact on how well your bracket does. Historical research shows that the winner is always in the top 25 in defensive and offensive rank. Thus, I created a feature to allow you to see what teams have a lower or equal to defensive and offensive rank based on the values you put in (see image below). 

The defensive and offensive rank gives a holistic view of how good the team is, but I also wanted to be able to see details of head to head matchups. Sometimes certain matchups causes the lower ranked team to win. For example, if a good 3 point shooting team gets hot, they may have a better chance against a bad 3 point shooting team no matter what they are ranked. Therefore, I created a visualization where you could choose spcefic teams and see their head to head matchups (see image below).

Lastly, I wanted to see historical seed win percentages. This helps with a gut check of knowing if your upset is maybe too crazy. Do not get me wrong, history is made to be broken. This historical data just lets you know how much justification you need on choosing that 16 seed beating that 1 seed (see image below). 

## App Build
I utilized Python to build this app ([Python Script](https://github.com/jacob35/March-Madness-App/blob/main/2024/App.py)). The key libraries I used were Streamlit and pandas. 

I used pandas to extract, clean, filter, and combine the data. Key functions I used were:
1. rank()
2. concat()
3. range()
4. append()

```Python
# Get the Offensive and Defensive Rankings
df_team_ratings['Off. Rank'] = df_team_ratings['ORtg'].rank(ascending=False)
df_team_ratings['Def. Rank'] = df_team_ratings['DRtg'].rank()
df_team_ratings['Net Rank'] = df_team_ratings['NRtg'].rank(ascending=False)
```
```Python
# Combine all DataFrames
df_team_1_data = df_team_1[['SRS','eFG%','TRB%','TOV%','Pace']]
df_team_1_data_appended = pd.concat([df_team_1_append, df_team_1_data, df_team_1_data_basic], axis=1)
df_1_seed_name = pd.DataFrame({'School':[team_1],'Seed':[seed_1]})
df1 = pd.concat([df_1_seed_name, df_team_1_data_appended], axis=1)
df1.index = range(1,len(df1)+1)
```
I also utilized for loops to help aggregate and join data. 
```Python
for i in range(len(teams)):
    for j in range(len(df_team_ratings['School'].values)):
        if teams[i] == df_team_ratings['School'][j]:
            Schools.append(df_team_ratings['School'][j]) 
            Off_Rank.append(df_team_ratings['Off. Rank'][j])
            Def_Rank.append(df_team_ratings['Def. Rank'][j])
            Net_Rank.append(df_team_ratings['Net Rank'][j])
```
