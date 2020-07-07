from django.shortcuts import render
from libs.helpers import time_it

# Create your views here.
from django.conf import settings
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# from accounts.users.permissions import HiroolReadOnly, HiroolReadWrit

# project level imports
from libs.constants import (
	BAD_REQUEST,
	BAD_ACTION,
)

from libs.exceptions import ParseException
# app level imports
from .models import  LeaveType,LeaveStatus,LeaveTracker

# project level imports
from accounts.models import User

from .serializers import (
	LeavetrackerRequestSerializer,
	LeavetrackerListSerializer,
	LeaveTypeRequestSerializer,
	LeaveTypeListSerializer,
	LeaveStatusRequestSerializer,
	LeaveStatusListSerializer

	)

from .service import LeaveTrackerServices
from .service import LeaveType_Services

from .service import LeaveStatus_Services






class LeaveTrackerViewSet(GenericViewSet):
	"""docstring for interview"""

	services = LeaveTrackerServices()

	# queryset = services.get_queryset()

	filter_backends = (filters.OrderingFilter,)
	authentication_classes = (TokenAuthentication,)

	ordering_fields = ('id',)
	ordering = ('id',)
	lookup_field = 'id'
	http_method_names = ['get', 'post', 'put']

	serializers_dict = {
		'add_leave': LeavetrackerRequestSerializer,
		'get_leave': LeavetrackerListSerializer,
		'leave_list':LeavetrackerListSerializer,

	}

	def get_serializer_class(self):
		"""
		:return:
		"""
		try:
			return self.serializers_dict[self.action]
		except KeyError as key:
			raise ParseException(BAD_ACTION, errors=key)

	@action(methods=['post'], detail=False, permission_classes=[IsAuthenticated, ], )
	def add_leave(self, request):

		serializer = self.get_serializer(data=request.data)
		if serializer.is_valid() is False:
			raise ParseException(BAD_REQUEST, serializer.errors)

		Leave_tracker = serializer.create(serializer.validated_data)
		if Leave_tracker:
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response({"status": "error"}, status.HTTP_404_NOT_FOUND)



	@action(methods=['get', 'patch'], detail=False, permission_classes=[IsAuthenticated, ], )
	def get_leave(self, request):
		"""
		Return client profile data and groups
		"""
		try:
			id= request.GET.get('id', None)
			if not id:
				return Response({"status": "Failed", "message":"id is required"})
			else:
				serializer = self.get_serializer(self.services.get_leave_service(id))
				return Response(serializer.data, status.HTTP_200_OK)
		except Exception as e:
			return Response({"status": "Not Found"}, status.HTTP_404_NOT_FOUND)


	@action(methods=['get'], detail=False, permission_classes=[IsAuthenticated,], )
	def leave_list(self, request, **dict):
		try:
			filter_data = request.query_params.dict()
			serializer = self.get_serializer(self.services.leave_filter_service(filter_data), many=True)
			return Response(serializer.data, status.HTTP_200_OK)
		except Exception as e:
			raise
			return Response({"status": "Not Found"}, status.HTTP_404_NOT_FOUND)





class LeaveTypeViewSet(GenericViewSet):
	"""docstring for interview"""

	services = LeaveType_Services()

	# queryset = services.get_queryset()

	filter_backends = (filters.OrderingFilter,)
	authentication_classes = (TokenAuthentication,)

	ordering_fields = ('id',)
	ordering = ('id',)
	lookup_field = 'id'
	http_method_names = ['get', 'post', 'put']

	serializers_dict = {
		'add_leavetype': LeaveTypeRequestSerializer,
		'get_leavetype': LeaveTypeListSerializer,
		'leavetype_list':LeaveTypeListSerializer,

	}

	def get_serializer_class(self):
		"""
		:return:
		"""
		try:
			return self.serializers_dict[self.action]
		except KeyError as key:
			raise ParseException(BAD_ACTION, errors=key)

	@action(methods=['post'], detail=False, permission_classes=[IsAuthenticated, ], )
	def add_leavetype(self, request):

		serializer = self.get_serializer(data=request.data)
		if serializer.is_valid() is False:
			raise ParseException(BAD_REQUEST, serializer.errors)

		leavetype = serializer.create(serializer.validated_data)
		if leavetype:
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response({"status": "error"}, status.HTTP_404_NOT_FOUND)



	@action(methods=['get', 'patch'], detail=False, permission_classes=[IsAuthenticated, ], )
	def get_leavetype(self, request):
		"""
		Return client profile data and groups
		"""
		try:
			id= request.GET.get('id', None)
			if not id:
				return Response({"status": "Failed", "message":"id is required"})
			else:
				serializer = self.get_serializer(self.services.get_leavetype_service(id))
				return Response(serializer.data, status.HTTP_200_OK)
		except Exception as e:
			return Response({"status": "Not Found"}, status.HTTP_404_NOT_FOUND)


	@action(methods=['get'], detail=False, permission_classes=[IsAuthenticated,], )
	def leavetype_list(self, request, **dict):
		try:
			filter_data = request.query_params.dict()
			serializer = self.get_serializer(self.services.LeaveType_filter_service(filter_data), many=True)
			return Response(serializer.data, status.HTTP_200_OK)
		except Exception as e:
			raise
			return Response({"status": "Not Found"}, status.HTTP_404_NOT_FOUND)



class LeaveStatusViewSet(GenericViewSet):
	"""docstring for interview"""

	services = LeaveStatus_Services()

	# queryset = services.get_queryset()

	filter_backends = (filters.OrderingFilter,)
	authentication_classes = (TokenAuthentication,)

	ordering_fields = ('id',)
	ordering = ('id',)
	lookup_field = 'id'
	http_method_names = ['get', 'post', 'put']

	serializers_dict = {
		'add_leavesatus': LeaveStatusRequestSerializer,
		'get_leavesatus': LeaveStatusListSerializer,
		'leavesatus_list':LeaveStatusListSerializer,

	}

	def get_serializer_class(self):
		"""
		:return:
		"""
		try:
			return self.serializers_dict[self.action]
		except KeyError as key:
			raise ParseException(BAD_ACTION, errors=key)

	@action(methods=['post'], detail=False, permission_classes=[IsAuthenticated, ], )
	def add_leavesatus(self, request):

		serializer = self.get_serializer(data=request.data)
		if serializer.is_valid() is False:
			raise ParseException(BAD_REQUEST, serializer.errors)

		leavestatus = serializer.create(serializer.validated_data)
		if leavestatus:
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response({"status": "error"}, status.HTTP_404_NOT_FOUND)



	@action(methods=['get', 'patch'], detail=False, permission_classes=[IsAuthenticated, ], )
	def get_leavesatus(self, request):
		"""
		Return client profile data and groups
		"""
		try:
			id= request.GET.get('id', None)
			if not id:
				return Response({"status": "Failed", "message":"id is required"})
			else:
				serializer = self.get_serializer(self.services.get_leavestatus_service(id))
				return Response(serializer.data, status.HTTP_200_OK)
		except Exception as e:
			return Response({"status": "Not Found"}, status.HTTP_404_NOT_FOUND)


	@action(methods=['get'], detail=False, permission_classes=[IsAuthenticated,], )
	def leavesatus_list(self, request, **dict):
		try:
			filter_data = request.query_params.dict()
			serializer = self.get_serializer(self.services.LeaveStatus_filter_service(filter_data), many=True)
			return Response(serializer.data, status.HTTP_200_OK)
		except Exception as e:
			raise
			return Response({"status": "Not Found"}, status.HTTP_404_NOT_FOUND)





