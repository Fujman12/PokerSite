from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from .models import Article
from django.contrib.auth.decorators import login_required

import facebook
import requests
# Create your views here.

def index(request):
    graph = facebook.GraphAPI(access_token='EAACEdEose0cBAPIdgzbTsyZBee5EZBV2lFaZBsgn0zJek8ZAyA9cQQk3E7h0jwKDntnE5MygBKIQq7wM8s4WzfjPMQy3yh6mZCp9i5ZAsc1ex3gCisrNEzI084Q0SgjIXQ6hc7ZCQ1andFAvsG1fs6P3kTiadK4ZCGSpGXaQW02ZBLOjpYpXcWZAK61ZAiVNlIocSMZD', version='2.7')

    album = graph.get_object(id='709922575777781', fields = 'photos{images}')
    #print(album)
    album_photos = album["photos"]
    all_pictures_in_album =[]

    while(True):
        try:
            for photo in album_photos["data"]:
                for image in photo["images"]:
                    if image["height"] == 320:
                        all_pictures_in_album.append(image["source"])
                        if len(all_pictures_in_album)>= 30:
                            raise KeyError("asdasd")
            album_photos = requests.get(album_photos["paging"]["next"]).json()
            #print(album_photos)
        except KeyError:
            # When there are no more pages (['paging']['next']), break from the
            # loop and end the script.
            break
    print(all_pictures_in_album)
    #context = dict()
    #context['articles'] = Article.objects.all()
    context = dict()
    context['images'] =  all_pictures_in_album

    return render(request, 'main/index.html', context)

@login_required
def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = dict()
    context['article'] = article
    return render(request, 'main/article.html', context)
