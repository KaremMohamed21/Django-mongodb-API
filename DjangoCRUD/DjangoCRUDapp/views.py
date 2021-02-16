from bson import ObjectId
from django.http import HttpResponse
from django.shortcuts import render
from DjangoCRUDapp.models import Post


# Create your views here.
def welcome_page(request):
    return HttpResponse("Welcome to Django!")


def add_post(request):
    comment = request.POST.get("comment").split(",")
    tags = request.POST.get("tags").split(",")
    user_details = {"first_name": request.POST.get("first_name"), "last_name": request.POST.get("last_name")}
    post = Post(post_title=request.POST.get("post_title"), post_description=request.POST.get("post_description"),
              comment = comment, tags = tags, user_details = user_details)
    post.save()
    return HttpResponse("CREATED!")


def update_post(request, id):
    post = Post.objects.get(id=ObjectId(id))
    post.user_details['first_name'] = request.POST.get('first_name')
    post.save()
    return HttpResponse("Post Updated")


def delete_post(request, id):
    post = Post.objects.get(id=ObjectId(id))
    post.delete()
    return HttpResponse("Post Deleted")


def read_post(request, id):
    post = Post.objects.get(id=ObjectId(id))
    stringval = "First Name : " + post.user_details['first_name'] + " Last name : " + post.user_details[
        'last_name'] + " Post Title " + post.post_title + " Comment " + post.comment[0]
    return HttpResponse(stringval)


def read_post_all(request):
    posts = Post.objects.all()
    stringval = ""
    for post in posts:
        stringval += "First Name : " + post.user_details['first_name'] + " Last name : " + post.user_details[
            'last_name'] + " Post Title " + post.post_title + " Comment " + post.comment[0] + "<br>"

    return HttpResponse(stringval)
