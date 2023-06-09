"""TP_codoAcodo_grupo12 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from tasks import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('accesories/', views.accesories, name='accesories'),
    path('eliminar-accesorio/', views.eliminar_accesorio, name='eliminar_accesorio'),
    path('buscar-accesorios/', views.buscar_accesorios, name='buscar_accesorios'),
    path('buscar_acc_brand_cat/', views.buscar_acc_brand_cat, name='buscar_acc_brand_cat'),
    path('cars/', views.cars , name='car'),
    path('login/', views.login_user , name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('accesories/add', views.add_accessory, name='add_accessory'),
    path('consulta-enviada/<str:nombre>/', views.consulta_enviada, name='consulta_enviada'),
]
#RUTA PARA PODER MOSTRAR LAS IMAGENES
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)