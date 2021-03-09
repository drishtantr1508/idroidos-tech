from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import(TemplateView,CreateView,DetailView,ListView,UpdateView,DeleteView)
from django.contrib.auth.models import User
from idroidos.models import (UserProfileInfo,QuickLinks,SmartphonesInfo,ComparisonInfo,NewsArticle,SmartphoneComment,NewsComment,ComparisonComment)
from idroidos import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from django.utils import timezone

#shashwat mishra portfolio view
def index(request):
    return render(request,"idroidos/index.html",{})

# Create your views here.
def des_encrypt(plain_text,password):
    import pyDes as pd
    imported_algo=pd.des(password, pd.CBC, "\0\0\0\0\0\0\0\0", padmode=pd.PAD_PKCS5)
    encr_text=imported_algo.encrypt(plain_text)
    return encr_text

def des_decrypt(cipher_text,password):
    import pyDes as pd
    imported_algo=pd.des(password, pd.CBC, "\0\0\0\0\0\0\0\0",  padmode=pd.PAD_PKCS5)
    decr_text=imported_algo.decrypt(cipher_text)
    return decr_text

class AdminStaffRequiredMixin(LoginRequiredMixin,UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
class HomepageView(ListView):
    context_object_name='quicklinks'
    model=QuickLinks
    template_name='idroidos/homepage.html'
    def get_queryset(self):
        return QuickLinks.objects.all().order_by('-create_date')

class AboutView(TemplateView):
    template_name='idroidos/about.html'

class HomePost(AdminStaffRequiredMixin,CreateView):
    model=QuickLinks
    login_url='/login/'#this will check if user is logged in or not?
    redirect_field_name = 'idroidos/homepage.html'
    form_class = forms.QuickLinksForm

    # note that a template_name= model_form.html is already fixed and will find it if not cjanged

def register(request):
    registered=False
    if request.method=='POST':
        user_form=forms.UserForm(request.POST)
        profile_form=forms.UserProfileInfoForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            encr_pass=des_encrypt(user.password,"@3X/X*&X")
            user.set_password(str(encr_pass)[2:-1])
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()

            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=forms.UserForm()
        profile_form=forms.UserProfileInfoForm()
    return render(request,'idroidos/register.html',{'registered':registered,'profile_form':profile_form,'user_form':user_form})

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        decr_pass=str(des_encrypt(password,"@3X/X*&X"))[2:-1]
        user=authenticate(username=username,password=decr_pass)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse("homepage"))
            else:
                return HttpResponse("<h1>Account not Active</h1>")
        else:
            print("Someone tried to login and failed.")
            print("Username: {} and Password: {}".format(username,decr_pass))
            return HttpResponse("<h1>invalid login details</h1>")
    else:
        return render(request,'idroidos/login.html',{})


#####################################
#####################################
############# Post Work #############
#####################################
#####################################

#####################################
######### SmartPhones Info ##########
#####################################

class SmartphonesInfoListView(ListView):
    context_object_name='smartphones'
    model=SmartphonesInfo
    template_name='idroidos/smartphonesinfo_list.html'

    def get_queryset(self):
        return SmartphonesInfo.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class SmartphonesInfoDetailView(DetailView):
    model=SmartphonesInfo
    template_name='idroidos/post_detail.html'

class SmartphonesInfoCreateView(AdminStaffRequiredMixin,CreateView):
    model=SmartphonesInfo#to tell django that form data should be saved in that specific model
    login_url='/login/'#this will check if user is logged in or not?
    redirect_field_name = 'idroidos/post_detail.html'
    form_class = forms.SmartphonesInfoForm# to tell django which form is to be rendered.
class SmartphonesInfoUpdateView(AdminStaffRequiredMixin,UpdateView):# same as create view
    model=SmartphonesInfo
    login_url='/login/'#this will check if user is logged in or not?
    redirect_field_name = 'idroidos/post_detail.html'
    form_class = forms.SmartphonesInfoForm

class SmartphonesInfoDeleteView(AdminStaffRequiredMixin,DeleteView):
    model=SmartphonesInfo
    success_url= reverse_lazy('smartphone_list')

class SmartphonesInfoDraftListView(AdminStaffRequiredMixin,ListView):
    login_url='/login/'
    redirect_field_name='idroidos/smartphone_draft_list.html'
    model=SmartphonesInfo
    context_object_name='smartphones'

    def get_queryset(self):
        return SmartphonesInfo.objects.filter(published_date__isnull=True).order_by('create_date')


#####################################
########## Comparison Info ##########
#####################################

class ComparisonInfoListView(ListView):
    model=ComparisonInfo
    template_name='idroidos/comparison_list.html'
    context_object_name='comparisons'

    def get_queryset(self):
        return ComparisonInfo.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class ComparisonInfoDetailView(DetailView):
    model=ComparisonInfo
    template_name='idroidos/post_detail.html'

class ComparisonInfoCreateView(AdminStaffRequiredMixin,CreateView):
    model=ComparisonInfo
    login_url='/login/'#this will check if user is logged in or not?
    redirect_field_name = 'idroidos/post_detail.html'
    form_class = forms.ComparisonInfoForm

class ComparisonInfoUpdateView(AdminStaffRequiredMixin,UpdateView):
    model=ComparisonInfo
    login_url='/login/'#this will check if user is logged in or not?
    redirect_field_name = 'idroidos/post_detail.html'
    form_class = forms.ComparisonInfoForm

class ComparisonInfoDeleteView(AdminStaffRequiredMixin,DeleteView):
    model=ComparisonInfo
    success_url= reverse_lazy('comparison_list')

class ComparisonInfoDraftListView(AdminStaffRequiredMixin,ListView):
    login_url='/login/'
    redirect_field_name='idroidos/comparison_draft_list.html'
    model=ComparisonInfo
    context_object_name='comparisons'

    def get_queryset(self):
        return ComparisonInfo.objects.filter(published_date__isnull=True).order_by('create_date')


#####################################
########### News Article ############
#####################################

class NewsArticleListView(ListView):
    context_object_name='newsarticles'
    model=NewsArticle
    template_name='idroidos/news_list.html'

    def get_queryset(self):
        return NewsArticle.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class NewsArticleDetailView(DetailView):
    model=NewsArticle
    template_name='idroidos/post_detail.html'

class NewsArticleCreateView(AdminStaffRequiredMixin,CreateView):
    model=NewsArticle
    login_url='/login/'#this will check if user is logged in or not?
    redirect_field_name = 'idroidos/post_detail.html'

    form_class = forms.NewsArticleForm
    model= NewsArticle

class NewsArticleUpdateView(AdminStaffRequiredMixin,UpdateView):
    model=NewsArticle
    login_url='/login/'#this will check if user is logged in or not?
    redirect_field_name = 'idroidos/post_detail.html'

    form_class = forms.NewsArticleForm
    model= NewsArticle

class NewsArticleDeleteView(AdminStaffRequiredMixin,DeleteView):
    model=NewsArticle
    success_url= reverse_lazy('news_list')

class NewsArticleDraftListView(AdminStaffRequiredMixin,ListView):
    login_url='/login/'
    redirect_field_name='idroidos/comparison_draft_list.html'
    model=NewsArticle
    context_object_name='newsarticles'

    def get_queryset(self):
        return NewsArticle.objects.filter(published_date__isnull=True).order_by('create_date')



#####################################
#####################################
########### Comments Work ###########
#####################################
#####################################

#####################################
########## Smartphones ##############
#####################################

@login_required
def add_comment_to_smartphone(request,pk):
    smartphone=get_object_or_404(SmartphonesInfo,pk=pk)
    if request.method=='POST':
        form=forms.SmartphoneCommentForm(data=request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.smartphone=smartphone
            comment.save()
            return redirect('smartphone_details',pk=smartphone.pk)
    else:
        form=forms.SmartphoneCommentForm()
    return render(request,'idroidos/smartphone_comment_form.html',{'form':form})

@login_required
def smartphone_comment_approve(request,pk):
    comment=get_object_or_404(SmartphoneComment,pk=pk)
    comment.approve()
    return redirect('smartphone_details',pk=comment.smartphone.pk)

@login_required
def smartphone_comment_remove(request,pk):
    comment=get_object_or_404(SmartphoneComment,pk=pk)
    post_pk=comment.smartphone.pk
    comment.delete()
    return redirect('smartphone_details',pk=post_pk)


@login_required
def smartphone_post_publish(request,pk):
    post=get_object_or_404(SmartphonesInfo,pk=pk)#post is an instance of Post class and we can use methods attached to it.
    post.publish()
    return redirect('smartphone_details',pk=pk)


#####################################
########## Comparisons ##############
#####################################

@login_required
def add_comment_to_comparison(request,pk):
    comparison=get_object_or_404(ComparisonInfo,pk=pk)
    if request.method=='POST':
        form=forms.ComparisonCommentForm(data=request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.comparison=comparison
            comment.save()
            return redirect('comparison_details',pk=comparison.pk)
    else:
        form=forms.ComparisonCommentForm()
    return render(request,'idroidos/comparison_comment_form.html',{'form':form})

@login_required
def comparison_comment_approve(request,pk):
    comment=get_object_or_404(ComparisonComment,pk=pk)
    comment.approve()
    return redirect('comparison_details',pk=comment.comparison.pk)

@login_required
def comparison_comment_remove(request,pk):
    comment=get_object_or_404(ComparisonComment,pk=pk)
    post_pk=comment.comparison.pk
    comment.delete()
    return redirect('comparison_details_detail',pk=post_pk)


@login_required
def comparison_post_publish(request,pk):
    post=get_object_or_404(ComparisonInfo,pk=pk)#post is an instance of ComparisonInfo class and we can use methods attached to it.
    post.publish()
    return redirect('comparison_details',pk=pk)


#####################################
########## News Article #############
#####################################

@login_required
def add_comment_to_news(request,pk):
    news=get_object_or_404(NewsArticle,pk=pk)
    if request.method=='POST':
        form=forms.NewsCommentForm(data=request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.news=news
            comment.save()
            return redirect('news_details',pk=news.pk)
    else:
        form=forms.NewsCommentForm()
    return render(request,'idroidos/news_comment_form.html',{'form':form})

@login_required
def news_comment_approve(request,pk):
    comment=get_object_or_404(NewsComment,pk=pk)
    comment.approve()
    return redirect('news_details',pk=comment.news.pk)

@login_required
def news_comment_remove(request,pk):
    comment=get_object_or_404(NewsComment,pk=pk)
    post_pk=comment.news.pk
    comment.delete()
    return redirect('news_details',pk=post_pk)


@login_required
def news_post_publish(request,pk):
    post=get_object_or_404(NewsArticle,pk=pk)#post is an instance of Post class and we can use methods attached to it.
    post.publish()
    return redirect('news_details',pk=pk)
