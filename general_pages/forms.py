from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Div
from crispy_forms.bootstrap import FormActions
from django.utils.translation import ugettext as _
from .models import ContactUs
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible
from utils.emailer import send_email as email_send


class TopContactUsForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={"rows": 5}))
    captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)

    class Meta:
        model = ContactUs
        fields = ("name", "email", "message", 'phone', "captcha")

    def __init__(self, *args, **kwargs):
        super(TopContactUsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(Field("name", css_class="form-control form-control-lg",
                          placeholder="Your name",
                          required=True), css_class='form-group'),
                Div(Field("email", css_class="form-control form-control-lg",
                      placeholder="Email address",
                      required=True), css_class='form-group'),
                Div(Field("phone", css_class="form-control form-control-lg",
                          placeholder="Contact number",
                          required=True), css_class='form-group'),
                Div(Field("message", css_class="form-control form-control-lg textarea-autosize",
                  placeholder="Type your message",
                  required=True), css_class='form-group'),
            Div(FormActions(Submit('save', _('Get a Quote'),
                                   css_class="btn btn-primary btn-xl text-uppercase",
                                   css_id='sendMessageButton'),
                            ),
                css_class="col-md-4 text-center"),
            'captcha',
            )
        )