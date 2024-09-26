from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
import datetime
from django.shortcuts import render
from django.template.loader import render_to_string

def CurrentDateTime(request):
    now = datetime.datetime.now()
    html = "<html><body> It is now %s. </body></html>" %now
    return HttpResponse(html)


def my_view(request):
    foo = ""
    if foo:
        return HttpResponseNotFound("<h1>Page Not Found</h1>")
    else:
        return HttpResponse("<h1>Page was found</h1>")
    

def detail(request, poll_id):
    Poll = ["jim, jessy"]
    try:
        p = Poll.objects.all(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404("poll does not exist")
    return render(request, "polls/detail.html", {"poll": p})

def Days(request, day):
     if day == "saurday":
        return HttpResponse("this day is Saturday")
     if day == "sunday":
        return HttpResponse("this day is a Sunday")
     if day == "monday":
          return HttpResponse("this day is monday")
     
def Saturday(requst):
        return HttpResponse("this day is Saturday")

def Sunday(request):
        return HttpResponse("this day is a Sunday")

def DynamicDays(request, day):
     return HttpResponse(day)

def MonthDay(request, day, month):
     return HttpResponse(f"day is {day} and month is {month}" )

days = {
     'saturday': 'this day is saturday',
     'sunday': 'this day is sunday',
     'monday': 'this day is monday',
     'tuesday': 'this day is tuesday',
     'wendsday': 'this day is wendsday',
     'thursday': 'this day is thursday',
     'friday': 'this day is friday'
}

def ArrayDay(request, day_name):
     name = days.get(day_name)
     if name is not None:
          return HttpResponse(name)
     else:
          return HttpResponseNotFound("Response should be day name")
     

def DayByNumber(request, day_num):
    try:
        day_num = int(day_num)
        if 0 <= day_num < len(days):
            key, value = list(days.items())[day_num]              
            return HttpResponse(f"Day: {key} , Message: {value}")
        else:
            return HttpResponseNotFound("Invalid day number")
    except ValueError:
        return HttpResponseNotFound("Day number must be integer")
          
def DayRedirect(request, day_num):
     days_name = list(days.keys())
     print(days_name)
     redirect_day = days_name[day_num - 1]
     return HttpResponseRedirect(f"{redirect_day}")

def DaysList(request):
     content = """
        <ul>
            <li>
              <a href="/enter/saturday> Saturday </a>
             </li>
        </ul>
        """
     return HttpResponse(content)

def DayTemplateView(request, day):
     days_data = days.get(day)
     context = { "day_data" : days_data}
     if days_data is not None:
          return render(request, 'challenges/challenges.html', context)
        #   response_data = render_to_string('challenges/challenges.html')
        #   return HttpResponse(response_data)
     return HttpResponseNotFound('days does not exist')
