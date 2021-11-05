# from rest_framework import permission_classes
from .models import Company, Invoice
from rest_framework import viewsets, permissions
from .serializers import CompanySerializer, InvoiceSerializer

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
