from documents.models import Incoming, Outbound, Resolution
from django.contrib import admin


admin.site.register([Incoming, Outbound, Resolution])
