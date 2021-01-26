from django.shortcuts import render
from movieapp.forms import MoviedetailsForm


def homepage_movie(request):
	return render(request=request, template_name='movieapp/homepage.html')



def addmovie_details(request):

	movie_form=MoviedetailsForm()
    

	
     #inorder to collect the data
	if request.method=='POST':
		form_data=MoviedetailsForm(request.POST)
		if form_data.is_valid():
			form_data.save(commit=True)

		#to display on the server end
	if request.method=='POST':
		form_data=MoviedetailsForm(request.POST)
		if form_data.is_valid():
			print(f'releasedate:{form_data.cleaned_data["releasedate"]}')
			print(f'moviename:{form_data.cleaned_data["moviename"]}')
			print(f'hero:{form_data.cleaned_data["hero"]}')
			print(f'heroine:{form_data.cleaned_data["heroine"]}')
			print(f'rating:{form_data.cleaned_data["rating"]}')


	


	my_dict={'movie_form':movie_form}
	return render(request=request, template_name='movieapp/addmovie.html',context=my_dict)


from movieapp.models import Moviedetails

def listofmovies_details(request):
	movie_data=Moviedetails.objects.all()
	my_dict={'movie_data':movie_data}


	return render(request=request, template_name='movieapp/listofmovies.html',context=my_dict) 



# Create your views here.
