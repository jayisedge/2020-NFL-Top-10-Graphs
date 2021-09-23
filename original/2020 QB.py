import pandas as pd
import matplotlib.pyplot as plt

qb=pd.read_csv('2020 QB.txt')

#Dictionary to convert team names to team colors
colors={'ARI':'#97233f','ATL':'#a71930','BAL':'#241773','BUF':'#00338d','CAR':'#0085ca','CHI':'#0b162a','CIN':'#fb4f14','CLE':'#311d00','DAL':'#041e42','DEN':'#002244','DET':'#0076b6',
        'GNB':'#203731','HOU':'#03202f','IND':'#002c5f','JAX':'#006778','KAN':'#e31837','LAC':'#002a5e','LAR':'#003594','LVR':'#000000','MIA':'#008e97','MIN':'#4f2683','NWE':'#002244','NOR':'#d3bc8d',
        'NYG':'#0b2265','NYJ':'#125740','PHI':'#004c54','PIT':'#ffb612','SFO':'#aa0000','SEA':'#002244','TAM':'#d50a0a','TEN':'#0c2340','WAS':'#773141','2TM':'#000000'}

#Reference for Columns in dataframe
#Index ['Rk', 'Player', 'Tm', 'Age', 'Pos', 'G', 'GS', 'QBrec', 'Cmp', 'Att',
#      'Cmp%', 'Yds?', 'TD', 'TD%', 'Int', 'Int%', '1D', 'Lng', 'Y/A', 'AY/A',
#      'Y/C', 'Y/G', 'Rate', 'QBR', 'Sk', 'Yds', 'NY/A', 'ANY/A', 'Sk%', '4QC',
#      'GWD']

#Drop unnecessary columns and filter out non-quarterbacks
qb=qb.drop(columns=['Rk','Age','QBrec','TD%','Int%','Lng', 'Y/A', 'Y/C','Rate','QBR','Yds','NY/A','ANY/A','Sk%','4QC','GWD'])
qb=qb.loc[(qb['Pos']=='qb')|(qb['Pos']=='QB')]

#Remove PFR links in names
for name in qb['Player']:
    slash=name.index('\\')
    qb['Player']=qb['Player'].replace(name,name[0:slash])

#Add team color Column and convert to Hex
qb['Color']=qb['Tm']
for color in qb['Color']:
    if color[0]!='#':
        qb['Color']=qb['Color'].replace(color,colors[color])
    else:
        pass
    
#Top 10 by Passing Yards
def qb_yds():
    qb_yds=qb.sort_values('Yds?',ascending=False)
    qb_yds=qb_yds.head(10)
    qb_yds=qb_yds.sort_values('Player')
    
    plt.figure(figsize=(20,8))
    plt.bar(qb_yds['Player'],qb_yds['Yds?'],color=qb_yds['Color'])
    plt.title('Top 10 QBs by Passing Yards (2020 Season)')
    plt.ylim(3800)
    plt.ylabel('Yards')
    plt.xlabel('Quarterback\n(* denotes Pro Bowl selection)\n(+ denotes First Team All Pro)')

#Top 10 by Passing Touchdowns
def qb_tds():
    qb_td=qb.sort_values('TD',ascending=False)
    qb_td=qb_td.head(10)
    qb_td=qb_td.sort_values('Player')
    
    plt.figure(figsize=(20,8))
    plt.bar(qb_td['Player'],qb_td['TD'],color=qb_td['Color'])
    plt.title('Top 10 QBs by Passing Touchdowns (2020 Season)')
    plt.ylim(25)
    plt.ylabel('Touchdowns')
    plt.xlabel('Quarterback\n(* denotes Pro Bowl selection)\n(+ denotes First Team All Pro)')
    
#Top 10 by Average Yards per Attempt
def qb_aya():
    qb_aya=qb.sort_values('AY/A',ascending=False)
    qb_aya=qb_aya.head(10)
    qb_aya=qb_aya.sort_values('Player')
    
    plt.figure(figsize=(20,8))
    plt.bar(qb_aya['Player'],qb_aya['AY/A'],color=qb_aya['Color'])
    plt.title('Top 10 QBs by Average Yards Per Attempt (2020 Season)')
    plt.ylim(7.5)
    plt.ylabel('AY/A')
    plt.xlabel('Quarterback\n(* denotes Pro Bowl selection)\n(+ denotes First Team All Pro)')

qb_yds()
qb_tds()
qb_aya()
