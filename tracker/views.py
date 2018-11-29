from django.shortcuts import render
import logic, map_logo
from datetime import datetime

# Create your views here.
def index(request):

	context = {
		'data': logic.get_data(),
		'standings': logic.get_standings(),
		'today': datetime.now()
	}

	map_logo.update_data(context['data'])
	map_logo.update_standings(context['standings'])

	return render(request, 'tracker/index.html', context)
