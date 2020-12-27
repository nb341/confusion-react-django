from django.contrib import admin
from django.urls import path, include                 # add this
from rest_framework import routers                    # add this
from dish import views as dv
from comments import views as cv                            # add this
from leaders import views as lv
from promotions import views as pv
from django.conf import settings
from django.conf.urls.static import static



router = routers.DefaultRouter()                      # add this
router.register(r'dishes', dv.DishesView, 'dish')     # add this
router.register(r'comments', cv.CommentsView, 'comment')
router.register(r'leaders', lv.LeadersView, 'leader')
router.register(r'promotions', pv.PromotionsView, 'promotion')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))                # add this
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)