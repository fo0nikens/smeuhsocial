from django.conf.urls import *



urlpatterns = patterns("",
    # all photos or latest photos
    url(r"^$", "photos.views.photos", name="photos"),
    # most viewed photos
    url(r"^most_viewed/$", "photos.views.most_viewed", name="photo_most_viewed"),
    # a photos details
    url(r"^details/(?P<id>\d+)/$", "photos.views.details", name="photo_details"),
    # upload photos
    url(r"^upload/$", "photos.views.upload", name="photo_upload"),
    # your photos
    url(r"^yourphotos/$", "photos.views.yourphotos", name="photos_yours"),
    # a members photos
    url(r"^member/(?P<username>[\w]+)/$", "photos.views.memberphotos", name="photos_member"),
    #destory photo
    url(r"^destroy/(?P<id>\d+)/$", "photos.views.destroy", name="photo_destroy"),
    #edit photo
    url(r"^edit/(?P<id>\d+)/$", "photos.views.edit", name="photo_edit"),
)