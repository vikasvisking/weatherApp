
# Task:2 create the objects from the Url

from django.core.management.base import BaseCommand
import json
import urllib
from MainApp.models import *
from datetime import datetime

class Command(BaseCommand):


	def handle(self, *args, **kwargs):
		dictV = {}
		metrics = ['Tmax' , 'Tmin', 'Rainfall' ]
		locations = ['UK', 'England', 'Scotland', 'Wales']
		for location in locations:
			for metric in metrics:

				# check if object already exist

				metricObjs = Metrics.objects.filter(metric = metric ,location = location)
				if metricObjs:
					#if Metrics objects exist send error responce\
					dictV['message'] = 'Oops! Data already exist'				
					
				else:
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
						dictV['message'] = 'Objects Created Successfull'
					Objs = 'objects of {}:{} is created'.format(metric,location)
					print(Objs)
				
		print(dictV['message'])
