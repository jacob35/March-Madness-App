# Overview
March is one of my favorite time's of the year! I love this time of the year because the top 68 college basketball teams come together and play in a single elimination tournament to crown a champion. Since, it is single elimination, crazy upsets happen. Schools you have never heard of before are all of a sudden taking down the top teams because they are on a hot streak. All it takes is for a team to have enough grit, stamina, and luck for 40 minutes to cause these awe inspiring upsets. 

With this amazing tournament also comes the March madness bracket challenge. This is an opportunity to gain bragging rights and show your superior college basketball knowledge against your family and friends. With the nature of this tournament and the crazy upsets, picking the correct team  I have noticed a theme from my friends and family members when they pick an unthickable upset. They state, "I knew this upset was coming from X statistic". Maybe that statistic was important or maybe they just got lucky, but it made me want to choose my bracket less on my gut feeling and more on what the data says. Thus, I built an app to help visualize and show key data and statistics. 

Links to the March Madness Streamlis Apps: 
1. [2023-2024 Regular Season Data](https://march-madness-app-2024.streamlit.app/)
2. [2022-2023 Regular Season Data](https://jacob35-march-madness-app-app-lt3kow.streamlit.app/)

These app allows for you to do the following:
1. Look at head to head matchups with key statistics.
2. Group teams according to their defensive and offensive efficiency rankings.
3. See historical seed statistics.

This app utilizes data from sports-reference.com. This app uses pandas to clean, manipulate, and analyze the data. This app uses Streamlit for all front end features. 
- [Python Script](https://github.com/jacob35/March-Madness-App/blob/main/2024/App.py)
- [GitHub Repository](https://github.com/jacob35/March-Madness-App/tree/main)

## Research

Prior to creating the app, I did thorough research to understand what statistics I wanted to see. One key to having a successful bracket is to make sure you pick the correct final four teams. Generally, you get more points on your bracket if you pick the correct team in later rounds. Thus, being able to pick a champion or the final four teams has a huge impact on how well your bracket does. Historical research shows that the winner is always in the top 25 in defensive and offensive rank. Thus, I created a feature to allow you to see what teams have a lower or equal to defensive and offensive rank based on the values you put in (see image below). 

The defensive and offensive rank gives a holistic view of how good the team is, but I also wanted to be able to see details of head to head matchups. Sometimes certain matchups causes the lower ranked team to win. For example, if a good 3 point shooting team gets hot, they may have a better chance against a bad 3 point shooting team no matter what they are ranked. Therefore, I created a visualization where you could choose spcefic teams and see their head to head matchups (see image below).

Lastly, I wanted to see historical seed win percentages. This helps with a gut check of knowing if your upset is maybe too crazy. Do not get me wrong, history is made to be broken. This historical data just lets you know how much justification you need on choosing that 16 seed beating that 1 seed (see image below). 

## App Building
I utilized Python to build this app ([Python Script](https://github.com/jacob35/March-Madness-App/blob/main/2024/App.py)). The key libraries I used were Streamlit and pandas. 

I used pandas to extract, clean, filter, and combine the data. Key functions I used were:
1. rank()
2. concat()
3. range()
4. append()

'''# Combine all DataFrames
df_team_1_data = df_team_1[['SRS','eFG%','TRB%','TOV%','Pace']]
df_team_1_data_appended = pd.concat([df_team_1_append, df_team_1_data, df_team_1_data_basic], axis=1)
df_1_seed_name = pd.DataFrame({'School':[team_1],'Seed':[seed_1]})
df1 = pd.concat([df_1_seed_name, df_team_1_data_appended], axis=1)
df1.index = range(1,len(df1)+1)'''
