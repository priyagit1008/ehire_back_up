from rest_framework import serializers

from libs.helpers import time_it

from accounts.models import User
from .models import  LeaveType,LeaveTracker



class LeavetrackerRequestSerializer(serializers.Serializer):
	"""
	LeaveCreateRequestSerializer
	"""
	
	user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),required=True)
	from_date = serializers.DateField(input_formats=['%d-%m-%Y',],required=True)
	to_date = serializers.DateField(input_formats=['%d-%m-%Y',],required=True)
	approved_date = serializers.DateField(input_formats=['%d-%m-%Y',],required=False)
	total_leaves = serializers.CharField(required=False)
	leave_type = serializers.PrimaryKeyRelatedField(queryset=LeaveType.objects.all(),required=True)
	leave_status = serializers.CharField(required=False)
	discription = serializers.CharField(required=False)
	approved_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),required=False)


	class Meta:
		models = LeaveTracker
		# fields='__all__'
		fields = ('id','user','from_date','to_date','approved_date','total_leaves','leave_type','leave_status','discription',
				'approved_by')


	def  create(self,validated_data):
		Leave_tracker= LeaveTracker.objects.create(**validated_data)
		Leave_tracker.save()
		return Leave_tracker


class LeavestatusDrowpdownGetSerializer(serializers.ModelSerializer):
	value = serializers.CharField(source='leave_status',required=True, min_length=2)
	label = serializers.CharField(source='leave_status',required=True, min_length=2)
	leavestatus_id=serializers.CharField(source='id',required=True)

	class Meta:
		model = LeaveType
		fields = ('leavestatus_id','value','label')



class UserGetSerializer(serializers.ModelSerializer):

	full_name = serializers.SerializerMethodField()

	def get_full_name(self, obj):
		return '{} {}'.format(obj.first_name, obj.last_name)

	class Meta:

		model = User
		# fields ='__all__'
		fields= ('id','full_name')

class LeavetrackerListSerializer(serializers.ModelSerializer):
	user = UserGetSerializer()
	approved_by=UserGetSerializer()
	class Meta:
		model= LeaveTracker
		fields=('id','user','from_date','to_date','approved_date','total_leaves','leave_type','leave_status','discription',
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




class LeaveTypeListSerializer(serializers.ModelSerializer):

	class Meta:
		model= LeaveType
		fields= '__all__'



class LeaveTypeDrowpdownGetSerializer(serializers.ModelSerializer):
	value = serializers.CharField(source='leave_type',required=True, min_length=2)
	label = serializers.CharField(source='leave_type',required=True, min_length=2)
	leavetype_id=serializers.CharField(source='id',required=True)

	class Meta:
		model = LeaveType
		fields = ('leavetype_id','value','label')

		# fields = '__all__'


# class LeaveStatusRequestSerializer(serializers.Serializer):
#   leave_status = serializers.CharField(required=True) 
#   discription = serializers.CharField(required=True) 
#   last_updater = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),required=False)

#   class Meta:
#       models = LeaveStatus
#       fields =('id','leave_status','discription','last_updater') 

#   def create(self,validated_data):
#       leavestatus=LeaveStatus.objects.create(**validated_data)
#       leavestatus.save()
#       return leavestatus

# class LeaveStatusListSerializer(serializers.Serializer):

#   class Meta:
#       models = LeaveType
#       fields = '__all__'




