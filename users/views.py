from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from customers.models import User, Courses, Customers
from customers.forms import CreateUserForm, ChangeUserForm, CreateCoursesForm


__author__ = 'Yevhenii Onoshko'


def courses_list(request):
    queryset_list = Courses.objects.all()
    return render(request, "courses.html", {'queryset_list': queryset_list,
                                            'courses': True})


def change_user(request, user_id):
    user = Customers.objects.get(id=int(user_id))
    form = ChangeUserForm(instance=user)
    if request.method == 'POST':
        form = ChangeUserForm(request.POST, instance=user)
        if form.is_valid():
            user.email = form.cleaned_data['email']
            user.phone = form.cleaned_data['phone']
            user.mobile_phone = form.cleaned_data['mobile_phone']
            user.status = True if form.cleaned_data['status'] == u'True' else False
            user.save()
            return render(request, 'change_user.html', context={'form': form,
                                                                'user_id': user_id,
                                                                'message': 'User changed successfully'})

    return render(request, 'change_user.html', context={'form': form,
                                                        'user_id': user_id})

def delete_user(request, user_id):
    Customers.objects.get(id=int(user_id)).delete()
    return redirect('/')



def create_course(request):
    queryset_list = Courses.objects.all()
    form = CreateCoursesForm()
    if request.method == 'POST':
        form = CreateCoursesForm(request.POST)
        if form.is_valid():
            try:
                course = Courses.objects.get(code=form.cleaned_data['code'])
                raise ValueError('This course already exists. Please try again')
            except:
                course = Courses.objects.create(
                    name=form.cleaned_data['name'],
                    code=form.cleaned_data['code'])
                return render(request, 'create_course.html', context={'form': form,
                                                                      'message': 'Course created successfully'})
    return render(request, "create_course.html", {'form': form,
                                                  'courses': True})


def create_user(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            try:
                user = Customers.objects.get(email=form.cleaned_data['email'])
                raise ValueError('This email address already exists. Please try again')
            except:
                user = Customers.objects.create(
                    name=form.cleaned_data['name'],
                    email=form.cleaned_data['email'],
                    phone=form.cleaned_data['phone'] or None,
                    mobile_phone=form.cleaned_data['mobile_phone'] or None,
                    status=True if form.cleaned_data['status'] == u'True' else False)
                return render(request, 'create_user.html', context={'form': form,
                                                                    'message': 'User created successfully'})
        else:
            return render(request, 'create_user.html', context={'form': form})
    return render(request, 'create_user.html', context={'form': form})


def users_list(request):
    queryset_list = Customers.objects.all()
    query = request.GET.get("q")
    try:
        take = request.GET.get("take")
    except:
        take = False
    if query:
        queryset_list = queryset_list.filter(Q(name__icontains=query))
    else:
        query = u''
    if take and int(take) in (10, 15, 20):
        paginator = Paginator(queryset_list, int(take)) # Show count contacts per page
    else:
        take = 10
        paginator = Paginator(queryset_list, int(take))
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    if u'?' in request.get_full_path('url'):
        url = request.get_full_path('url')[:request.get_full_path('url').find('?') + 1]
        params = request.get_full_path('url')[request.get_full_path('url').find('?'):]
        if u'take' in params:
            url = request.get_full_path('url')[:request.get_full_path('url').find('take')]
        else:
            url = request.get_full_path('url')+ '&'
    else:
        url = request.get_full_path('url') + u'?'
        params = False
    
    context = {
        "query": query,
        'courses': False,
        "url": url,
        'params': params,
        "take": take,
        "object_list": queryset, 
        "title": "List",
        "page_request_var": page_request_var,
    }

    return render(request, "users.html", context)
