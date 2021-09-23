import pandas as pd
import matplotlib.pyplot as plt

qb=pd.read_csv('2020 QB.txt')
rush=pd.read_csv('2020 RB.txt')
rec=pd.read_csv('2020 WR.txt')

#Adjust Column Names for Drop Down Boxes
qb.columns=(['Rank', 'Player', 'Team', 'Age', 'Position', 'Games', 'Games Started', 'Record', 'Completions', 'Attempts','Completion Percentage', 
             'Pass Yards', 'Passing Touchdowns', 'Touchdown Percentage', 'Interceptions', 'Interception Percentage', '1st Downs', 'Longest Completion', 
             'Yards Per Attempt', 'Adjusted Yards Per Attempts', 'Yards Per Completion', 'Yards Per Game', 'QBR', 'Total QBR', 'Sacks', 'Sack Yards Lost', 
             'Net Yards Per Attempt', 'Adjusted Net Yards Per Attempt', 'Sack Percentage', '4th Quarter Comebacks', 'Game Winning Drives'])

rush.columns=(['Rank', 'Player', 'Team', 'Age', 'Position', 'Games', 'Games Started', 'Carries', 'Rushing Yards', 'Rushing Touchdowns', '1st Downs',
             'Longest Rush', 'Yards Per Carry', 'Yards Per Game', 'Fumbles'])

rec.columns=(['Rank', 'Player', 'Team', 'Age', 'Position', 'Games', 'Games Started', 'Targets', 'Receptions', 'Catch Percentage','Receiving Yards', 
             'Yards Per Reception', 'Receiving Touchdowns', '1st Downs', 'Longest Reception', 'Yards Per Target', 'Receptions Per Game', 'Yards Per Game', 'Fumbles'])

#Remove PFR Links From Player Names
for name in qb['Player']:
    slash=name.index('\\')
    qb['Player']=qb['Player'].replace(name,name[0:slash])

for name in rush['Player']:
    slash=name.index('\\')
    rush['Player']=rush['Player'].replace(name,name[0:slash])

for name in rec['Player']:
    slash=name.index('\\')
    rec['Player']=rec['Player'].replace(name,name[0:slash])

#Remove non-qualifiers for 'Per' Categories
qb=qb.loc[(qb['Attempts']>=14)]
rush=rush.loc[(rush['Carries']>=100)]
rec=rec.loc[(rec['Receptions']>=30)]

#Dictionary to convert team names to team colors
colors={'ARI':'#97233f','ATL':'#a71930','BAL':'#241773','BUF':'#00338d','CAR':'#0085ca','CHI':'#0b162a','CIN':'#fb4f14','CLE':'#311d00','DAL':'#041e42','DEN':'#002244','DET':'#0076b6',
        'GNB':'#203731','HOU':'#03202f','IND':'#002c5f','JAX':'#006778','KAN':'#e31837','LAC':'#002a5e','LAR':'#003594','LVR':'#000000','MIA':'#008e97','MIN':'#4f2683','NWE':'#002244','NOR':'#d3bc8d',
        'NYG':'#0b2265','NYJ':'#125740','PHI':'#004c54','PIT':'#ffb612','SFO':'#aa0000','SEA':'#002244','TAM':'#d50a0a','TEN':'#0c2340','WAS':'#773141','2TM':'#000000'}

#Add Team Color Column and Convert to Hex
qb['Color']=qb['Team']
for color in qb['Color']:
    if color[0]!='#':
        qb['Color']=qb['Color'].replace(color,colors[color])
    else:
        pass

rush['Color']=rush['Team']
for color in rush['Color']:
    if color[0]!='#':
        rush['Color']=rush['Color'].replace(color,colors[color])
    else:
        pass

rec['Color']=rec['Team']
for color in rec['Color']:
    if color[0]!='#':
        rec['Color']=rec['Color'].replace(color,colors[color])
    else:
        pass
    
def passing(stat):
    passing=qb.sort_values(stat,ascending=False)
    passing=passing.head(10)
    passing=passing.sort_values('Player')
    
    plt.figure(figsize=(20,8))
    plt.bar(passing['Player'],passing[stat],color=passing['Color'])
    plt.title('Top 10 Quarterbacks by '+stat+' (2020 Season)')
    plt.ylim((min(passing[stat]*.8)))
    plt.ylabel(stat)
    plt.xlabel('Quarterback\n(* denotes Pro Bowl selection)\n(+ denotes First Team All Pro)')

def rushing(stat):
    rushing=rush.sort_values(stat,ascending=False)
    rushing=rushing.head(10)
    rushing=rushing.sort_values('Player')
    
    plt.figure(figsize=(20,8))
    plt.bar(rushing['Player'],rushing[stat],color=rushing['Color'])
    plt.title('Top 10 Players by '+stat+' (2020 Season)')
    plt.ylim((min(rushing[stat]*.8)))
    plt.ylabel(stat)
    plt.xlabel('Player\n(* denotes Pro Bowl selection)\n(+ denotes First Team All Pro)')

def receiving(stat):
    receiving=rec.sort_values(stat,ascending=False)
    receiving=receiving.head(10)
    receiving=receiving.sort_values('Player')
    
    plt.figure(figsize=(20,8))
    plt.bar(receiving['Player'],receiving[stat],color=receiving['Color'])
    plt.title('Top 10 Players by '+stat+' (2020 Season)')
    plt.ylim((min(receiving[stat]*.8)))
    plt.ylabel(stat)
    plt.xlabel('Player\n(* denotes Pro Bowl selection)\n(+ denotes First Team All Pro)')
