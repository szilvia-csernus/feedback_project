from django.shortcuts import render

def review(request):
    
    if request.method == 'POST':
        entered_username = request.POST['username']
        print(entered_username)
        return redirect('review')
    
    return render(request, 'reviews/review.html')


def thank_you(request):
    return render(request, 'reviews/thank_you.html')
