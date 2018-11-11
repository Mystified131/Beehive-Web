#This code imports the necessary modules.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

#This code configures the web app.

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mystified131:Jackson131!@mystified131.mysql.pythonanywhere-services.com/mystified131$beehive'
db = SQLAlchemy(app)
app.secret_key = 'noipaegojpg'

#This code sets up the model for the database.

class Beehive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String(120))
    phrase = db.Column(db.String(120))
    phrasecount = db.Column(db.Integer)
    quecount = db.Column(db.Integer)
    actcount = db.Column(db.Integer)

    def __init__(self, id, timestamp, phrase, phrasecount, quecount, actcount):
        self.id = id
        self.timestamp = timestamp
        self.phrase = phrase
        self.phrasecount = phrasecount
        self.quecount = quecount
        self.actcount = actcount

#This code queries the database and sets up the report.

right_now = datetime.datetime.now().isoformat()

totaldata = []
totphr = 0
totque = 0
totact = 0

allrows = []
topfifty = []
totaldata = Beehive.query.all()
totrow = len(totaldata)
for elem in totaldata:
    totphr += elem.phrasecount
    totque += elem.quecount
    totact += elem.actcount
    curcount = str(elem.actcount)

    allrows.append(curcount + " total activity: " + elem.phrase)

stotrow = str(totrow)
stotphr = str(totphr)
stotque = str(totque)
stotact = str(totact)

allrows.sort(reverse=True)
for x in range(50):
    topfifty.append(allrows[x])

#This code writes the report data to text files and saves them.

outstr = ""

filnm = "HIVE_Use_Report_Log_" + right_now +".txt"

outfile = open(filnm, "w")

outfile.write('Beehive Application Use Report Log (As of 11/11/2018, 8:00 am Central US time):'  + '\n')
outfile.write('\n')
outfile.write('Report created at: ' + right_now  + '\n')
outfile.write('\n')

outfile.write('Total rows in database: ' + stotrow + '\n')
outfile.write('Total phrases added in database: ' + stotphr + '\n')
outfile.write('Total query hits made on database: ' + stotque + '\n')
outfile.write('Total phrases added and query hits in database: ' + stotact + '\n')
outfile.write('\n')

for y in range(50):
    outstr = topfifty[y]
    yz = str(y + 1)
    outfile.write(yz + ': ' + outstr + '\n')

outfile.close()

outstr = ""

## THE GHOST OF THE SHADOW ##