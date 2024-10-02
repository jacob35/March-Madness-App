# Overview
**Results: An app that analyzes 68 college basketball teams (1,200 rows of data) and empowers bracket selections based on insightful data.**

Links to the March Madness Streamlit Apps: 🏀
1. [2023-2024 App](https://march-madness-app-2024.streamlit.app/)
2. [2022-2023 App](https://jacob35-march-madness-app-app-lt3kow.streamlit.app/)

March is one of my favorite months! I love this season because 68 of the best college basketball teams compete in a single-elimination tournament to crown a champion. The single-elimination format creates opportunities for thrilling upsets, where lesser-known schools suddenly topple top-ranked teams. Grit, stamina, and a bit of luck for 40 minutes are all a team needs to pull off these awe-inspiring victories.

Along with this incredible tournament comes the March Madness bracket challenge, a chance to earn bragging rights and prove superior college basketball knowledge to friends and family. Given the tournament's unpredictability and frequent upsets, choosing the right team often comes down to luck. I've noticed a pattern when friends or family pick an improbable upset—they say, "I knew this upset was coming because of X statistic." Whether that statistic actually mattered or luck played the larger role, those claims pushed me to rely less on gut feelings and more on data when making picks. That’s why I built an app to visualize key statistics and provide a data-driven approach to filling out brackets.

These apps provide the following features:
1. Look at head to head matchups with key statistics.
2. Group teams according to their defensive and offensive efficiency rankings.
3. See historical seed statistics.

These apps utilizes data from sports-reference.com. These apps utilize pandas to clean, manipulate, and analyze the data. These apps use Streamlit for all front end features. 
- [Python Script](https://github.com/jacob35/March-Madness-App/blob/main/2024/App.py)
- [GitHub Repository](https://github.com/jacob35/March-Madness-App/tree/main)

## Research & Key App Features
Before building the app, I conducted thorough research to identify the most important statistics to track. Picking the correct Final Four teams is crucial for a successful bracket, as later rounds generally award more points. Choosing the champion or Final Four teams can significantly impact overall bracket performance. Historical data reveals that every tournament winner ranks in the top 25 for both offense and defense. Based on this, I developed a feature that allows users to filter teams by offensive and defensive rankings, using the values they input. 

[Offensive & Defensive Rank App Feature Image](https://github.com/user-attachments/assets/a53e7e2c-de21-4e6b-8400-e7d9dec873a5)
<img width="1319" alt="off_def_ranks" src="https://github.com/user-attachments/assets/a53e7e2c-de21-4e6b-8400-e7d9dec873a5">

Offensive and defensive rankings provide a solid overview of a team's strength, but I also wanted to dive deeper into head-to-head matchups. Sometimes, specific matchups give lower-ranked teams the edge. For instance, a strong three-point shooting team on a hot streak can outplay a poor three-point defending team, regardless of overall rankings. To capture these dynamics, I created a visualization that allows users to select specific teams and analyze their head-to-head matchups. 

[Head to Head App Feature Image](https://github.com/user-attachments/assets/a706d9df-dec7-4d71-90bb-a6feee45529d)
![head_to_head](https://github.com/user-attachments/assets/a706d9df-dec7-4d71-90bb-a6feee45529d)

Lastly, I wanted to include historical seed win percentages to provide a reality check when picking upsets. This data helps gauge whether an upset pick is a bold move or simply too far-fetched. Don’t get me wrong—history is made to be broken—but these stats help measure just how much confidence you need to back that 16 seed taking down a 1 seed. 

[Seed Statistics App Feature Image](https://github.com/user-attachments/assets/ea87b150-2cb4-45df-8e96-3313458186f9)
![seed_stats](https://github.com/user-attachments/assets/ea87b150-2cb4-45df-8e96-3313458186f9)

## App Build
I utilized Python to build this app ([Python Script](https://github.com/jacob35/March-Madness-App/blob/main/2024/App.py)). The key libraries I used were Streamlit and pandas. 

I used pandas to extract, clean, filter, and join the data. Key functions I used were:
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
