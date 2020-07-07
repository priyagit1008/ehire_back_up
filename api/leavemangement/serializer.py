from rest_framework import serializers

from libs.helpers import time_it

from accounts.models import User
from .models import  LeaveType,LeaveStatus,LeaveTracker



class LeavetrackerRequestSerializer(serializers.Serializer):
	"""
	LeaveCreateRequestSerializer
	"""
	
	user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),required=False)
	from_date = serializers.CharField(required=False)
	to_date = serializers.CharField(required=False)
	approved_date = serializers.CharField(required=True)
	total_leaves = serializers.CharField(required=True)
	leave_type = serializers.PrimaryKeyRelatedField(queryset=LeaveType.objects.all(),required=False)
	leave_status = serializers.PrimaryKeyRelatedField(queryset=LeaveStatus.objects.all(),required=False)
	discription = serializers.CharField(required=False)
	approved_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),required=False)

class Meta:
	models = LeaveTracker
	fields = ('id','user','from_date','to_date','approved_date','total_leaves','leave_type','Leave_status','discription',
			  'approved_by')

	def  create(self,validated_data):
		Leave_tracker= LeaveTracker.objects.create(**validated_data)
		return Leave_tracker


class LeavetrackerListSerializer(serializers.Serializer):

	class Meta:
		models = LeaveTracker
		fields = '__all__'



class LeaveTypeRequestSerializer(serializers.Serializer):
	available_leaves = serializers.CharField(required=False)

	class Meta:
		models = LeaveType
		fields = ('id','available_leaves')

		def create(self,validated_data):
			leavetype=LeaveType.objects.create(**validated_data)
			return leavetype


	class LeaveTypeListSerializer(serializers.Serializer):

		class Meta:
			models = LeaveType
			fields = '__all__'


class LeaveStatusRequestSerializer(serializers.Serializer):
	leave_status = serializers.CharField(required=True) 
	discription = serializers.CharField(required=True) 
	last_updater = serializers.CharField(required=True)

	class Meta:
		models = LeaveStatus
		fields ='__all__' 

	def create(self,validated_data):
		leavestatus=LeaveStatus.objects.create(**validated_data)
		return Leavestatus


	class LeaveStatusListSerializer(serializers.Serializer):

		class Meta:
			models = LeaveType
			fields = '__all__'




