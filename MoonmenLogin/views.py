from django.http import HttpResponse
from django.shortcuts import render
from social_core.backends.github import GithubOAuth2
from github import Github
from MoonmenLogin.forms import HomeForm,InfoHome
from MoonmenLogin.models import User
import requests



def home(request,*args,**kwargs):
	
	return render(request,'WelcomePage.html') #welcome page 

def searchUser(request): 
	"""
	Handling post request "name" sent from text box
	"""
	if request.method == 'POST' and 'name' in request.POST:
		form1 = HomeForm(request.POST)
		if form1.is_valid():
			name=form1.cleaned_data['name']
			g = Github("2e7e270662c6f05e06c16f2f40dce8c055f0261d") #github access token
			users = g.search_users(name, location="India")[0:10] #searching the user based on the "name"
			return render(request,'GithubUserSearch.html',{'data':users}) #rendering the searched data to respective html page

	else:
		
		#Handling the get request showing the details of 
		
		form1 = HomeForm()
	
	if request.method=='POST' and 'loginInfo' in request.POST:
		"""
		Handling the post request sent after selecting radio button
		"""
		form1 = InfoHome(request.POST)
		if form1.is_valid():
			loginInfo=form1.cleaned_data['loginInfo'] #accepting the sent data
			detail=loginInfo.split(",") #splitting the data 
			url = "https://api.github.com/users/%s" %detail[0]   #making api based on the loginName 

			response = requests.get(url)#fetching the "created_date" based on the api
			geodata = response.json() #fetching the deatils of json 
			created_date = geodata['created_at']  #taking out only created_at 
			u=User.objects.create(username=detail[0],usertype=detail[1],userAvatarUrl=detail[2],createdDate=created_date[:10]) # saving the fields in database
			u.save()
	else:
		form1 = InfoHome() #handling get request

	all_users=User.objects.all()# all users details fetched
	return render(request, 'GithubUserSearch.html', {'form1': form1,'all_users':all_users}) # rendered on template