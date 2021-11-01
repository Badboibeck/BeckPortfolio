from django.shortcuts import render


def about(request):
    return render(
        request,
        'about.html',
        {
            'title': 'About Me',
            'name': 'Chandler G. Beck',
        }
    )


def resume(request):
    return render(
        request,
        'resume.html',
        {
            'title': 'Resume',
            'name': 'Chandler G. Beck',
        }
    )