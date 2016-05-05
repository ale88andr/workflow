from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Incoming, Outbound, Resolution
from .forms import ResolutionForm


def index(request):
    return render(request, 'documents/index.html')


def incoming(request):
    incoming_documents = Incoming.objects.filter()
    quantity = incoming_documents.count()
    return render(request, 'documents/incoming.html', {'incoming': incoming_documents, 'quantity': quantity})


def outbound(request):
    outbound_documents = Outbound.objects.filter()
    return render(request, 'documents/outbound.html', {'outbound': outbound_documents})


def resolutions(request):
    return get_resolutions(request)


def delete_resolution(request, resolution_id):
    resolution = get_object_or_404(Resolution, id=resolution_id)
    resolution.delete()
    return redirect('documents.views.resolutions')


def create_resolution(request):
    if request.method == "POST":
        form = ResolutionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('documents.views.resolutions')
        else:
            return get_resolutions(request, form)


def get_resolutions(request, form = None):
    if not form:
        form = ResolutionForm()
    resolution_list = Resolution.objects.all()
    return render(request, 'documents/resolutions/index.html', {'resolutions': resolution_list, 'form': form})