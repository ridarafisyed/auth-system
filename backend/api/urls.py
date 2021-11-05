
from api.views import *
from .api import *
from rest_framework import routers


router = routers.DefaultRouter()
# router.register('user', UserViewset, 'user')
router.register('company', CompanyViewset,  'company')
router.register('invoice', InvoiceViewset,  'invoice')
router.register('profile', ProfileViewset, 'profile')
router.register('country', CountryViewset, 'country')
router.register('county-record', CountyRecorderViewset, 'county-recorder')
router.register('office', OfficeViewset, 'office')
router.register('court-record', CourtRecordViewset, 'court-record')
router.register('efile-services',EFileServicesViewset , 'efile-serivees')
router.register('lead',LeadViewset , 'lead')
router.register('client-vic-atty',ClientVicAttyViewset , 'client-vic-atty')
router.register('client-vic-info', ClientVicInfoViewset , 'client-vic-info')
router.register('sheriff-detail',SheriffDetailViewset , 'sheriff-detail')
router.register('job-board', JobBoardViewset , 'job-board')
router.register('matter', MatterViewset, 'matter')

# install axios in react app and pip install django-cors-headers in django app 

urlpatterns = router.urls
# urlpatterns = [
    
#     path('api', InvoiceView.as_view())
# ]
