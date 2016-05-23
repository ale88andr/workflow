from django.contrib import messages
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import FormMixin

from .models import Resolution
from .forms import ResolutionForm, ResolutionSearchForm


"""
Resolutions CRUD
"""


class ResolutionsController(ListView, FormMixin):

    model = Resolution
    context_object_name = 'resolutions'
    template_name = 'documents/resolutions/list.html'
    form_class = ResolutionForm

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.search_form = None
        self.create_form = None

    def get(self, request, *args, **kwargs):
        # From ProcessFormMixin
        form_class = self.get_form_class()
        self.create_form = self.get_form(form_class)

        # From BaseListView
        self.object_list = self.get_queryset()
        context = self.get_context_data(object_list=self.object_list, create_form=self.create_form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = ResolutionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Резолюция добавленна.')
        else:
            messages.error(request, 'Ошибка при добавлении резолюции.')
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ResolutionsController, self).get_context_data(**kwargs)
        context['create_form'] = self.create_form
        context['search_form'] = self.search_form
        return context

    def dispatch(self, request, *args, **kwargs):
        self.search_form = ResolutionSearchForm(request.GET)
        self.search_form.is_valid()
        return super(ResolutionsController, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Resolution.objects.all()

        if self.search_form.cleaned_data.get('search'):
            queryset = queryset.filter(title__icontains=self.search_form.cleaned_data['search'])

        if self.search_form.cleaned_data.get('sorted_by'):
            queryset = queryset.order_by(self.search_form.cleaned_data.get('sorted_by'))

        return queryset


class DeleteResolution(DeleteView):

    model = Resolution
    success_url = '/workflow/resolutions'
    success_message = 'Резолюция удаленна!'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(request, self.success_message)
        return super(DeleteResolution, self).delete(request, *args, **kwargs)
