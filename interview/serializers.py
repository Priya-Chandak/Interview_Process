from rest_framework import serializers
from . models import Degree,Subject,Employee, Schedule_Interview, Documents, Offer_Letter, Account_Setup,Project_Allocation,Leave_Management,Salary_Account,Attendance,Resignation,Experiance_Letter

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'

class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Degree
        fields='__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields='__all__'

class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Schedule_Interview
        fields='__all__'

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Documents
        fields='__all__'

class OfferLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Offer_Letter
        fields='__all__'

class AccountSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account_Setup
        fields='__all__'

class ProjectAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project_Allocation
        fields='__all__'

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model=Leave_Management
        fields='__all__'

class SalaryAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Salary_Account
        fields='__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields='__all__'

    
class ResignationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Resignation
        fields='__all__'

        
class ExperianceLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Experiance_Letter
        fields='__all__'