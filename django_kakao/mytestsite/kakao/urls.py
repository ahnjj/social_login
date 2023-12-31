from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='kakao'),
    path('test/', views.test),
    path('kakaoLoginLogic/', views.kakaoLoginLogic),
    path('kakaoLoginLogicRedirect/', views.kakaoLoginLogicRedirect),
    path('kakaoLogout/', views.kakaoLogout),
    path('kakaoPay/', views.kakaoPay),
    path('kakaoPayLogic/', views.kakaoPayLogic),
    path('paySuccess/', views.paySuccess),
    path('payFail/', views.payFail),
    path('payCancel/', views.payCancel),
    # FLutter & Django
    path('kakaoPayLogic2/', views.kakaoPayLogic2),
    path('paySuccess2/', views.paySuccess2),
    # GET | POST - Methods / Params | QueryString
    path('methodsCheck/<int:id>', views.methodsCheck),
]