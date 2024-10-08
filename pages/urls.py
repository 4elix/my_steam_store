from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_page, name='home_path'),
    path('game/detail/<slug:slug_path>/', views.show_detail, name='detail_path'),
    path('catalog/', views.CatalogPage.as_view(), name='catalog_path'),
    path('category/<int:cat_id>/', views.ShowGameRelatedCategories.as_view(), name='category_path'),
    path('catalog/search/', views.SearchGameToTitle.as_view(), name='search_catalog'),

    path('favorite/<int:pk_game>/', views.favorite_logic, name='like_active_path'),
    path('desired/<int:user_id>', views.page_desired, name='desired_path'),

    path('comment/<int:pk>/reply', views.add_reply, name='add_reply_path'),
    path('download/<slug:slug_path>/', views.download_file, name='download_path'),

    path('rating/<int:pk_path>/', views.rating_logic, name='rating_activate'),
    path('like/comment/<int:comment_id>/', views.comment_like_logic, name='active_like_logic')
]
