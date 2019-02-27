from rest_framework import serializers
from .models import *
from datetime import datetime


# Metric Value Model Serializer

class MetricsValuesSerializer(serializers.ModelSerializer):
	date = serializers.SerializerMethodField()
	class Meta:
		model = MetricsValues
		fields	 = ('value' , 'date')

	def get_date(self,obj):
		dateobj = datetime.strptime(str(obj.date), '%Y-%m-%d')
		date = '{}-{:02d}'.format(dateobj.year, dateobj.month)
		return date

