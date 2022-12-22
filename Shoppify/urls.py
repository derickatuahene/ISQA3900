from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.home, name = "home"),
	path('store/', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('login/', views.LoginPage, name='login'),
	path('signup/', views.SignupPage, name = 'signup'),
	path('logout/', views.LogoutPage, name= 'logout'),
	path("reset_password/", auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"), name ="reset_password"),
	path("reset_password_sent/",auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"), name="password_reset_done"),
	path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_change.html"), name = "password_reset_confirm"),
	path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_completed.html"), name= "password_reset_complete"),
]