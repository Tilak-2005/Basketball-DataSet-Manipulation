import pandas as pd
import matplotlib.pyplot as plt


url = "https://www.basketball-reference.com/leagues/NBA_2024_totals.html"
raw = pd.read_html(url)
df = raw[0]
df = df[df['Rk'] != 'Rk']   #Repeated
df = df.drop_duplicates() #Removes the duplicates if any 
df = df.reset_index(drop = True) #Drops the index and resets it
df = df.fillna(0) #Replaces the blank cells with 0 which is the best option for sport dataset
# print(df.head()) #Display top 5 elements in the given uncleaned or cleaned dataset

#Whole process is for computing average

avgp = df['PTS'].mean()
avgr = df['TRB'].mean()
avga = df['AST'].mean()

print(f"Average Points: {avgp:.2f}")
print(f"Average Rebounds: {avgr:.2f}")
print(f"Average Assists: {avga:.2f}")

df.to_csv("nba_stats.csv", index=False) #Saves the cleaned dataset
df_stats = df[['PTS', 'TRB', 'AST']]
print(df_stats.describe())

#Entire Data Visualisation and Graph making (Histogram) Code

plt.figure(figsize=(8,6))

#Distribution of Points
plt.subplot(2,3,1)
plt.hist(df['PTS'], bins=20, edgecolor='black')
plt.axvline(avgp, color='red', linestyle='dashed', linewidth=2, label=f'Avg: {avgp:.1f}')
plt.title('Distribution of Points')
plt.xlabel('Points')
plt.ylabel('Frequency')


#Distribution of Rebounds
plt.subplot(2,3,2)
plt.hist(df['TRB'], bins=20, edgecolor='black')
plt.axvline(avgp, color='red', linestyle='dashed', linewidth=2, label=f'Avg: {avgr:.1f}')
plt.title('Distribution of Rebounds')
plt.xlabel('Rebounds')
plt.ylabel('Frequency')

#Distribution of Assists
plt.subplot(2,3,3)
plt.hist(df['AST'], bins=20, edgecolor='black')
plt.axvline(avgp, color='red', linestyle='dashed', linewidth=2, label=f'Avg: {avga:.1f}')
plt.title('Distribution of Assists')
plt.xlabel('Assists')
plt.ylabel('Frequency')

#All the values in one graph
plt.subplot(2,3,4)
plt.hist(df['PTS'], bins=20, histtype='step', linewidth=2, label='Points', color='red', density=True)
plt.hist(df['TRB'], bins=20, histtype='step', linewidth=2, label='Rebounds', color='blue', density=True)
plt.hist(df['AST'], bins=20, histtype='step', linewidth=2, label='Assists', color='green', density=True)

plt.axvline(avgp, color='red', linestyle='dashed', linewidth=2)
plt.axvline(avgr, color='blue', linestyle='dashed', linewidth=2)
plt.axvline(avga, color='green', linestyle='dashed', linewidth=2)

#basicaly what happend is axvline is drawing a vertical line on the plot(plot of Averages,Rebounds,Assists) of its averages

plt.title('Distribution of Points, Rebounds, Assists')
plt.xlabel('Values')      
plt.ylabel('Density')    


plt.legend(loc='upper right')

#Display of Graphs
plt.suptitle("NBA 2024 Player Totals Analysis", fontsize=14)
plt.tight_layout()
plt.show()