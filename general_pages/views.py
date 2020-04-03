from datetime import datetime

from django.views import generic
from django.urls import reverse_lazy
from portfolio import settings

from .forms import ContactUsForm, TopContactUsForm
from .models import ContactUs, TermsPolicy
from blog.models import BlogPost
from utils.emailer import send_email


class HomeView(generic.CreateView):
    template_name = 'general_pages/home.html'
    form_class = TopContactUsForm
    success_url = reverse_lazy("home")
    model = BlogPost
    queryset = BlogPost.objects.all_published()
    paginate_by = settings.BLOG_PAGE_SIZE
    ordering = ["-order_index"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["object_featured_list"] = BlogPost.objects.all_featured().order_by('-created')[:3]
        context['year'] = datetime.now().year
        return context

    def form_valid(self, form):
        client_email = send_email(form.email, form.name, form.message, form.phone)
        if client_email:
            message = client_email['MessageId']
            notes = ContactUs.objects.get(email=form.email)
            notes['email_sent'] = message
            notes.save(commit=True)
        return super().form_valid(form)




class TosView(generic.TemplateView):
    template_name = 'general_pages/tos.html'
    model = TermsPolicy

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['tos'] = TermsPolicy.objects.get(name='tos')
        return context


class PrivacyPolicyView(generic.TemplateView):
    template_name = 'general_pages/privacy.html'
    model = TermsPolicy

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['privacy'] = TermsPolicy.objects.get(name='privacy')
        return context