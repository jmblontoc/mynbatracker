import logic
import win32com.client
import pyttsx3 as text_to_speech
from datetime import datetime
from random import randint

# init text to speech
engine = text_to_speech.init()
engine.setProperty('rate', 130)

data = logic.get_data()
data = data['game_data']

def game_finished(game):

	return 'team1_score' in game


# to give thrill while announcing the results
def randomize(game):

	annoucements = ['%s versus %s' % (game['team1_name'], game['team2_name']), '%s versus %s' % (game['team2_name'], game['team1_name'])]

	return annoucements[randint(0, len(annoucements) - 1)]


def get_winner(game):


	team1 = game['team1_name']
	team2 = game['team2_name']

	score1 = game['team1_score']
	score2 = game['team2_score']

	if score1 > score2:
		return team1

	if score2 > score1:
		return team2


def announce_winner(game):

	winner = get_winner(game)

	if winner == game['team1_name']:

		return '%s to %s %s' % (game['team1_score'], game['team2_score'], game['team1_name'])

	if winner == game['team2_name']:

		return '%s to %s %s' % (game['team2_score'], game['team1_score'], game['team2_name'])


def talk(games):

	today = datetime.now().strftime("%A, %B %d %Y %I:%M%p")

	engine.say("NBA Updates as of %s" % today)
	engine.runAndWait()

	for game in games:

		matchup = randomize(game)
		engine.say(matchup)
		engine.runAndWait()

		if game_finished(game):

			final_score = announce_winner(game)
			stats = '%s from %s finished with %s while %s from %s finished with %s' % (game['team1_pog'], game['team1_name'], game['team1_points'].replace('Pts', 'points'), game['team2_pog'], game['team2_name'], game['team2_points'].replace('Pts', 'points'))

			engine.say(final_score)
			engine.runAndWait()

			engine.say(stats)
			engine.runAndWait()

	engine.say("That's all as for now. Thank you")
	engine.runAndWait()


# # # # # 

talk(data)






