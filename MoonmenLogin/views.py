from django.http import HttpResponse
from django.shortcuts import render
from social_core.backends.github import GithubOAuth2
from github import Github
from MoonmenLogin.forms import HomeForm,InfoHome
from MoonmenLogin.models import User
import requests


def index(request):
	return HttpResponse("<h1>This is login page</h1>")
def home(request,*args,**kwargs):
	
	return render(request,'WelcomePage.html')

def getName(request):
	if request.method == 'POST' and 'name' in request.POST:
		form1 = HomeForm(request.POST)
		#form2 = HomeForm(request.POST,prefix="loginInfo")
		if form1.is_valid():
			name=form1.cleaned_data['name']
			print(name)
			g = Github("c9ee585605e7c3bbc49d312e7275a9463ff07d21")
			users = g.search_users(name, location="India")[0:10]
			# for user in users:
			# 	print(user.avatar_url)
			return render(request,'GithubUserSearch.html',{'data':users})
			# if form2.is_valid():
			# 	loginInfo=form2.cleaned_data['loginInfo']
			# return render(request,'GithubUserSearch.html',{'data':users,'loginInfo':loginInfo})

	else:
			form1 = HomeForm()
			
	

	if request.method=='POST' and 'loginInfo' in request.POST:
		#print("sandhya")
		form1 = InfoHome(request.POST)
		if form1.is_valid():
			#print("hello")
			userdetails=[]
			loginInfo=form1.cleaned_data['loginInfo']
			#print(loginInfo)
			
			detail=loginInfo.split(",")		
			#print(detail[0])
			url = "https://api.github.com/users/%s" %detail[0]
			print(url)
			response = requests.get(url)
			geodata = response.json()
			created_date = geodata['created_at']
			u=User.objects.create(username=detail[0],usertype=detail[1],userAvatarUrl=detail[2],createdDate=created_date[:10])
			u.save()
	else:
		form1 = InfoHome()

	all_users=User.objects.all()
	for user in all_users:
		print (user.username)
	return render(request, 'GithubUserSearch.html', {'form1': form1,'all_users':all_users})