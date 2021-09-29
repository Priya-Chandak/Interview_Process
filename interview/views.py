from django.shortcuts import render
from . models import Degree,Subject,Employee, Schedule_Interview,Documents, Offer_Letter, Account_Setup,Project_Allocation,Leave_Management,Salary_Account,Attendance,Resignation,Experiance_Letter
from .serializers import EmployeeSerializer, DegreeSerializer, SubjectSerializer, InterviewSerializer, OfferLetterSerializer ,DocumentSerializer,AccountSetupSerializer, ProjectAllocationSerializer, LeaveSerializer, SalaryAccountSerializer, AttendanceSerializer, ResignationSerializer, ExperianceLetterSerializer
from django.db.models.query import QuerySet 
from rest_framework import generics
from rest_framework.views import APIView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class EmployeeView(APIView):

    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer


    def get(self, request, id, format=None):
        try:
            item = Employee.objects.get(pk=id)
            serializer = EmployeeSerializer(item)
            return Response(serializer.data)
        except Employee.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Employee.objects.get(pk=id)
        except Employee.DoesNotExist:
            return Response(status=404)
        serializer = EmployeeSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Employee.objects.get(pk=id)
        except Employee.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)

    
class EmployeeListView(APIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

    def get(self, request, format=None):
        item = Employee.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(item, request)
        serializer = EmployeeSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class DegreeView(APIView):

    queryset=Degree.objects.all()
    serializer_class=DegreeSerializer

    def get(self, request, id, format=None):
        try:
            item = Degree.objects.get(pk=id)
            serializer = DegreeSerializer(item)
            return Response(serializer.data)
        except Employee.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Degree.objects.get(pk=id)
        except Degree.DoesNotExist:
            return Response(status=404)
        serializer = DegreeSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Degree.objects.get(pk=id)
        except Degree.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)

    
class DegreeListView(APIView):
    queryset=Degree.objects.all()
    serializer_class=DegreeSerializer

    def get(self, request, format=None):
        item = Degree.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(item, request)
        serializer = DegreeSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = DegreeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class SubjectView(APIView):

    queryset=Subject.objects.all()
    serializer_class=SubjectSerializer


    def get(self, request, id, format=None):
        try:
            item = Subject.objects.get(pk=id)
            serializer = SubjectSerializer(item)
            return Response(serializer.data)
        except Subject.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Subject.objects.get(pk=id)
        except Subject.DoesNotExist:
            return Response(status=404)
        serializer = SubjectSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Subject.objects.get(pk=id)
        except Subject.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)

    
class SubjectListView(APIView):
    queryset=Subject.objects.all()
    serializer_class=SubjectSerializer

    def get(self, request, format=None):
        item = Subject.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(item, request)
        serializer = SubjectSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = SubjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class InterviewScheduleView(APIView):

    queryset=Schedule_Interview.objects.all()
    serializer_class=InterviewSerializer


    def get(self, request, id, format=None):
        try:
            item = Schedule_Interview.objects.get(pk=id)
            serializer = InterviewSerializer(item)
            return Response(serializer.data)
        except Schedule_Interview.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Schedule_Interview.objects.get(pk=id)
        except Schedule_Interview.DoesNotExist:
            return Response(status=404)
        serializer = InterviewSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Schedule_Interview.objects.get(pk=id)
        except Schedule_Interview.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)

class InterviewScheduleListView(APIView):
    queryset=Schedule_Interview.objects.all()
    serializer_class=InterviewSerializer

    def get(self, request, format=None):
        item = Schedule_Interview.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(item, request)
        serializer = InterviewSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = InterviewSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class DocumentView(APIView):
    queryset=Documents.objects.all()
    serializer_class=DocumentSerializer

class DocumentListView(APIView):
    queryset=Documents.objects.all()
    serializer_class=DocumentSerializer


class OfferLetterView(APIView):

    queryset=Offer_Letter.objects.all()
    serializer_class=OfferLetterSerializer


    def get(self, request, id, format=None):
        try:
            item = Offer_Letter.objects.get(pk=id)
            serializer = OfferLetterSerializer(item)
            return Response(serializer.data)
        except Offer_Letter.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Offer_Letter.objects.get(pk=id)
        except Offer_Letter.DoesNotExist:
            return Response(status=404)
        serializer = OfferLetterSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Offer_Letter.objects.get(pk=id)
        except Offer_Letter.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)

class OfferLetterListView(APIView):
    queryset=Offer_Letter.objects.all()
    serializer_class=OfferLetterSerializer

    def get(self, request, format=None):
        item = Offer_Letter.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(item, request)
        serializer = OfferLetterSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = OfferLetterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AccountSetupView(APIView):
    queryset=Account_Setup.objects.all()
    serializer_class=AccountSetupSerializer


    def get(self,request,id,Format=None):
        try:
            item=Account_Setup.objects.get(pk=id)
            serializer=AccountSetupSerializer(item)
            return Response(serializer.data)
        except Account_Setup.DoesNotExist:
            return Response(status=404)

    def put(self,request,id,Format=None):
        try:
            item=Account_Setup.objects.get(pk=id) 
        except Account_Setup.DoesNotExist:
            return Response(status=404)

        serializer=AccountSetupSerializer(item,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)

    def delete(self,request,id,Format=None):
        try:
            item=Account_Setup.objects.get(pk=id)
        except Account_Setup.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)
    
class AccountSetupListView(APIView):
    queryset=Account_Setup.objects.all()
    serializer_class=AccountSetupSerializer

    def get(self,request,Format=None):
        item=Account_Setup.objects.order_by('pk')
        paginator=PageNumberPagination()
        result_page=paginator.paginate_queryset(item,request)
        serializer=AccountSetupSerializer(result_page,many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self,request,Format=None):
        serializer = AccountSetupSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
	


class ProjectAllocationView(APIView):
    queryset=Project_Allocation.objects.all()
    serializer_class=ProjectAllocationSerializer


    def get(self,request,id,Format=None):
        try:
            item=Project_Allocation.objects.get(pk=id)
            serializer=ProjectAllocationSerializer(item)
            return Response(serializer.data)
        except Account_Setup.DoesNotExist:
            return Response(status=404)

    def put(self,request,id,Format=None):
        try:
            item=Project_Allocation.objects.get(pk=id) 
        except Project_Allocation.DoesNotExist:
            return Response(status=404)

        serializer=ProjectAllocationSerializer(item,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)

    def delete(self,request,id,Format=None):
        try:
            item=Project_Allocation.objects.get(pk=id)
        except Project_Allocation.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)
    
class ProjectAllocationListView(APIView):
    queryset=Project_Allocation.objects.all()
    serilaizer_class=ProjectAllocationSerializer

    def get(self,request,Format=None):
        item=Project_Allocation.objects.order_by('pk')
        paginator=PageNumberPagination()
        result_page=paginator.paginate_queryset(item,request)
        serializer=ProjectAllocationSerializer(result_page,many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self,request,Format=None):
        serializer=ProjectAllocationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=404) 
    
class LeaveManagementView(APIView):
    queryset=Leave_Management.objects.all()
    serializer_class=LeaveSerializer


    def get(self,request,id,Format=None):
        try:
            item=Leave_Management.objects.get(pk=id)
            serializer=LeaveSerializer(item)
            return Response(serializer.data)
        except Account_Setup.DoesNotExist:
            return Response(status=404)

    def put(self,request,id,Format=None):
        try:
            item=Leave_Management.objects.get(pk=id) 
        except Leave_Management.DoesNotExist:
            return Response(status=404)

        serializer=LeaveSerializer(item,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)

    def delete(self,request,id,Format=None):
        try:
            item=Leave_Management.objects.get(pk=id)
        except Leave_Management.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)
    
class LeaveManagementListView(APIView):
    queryset=Leave_Management.objects.all()
    serilaizer_class=LeaveSerializer

    def get(self,request,Format=None):
        item=Leave_Management.objects.order_by('pk')
        paginator=PageNumberPagination()
        result_page=paginator.paginate_queryset(item,request)
        serializer=LeaveSerializer(result_page,many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self,request,Format=None):
        serializer=LeaveSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=404) 

class SalaryAccountView(APIView):
    queryset=Salary_Account.objects.all()
    serializer_class=SalaryAccountSerializer


    def get(self,request,id,Format=None):
        try:
            item=Salary_Account.objects.get(pk=id)
            serializer=SalaryAccountSerializer(item)
            return Response(serializer.data)
        except Account_Setup.DoesNotExist:
            return Response(status=404)

    def put(self,request,id,Format=None):
        try:
            item=Salary_Account.objects.get(pk=id) 
        except Salary_Account.DoesNotExist:
            return Response(status=404)

        serializer=SalaryAccountSerializer(item,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)

    def delete(self,request,id,Format=None):
        try:
            item=Salary_Account.objects.get(pk=id)
        except Salary_Account.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)
    
class SalaryAccountListView(APIView):
    queryset=Salary_Account.objects.all()
    serilaizer_class=SalaryAccountSerializer

    def get(self,request,Format=None):
        item=Salary_Account.objects.order_by('pk')
        paginator=PageNumberPagination()
        result_page=paginator.paginate_queryset(item,request)
        serializer=SalaryAccountSerializer(result_page,many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self,request,Format=None):
        serializer=SalaryAccountSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=404) 

class AttendanceView(APIView):
    queryset=Attendance.objects.all()
    serializer_class=AttendanceSerializer


    def get(self,request,id,Format=None):
        try:
            item=Attendance.objects.get(pk=id)
            serializer=AttendanceSerializer(item)
            return Response(serializer.data)
        except Account_Setup.DoesNotExist:
            return Response(status=404)

    def put(self,request,id,Format=None):
        try:
            item=Attendance.objects.get(pk=id) 
        except Attendance.DoesNotExist:
            return Response(status=404)

        serializer=AttendanceSerializer(item,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)

    def delete(self,request,id,Format=None):
        try:
            item=Attendance.objects.get(pk=id)
        except Attendance.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)
    
class AttendanceListView(APIView):
    queryset=Attendance.objects.all()
    serilaizer_class=AttendanceSerializer

    def get(self,request,Format=None):
        item=Attendance.objects.order_by('pk')
        paginator=PageNumberPagination()
        result_page=paginator.paginate_queryset(item,request)
        serializer=AttendanceSerializer(result_page,many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self,request,Format=None):
        serializer=AttendanceSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=404) 

class ResignationView(APIView):
    queryset=Resignation.objects.all()
    serializer_class=ResignationSerializer


    def get(self,request,id,Format=None):
        try:
            item=Resignation.objects.get(pk=id)
            serializer=ResignationSerializer(item)
            return Response(serializer.data)
        except Account_Setup.DoesNotExist:
            return Response(status=404)

    def put(self,request,id,Format=None):
        try:
            item=Resignation.objects.get(pk=id) 
        except Resignation.DoesNotExist:
            return Response(status=404)

        serializer=ResignationSerializer(item,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)

    def delete(self,request,id,Format=None):
        try:
            item=Resignation.objects.get(pk=id)
        except Resignation.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)
    
class ResignationListView(APIView):
    queryset=Resignation.objects.all()
    serilaizer_class=ResignationSerializer

    def get(self,request,Format=None):
        item=Resignation.objects.order_by('pk')
        paginator=PageNumberPagination()
        result_page=paginator.paginate_queryset(item,request)
        serializer=ResignationSerializer(result_page,many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self,request,Format=None):
        serializer=ResignationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=404) 

class ExperianceLetterView(APIView):
    queryset=Experiance_Letter.objects.all()
    serializer_class=ExperianceLetterSerializer


    def get(self,request,id,Format=None):
        try:
            item=Experiance_Letter.objects.get(pk=id)
            serializer=ExperianceLetterSerializer(item)
            return Response(serializer.data)
        except Account_Setup.DoesNotExist:
            return Response(status=404)

    def put(self,request,id,Format=None):
        try:
            item=Experiance_Letter.objects.get(pk=id) 
        except Experiance_Letter.DoesNotExist:
            return Response(status=404)

        serializer=ExperianceLetterSerializer(item,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)

    def delete(self,request,id,Format=None):
        try:
            item=Experiance_Letter.objects.get(pk=id)
        except Experiance_Letter.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)
    
class ExperianceLetterListView(APIView):
    queryset=Experiance_Letter.objects.all()
    serilaizer_class=ExperianceLetterSerializer

    def get(self,request,Format=None):
        item=Experiance_Letter.objects.order_by('pk')
        paginator=PageNumberPagination()
        result_page=paginator.paginate_queryset(item,request)
        serializer=ExperianceLetterSerializer(result_page,many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self,request,Format=None):
        serializer=ExperianceLetterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=404) 
