from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
# 특정 유저객체가 데이터베이스에 있는지 없는지를 판단, 로그인,로그아웃기능 수행해주는 것이 내장되어있음
from .models import User
# 우리가 models.py 에 등록해 준 적은 없지만 장고라는 User라는 객체를 갖고 있음
# superuser 만들었던 거 기억하시나요 -> 그것도 user 모델을 만들어주지 않앗지만 자동으로 어딘가에 들어가짐

def login(request):
    # POST 요청이 들어오면 로그인 처리를 해줌
    if request.method == 'POST':
        userId = request.POST['userid']
        password = request.POST['password']
        # username, password 가 실제 장고에 등록되어있는 회원인지 아닌지 확인해보겠다.
        # 이미 있는 회원이라면 저장되어있다면 유저객체 반환))
        # 그렇지 않다면 none을 반환
        user = authenticate(request, username=userId, password=password)
        if user is not None:
            auth_login(request, user) # 해당 유저 객체로 로그인 (임포트하는 거 말하기)
            return redirect('main')
        else:
            return render(request, 'login.html')

    # Get 요청인 경우는 <a href="{% url 'login' %}">로그인</a>
    # login form 을 담고 있는 login.html 띄워줌
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        user = User()
        if request.POST['password'] == request.POST['confirmPassword']:
            user.username = request.POST['userid']
            user.set_password(request.POST['password'])
            user.nickname = request.POST['nickname']
            user.save()
            return redirect('login')
        return render(request, 'register.html')
    return render(request, 'register.html')

def logout(request):
    auth_logout(request)
    return redirect('main')