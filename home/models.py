from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm, Textarea, TextInput


class Setting(models.Model):
    title = models.CharField(blank=True, max_length=110)
    keywords = models.CharField(blank=True, max_length=255)
    description = models.CharField(blank=True, max_length=255)

    campony = models.CharField(blank=True, max_length=110)
    address = models.CharField(blank=True, max_length=255)
    logo = models.ImageField(blank=True, upload_to='imgFile/')

    phone = models.CharField(blank=True, max_length=110)
    fax = models.CharField(blank=True, max_length=255)
    facebook = models.CharField(blank=True, max_length=110)
    instegram = models.CharField(blank=True, max_length=255)
    twitter = models.CharField(blank=True, max_length=255)

    email = models.CharField(blank=True, max_length=255)
    smtpemail = models.CharField(blank=True, max_length=110)
    smtpserver = models.CharField(blank=True, max_length=255)
    smtppasword = models.CharField(blank=True, max_length=255)
    smtpport = models.CharField(blank=True, max_length=255)
    aboutus = RichTextUploadingField(blank=True, )
    Aumainpic = models.ImageField(blank=True, upload_to='imgFile/')
    Ausidepic = models.ImageField(blank=True, upload_to='imgFile/')
    contact = RichTextUploadingField(blank=True, )
    references = RichTextUploadingField(blank=True, )

    rflocation = RichTextUploadingField(blank=True, )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Contact_MSJ(models.Model):
    Status = (
        ('New', 'New'),
        ('Read', 'Read'),
    )

    name = models.CharField(blank=True, max_length=40)
    email = models.CharField(blank=True, max_length=40)
    subject = models.CharField(blank=True, max_length=40)

    massage = models.CharField(blank=True, max_length=255)
    message = models.CharField(blank=True, max_length=255)
    status = models.CharField(max_length=30, choices=Status, default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class contactForm(ModelForm):
    class Meta:
        model = Contact_MSJ
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'Ad Soyad'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Konu'}),
            'email': TextInput(attrs={'class': 'input', 'placeholder': 'Mail Adresi'}),
            'message': Textarea(attrs={'class': 'input', 'placeholder': 'Mesajınız', 'row': '7'}),
        }
