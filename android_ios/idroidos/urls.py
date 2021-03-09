from django.urls import path
from django.conf.urls import url
from idroidos import views
urlpatterns=[
    url(r'^$',views.HomepageView.as_view(),name='homepage'),
    url(r'^about/',views.AboutView.as_view(),name="about"),
    url(r'^user_login/$',views.user_login,name="user_login"),
    url(r'^register/$',views.register,name="register"),
    url(r'logout/$',views.user_logout,name='logout'),
    #shashwat_mishra
    url(r'^shashwat_mishra/$',views.index,name="shashwat"),
    #smartphone urls
    url(r'^smartphone_list/$',views.SmartphonesInfoListView.as_view(),name="smartphone_list"),
    url(r'^smartphone_list/(?P<pk>[-\w]+)/$',views.SmartphonesInfoDetailView.as_view(),name='smartphone_details'),
    url(r'^smartphones_list/new/$',views.SmartphonesInfoCreateView.as_view(),name="new_smartphone"),
    #url(r'^smartphones_list/new/$',views.smartphone_media,name='smartphone_media'),
    url(r'^smartphone_list/(?P<pk>[-\w]+)/edit/$',views.SmartphonesInfoUpdateView.as_view(),name="edit_smartphone"),
    url(r'^smartphone_list/(?P<pk>[-\w]+)/remove/$',views.SmartphonesInfoDeleteView.as_view(),name='remove_smartphone'),
    url(r'^smartphone_drafts/$',views.SmartphonesInfoDraftListView.as_view(),name="smartphone_draft_list"),
    #comparison urls
    url(r'^comparison_list/$',views.ComparisonInfoListView.as_view(),name="comparison_list"),
    url(r'^comparison_list/(?P<pk>[-\w]+)$',views.ComparisonInfoDetailView.as_view(),name='comparison_details'),
    url(r'^comparison_list/new/$',views.ComparisonInfoCreateView.as_view(),name="new_comparison"),
    url(r'^comparison_list/(?P<pk>[-\w]+)/edit/$',views.ComparisonInfoUpdateView.as_view(),name="edit_comparison"),
    url(r'^comparison_list/(?P<pk>[-\w]+)/remove/$',views.ComparisonInfoDeleteView.as_view(),name='remove_comparison'),
    url(r'^comparison_drafts/$',views.ComparisonInfoDraftListView.as_view(),name="comparison_draft_list"),
    #news article urls
    url(r'^news_list/$',views.NewsArticleListView.as_view(),name="news_list"),
    url(r'^news_list/(?P<pk>[-\w]+)$',views.NewsArticleDetailView.as_view(),name='news_details'),
    url(r'^news_list/new/$',views.NewsArticleCreateView.as_view(),name="new_news"),
    url(r'^news_list/(?P<pk>[-\w]+)/edit/$',views.NewsArticleUpdateView.as_view(),name="edit_news"),
    url(r'^news_list/(?P<pk>[-\w]+)/remove/$',views.NewsArticleDeleteView.as_view(),name='remove_news'),
    url(r'^news_drafts/$',views.NewsArticleDraftListView.as_view(),name="news_draft_list"),
    ##comments urlpatterns##
    #smartphone
    url(r'^smartphone_list/(?P<pk>[-\w]+)/comment',views.add_comment_to_smartphone,name='smartphone_comment'),
    url(r'^smartphone_comment/(?P<pk>[-\w]+)/approve',views.smartphone_comment_approve,name='smartphone_comment_approve'),
    url(r'^smartphone_comment/(?P<pk>[-\w]+)/remove',views.smartphone_comment_remove,name='smartphone_comment_remove'),
    url(r'^smartphone_list/(?P<pk>[-\w]+)/publish/$',views.smartphone_post_publish,name='smartphone_publish'),
    #comparison
    url(r'^comparison_list/(?P<pk>[-\w]+)/comment',views.add_comment_to_comparison,name='comparison_comment'),
    url(r'^comparison_comment/(?P<pk>[-\w]+)/approve',views.comparison_comment_approve,name='comparison_comment_approve'),
    url(r'^comparison_comment/(?P<pk>[-\w]+)/remove',views.comparison_comment_remove,name='comparison_comment_remove'),
    url(r'^comparison_list/(?P<pk>[-\w]+)/publish/$',views.comparison_post_publish,name='comparison_publish'),
    #news
    url(r'^news_list/(?P<pk>[-\w]+)/comment',views.add_comment_to_news,name='news_comment'),
    url(r'^news_comment/(?P<pk>[-\w]+)/approve',views.news_comment_approve,name='news_comment_approve'),
    url(r'^news_comment/(?P<pk>[-\w]+)/remove',views.news_comment_remove,name='news_comment_remove'),
    url(r'^news_list/(?P<pk>[-\w]+)/publish/$',views.news_post_publish,name='news_publish'),
    url(r'^post_headline/$',views.HomePost.as_view(),name="add_post_headline"),
]
