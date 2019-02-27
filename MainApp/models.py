from django.db import models

# Task 1: Create appropriate data models using Django ORM


class Metrics(models.Model):
	location = models.CharField(max_length = 50)
	metric = models.CharField(max_length = 50)

	def __str__(self):
		return self.location + ' has ' + self.metric

class MetricsValues(models.Model):
	metricsVal = models.ForeignKey(Metrics, on_delete = models.CASCADE)
	value = models.FloatField()
	date = models.DateField()

	def __str__(self):
		return "{} has {} of {} on {}".format(self.metricsVal.location ,
		 self.value, self.metricsVal.metric, self.date)

