from django.urls import path
from app2 import views

urlpatterns=[
    path('hello',views.func2,name="evenpage"),
    path('prime',views.func3,name="evenpage"),
    path('greatest',views.func4,name="evenpage"),
    path('armstrong',views.func5,name="evenpage"),
    path('studentresult',views.func6,name="evenpage"),
]
