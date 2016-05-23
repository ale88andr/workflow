from django.shortcuts import resolve_url
from django.views.generic import ListView, CreateView

from .models import Question
from .forms import QuestionForm, NewQuestionForm


class QuestionCreate(CreateView):

    model = Question
    fields = ['title', 'text']

    def get_success_url(self):
        return resolve_url('questions:question_index')


class QuestionsIndex(ListView):

    template_name = 'questions/index.html'
    model = Question

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.form = None
        self.new_question_form = None

    def dispatch(self, request, *args, **kwargs):
        self.form = QuestionForm(request.GET)
        self.form.is_valid()
        self.new_question_form = (NewQuestionForm or None)
        return super(QuestionsIndex, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Question.objects.all()

        if self.form.cleaned_data.get('sort'):
            queryset = queryset.order_by(self.form.cleaned_data['sort'])

        if self.form.cleaned_data.get('search'):
            queryset = queryset.filter(title__icontains=self.form.cleaned_data['search'])

        return queryset

    def get_context_data(self, **kwargs):
        context = super(QuestionsIndex, self).get_context_data(**kwargs)
        context['form'] = self.form
        context['new_question_form'] = self.new_question_form
        return context
