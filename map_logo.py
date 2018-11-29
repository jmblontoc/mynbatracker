
path = '/static/tracker/logos'

MAP = {
	'Atlanta': '%s/hawks.svg' % path,
	'Brooklyn': '%s/nets.svg' % path,
	'Boston': '%s/celtics.svg' % path,
	'Phoenix': '%s/suns.svg' % path,
	'Los Angeles': '%s/lakers.svg' % path,
	'Washington': '%s/wizards.svg' % path,
	'Golden State': '%s/warriors.svg' % path,
	'Chicago': '%s/bulls.svg' % path,
	'Orlando': '%s/magic.svg' % path,
	'Miami': '%s/heat.svg' % path,
	'LA': '%s/clippers.svg' % path,
	'Philadelphia': '%s/sixers.svg' % path,
	'Milwaukee': '%s/bucks.svg' % path,
	'Toronto': '%s/raptors.svg' % path,
	'Dallas': '%s/mavs.svg' % path,
	'Cleveland': '%s/cavs.svg' % path,
	'New York': '%s/knicks.svg' % path,
	'Houston': '%s/rockets.svg' % path,
	'Minnesota': '%s/wolves.svg' % path,
	'Memphis': '%s/grizzlies.svg' % path,
	'Oklahoma City': '%s/thunder.svg' % path,
	'Utah': '%s/jazz.svg' % path,
	'Denver': '%s/nuggets.svg' % path,
	'Portland': '%s/blazers.svg' % path,
	'San Antonio': '%s/spurs.svg' % path,
	'Detroit': '%s/pistons.svg' % path,
	'Charlotte': '%s/hornets.svg' % path,
	'New Orleans': '%s/pelicans.svg' % path,
	'Indiana': '%s/pacers.svg' % path,
	'Sacramento': '%s/kings.svg' % path,
}

CODE = {
	'ATL': 'Atlanta',
	'BKN': 'Brooklyn',
	'BOS': 'Boston',
	'PHX': 'Phoenix',
	'LAL': 'Los Angeles',
	'WSH': 'Washington',
	'GS': 'Golden State',
	'CHI': 'Chicago',
	'ORL': 'Orlando',
	'MIA': 'Miami',
	'LAC': 'LA',
	'PHI': 'Philadelphia',
	'TOR': 'Toronto',
	'DAL': 'Dallas',
	'CLE': 'Cleveland',
	'NY': 'New York',
	'HOU': 'Houston',
	'MIN': 'Minnesota',
	'OKC': 'Oklahoma City',
	'UTAH': 'Utah',
	'DEN': 'Denver',
	'POR': 'Portland',
	'SA': 'San Antonio',
	'DET': 'Detroit',
	'CHA': 'Charlotte',
	'NO': 'New Orleans',
	'IND': 'Indiana',
	'SAC': 'Sacramento',
	'MIL': 'Milwaukee',
	'MEM': 'Memphis'
}

def update_data(data):

	for item in data['game_data']:
		item['logo1'] = MAP[item['team1_name']]
		item['logo2'] = MAP[item['team2_name']]


def update_standings(standings):

	# east
	for team in standings['east_data']:
		city = team['name'].split(" ")[:-1]
		city = ' '.join(city)
		team['logo'] = MAP[city]

	# west
	for team in standings['west_data']:
		city = team['name'].split(" ")[:-1]
		city = ' '.join(city)

		# for PORTLAND ONLY
		if city == 'Portland Trail':
			city = 'Portland'

		team['logo'] = MAP[city]


