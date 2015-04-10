from datetime import datetime
import json
from django.shortcuts import render
from django.http import JsonResponse,Http404
from django.views.decorators.csrf import csrf_exempt
from todos_api.models import Todo,User
# Create your views here.

@csrf_exempt
def index_view(request):
    return render(request,'todos_api/index.html')

@csrf_exempt
def invalid_url(request):
    raise Http404("Invalid url.")

@csrf_exempt
def list(request,key):
    try:
        User.objects.get(key=key)
    except User.DoesNotExist:
        return Http404("That user key is invalid.")
    todos = Todo.objects.filter(user__key=key)
    if todos:
        for todo in todos:
            todo_list.append({
                'todo':[
                    {'id': todo.id},
                    {'name':todo.name},
                    {'description':todo.description},
                    {'status': todo.status}
                ]
            }) 
    else:
        todos =  'Nothing to do.'
    return JsonResponse({'todos': todo_list})

@csrf_exempt
def incomplete(request,key):
    try:
        User.objects.get(key=key)
    except User.DoesNotExist:
        raise Http404("That user key is invalid.")
    todos = Todo.objects.filter(user__key=key).exclude(status=True)
    if todos:
        for todo in todos:
            todo_list.append({
                'todo':[
                    {'id': todo.id},
                    {'name':todo.name},
                    {'description':todo.description},
                    {'status': todo.status}
                ]
            })  
    else:
        todo_list = 'Nothing to do.'
    return JsonResponse({'todos': todo_list})

@csrf_exempt
def date(request,key,date):
    try:
        User.objects.get(key=key)
    except User.DoesNotExist:
        raise Http404("That user key is invalid.")
    date = datetime.strptime(date,'%m-%d-%Y')
    todos = Todo.objects.filter(user__key=key).filter(created_at=date.date())
    if todos:
        for todo in todos:
            todo_list.append({
                'todo':[
                    {'id': todo.id},
                    {'name':todo.name},
                    {'description':todo.description},
                    {'status': todo.status}
                ]
            }) 
    else:
        todo_list = 'Nothing to do.'
    return JsonResponse({'todos': todo_list})

@csrf_exempt
def add(request,key):
    try:
        user = User.objects.get(key=key)
    except User.DoesNotExist:
        raise Http404("That user key is invalid.")
    todo = Todo.objects.create(
        name=request.POST['name'], 
        description=request.POST['description'],
        user=user
    )
    return JsonResponse({
        'todos':[
                {'todo':[todo.id,
                todo.name,
                todo.description,
                todo.status]}
        ]
    })
    # return JsonResponse({
    #     'todos':[
    #         {'id': todo.id},
    #         {'name':todo.name},
    #         {'description':todo.description},
    #         {'status': todo.status}
    #     ]
    # })

@csrf_exempt
def update(request,key,todo_id):
    try:
        user = User.objects.get(key=key)
    except User.DoesNotExist:
        raise Http404("That user key is invalid.")
    try:
        todo = Todo.objects.get(pk=todo_id)
    except Todo.DoesNotExist:
        raise Http404("Invalid Todo.")
    todo.name = name 
    todo.description = description 
    todo.status = status
    todo.save()
    return JsonResponse({
        'todos':[
            {'id': todo.id},
            {'name':todo.name},
            {'description':todo.description},
            {'status': todo.status}
        ]
    })

@csrf_exempt
def delete(request,key,todo_id):
    try:
        User.objects.get(key=key)
    except User.DoesNotExist:
        raise Http404("That user key is invalid.")
    try:
        todo = Todo.objects.get(pk=todo_id)
    except Todo.DoesNotExist:
        raise Http404("Invalid Todo.")
    todo.delete()
    return JsonResponse({
        'todo':[
            {'id': todo.id},
            {'name':todo.name},
            {'description':todo.description},
            {'status': todo.status}
        ]
    })

@csrf_exempt
def done(request,key,todo_id):
    # any user can mark any task done
    try:
        User.objects.get(key=key)
    except User.DoesNotExist:
        raise Http404("That user key is invalid.")
    try:
        todo = Todo.objects.get(pk=todo_id)
    except Todo.DoesNotExist:
        raise Http404("Invalid Todo.")
    todo.status = True
    todo.save()
    return JsonResponse({
        'todo':[
            {'id': todo.id},
            {'name':todo.name},
            {'description':todo.description},
            {'status': todo.status}
        ]
    })

@csrf_exempt
def new_user(request):
    user = User.objects.create(
        username=request.POST['username'],
        password=request.POST['password']
    )
    return JsonResponse({'user_key': user.key})

@csrf_exempt
def sign_in(request):
    try:
        user = User.objects.get(username=request.POST['username'])
    except User.DoesNotExist:
        raise Http404("Invalid username.")
    if request.POST['password'] == user.password:
        return JsonResponse({'user_key': user.key})
    return JsonResponse({'Invalid': 'Username/password do not match.'})

@csrf_exempt
def log_out(request):
    request.session.flush()
    return JsonResponse({'log_out': 'good bye'})