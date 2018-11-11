#This code imports the necessary modules.

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from Hivebuilder import blobintophrases

import cgi, datetime

#This code configures the web app.

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mystified131:Jackson131!@mystified131.mysql.pythonanywhere-services.com/mystified131$beehive'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'pgojaeopaiern'

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

#This code defines the main page, where users can submit text to the database.

@app.route('/', methods=['POST', 'GET'])
def indexb():
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
                current.actcount += 1
                db.session.commit()
            else:
                beeall = Beehive.query.all()
                num1 = len(beeall)
                id = num1
                quecount = 0
                actcount = 1
                new_phrase = Beehive(id, timestamp, phrase, phrasecount, quecount, actcount)
                db.session.add(new_phrase)

        db.session.commit()

        return render_template('indexb.html')

    else:
        return render_template('indexb.html')

#This code defines the query page, where users can see if certain pieces of text are in the database.

@app.route('/query', methods=['POST', 'GET'])
def query():
    if request.method == 'POST':
        quechunk = request.form["quechunk"]
        quechunk = cgi.escape(quechunk)
        quechunk = quechunk.lower()
        quechunk2 = request.form["quechunk2"]
        quechunk2 = cgi.escape(quechunk2)
        quechunk2 = quechunk2.lower()
        quelst = []
        queset = Beehive.query.all()
        for elem in queset:
            if quechunk in elem.phrase and quechunk2 in elem.phrase:
                newstr = str(elem.actcount) +  " Total activity / " + str(elem.phrasecount) +  " Times entered / " +  str(elem.quecount) +  " Times queried: " + elem.phrase
                error = ""
                elem.quecount += 1
                elem.actcount += 1
                quelst.append(newstr)

            if not quelst:
                error = "No results found. Please try again."

        db.session.commit()
        quelst.sort(reverse=True)

        return render_template('query.html', honey = quelst, error = error)

    else:

        return render_template('query.html')

    ## THE GHOST OF THE SHADOW ##