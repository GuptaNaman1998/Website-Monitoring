import requests
import sqlite3
from twisted.internet import task, reactor
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('test.db')
# print("Opened database successfully")

conn.execute('''CREATE TABLE WebStatus
         (Count INT PRIMARY KEY NOT NULL,
         Date TEXT NOT NULL,
         Status INT NOT NULL);''')
# print("Table created successfully")

# datetime object containing current date and time

# dd/mm/YY H:M:S

timeout = 1 # 2 seconds
nt=[]
def Count(a):
    if len(nt)==0:
        nt.append(a)
        return a
    else:
        nt.append(nt[-1]+a)
        return nt[-1]
def doWork():
    #do work here
    #Count+=1
    #H  = httplib2.Http()
    now = datetime.now()
    resp = requests.get("https://www.xyz.in/", 'HEAD')
    Stat= resp.status_code
    Date= now.strftime("%d %H:%M:%S")
    Val=Count(1)
    print("will be running ",Val)
    conn.execute("INSERT INTO WebStatus VALUES (?, ?, ?)", (Val, Date, Stat))
    if Val%60==0:
        a=conn.execute('''Select * From WebStatus ORDER BY Count LIMIT 60''')
        df=pd.DataFrame(a,columns=['count','datetime','status'])
        df.plot(kind='line',x='datetime',y='status')
        plt.xticks(rotation=90)
        plt.savefig('image\Img2.png',dpi=600,bbox_inches='tight')
    conn.commit()
l = task.LoopingCall(doWork)
l.start(timeout) # call every sixty seconds
reactor.run()