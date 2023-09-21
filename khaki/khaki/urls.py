
from django.contrib import admin
from django.urls import path
from khaki import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.home,name='home'),
    path("signup/",views.signup,name='signup'),
    path("login/",views.Login,name='login'),
    path('forgetpassword/',views.forgetPassword,name='forgetpassword'),
    path('account/',views.account,name='account'),
    path('about/',views.AboutUs,name='about'),
    path('cart/<slug>/',views.cart,name='cart'),
    path('cartview/',views.cart,name='cartview'),
    path('changepassword/',views.changePassword,name='changepassword'),
    path('checkout/',views.checkOut,name='checkout'),
    path('checkoutwhitelist/<int:id>/',views.checkOut,name='checkoutwhitelist'),
    path('checkoutsingle/<slug>/',views.checkOut,name='checkoutsingle'),
    path('contact/',views.contact,name='contact'),
    path('orders/',views.orders,name='orders'),
    path('product/<slug>/',views.product,name='product'),
    path('refund/',views.refund,name='refund'),
    path('shop/',views.shop,name='shop'),
    path('terms/',views.terms,name='terms'),
    path('logout/',views.logoutUser,name='logout'),
    path('whitelist/<slug>/',views.Whitelist,name='whitelist'),
    path('whitelistview/',views.Whitelist,name='whitelistview'),
    path('deletecartitem/<slug>/',views.DeleteCartItem,name='deletecartitem'),
    path('printbill/<int:id>/',views.PrintBill,name='printbill'),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
