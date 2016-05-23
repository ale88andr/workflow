from django.contrib import messages
from django.core.urlresolvers import reverse
from django.middleware import http
from django.views.generic import CreateView, TemplateView

from .forms import MainEnterpriseForm
from .models import Enterprise


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
        return reverse('View:Enterprise')


class EnterpriseView(TemplateView):
    template_name = 'foundation/enterprise/v2/enterprise.html'

    def get_context_data(self, **kwargs):
        context = super(EnterpriseView, self).get_context_data(**kwargs)
        head_enterprise = Enterprise.get_head_enterprise()

        if head_enterprise is None:
            context['head_enterprise'] = head_enterprise
            context['form'] = MainEnterpriseForm()

        return context
