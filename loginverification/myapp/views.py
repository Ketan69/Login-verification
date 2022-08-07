from django.shortcuts import render
from django.http import HttpResponse
from .models import id
from random import *
from django.conf import settings
from django.core.mail import send_mail


def home(req):
 return render(req,'home.html',{})

def log(req):
 if 'signin' in req.POST:
  try:
   print(req.POST['passwd'])
   a=id.objects.get(loginid=req.POST['id'])
   if req.POST['passwd']!=a.password:
    raise ValueError
   html='''LOGIN SUCCESSFULLY<br><br><a href='/'>LOGOUT</a>'''
   return HttpResponse(html)
  except Exception as e:
   print(str(e))
   html='''invalid Id or Password <a href='/'>try again</a>'''
   return HttpResponse(html)
 else:
  return render(req,'detail.html',{})
  
def detail(req):
 try:
  a=id.objects.get(loginid=req.POST['id'])
  html='''Login-Id already exists <a href='/log'>try again</a>'''
  return HttpResponse(html)
 except:
  if req.POST['passwd']!=req.POST['rpasswd']:
   html='''Password didn't match <a href='/log'>try again</a>'''
   return HttpResponse(html)
  try:
   r=randint(999,9999)
   send_mail('OTP','str(r)',settings.EMAIL_HOST_USER,[req.POST['eid']]) 
  except BaseException as e:
   print(e)
   html='''Invalid Email-Id <a href='/log'>try again</a>'''
   return HttpResponse(html) 
  return render(req,'verify.html',{'id':req.POST['id'],'passwd':req.POST['passwd'],'nam':req.POST['nam'],'eid':req.POST['eid'],'num':req.POST['num']})     
    
def verify(req):
 if req.POST['otp']!=str(r):
  html='''Wrong otp <a href='/detail'>try again</a>'''
  return HttpResponse(html)
 else:
  id(req.POST['id'],req.POST['passwd'],req.POST['nam'],req.POST['eid'],int(req.POST['num'])).save()
  html='''Account created Successfully<a href='/'>login</a>'''
  return HttpResponse(html)      

def forgot(req):
  return render(req,'forgot.html',{})  

def fore(req):
 try:
  print(req.POST['id'])
  r=randint(999,9999)
  send_mail('OTP',str(r),settings.EMAIL_HOST_USER,[req.POST['id']]) 
 except BaseException as e:
  print(str(e))
  html='''Invalid Email-Id <a href='/forgot'>try again</a>'''
  return HttpResponse(html)
 return render(req,'new.html',{})

def new(req):
 if req.POST['otp']!=str(r):
  html='''Wrong OTP <a href='/forgot'>try again</a>'''
  return HttpResponse(html)
 return render(req,'confirm.html',{})

def confirm(req):
 try:
  a=id.objects.get(loginid=req.POST['id'])
  if req.POST['passwd']!=req.POST['rpasswd']:
   raise ValueError  
 except ValueError as e:
  html='''Password doesn't match <a href='/confirm'>try again</a>'''
  return HttpResposne(html)
 except:
  html='''Invalid loginid <a href='/confirm'>try again</a>''' 
  return HttpResposne(html) 
 a.passwd=req.POST['passwd']
 a.save()
 return HttpResponse('Password changed Successfully..<a href='/'>Login</a>')
   