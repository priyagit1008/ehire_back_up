
# Create your models here.
# python imports
import uuid
# django rest_framwork imports
from django.db import models
# project level imports
from libs.models import TimeStampedModel
# from accounts.users.models import User
from accounts.models import User

# third party imports
from model_utils import Choices
from django.contrib.postgres.fields import JSONField


class LeaveType(TimeStampedModel):
	LEAVE_TYPE = Choices(
		('Planned', 'PLANNED'),
		('Emergancy', 'EMERGANCY'),
		('Sick', 'SICK'),
	)
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	available_leaves = models.IntegerField()



class LeaveStatus(TimeStampedModel):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	leave_status = models.CharField(
		max_length=256,
		unique=True,
		blank=False
		)
	discription = models.TextField(blank=True)
	last_updater = models.ForeignKey(User,on_delete=models.PROTECT, limit_choices_to={'is_staff': True})

	

	
class  LeaveTracker(TimeStampedModel):
	id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
	user = models.ForeignKey(User,on_delete=models.PROTECT)
	leave_type = models.ForeignKey(LeaveType,on_delete=models.PROTECT)
	leave_status = models.ForeignKey(LeaveStatus,on_delete=models.PROTECT)
	from_date = models.DateField()
	to_date = models.DateField()
	approved_date =models.DateField(blank=True,null=True)
	total_leaves = models.IntegerField(default=1)
	discription = models.TextField(max_length=250,blank=True)
	approved_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name = 'approved_by',blank=True)

	def modify(self, payload):
		"""
		This method will update tasks attributes
		"""
		for key, value in payload.items():
			setattr(self, key, value)
		self.save()

	class Meta:
		app_label = 'leave_management'
		db_table = 'api_tracker'

