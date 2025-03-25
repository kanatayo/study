from django.shortcuts import render

from video.models import Video, Category


# Create your views here.


def index(request):
    videos = Video.objects.filter(category__categoryName='电视剧')
    print(videos)
    return render(request, 'index.html', {'videos': videos})


def video_list(request, categoryName):
    category = Category.objects.all()
    videos = Video.objects.filter(category__categoryName=categoryName)
    print(videos)
    return render(request, 'list.html', {'category': category, 'videos': videos})


def video_details(request, video_id):
    video = Video.objects.get(id=video_id)
    return render(request, 'details.html', {'video': video})