from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, TemplateView, View, FormView, CreateView, UpdateView, DeleteView

from .forms import FeedbackForm
from .models import Feedback


class CreateFeedBackView(CreateView):

    model = Feedback
    form_class = FeedbackForm
    template_name = 'html/feedback.html'
    success_url = 'done/'


class UpdateFeedBackView(UpdateView):

    form_class = FeedbackForm
    template_name = 'html/feedback.html'
    model = Feedback
    success_url = '/done/'


class DoneView(TemplateView):
    template_name = 'html/done.html'


class listFeedback(ListView):
    template_name = 'html/list_feedback.html'
    model = Feedback
    context_object_name = 'all_feedback'

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_qs = queryset.filter(rating__gt=1)

        return filter_qs


class DetailFeedback(TemplateView):
    template_name = 'html/detail_feedback.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['one_feedback'] = Feedback.objects.get(id=kwargs['pk'])

        return context


