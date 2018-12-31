from django.shortcuts import render

def write_review(request):
    return render(request, 'write_review.html')