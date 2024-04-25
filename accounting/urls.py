from django.urls import path
from accounting.views import AddSubUser, ListSubUser, DestroySubUserView, RetrieveSubUserView, UpdateSubUserView, MeView, RemainAccountView


urlpatterns = [
    path('me/', MeView.as_view(), name='me'),
    path('list-user/', ListSubUser.as_view(), name='list_user'),
    path('add-user/', AddSubUser.as_view(), name='add_user'),
    path('user/<int:pk>/', RetrieveSubUserView.as_view(), name='retrieve-user'),
    path('user/<int:pk>/edit', UpdateSubUserView.as_view(), name='update-user'),
    path('user/<int:pk>/delete', DestroySubUserView.as_view(), name='destroy-user'),

    path('user/<str:username>/remain_account/', RemainAccountView.as_view(), name='remain_account')
]
