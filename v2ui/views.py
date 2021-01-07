from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
import time,datetime
from v2ui import models
import random,string

# Create your views here.
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        ctx={}
        getUser = models.User.objects.filter(user_email=email, user_pass=password)
        userExist=(len(getUser)==1)
        if userExist:
                user_id = getUser[0].user_id
                ctx["user_name"]=getUser[0].user_name
                getUser_money_left = models.Money.objects.get(user_id=user_id)
                money_left = getUser_money_left.money_left
                ctx["money_left"] = money_left
                getLines = models.Line.objects.filter(line_user_id=user_id)
                line_id=[]
                for lines in getLines:
                        line_id.append(lines.line_id)
                ctx["line_id"]=line_id
                return render(request, 'user.html', ctx)
        else:
            html = '''
            <a href='/'>邮箱或者密码错误 点击重新登录</a>
                '''
            return HttpResponse(html)
    else:
        return render(request, 'login.html')

def register(request):
    if request.method=="POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        username = ''.join(random.sample(string.ascii_letters + string.digits, 16))
        contact_type = request.POST.get("contact_type")
        contact_number = request.POST.get("contact_number")
        user_reg_date = datetime.datetime.now()
        try:
            getUserbyEmail = models.User.objects.get(user_email=email)
            if (getUserbyEmail):
                html = '''<a href='/register'>邮箱已经存在 点击重新注册</a>'''
                return HttpResponse(html)
        except:
            insert = models.User(user_name=username, user_pass=password, user_email=email,
                                 user_contact_type=contact_type,
                                 user_contact_num=contact_number, user_reg_date=user_reg_date)
            insert.save()

            user_id = models.User.objects.get(user_email=email).user_id
            Inite_money = models.Money(user_id=user_id,money_total=0,money_left=0)
            Inite_money.save()
            html = '''<a href='/'>注册成功 点击登录</a>'''
            return HttpResponse(html)
    else:
        return render(request, 'register.html')







