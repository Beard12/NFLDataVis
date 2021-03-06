
from flask import Flask, request, render_template, session, redirect, Markup, flash, jsonify
import nflgame

app = Flask(__name__)
app.secret_key= 'thisismysecretkey'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/passing')
def passing():
	quarterbacks_over_time = dict()
	limit = 20
	for i in range(2009,2016):	
		season = nflgame.games(i)
		all_players = nflgame.combine_game_stats(season)
		qbs = all_players.passing().sort('passing_yds').limit(limit)
		qbslist = []
		for j in qbs:
			obj = dict()
			obj = {'name': j.name,'yards': j.passing_yds, 'tds': j.passing_tds}
			qbslist.append(obj)
		quarterbacks_over_time['pass' + str(i)] = qbslist

	return jsonify(**quarterbacks_over_time)

@app.route('/passvsrushbyyear')
def passvsrushbyyear():
	pass_vs_rush = dict()
	for i in range(2009,2016):
		season = nflgame.games(i)
		all_players = nflgame.combine_game_stats(season)
		sumofpass=0
		sumofrush=0
		sumofrushtds = 0
		sumofpasstds = 0
		obj = dict()
		for j in all_players:
			sumofrushtds += j.rushing_tds
			sumofpasstds += j.passing_tds
			sumofpass += j.passing_yds
			sumofrush += j.rushing_yds
		obj = {'pass': sumofpass, 'rush':sumofrush, 'rushtds': sumofrushtds, 'passtds': sumofpasstds}
		pass_vs_rush['passvsrush' + str(i)] = obj

	return jsonify(**pass_vs_rush)

@app.route('/playerover1000')
def playerover1000():
	player_over_1000 = dict()
	for i in range(2009, 2016):
		season = nflgame.games(i)
		all_players = nflgame.combine_game_stats(season)
		qbs_4000 = filter(lambda x: x.passing_yds > 4000, all_players)
		run_1000 = filter(lambda x: x.rushing_yds > 1000, all_players)
		rec_1000 = filter(lambda x: x.receiving_yds > 1000, all_players)
		sumofqbs = len(qbs_4000)
		sumofrun = len(run_1000)
		sumofrec = len(rec_1000)
		obj = {'qbs': sumofqbs, 'run': sumofrun, 'rec': sumofrec}
		player_over_1000['playercount' + str(i)] = obj
		#10,5,10,11,9,11,12
	return jsonify(**player_over_1000)

app.run(debug=True)