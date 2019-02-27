from .models import *
from .serializers import *
import json
import urllib
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime



# Task:2 create the objects from the Url
@api_view()
def storeWeatherData(request):
	dictV = {}
	metrics = ['Tmax' , 'Tmin', 'Rainfall' ]
	locations = ['UK', 'England', 'Scotland', 'Wales']
	for location in locations:
		for metric in metrics:

			# check if object already exist

			metricObjs = Metrics.objects.filter(metric = metric ,location = location)
			if not metricObjs:

				#if Metrics object does not exist, create metricObj
				metricObj = Metrics.objects.create(metric = metric ,location = location)

				# fetch data from url and convert it to valid python type format.
				url = "https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/{metric}-{location}.json".format(metric = metric, location = location)
				r = urllib.request.urlopen(url)
				jsonOutput = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
				for obj in jsonOutput:

					# give the valid format for date
					date = datetime(year = int(obj['year']) , month = int(obj['month']) , day = 1)

					# create MetricsValues obj
					MetricsValues.objects.create(metricsVal = metricObj, value = obj['value'], date = date)
				dictV['code'] = 200
				dictV['message'] = 'Objects Created Successfull'
			else:

				#if Metrics objects exist send error responce
				dictV['code'] = 403
				dictV['message'] = 'Data of {metric} at {location} already exist'.format(metric= metric , location = location )
				
	return Response(dictV)



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





			

			

