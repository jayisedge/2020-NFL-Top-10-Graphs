from tkinter import *
from tkinter import ttk
from Master import top_ten

cat=['Passing', 'Rushing', 'Receiving']

pass_cat=['Passing Yards', 'Passing Touchdowns',  'Interceptions', 'Attempts', 'Completions', 'Yards Per Game', 'Sacks', 'Sack Yards Lost', '1st Downs', 
          'Longest Completion', '4th Quarter Comebacks', 'Game Winning Drives']

rush_cat=['Rushing Yards', 'Rushing Touchdowns', 'Carries', 'Yards Per Carry', 'Yards Per Game', 'Fumbles', '1st Downs', 'Longest Rush']

rec_cat=['Receiving Yards', 'Receiving Touchdowns', 'Receptions', 'Targets', 'Yards Per Game', 'Receptions Per Game', 'Yards Per Reception', 'Yards Per Target',
         'Fumbles', '1st Downs', 'Longest Reception']

def populate_stats(event):
    if categories.get()=='Passing':
        statistics.config(value=pass_cat)
    elif categories.get()=='Rushing':
        statistics.config(value=rush_cat)
    else:
        statistics.config(value=rec_cat)

def graph(event):
    if categories.get()=='Passing':
        top_ten(statistics.get(), 'qb')
    elif categories.get()=='Rushing':
        top_ten(statistics.get(), 'rush')
    else:
        top_ten(statistics.get(), 'rec')
        
def _quit():
    root.quit()
    root.destroy()
        
root=Tk()
root.title('Graph 2020 NFL League Leaders')
root.geometry('400x400')

categories=ttk.Combobox(root,value=cat)
categories.pack(pady=20)
categories.bind('<<ComboboxSelected>>', populate_stats)

statistics=ttk.Combobox(root,value=None)
statistics.pack(pady=20)
statistics.bind('<<ComboboxSelected>>', graph)

graph_button=Button(root, text='Display Top 10 Graph', command=_quit)
graph_button.pack(pady=20)

root.mainloop()
