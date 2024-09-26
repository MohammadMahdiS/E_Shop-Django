from django.urls import path
from .views import CurrentDateTime, Saturday, Sunday, Days, DynamicDays, MonthDay, ArrayDay, DayByNumber, DayRedirect, DaysList, DayTemplateView

urlpatterns = [
    path('', CurrentDateTime, name="now-time"),
    path('sunday', Sunday),
    path('saturday', Saturday),
    path('<str:day>', Days),
    path('dynamic/<day>', DynamicDays),
    path('monthday/<day>/<month>', MonthDay),
    path('enter/<int:day_num>', DayByNumber),
    path('enter/<str:day_name>', ArrayDay),
    path('redirect/<int:day_num>', DayRedirect),
    path('daylist', DaysList),
    path('template/<day>', DayTemplateView),
]