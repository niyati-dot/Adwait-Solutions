from django import forms
from .models import AdwaitappInquiries, AdwaitappNewsletterSubscriber
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.forms.widgets import PasswordInput, TextInput

class ContactForm(forms.ModelForm):
  class Meta:
    model = AdwaitappInquiries
    fields = ['name', 'subject', 'email', 'phone', 'message', 'status', ]
    widgets = {
            'note': forms.Textarea(attrs={'rows': 4}) 
        }
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      # Set required=False for optional fields
      self.fields['phone'].required = False
      self.fields['message'].required = False

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = AdwaitappNewsletterSubscriber
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if AdwaitappNewsletterSubscriber.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already subscribed.")
        return email

class ContactInquiryForm(forms.ModelForm):
    class Meta:
        model = AdwaitappInquiries
        fields = ['name', 'email', 'subject', 'message']