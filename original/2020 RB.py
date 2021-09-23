import pandas as pd
import matplotlib.pyplot as plt

rb=pd.read_csv('2020 RB.txt')

#Dictionary to convert team names to team colors
colors={'ARI':'#97233f','ATL':'#a71930','BAL':'#241773','BUF':'#00338d','CAR':'#0085ca','CHI':'#0b162a','CIN':'#fb4f14','CLE':'#311d00','DAL':'#041e42','DEN':'#002244','DET':'#0076b6',
        'GNB':'#203731','HOU':'#03202f','IND':'#002c5f','JAX':'#006778','KAN':'#e31837','LAC':'#002a5e','LAR':'#003594','LVR':'#000000','MIA':'#008e97','MIN':'#4f2683','NWE':'#002244','NOR':'#d3bc8d',
        'NYG':'#0b2265','NYJ':'#125740','PHI':'#004c54','PIT':'#ffb612','SFO':'#aa0000','SEA':'#002244','TAM':'#d50a0a','TEN':'#0c2340','WAS':'#773141','2TM':'#000000'}

#Reference for Columns in dataframe
#Index ['Rk', 'Player', 'Tm', 'Age', 'Pos', 'G', 'GS', 'Att', 'Yds', 'TD', '1D',
#      'Lng', 'Y/A', 'Y/G', 'Fmb']

#Drop unnecessary columns and filter out non-running backs
rb=rb.drop(columns=['Rk', 'Age', 'G', 'GS', '1D', 'Lng', 'Y/G', 'Fmb'])
rb=rb.loc[(rb['Pos']=='rb')|(rb['Pos']=='RB')]

#Remove PFR links in names
for name in rb['Player']:
    slash=name.index('\\')
    rb['Player']=rb['Player'].replace(name,name[0:slash])
    
#Add team color Column and convert to Hex
rb['Color']=rb['Tm']
for color in rb['Color']:
    if color[0]!='#':
        rb['Color']=rb['Color'].replace(color,colors[color])
    else:
        pass
    
#Top 10 Running Backs by Rushing Yards
def rb_yds():
    rb_yds=rb.sort_values('Yds',ascending=False)
    rb_yds=rb_yds.head(10)
    rb_yds=rb_yds.sort_values('Player')
    
    plt.figure(figsize=(20,8))
    plt.bar(rb_yds['Player'],rb_yds['Yds'],color=rb_yds['Color'])
    plt.title('Top 10 RBs by Rushing Yards (2020 Season)')
    plt.ylim(800)
    plt.ylabel('Yards')
    plt.xlabel('Running Back\n(* denotes Pro Bowl selection)\n(+ denotes First Team All Pro)')

#Top 10 Running Backs by Rushing Touchdowns
def rb_tds():
    rb_td=rb.sort_values('TD',ascending=False)
    rb_td=rb_td.head(10)
    rb_td=rb_td.sort_values('Player')
    
    plt.figure(figsize=(20,8))
    plt.bar(rb_td['Player'],rb_td['TD'],color=rb_td['Color'])
    plt.title('Top 10 RBs by Rushing Touchdowns (2020 Season)')
    plt.ylim(7)
    plt.ylabel('Touchdowns')
    plt.xlabel('Running Back\n(* denotes Pro Bowl selection)\n(+ denotes First Team All Pro)')
    
#Top 10 Running Backs Rush Yards per Attempt
def rb_ya():
    rb_ya=rb.sort_values('Y/A',ascending=False)
    rb_ya=rb_ya.head(10)
    rb_ya=rb_ya.sort_values('Player')
    
    plt.figure(figsize=(20,8))
    plt.bar(rb_ya['Player'],rb_ya['Y/A'],color=rb_ya['Color'])
    plt.title('Top 10 RBs by Average Yards Per Attempt (2020 Season)')
    plt.ylim(4.5)
    plt.ylabel('Yards Per Attempt')
    plt.xlabel('Running Back\n(* denotes Pro Bowl selection)\n(+ denotes First Team All Pro)')
    
#Top 10 Running Backs by Rush Attempt
def rb_att():
    rb_att=rb.sort_values('Att',ascending=False)
    rb_att=rb_att.head(10)
    rb_att=rb_att.sort_values('Player')
    
    plt.figure(figsize=(20,8))
    plt.bar(rb_att['Player'],rb_att['Att'],color=rb_att['Color'])
    plt.title('Top 10 RBs by Rushing Attempts (2020 Season)')
    plt.ylim(150)
    plt.ylabel('Rush Attempts')
    plt.xlabel('Running Back\n(* denotes Pro Bowl selection)\n(+ denotes First Team All Pro)')
    
rb_yds()
rb_tds()
rb_ya()
rb_att()
