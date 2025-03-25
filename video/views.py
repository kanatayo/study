from django.shortcuts import render

from video.models import Video


# Create your views here.


def index(request):
    videos = Video.objects.filter(category__categoryName='电视剧')
    print(videos)
    return render(request, 'category_video.html', {'videos': videos})


