from django .urls import path
from tags import views 

urlpatterns = [
    path ('create/',views.CreateTag.as_view(),name='tag_create'),
    path ('List/',views.ListTagV1.as_view(),name='tag_list'),
    path ('Listtag/',views.ListTagV2.as_view(),name='tag_list'),
    path ('details/<slug:slug>',views.TagDetail.as_view(),name='tag_details'),
    path ('ldetials/<int:id>',views.TagDetailV2.as_view(),name='tag_details'),
]