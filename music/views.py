from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1>this is the homepage")

def detail(request,album_id):
	return HttpResponse("<h2>Details for ALbum id: "+str(album_id)+"</h2>")
