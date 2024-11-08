from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
# def index(request):
#     return HttpResponse("hello world")
# def about(request):
#     return HttpResponse ("hi Ansu,Welcome")
# def contact(request):
#     return HttpResponse ("hi Adarsh")

# def self1(request):
#     return render (request,'self.html')

@login_required()
def home1(request):
    return render(request,'home.html')

def base(request):
    return render(request,'base.html')

# def contact(request):
#     return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def booking(request):
    return render(request,'booking.html')
def departments(request):
    dict1 = {
        'dept':department.objects.all()
    }
    return render (request,'department.html',dict1)

# def doctors(request):
#     return render(request,'doctors.html')

# def basic(request):
#     var1={}
#     var1['name']='Deertha'
#     var1['age']='22'
#     var1['Address']='Thiruvananthapuram'
#     var1['products']=['book','pen','pencil']
#     var1['gender']=1
#     var1['phone']='123456789'

#     return render(request=request, template_name='context.html',context=var1)

def create_todo(request):
    if request.method == 'GET' :
        return render (request, 'booking.html')
    elif request.method == 'POST':
        title1= request.POST['title']
        description = request.POST.get( 'des', None)
        rating = request.POST.get('rating', None)
        status = request.POST.get('status', 'off')
        if status == 'on':
            status = True
        else:
            status = False
        todo = Todo(title=title1, description=description, rating=rating, status=status)
        todo.save()
        return HttpResponse('<h1>Completed</h1>')
    
def create_contact(request):
    if request.method == 'GET' :
        return render (request, 'contact.html')
    elif request.method == 'POST':
        Name1= request.POST['Name']
        phone_number1 = request.POST.get( 'phone_number',None)
        Contact = contact(Name=Name1, phone_number=phone_number1)
        Contact.save()
        return HttpResponse('<h1>Completed</h1>')

from .forms import BookingForm

def bookingss(request):
    if request.method == "POST" :
        form = BookingForm(request. POST)
        if form. is_valid():
            form.save()
    form = BookingForm()
    dict_form = {
            'form': form
    }
    return render (request, 'login', dict_form)

from .models import *
# def departments (request):
#     dict1= {
#     'dept' : department.objects.all()
#     }
#     return render (request, 'department.html' ,dict1)
from django.views.generic import ListView
class Tasklistviews(ListView):
    model = department
    template_name = 'department.html'
    context_object_name = 'dept'

from django.views.generic.detail import DetailView
class TaskDetailview(DetailView):
    model = department
    template_name = 'depart_detail.html'
    context_object_name = 'dept'

from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
class TaskUpdateView(UpdateView):
    model = department
    template_name = 'update.html'
    fields = ('dep_name','description')

    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs = {'pk':self.object.id})
    

class TaskDeleteView(DeleteView):
    model = department
    template_name = 'delete.html'
    success_url = reverse_lazy('home1')

from django.views.generic.edit import CreateView 
class EmployeeCreate (CreateView):
    model = department
    template_name = 'create_view.html'
    fields = '__all__'
    success_url = reverse_lazy ('home1' )

def doctor (request) :
    dict_docs = {
    'doctors': Doctors.objects.all
    }
    return render (request, 'doctors.html', dict_docs)

from django.urls import reverse
from .forms import CustomUserCreationForms
from django.shortcuts import render,redirect

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home1')
    form = CustomUserCreationForms()
    if request.method == 'POST':
        form = CustomUserCreationForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    return render(request,'register.html',{'form':form})