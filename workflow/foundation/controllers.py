import json

from django.contrib import messages
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.middleware import http
from django.views.generic import CreateView, TemplateView

from .forms import MainEnterpriseForm, BranchEnterpriseForm, DepartmentForm
from .models import Enterprise, Department


class HeadEnterpriseInstall(CreateView):
    model = Enterprise
    form_class = MainEnterpriseForm
    template_name = 'foundation/enterprise/v2/enterprise.html'
    http_method_names = ['post']

    def http_method_not_allowed(self, request, *args, **kwargs):
        return http.HttpResponseNotAllowed(self._allowed_methods())

    def form_valid(self, form):
        form.instance.id = 0
        messages.success(self.request, 'Головная организация созданна, её реквизиты можно отредактировать в настройках.')
        return super(HeadEnterpriseInstall, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Поля формы заполненны некорректно.')
        return super(HeadEnterpriseInstall, self).form_invalid(form)

    def get_success_url(self):
        return reverse('enterprise')


class EnterpriseView(TemplateView):
    template_name = 'foundation/enterprise/v2/enterprise.html'

    def get_context_data(self, **kwargs):
        context = super(EnterpriseView, self).get_context_data(**kwargs)
        head_enterprise = Enterprise.get_head_enterprise()

        if head_enterprise is None:
            context['form'] = MainEnterpriseForm()
        else:
            context['head_enterprise'] = head_enterprise
            context['form'] = BranchEnterpriseForm()

        return context


class DepartmentsController(TemplateView):
    template_name = 'foundation/departments/v1/depts.html'
    title = 'Отделы организации'

    def post(self, request):
        form = DepartmentForm(request.POST)
        response_data = {}

        if form.is_valid():
            form.instance.title = form.instance.title.capitalize()
            form.save()
            response_data['success'] = 'Подразделение "%s" созданно!' % form.instance.title
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )
        else:
            return HttpResponse(
                json.dumps({"errors": form.errors}),
                content_type="application/json",
                status=400
            )

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            departments = serializers.serialize('json', self.departments())
            return JsonResponse(departments, safe=False)
        else:
            return super(DepartmentsController,self).get(self,request,*args,**kwargs)

    def departments(self):
        return Department.objects.all()

    def form(self):
        return DepartmentForm()
