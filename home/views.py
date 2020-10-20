import json

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from home.foms import SearchForm, SginupForm
from home.models import Setting, contactForm, Contact_MSJ
from Events.models import Category, News, Comment, Imgs, CommentForm
from django.contrib import messages


def index(request):
    setting = Setting.objects.get(pk=1)
    items = Category.objects.all()

    context = {'setting': setting, 'items': items}
    return render(request, "index.html", context)


def aboutus(request):
    setting = Setting.objects.get(pk=1)
    items = Category.objects.all()
    context = {'setting': setting, 'items': items}
    return render(request, "aboutus.html", context)


def contact(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            data = Contact_MSJ()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.save()
            messages.success(request, "Mesajınız başarı ile göderilmiştir.Teşekkür Ederiz")
            return HttpResponseRedirect('/contact')
    else:
        form = contactForm()
    setting = Setting.objects.get(pk=1)
    items = Category.objects.all()
    context = {'setting': setting, 'items': items, 'form': form}
    return render(request, "contact.html", context)


def references(request):
    setting = Setting.objects.get(pk=1)
    items = Category.objects.all()
    context = {'setting': setting, 'items': items}
    return render(request, "references.html", context)


def cat_news(request, id, slug):
    news = News.objects.filter(category_id=id)
    items = Category.objects.all
    context = {'news': news, 'items': items}
    return render(request, "categori.html", context)


def all_cat(request, ):
    news = News.objects.all()
    items = Category.objects.all()

    context = {'news': news,
               'items': items,

               }
    return render(request, "categori.html", context)


def detail(request, id, slug):
    newss = News.objects.get(pk=id)
    items = Category.objects.all()

    # imgs = Imgs.objects.filter(news_id=id)
    cmnts = Comment.objects.filter(news_id=id, status='True')
    context = {'newss': newss,
               'items': items,
               'cmnts': cmnts,
               }
    return render(request, "detail.html", context)


@login_required(login_url='/login')
def add_Comment(request, id):
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            current_user = request.user
            data = Comment()
            data.user_id = current_user.id
            data.news_id = id
            data.subject = form.cleaned_data['subject']
            data.note = form.cleaned_data['note']
            data.comment = form.cleaned_data['comment']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Yorumunuz başarı ile göderilmiştir.Teşekkür Ederiz")
            return HttpResponseRedirect(url)

    messages.error(request, "Yorumunuz Gönderilmedi .Kontrol Ediniz", )
    return HttpResponseRedirect(url)


def news_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            items = Category.objects.all()
            query = form.cleaned_data['query']
            news = News.objects.filter(title__icontains=query)  # SELECT ... WHERE headline ILIKE '%Lennon%';

            context = {'items': items,
                       'news': news,
                       }
            return render(request, 'categori.html', context)
    return HttpResponseRedirect('/')


def newsSrch_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        news = News.objects.filter(title__icontains=q)
        results = []
        for pl in news:
            news_json = {}
            news_json = pl.title
            results.append(news_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Kullancı Adı veya Şireniz Komtrol Ediniz  ")
            return HttpResponseRedirect('/login')

    setting = Setting.objects.get(pk=1)
    items = Category.objects.all()
    context = {'setting': setting, 'items': items}
    return render(request, "signin.html", context)


def Sginup_view(request):
    if request.method == 'POST':
        form = SginupForm(request.POST)
        # kontrol amaçlı
        #         return HttpResponse('signup.html')
        if form.is_valid():

            form.save()
            return HttpResponse('dfgdgdfgdgdfghtml')
            #data.username = form.cleaned_data['username']
            #data.email = form.cleaned_data['email']

            #data.first_name = form.cleaned_data['first_name']

            #data.last_name = form.cleaned_data['last_name']
           # data.password1 = form.cleaned_data['password1']
            #data.password2 = form.cleaned_data['password2']

    form = SginupForm()
    items = Category.objects.all()
    context = { 'items': items, 'form': form}
    return render(request, "signup.html", context)


def sginup_view(request):
    if request.method == 'POST':
        form = SginupForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
        #

    form = SginupForm()
    items = Category.objects.all()
    context = { 'items': items, 'form': form}
    return render(request, "signup.html", context)