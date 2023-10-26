from django.shortcuts import render, redirect ,get_object_or_404
from .models import Employee
from .models import Event
from .models import News, NewsImage
from .models import Notification
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import date
#home
def index(request):
    # employees = Employee.objects.all()
    evt = Event.objects.all().order_by('-date')[:3]
    
    nws = News.objects.all().order_by('-id')[:3]
    return render(request, 'index.html',{'events': evt,'news': nws})

def news(request,nw_id):
    nw = get_object_or_404(News, pk=nw_id)
    nws = News.objects.all().order_by('-id')[:3]
    return render(request, 'news.html',{'news': nw,'newses': nws})

def events(request,ev_id):
    ev = get_object_or_404(Event, pk=ev_id)
    evt = Event.objects.all().order_by('-date')[:3]
    return render(request, 'events.html',{'eventses': evt,'evt': ev})

def faculty(request,dept):
    employees = Employee.objects.filter(department=dept)
    return render(request, 'faculty.html',{'employees':employees})
def club(request):
    # employees = Employee.objects.all()
    return render(request, 'nss.html')
def fitness(request):
    # employees = Employee.objects.all()
    return render(request, 'fitness.html')
def bhoomi(request):
    # employees = Employee.objects.all()
    return render(request, 'bhoomi.html')
def courses(request):
    # employees = Employee.objects.all()
    return render(request, 'courses.html')
def notification(request):
    noti = Notification.objects.all().order_by('-id')
    return render(request, 'notification2.html',{'notifications':noti})
def notification2(request ,noti_id):
    notification = get_object_or_404(Notification, pk=noti_id)

    return render(request, 'notifications.html', {'notification': notification})
    # return render(request, 'notifications.html',{'notification':noti2})

#Employee
def create_employee(request):
    if request.method == 'POST':
        # Extract data from the request
        name = request.POST.get('name')
        position = request.POST.get('position')
        department = request.POST.get('department')
        photo = request.FILES['photo']
        qualification = request.POST.get('qualification')

        # Create and save a new Employee instance
        employee = Employee(name=name, position=position, photo=photo, qualification=qualification,department=department)
        employee.save()

        return redirect('employee_list')  # Redirect to the list view

    return render(request, 'create_employee.html')
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def update_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        position = request.POST.get('position')
        photo = request.FILES.get('photo')
        qualification = request.POST.get('qualification')
        department = request.POST.get('department')
        employee.name = name
        employee.position = position
        employee.department = department
        if photo:
            employee.photo = photo

        employee.qualification = qualification
        employee.save()
        return redirect('employee_list')

    return render(request, 'update_employee.html', {'employee': employee})

def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    employee.delete()
    return redirect('employee_list')

#Event

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def event_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        time = request.POST.get('time')
        date = request.POST.get('date')
        description = request.POST.get('description')
        venue = request.POST.get('venue')
        url = request.POST.get('url')

        event = Event(title=title, time=time, date=date, description=description, venue=venue, url=url)
        event.save()
        return redirect('event_list')
    return render(request, 'event_create.html')

def event_update(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        event.title = request.POST.get('title')
        event.time = request.POST.get('time')
        event.date = request.POST.get('date')
        event.description = request.POST.get('description')
        event.venue = request.POST.get('venue')
        event.url = request.POST.get('url')
        event.save()
        return redirect('event_list')
    return render(request, 'event_update.html', {'event': event})

def event_delete(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    return redirect('event_list')

#News
def news_list(request):
    news_articles = News.objects.all()
    return render(request, 'news_list.html', {'news_articles': news_articles})

def create_news(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        d = date.today()
        # Create the news article
        news_article = News.objects.create(title=title, description=description,date=d)

        # Handle multiple image uploads
        for image_file in request.FILES.getlist('photos'):
            NewsImage.objects.create(news_article=news_article, image=image_file)

        return redirect('news_list')

    return render(request, 'create_news.html')

def update_news(request, pk):
    article = get_object_or_404(News, pk=pk)

    if request.method == 'POST':
        # Update the text fields (title and description)
        article.title = request.POST['title']
        article.description = request.POST['description']
        article.save()

        # Handle multiple image uploads
        for image_file in request.FILES.getlist('photos'):
            NewsImage.objects.create(news_article=article, image=image_file)

        # Redirect to the news list view or another appropriate page
        return redirect('news_list')

    return render(request, 'update_news.html', {'article': article})

# news/views.py


def delete_news(request, pk):
    event = get_object_or_404(News, pk=pk)
    event.delete()
    return redirect('news_list')

#Notificationreturn redirect('news_list')
def create_notification(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        title = request.POST.get('title')
        description = request.POST.get('description')
        file = request.FILES.get('file')
        
        notification = Notification(category=category, title=title, description=description, file=file)
        notification.save()
        return redirect('list_notifications')
        return JsonResponse({'message': 'Notification created successfully'})
    return render(request, 'notification_create.html')
@csrf_exempt
def update_notification(request, notification_id):
    notification = get_object_or_404(Notification, pk=notification_id)

    if request.method == 'POST':
        category = request.POST.get('category')
        title = request.POST.get('title')
        description = request.POST.get('description')
        file = request.FILES.get('file')

        # Update the notification attributes
        notification.category = category
        notification.title = title
        notification.description = description

        if file:
            notification.file = file

        # Save the updated notification
        notification.save()

        # Redirect to the list of notifications
        return redirect('list_notifications')

    return render(request, 'notification_update.html', {'notification': notification})

@csrf_exempt
def delete_notification(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    notification.delete()
    return redirect('list_notifications')
    # return JsonResponse({'message': 'Notification deleted successfully'})

def list_notifications(request):
    notifications = Notification.objects.all()
    return render(request, 'notification_list.html', {'notifications': notifications})