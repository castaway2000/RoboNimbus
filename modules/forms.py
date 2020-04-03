from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Div
from crispy_forms.bootstrap import FormActions
from django.utils.translation import ugettext as _
from general_pages.models import ContactUs
from captcha.fields import ReCaptchaField


class ContactUsForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={"rows": 5}))
    captcha = ReCaptchaField()

    class Meta:
        model = ContactUs
        fields = ("name", "email", "message", "captcha")

    def __init__(self, *args, **kwargs):
        # self.user = kwargs.pop("user")
        super(ContactUsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Field("name", css_class="form-control form-control-lg", placeholder="Your name"),
            Field("email", css_class="form-control form-control-lg", placeholder="Email address"),
            Field("message", css_class="form-control form-control-lg textarea-autosize", placeholder="Type your message"),
            Div(
                FormActions(
                        Submit('save', _('Send message'), css_class="btn btn-dark rounded-pill mt-4"),
                    )
                    , css_class="text-left"
                ),
            'captcha'
            )
