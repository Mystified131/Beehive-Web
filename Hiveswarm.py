#This code imports the necessary modules.

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from Hivebuilder import blobintophrases

import cgi, datetime, random

#This code configures the web app.

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mystified131:Jackson131!@mystified131.mysql.pythonanywhere-services.com/mystified131$HIVETotal'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'pgojaeopaiern'

#This code sets up the model for the database

class Beehive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String(120))
    phrase = db.Column(db.String(120))
    phrasecount = db.Column(db.Integer)

    def __init__(self, timestamp, phrase, phrasecount):
        self.timestamp = timestamp
        self.phrase = phrase
        self.phrasecount = phrasecount

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        textchunk = request.form["textchunk"]
        textchunk = cgi.escape(textchunk)
        phraseset = blobintophrases(textchunk)
        right_now = datetime.datetime.now().isoformat()
        lista = []
        for i in right_now:
            if i.isnumeric():
                lista.append(i)
            tim = "".join(lista)
        timestamp = tim

        for elem in phraseset:
            phrase = elem
            phrasecount = 1
            current = Beehive.query.filter_by(phrase=phrase).first()
            if current:
                current.phrasecount += 1
                db.session.commit()
            else:
                new_phrase = Beehive(timestamp, phrase, phrasecount)
                db.session.add(new_phrase)
                db.session.commit()

        return render_template('index.html')
    
    else:
        return render_template('index.html')

@app.route('/query', methods=['POST', 'GET'])
def query():
    if request.method == 'POST':
        quechunk = request.form["quechunk"]
        quechunk = cgi.escape(quechunk)
        quechunk = quechunk.lower()
        quelst = []
        queset = Beehive.query.all()
        for elem in queset:
            if quechunk in elem.phrase:
                newstr = str(elem.phrasecount) +  " times used: " +  elem.phrase 
                quelst.append(newstr)
        quelst.sort(reverse=True)
        
        return render_template('query.html', honey = quelst)

    else:

        return render_template('query.html')

    ## THE GHOST OF THE SHADOW ##
