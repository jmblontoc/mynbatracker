import logic
import win32com.client
import pyttsx3 as text_to_speech
from datetime import datetime

# init text to speech
engine = text_to_speech.init()

data = logic.get_data()
data = data['game_data']

def game_finished(game):

	return 'team1_score' in game


def talk(games):

	today = datetime.now().strftime("%A, %B %d %Y %I:%M%p")

	engine.say("NBA Updates as of %s" % today)
	engine.runAndWait()

	for game in games:

		matchup = '%s versus %s' % (game['team1_name'], game['team2_name'])
		engine.say(matchup)
		engine.runAndWait()

		if game_finished(game):

			final_score = '%s %s and %s %s' % (game['team1_name'], game['team1_score'], game['team2_name'], game['team2_score'])
			stats = '%s from %s finished with %s while %s from %s finished with %s' % (game['team1_pog'], game['team1_name'], game['team1_points'].replace('Pts', 'points'), game['team2_pog'], game['team2_name'], game['team2_points'].replace('Pts', 'points'))

			engine.say(final_score)
			engine.runAndWait()

			engine.say(stats)
			engine.runAndWait()

	engine.say("That's all as of now. Thank you")
	engine.runAndWait()


# # # # # 

talk(data)






