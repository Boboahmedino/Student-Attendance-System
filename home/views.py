from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Attendance, Level, Course, Category
from django.contrib import messages
import datetime


# for exporting to html

# from django.template.loader import render_to_string
# from weasyprint import HTML
# import tempfile


# Create your views here.

def home(request):
    return render (request, 'home/home.html')

@login_required(login_url='authentication/login')
def attendance(request):
    levels = Level.objects.all()
    courses = Course.objects.all()
    categories = Category.objects.all()
    
    context = {
        'levels' : levels,
        'courses' : courses,
        'categories' : categories,
    }
    if request.method == 'GET':
        return render (request, 'home/dashboard.html', context)
        
    if request.method == 'POST':
        level = request.POST['level']
        course = request.POST['course']
        category = request.POST['category']
        
        
        if request.user.is_authenticated: 
            attend = Attendance(student = request.user, level = level, course = course, category = category)
            attend.save()
            print("Attendance Submitted Succesfully")
            messages.success(request, f"You have submitted {category} for {course} attendance in today's class")
            # messages.success(request, f"You have submitted {course} attendance for today's class")
            return redirect('attendance')
        
    return render (request, 'home/dashboard.html', context)



@login_required(login_url='authentication/login')
def attendance_history(request):
    histories = Attendance.objects.filter(student = request.user)
    context = {
        'histories' : histories,
        'values' : histories
    }
    
    return render(request, 'home/history.html', context)


def export_pdf(request):
    pass
    # response = HttpResponse(content_type = "application/pdf")
    # response['Content-Disposition'] = 'attachment: filename = Attendance Report' + \
    #     str(datetime.datetime.now()) + ".pdf"
    # response["Content-Transfer-Encoding"] = "binary"
    
    # html_string = render_to_string(
    #     "home/pdf_output.html", {'histories' : []})

    # html = HTML(string = html_string)
    
    # result = html.write_pdf()
    # with tempfile.NamedTemporaryFile(delete = True) as output:
    #     output.write(result)
    #     output.flush()        
    #     # to open pdf for reading
    #     output = open(output.name, "rb")
    #     response.write(output.read())
    # return response
    
    
    
    

# @login_required(login_url='authentication/login')
# def password (request):
#     return render(request, 'home/password.html')