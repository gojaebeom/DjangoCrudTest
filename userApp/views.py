from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def user_list(request):
    users = User.objects.all()
    return render(request, 'userApp/list.html', context={'users': users})


def user_detail(request, id):
    user = User.objects.get(id=id)
    return render(request, 'userApp/detail.html', context={'user_detail': user})


def user_edit(request, id):
    user = User.objects.get(id=id)
    if request.user.id != user.id:
        print("로그인 안됨!!")
        return render(request, 'home.html', context={'message': '비정상적인 접근입니다'})

    return render(request, 'userApp/edit.html')


def user_delete(request, id):
    user = User.objects.get(id=id)
    if request.user.id != user.id:
        print("로그인 안됨!!")
        return render(request, 'home.html', context={'message': '비정상적인 접근입니다'})

    user.delete()
    return redirect('/')
