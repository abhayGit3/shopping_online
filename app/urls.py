from app import forms
from app.forms import LoginForm
from django.contrib import auth
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordConfirmForm, MyPasswordResetForm

urlpatterns = [
   
    path('', views.ProductView.as_view(), name="home"),
    path('product-detail/<int:pk>',views.ProductDetailView.as_view(), name='product-detail'),
    

    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='cart'),
    path('cart/',views.show_cart, name='showcart'),
    path('pluscart/',views.plus_cart),
    path('minuscart/',views.minus_cart),
    path('removecart/',views.remove_cart),
    

    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='app/password__reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MyPasswordConfirmForm), name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),

    path('kurta/', views.kurta, name='kurta'),
    path('kurta/<slug:data>', views.kurta, name='kurtadata'),
    path('sherwani/', views.sherwani, name='sherwani'),
    path('sherwani/<slug:data>', views.sherwani, name='sherwanidata'),
    path('suit/', views.suit, name='suit'),
    path('suit/<slug:data>', views.suit, name='suitdata'),
    path('kurti/', views.kurti, name='kurti'),
    path('kurti/<slug:data>', views.kurti, name='kurtidata'),
    path('saree/', views.saree, name='saree'),
    path('saree/<slug:data>', views.saree, name='sareedata'),
    path('women_suit/', views.women_suit, name='women_suit'),
    path('women_suit/<slug:data>', views.women_suit, name='women_suitdata'),
    path('boys/', views.boys, name='boys'),
    path('boys/<slug:data>', views.boys, name='boysdata'),
    path('girls/', views.girls, name='girls'),
    path('girls/<slug:data>', views.girls, name='girlsdata'),
    path('brooch/', views.brooch, name='brooch'),
    path('brooch/<slug:data>', views.brooch, name='broochdata'),
    path('mala/', views.mala, name='mala'),
    path('mala/<slug:data>', views.mala, name='maladata'),
    path('safa/', views.safa, name='safa'),
    path('safa/<slug:data>', views.safa, name='safadata'),
    path('juti/', views.juti, name='juti'),
    path('juti/<slug:data>', views.juti, name='jutidata'),
    path('jewellery/', views.jewellery, name='jewellery'),
    path('jewellery/<slug:data>', views.jewellery, name='jewellerydata'),
    path('kamarpatta/', views.kamarpatta, name='kamarpatta'),
    path('kamarpatta/<slug:data>', views.kamarpatta, name='kamarpattadata'),
    path('earrings/', views.earrings, name='earrings'),
    path('earrings/<slug:data>', views.earrings, name='earringsdata'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm), name='login' ),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('customerregistration/',views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('feedback/',views.FeedbackView.as_view(), name='feedback'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/',views.payment_done, name='paymentdone'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
