from .models import Company, Invoice
from rest_framework import viewsets, permissions
from .serializers import *


# Invoice Viewset
# class UserViewset(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     permission_classes = [
#         permissions.AllowAny
#     ]
#     serializer_class = UserSerializer

class CompanyViewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CompanySerializer

class InvoiceViewset(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = InvoiceSerializer

class CountryViewset(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CountrySerializer

class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProfileSerializer

class OfficeViewset(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = OfficeSerializer

class CountyRecorderViewset(viewsets.ModelViewSet):
    queryset = County_Recorder.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CountyRecorderSerializer

class ContactViewset(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ContactSerializer

class MatterViewset(viewsets.ModelViewSet):
    queryset = Matter.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MatterSerializer

class CourtRecordViewset(viewsets.ModelViewSet):
    queryset = Court_Record.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CourtRecordSerializer

class EFileServicesViewset(viewsets.ModelViewSet):
    queryset = EFIle_Services.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EFileServicesSerializer

class LeadViewset(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer

class ClientVicAttyViewset(viewsets.ModelViewSet):
    queryset = Client_Vic_Atty.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ClientVicAttySerializer

class ClientVicInfoViewset(viewsets.ModelViewSet):
    queryset = Client_Vic_Info.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ClientVicInfoSerializer

class SheriffDetailViewset(viewsets.ModelViewSet):
    queryset = Sheriff_Detail.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SheriffDetailSerializer

class JobBoardViewset(viewsets.ModelViewSet):
    queryset = Job_Board.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = JobBoardSerializer

class DebtorViewset(viewsets.ModelViewSet):
    queryset = Debtor.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DebtorSerializer
