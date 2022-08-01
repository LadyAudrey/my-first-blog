from django.shortcuts import render

blogs = [
    {'id':1, 'name':'Learning to code'},
    {'id':2, 'name':'Why learning to code is helping me age gracefully'},
    {'id':3, 'name':'How to think about your code'},
]

def home(request):
    context = {'blogs': blogs}
    return render(request, 'pages/home.html', context)

def blog(request, pk):
    room = None
    for i in blogs:
        if i['id'] == int(pk):
            room = i
    context = {'blog':blog}
    return render(request, 'pages/blog.html', context)