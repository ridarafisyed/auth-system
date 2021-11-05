from rest_framework import serializers
from .models import *


# 
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'
class CountyRecorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = County_Recorder
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
class MatterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matter
        fields = '__all__'

class CourtRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Court_Record
        fields = '__all__'

class EFileServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EFIle_Services
        fields = '__all__'

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
class ClientVicAttySerializer(serializers.ModelSerializer):
    class Meta:
        model = Client_Vic_Atty
        fields = '__all__'

class ClientVicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client_Vic_Info
        fields = '__all__'
class SheriffDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sheriff_Detail
        fields = '__all__'
class JobBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_Board
        fields = '__all__'
class DebtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debtor
        fields = '__all__'