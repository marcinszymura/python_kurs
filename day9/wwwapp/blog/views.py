from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from blog.models import Post


def test(request, imie, wiek):
    # imie = request.GET.get('imie')
    # return HttpResponse(f'<html><body><h1>Hello {imie}!!! Twoj wiek: {wiek}</h1></body></html>')
    template_data = {
        't_imie': imie,
        't_wiek': wiek,
    }
    return render(request, 'blog/test.html', template_data)


def homepage(request):

    # posts = Post.objects.all()
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'blog/homepage.html', {'posts': posts})


def post_show(request, slug):
    post = Post.objects.filter(is_published=True).get(slug=slug)
    return render(request, 'blog/post_show.html', {'post': post})







