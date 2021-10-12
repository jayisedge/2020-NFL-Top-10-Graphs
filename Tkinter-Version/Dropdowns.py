from tkinter import *
from tkinter import ttk
from Master import passing, rushing, receiving

cat=['Passing', 'Rushing', 'Receiving']

pass_cat=['Pass Yards', 'Passing Touchdowns',  'Interceptions', 'Attempts', 'Completions', 'Yards Per Game', 'Sacks', 'Sack Yards Lost', '1st Downs', 
          'Longest Completion', '4th Quarter Comebacks', 'Game Winning Drives']

rush_cat=['Rushing Yards', 'Rushing Touchdowns', 'Carries', 'Yards Per Carry', 'Yards Per Game', 'Fumbles', '1st Downs', 'Longest Rush']

rec_cat=['Receiving Yards', 'Receiving Touchdowns', 'Receptions', 'Targets', 'Yards Per Game', 'Receptions Per Game', 'Yards Per Reception', 'Yards Per Target',
         'Fumbles', '1st Downs', 'Longest Reception']

def statistic(event):
    if cat_drop.get()=='Passing':
        stat_drop.config(value=pass_cat)
    elif cat_drop.get()=='Rushing':
        stat_drop.config(value=rush_cat)
    else:
        stat_drop.config(value=rec_cat)

def graph(event):
    if cat_drop.get()=='Passing':
        passing(stat_drop.get())
    elif cat_drop.get()=='Rushing':
        rushing(stat_drop.get())
    else:
        receiving(stat_drop.get())
        
def _quit():
    root.quit()
    root.destroy()
        
root=Tk()
root.title('Graph 2020 NFL League Leaders')
root.geometry('400x400')

cat_drop=ttk.Combobox(root,value=cat)
cat_drop.pack(pady=20)
cat_drop.bind('<<ComboboxSelected>>', statistic)

stat_drop=ttk.Combobox(root,value=None)
stat_drop.pack(pady=20)
stat_drop.bind('<<ComboboxSelected>>', graph)

graph_button=Button(root, text='Display Top 10 Graph', command=_quit)
graph_button.pack(pady=20)

root.mainloop()
