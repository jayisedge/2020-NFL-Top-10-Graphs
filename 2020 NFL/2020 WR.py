import pandas as pd
import matplotlib.pyplot as plt

wr=pd.read_csv('2020 WR.txt')

#Dictionary to convert team names to team colors
colors={'ARI':'#97233f','ATL':'#a71930','BAL':'#241773','BUF':'#00338d','CAR':'#0085ca','CHI':'#0b162a','CIN':'#fb4f14','CLE':'#311d00','DAL':'#041e42','DEN':'#002244','DET':'#0076b6',
        'GNB':'#203731','HOU':'#03202f','IND':'#002c5f','JAX':'#006778','KAN':'#e31837','LAC':'#002a5e','LAR':'#003594','LVR':'#000000','MIA':'#008e97','MIN':'#4f2683','NWE':'#002244','NOR':'#d3bc8d',
        'NYG':'#0b2265','NYJ':'#125740','PHI':'#004c54','PIT':'#ffb612','SFO':'#aa0000','SEA':'#002244','TAM':'#d50a0a','TEN':'#0c2340','WAS':'#773141','2TM':'#000000'}

#Reference for Columns in dataframe
#Index['Rk', 'Player', 'Tm', 'Age', 'Pos', 'G', 'GS', 'Tgt', 'Rec', 'Ctch%',
#     'Yds', 'Y/R', 'TD', '1D', 'Lng', 'Y/Tgt', 'R/G', 'Y/G', 'Fmb']

#Drop unnecessary columns and filter out non-receivers
wr=wr.drop(columns=['Rk', 'Age', 'G', 'GS', 'Ctch%', 'Y/R', '1D', 'Lng', 'Y/Tgt', 'R/G', 'Y/G', 'Fmb'])
wr=wr.loc[(wr['Pos']=='wr')|(wr['Pos']=='WR')]

#Remove PFR links in names
for name in wr['Player']:
    slash=name.index('\\')
    wr['Player']=wr['Player'].replace(name,name[0:slash])
    
#Add team color Column and convert to Hex
wr['Color']=wr['Tm']
for color in wr['Color']:
    if color[0]!='#':
        wr['Color']=wr['Color'].replace(color,colors[color])
    else:
        pass
    
#Top 10 Wide Receivers by Receiving Yards
def wr_yds():
    wr_yds=wr.sort_values('Yds',ascending=False)
    wr_yds=wr_yds.head(10)
    wr_yds=wr_yds.sort_values('Player')
    
    plt.figure(figsize=(20,8))
    plt.bar(wr_yds['Player'],wr_yds['Yds'],color=wr_yds['Color'])
    plt.title('Top 10 WRs by Receiving Yards (2020 Season)')
    plt.ylim(1000)
    plt.ylabel('Yards')
    plt.xlabel('Wide Receiver\n(* denotes Pro Bowl selection)\n(+ denotes First Team All Pro)')

#Top 10 Wide Receivers by Receiving Touchdowns
def wr_tds():
    wr_td=wr.sort_values('TD',ascending=False)
    wr_td=wr_td.head(10)
    wr_td=wr_td.sort_values('Player')
    
    plt.figure(figsize=(20,8))
    plt.bar(wr_td['Player'],wr_td['TD'],color=wr_td['Color'])
    plt.title('Top 10 WRs by Receiving Touchdowns (2020 Season)')
    plt.ylim(6)
    plt.ylabel('Touchdowns')
    plt.xlabel('Wide Receiver\n(* denotes Pro Bowl selection)\n(+ denotes First Team All Pro)')
    
#Top 10 Wide Receivers by Receptions
def wr_rec():
    wr_rec=wr.sort_values('Rec',ascending=False)
    wr_rec=wr_rec.head(10)
    wr_rec=wr_rec.sort_values('Player')
    
    plt.figure(figsize=(20,8))
    plt.bar(wr_rec['Player'],wr_rec['Rec'],color=wr_rec['Color'])
    plt.title('Top 10 WRs by Receptions (2020 Season)')
    plt.ylim(80)
    plt.ylabel('Receptions')
    plt.xlabel('Wide Receiver\n(* denotes Pro Bowl selection)\n(+ denotes First Team All Pro)')
    
#Top 10 Wide Receivers by Targets
def wr_tgt():
    wr_tgt=wr.sort_values('Tgt',ascending=False)
    wr_tgt=wr_tgt.head(10)
    wr_tgt=wr_tgt.sort_values('Player')
    
    plt.figure(figsize=(20,8))
    plt.bar(wr_tgt['Player'],wr_tgt['Tgt'],color=wr_tgt['Color'])
    plt.title('Top 10 WRs by Targets (2020 Season)')
    plt.ylim(120)
    plt.ylabel('Receptions')
    plt.xlabel('Wide Receiver\n(* denotes Pro Bowl selection)\n(+ denotes First Team All Pro)')
    
wr_yds()
wr_tds()
wr_rec()
wr_tgt()