from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import LeaveForm
from .models import Leaves
from accounts.models import Students
# Create your views here.

def get_showing_leaves(request,leaves):
    print("INSIDE LEAVES SHOWING")
    if request.GET and request.GET.get('filter'):
        print("INSIDE LEAVES SHOWING IFFFFFFFFFFF")
        if request.GET.get('filter')=='All':
            print("INDIDE ALLLL")
            return leaves
        if request.GET.get('filter')=='Accepted':
            print("INSIDE ACCEPTED")
            return leaves.filter(action_taken = 'Accept')
        if request.GET.get('filter')=='Rejected':
            return leaves.filter(action_taken = 'Reject')
    return leaves.filter(action_taken = 'Pending')



def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        user = Students.objects.get(username=request.user)
        # print(user.category)
        category = user.category
        leaves = Leaves.objects.all()  
        leaves_user = Leaves.objects.filter (referring_user=request.user)  
        for i in leaves_user:
            print(i)   
        return render(request,'mysite/home.html',{'leaves':get_showing_leaves(request,leaves),'category':category,'leaves_user':leaves_user})


def leave_apply(request):
    print("INSIDE APPLY LEAVE")
    if request.method == 'POST':
        if request.method == 'POST' and 'accept' in request.POST:

            return redirect('home')
        leave_form = LeaveForm(request.POST)
        if leave_form.is_valid():

            # form.cleaned_data['my_form_field_name'] 
            # print form['my_field'].value()
            # print form.data['my_field']
            # print form.cleaned_data['my_field']
            # print form.instance.my_field

            s_date = leave_form.cleaned_data['start_date']
            e_date = leave_form.cleaned_data['end_date']
            object = leave_form.save(commit = False)
            days = e_date-s_date
            print(days.days)
            
            object.days_count = int(days.days)

            # print(leave_form.days_count)
            # print(leave_form.days_count)

            object.referring_user = request.user
            object.save()
            return redirect('home')
    else:
        print("INSIDE APPLY LEAVE else")
        leave_form = LeaveForm()
        # print("LEAVE::",leave_form)

    return render(request,'mysite/leave_apply.html',{'form':leave_form})

def leave_detial(request,id):
    leave = Leaves.objects.filter(pk=id)
    return render(request,'mysite/leave_detail.html',{'leave':leave})


def leave_decision(request,id):
    print('Inside leave_decision')
    leave = Leaves.objects.get(pk=id)
    if request.method =='POST' and 'reject' in request.POST:
        print('Inside REject')
        leave.action_taken = 'Reject'
        leave.status='True'
        leave.save()
        return redirect('home')
    if request.method =='POST' and 'accept' in request.POST:
        print('Inside Accept')
        leave.action_taken = 'Accept'
        leave.status='True'
        leave.save()
        return redirect('home')
    return render(request,'mysite/home.html')


