from rest_framework import serializers

from libs.helpers import time_it

from accounts.models import User
from .models import  LeaveType,LeaveTracker



class LeavetrackerRequestSerializer(serializers.Serializer):
	"""
	LeaveCreateRequestSerializer
	"""
	
	user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),required=False)
	from_date = serializers.DateField(input_formats=['%d-%m-%Y',],required=False)
	to_date = serializers.DateField(input_formats=['%d-%m-%Y',],required=False)
	approved_date = serializers.DateField(input_formats=['%d-%m-%Y',],required=True)
	total_leaves = serializers.CharField(required=True)
	leave_type = serializers.PrimaryKeyRelatedField(queryset=LeaveType.objects.all(),required=False)
	leave_status = serializers.CharField(required=False)
	discription = serializers.CharField(required=False)
	approved_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),required=False)


	class Meta:
		models = LeaveTracker
		# fields='__all__'
		fields = ('id','user','from_date','to_date','approved_date','total_leaves','leave_type','Leave_status','discription',
		        'approved_by')


	def  create(self,validated_data):
		Leave_tracker= LeaveTracker.objects.create(**validated_data)
		Leave_tracker.save()
		return Leave_tracker


class LeavetrackerListSerializer(serializers.Serializer):

	class Meta:
		models = LeaveTracker
		fields = ('id','user','from_date','to_date','approved_date','total_leaves','leave_type','Leave_status','discription',
		        'approved_by')


class LeaveTypeRequestSerializer(serializers.Serializer):
	leave_type=serializers.CharField(required=False)
	available_leaves = serializers.IntegerField(required=False)

	class Meta:
		model = LeaveType
		# fields =('id','leave_status','discription','last_updater') 
		fields ='__all__'

	def create(self,validated_data):
		leavestype=LeaveType.objects.create(**validated_data)
		leavestype.save()
		return leavestype


class LeaveTypeListSerializer(serializers.Serializer):

	class Meta:
		models = LeaveType
		fields = ('available_leaves','id','leave_type')
		# fields = '__all__'


# class LeaveStatusRequestSerializer(serializers.Serializer):
# 	leave_status = serializers.CharField(required=True) 
# 	discription = serializers.CharField(required=True) 
# 	last_updater = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),required=False)

# 	class Meta:
# 		models = LeaveStatus
# 		fields =('id','leave_status','discription','last_updater') 

# 	def create(self,validated_data):
# 		leavestatus=LeaveStatus.objects.create(**validated_data)
# 		leavestatus.save()
# 		return leavestatus

# class LeaveStatusListSerializer(serializers.Serializer):

# 	class Meta:
# 		models = LeaveType
# 		fields = '__all__'




