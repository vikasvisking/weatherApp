from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime

#Task 3  Get request to show weaather details.
# format of url with parameters should be :- http://localhost:8000?startDate=1910-02&lastDate=2000-02&metric=Rainfall&location=England
@api_view(['GET'])
def getWeather(request):
	dictV = {}
	dictV['code'] = 200
	data = request.GET
	# get parameters 
	metric = data['metric']
	location = data['location']
	startDate = "{}-01".format(data['startDate'])
	lastdate = "{}-01".format(data['lastDate'])
     
    # filtering objects
	metricObj = Metrics.objects.filter(metric = metric, location = location)

	# if objects exists.
	if metricObj:		
		metricvalue = MetricsValues.objects.filter( date__range = [startDate , lastdate], metricsVal__in = metricObj)

		# calling serializer
		serializer = MetricsValuesSerializer(metricvalue,context = {'request' : request}, many = True).data
		weatherData = {}
		for obj in serializer:
			weatherData[obj['date']] = obj['value']
		dictV['weatherData'] = weatherData
	else:
		# if object not exist
		dictV['code'] = 404
		dictV['message'] = 'objects not found'
	return Response(dictV)
