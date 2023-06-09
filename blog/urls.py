from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('new/', views.PostCreateView.as_view(), name='create'),
    path('draft/', views.DraftView.as_view(), name='draft'),
    path('post/', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update',views.PostUpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete',views.PostDeleteView.as_view(), name='delete'),
    path('post/publish/<int:pk>',views.PostPublishView, name='publish'),
    path('login/',views.StaffLoginView, name='login'),
    path('logout/',views.StaffLogoutView, name='logout'),
]