from django.http import HttpResponse
from django.shortcuts import render

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import simplejson as json
from django.http import JsonResponse

from social_core.backends.github import GithubOAuth2
from github import Github


from MoonmenLogin.forms import seachUser_form,saveData_form
from MoonmenLogin.models import User
import requests



def home(request,*args,**kwargs):
	
	return render(request,'WelcomePage.html') #welcome page 






def searchUser(request):
	"""
	Handling post request "name" sent from text box
	"""
	if request.method == 'POST' and 'name' in request.POST:
		form1 = seachUser_form(request.POST)
		if form1.is_valid():
			name=form1.cleaned_data['name']
			g = Github("ea40562a136a8f0693eb99149b40c846ad9202f6") #github access token
			users = g.search_users(name, location="India")[0:10] #searching the user based on the "name"
			return render(request,'GithubUserSearch.html',{'data':users}) #rendering the searched data to respective html page

	else:
		
		#Handling the get request showing the details of 
		
		form1 = seachUser_form()
	
	if request.method=='POST' and 'loginInfo' in request.POST:
		"""
		Handling the post request sent after selecting radio button
		"""
		form1 = saveData_form(request.POST)
		if form1.is_valid():
			loginInfo=form1.cleaned_data['loginInfo'] #accepting the sent data
			detail=loginInfo.split(",") #splitting the data 
			url = "https://api.github.com/users/%s" %detail[0]   #making api based on the loginName 
			geodata = requests.get(url).json() #fetching the deatils of json 
			created_date = geodata['created_at']  #taking out only created_at 

			u=User.objects.create(username=detail[0],usertype=detail[1],userAvatarUrl=detail[2],createdDate=created_date[:10]) # saving the fields in database
			u.save()
	else:
		form1 = saveData_form() #handling get request

	all_users=User.objects.all()# all users details fetched
	return render(request, 'GithubUserSearch.html', {'form1': form1,'all_users':all_users}) # rendered on template


@api_view(['GET', 'POST', ])
def getName(request):
	global reqName
	if(request.method=='POST'):
		try:
			reqName=str(request.body)  #for the requested name
			start=reqName.find('b')+2
			end=reqName.find('"')
			reqName=reqName[start:end] #eleminated unwanted characters
			return Response(status.HTTP_201_CREATED)
		except ValueError as e:
			return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
	if(request.method=='GET'):
		try:
			g = Github("debfdbf49ce456a73bf99c5c3a44ea9afcbaae2d")
			users = g.search_users(reqName, location="India")[0:10] #users search
			userList=[]
			for x in users:
				userList.append(x.login)
			return Response(userList,status.HTTP_201_CREATED) #sending to vue interface
		except ValueError as e:
			return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
