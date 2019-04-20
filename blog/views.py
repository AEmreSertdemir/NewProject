from django.shortcuts import render

# Create your views here.

def get_post_list(request):
    return render(request, 'blog/post_list.html', {})
