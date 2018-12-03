import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime
import map_logo

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
today = datetime.now().date()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# this will return the container containing the games for today
def get_current_container(dates):

	month = get_month(today.month)

	for h2 in dates:

		# do the date processing here
		temp_string = h2.contents[0]
		header_date = temp_string.split(",")[1].strip()
		
		current_date_str = '%s %s' % (month, str(today.day))

		if current_date_str == header_date:
			return h2.next_sibling

	return None


# gets the month in English
def get_month(month_now):

	return MONTHS[month_now - 1]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# this will be returned once all the data has been scraped

def get_data():
	main_context = {}

	url = 'http://tv5.espn.com/nba/fixtures'

	request = urllib.request.Request(url)
	response = urllib.request.urlopen(request)
	response_data = response.read()

	soup = BeautifulSoup(response_data, 'html.parser')

	# this is the main container
	main_div = soup.find_all('div', id='sched-container')[0]


	# get all the dates via h2's
	dates = list(main_div.find_all('h2'))

	current_container = get_current_container(dates)

	# process the current container
	table = current_container.contents[0]

	# get data
	game_list = list(table.tbody.children)

	game_data = []
	for game in game_list:

		td = list(game.children)
		# if game is not yet starting?

		per_game_data = {}

		if not len(td[2].a.contents) == 0:

			score = td[2].a.contents[0]

			split_score = score.split(",")

			if not len(split_score) == 1:

				team1 = split_score[0]
				team2 = split_score[1].strip()

				scores1 = td[3].contents
				scores2 = td[4].contents

				per_game_data['team1_name'] = map_logo.CODE[team1.split(" ")[0]]
				per_game_data['team2_name'] = map_logo.CODE[team2.split(" ")[0]]
				per_game_data['team1_score'] = int(team1.split(" ")[1])
				per_game_data['team2_score'] = int(team2.split(" ")[1])

				per_game_data['team1_pog'] = scores1[0].contents[0]
				per_game_data['team2_pog'] = scores2[0].contents[0]

				per_game_data['team1_points'] = scores1[1].strip()
				per_game_data['team2_points'] = scores2[1].strip()


			else:
				per_game_data['team1_name'] = td[0].span.contents[0]
				per_game_data['team2_name'] = td[1].span.contents[0]

		else:
			team1_name = td[0].span
			team2_name = td[1].span

			per_game_data['team1_name'] = team1_name.contents[0]
			per_game_data['team2_name'] = team2_name.contents[0]

		game_data.append(per_game_data)


	# for partially finished games for the day
	if not current_container.next_sibling.name == 'h2':

		next_table = current_container.next_sibling.contents[0]
		partial_game_list = list(next_table.children)[1:]


		for game in partial_game_list:

			td = list(game.children)

			per_game_data = {}

			# if game is not yet starting?

			if not len(td[2].a.contents) == 0:

				score = td[2].a.contents[0]

				split_score = score.split(",")

				scores1 = td[3].contents
				scores2 = td[4].contents

				if not len(split_score) == 1:

					team1 = split_score[0]
					team2 = split_score[1].strip()

					per_game_data['team1_name'] = map_logo.CODE[team1.split(" ")[0]]
					per_game_data['team2_name'] = map_logo.CODE[team2.split(" ")[0]]
					per_game_data['team1_score'] = int(team1.split(" ")[1])
					per_game_data['team2_score'] = int(team2.split(" ")[1])

					per_game_data['team1_pog'] = scores1[0].contents[0]
					per_game_data['team2_pog'] = scores2[0].contents[0]

					per_game_data['team1_points'] = scores1[1].strip()
					per_game_data['team2_points'] = scores2[1].strip()

			game_data.append(per_game_data)

	main_context['game_data'] = [data for data in game_data if len(data) > 0]

	return main_context
	

def get_standings():

	main_standings = {}

	url = 'http://tv5.espn.com/nba/table'

	request = urllib.request.Request(url)
	response = urllib.request.urlopen(request)
	response_data = response.read()

	soup = BeautifulSoup(response_data, 'html.parser')
	tables = soup.find_all('table', attrs={"class": "Table2__table__wrapper"})

	# Eastern Conference
	east_table = tables[0]

	east_data = []
	east_teams_list = list(list(list(east_table.tbody.tr.children)[0].children)[0].contents[2].children)

	records_list = list(east_table.tbody.tr.children)[1].contents[0].contents[0].contents[1]
	records_list = list(records_list.contents[0].tbody.tr.children)[0].contents[0]
	records_list = records_list.find_all("tbody")[0]
	records_list = list(records_list.children)
	
	for index, team in enumerate(east_teams_list):

		team_data = {}

		team_name = team.contents[0].find_all('span', attrs={"class": "hide-mobile"})[0].contents[0].contents[0]
		team_data['name'] = team_name

		team_data['wins'] = list(records_list[index].children)[0].contents[0].contents[0]
		team_data['losses'] = list(records_list[index].children)[1].contents[0].contents[0]
		team_data['streak'] = list(records_list[index].children)[11].contents[0].contents[0]

		east_data.append(team_data)

	main_standings['east_data'] = east_data

	# Western Conference
	west_table = tables[1]

	west_data = []

	west_teams_list = list(list(list(west_table.tbody.tr.children)[0].children)[0].contents[2].children)

	records_list = list(west_table.tbody.tr.children)[1].contents[0].contents[0].contents[1]
	records_list = list(records_list.contents[0].tbody.tr.children)[0].contents[0]
	records_list = records_list.find_all("tbody")[0]
	records_list = list(records_list.children)
	
	for index, team in enumerate(west_teams_list):

		team_data = {}

		team_name = team.contents[0].find_all('span', attrs={"class": "hide-mobile"})[0].contents[0].contents[0]
		team_data['name'] = team_name

		team_data['wins'] = list(records_list[index].children)[0].contents[0].contents[0]
		team_data['losses'] = list(records_list[index].children)[1].contents[0].contents[0]
		team_data['streak'] = list(records_list[index].children)[11].contents[0].contents[0]

		west_data.append(team_data)

	main_standings['west_data'] = west_data

	return main_standings




























