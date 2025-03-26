from django.http import HttpResponse
from django.shortcuts import render, redirect

from video.models import Video, Category, Comment as CommentModel

from django.views import View

# Create your views here.


def index(request):
    videos = Video.objects.filter(category__categoryName='电视剧')
    # print(videos)
    return render(request, 'index.html', {'videos': videos})


def video_list_default(request):
    category = Category.objects.all()
    videos = Video.objects.filter(category__id=category.first().id)
    return render(request, 'list.html', {'category': category, 'videos': videos})


def video_list(request, categoryId):
    category = Category.objects.all()
    videos = Video.objects.filter(category__id=categoryId)
    # print(videos)
    return render(request, 'list.html', {'category': category, 'videos': videos})


def video_details(request, video_id):
    video_target = Video.objects.get(id=video_id)
    # video_history = request.user.video.filter(id=video_id)
    # print(video_history)
    request.user.video.add(video_target)

    comments = CommentModel.objects.all()
    return render(request, 'details.html', {'video': video_target, 'comments': comments, 'video_id': video_id})


def delete_history(request, video_id):
    request.user.video.remove(video_id)
    return redirect('/user/my/')


class Comment(View):
    def get(self, request, video_id):
        return render(request, 'comment.html', {'video_id': video_id})

    def post(self, request, video_id):
        title = request.POST.get('title')
        content = request.POST.get('content')
        # print(title, content)
        # print(video_id)
        CommentModel.objects.create(
            user=request.user,
            commentTitle=title,
            commentContent=content,
            video=Video.objects.get(id=video_id)
        )
        return redirect(f'/video/details/{video_id}')
        # return HttpResponse('创建评论对象')
