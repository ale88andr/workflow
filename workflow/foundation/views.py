from django.shortcuts import render, redirect, get_object_or_404
from .models import Enterprise
from .forms import MainEnterpriseForm, BranchEnterpriseForm


def enterprise(request, form=None):
    enterprise_obj = None

    try:
        enterprise_obj = Enterprise.objects.get(id=0)
    except Enterprise.DoesNotExist:
        if form is None:
            form = MainEnterpriseForm()

    if form is None:
        form = BranchEnterpriseForm()

    return render(
        request,
        'foundation/enterprise/enterprise.html',
        {'enterprise': enterprise_obj, 'form': form}
    )


def create_main_enterprise(request):
    if request.method == "POST":
        form = MainEnterpriseForm(request.POST)
        if form.is_valid():
            main_enterprise = form.save(commit=False)
            main_enterprise.id = 0
            main_enterprise.save()
            return redirect('foundation.views.enterprise')
        else:
            return enterprise(request, form)