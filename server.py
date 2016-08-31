
from flask import Flask, request, render_template, session, redirect, Markup, flash
import nflgame

app = Flask(__name__)
app.secret_key= 'thisismysecretkey'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/make_table', methods = ['POST'])
def make_table():
	year = int(request.form['season'])
	limit = int(request.form['limit'])
	category = request.form['category']

	season = nflgame.games(year)
	all_players = nflgame.combine(season)

	if category == 'rushing_yds':
		stat = 'Rushing'
		players = all_players.rushing().sort(category).limit(limit)
	elif category == 'receiving_yds':
		stat = 'Receiving'
		players = all_players.receiving().sort(category).limit(limit)
	elif category == 'passing_yds':
		stat = 'Passing'
		players = all_players.passing().sort(category).limit(limit)	
	return render_template('index.html', players=players, stat=stat)
app.run(debug=True)