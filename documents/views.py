from django.http import HttpResponse
from django.shortcuts import render

from documents.models import Incoming, Outbound


def index(request):
    return render(request, 'documents/index.html')


def incoming(request):
    incoming_documents = Incoming.objects.filter()[:15]
    quantity = len(incoming_documents)
    return render(request, 'documents/incoming.html', {'incoming': incoming_documents, 'quantity': quantity})


def outbound(request):
    outbound_documents = Outbound.objects.filter()[:15]
    return render(request, 'documents/outbound.html', {'outbound': outbound_documents})
