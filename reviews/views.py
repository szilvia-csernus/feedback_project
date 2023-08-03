from typing import Any, Dict
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .models import Review

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        
        return render(request, 'reviews/review.html', {
            'form': form
        })
        
    def post(self, request):
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('thank_you')
        
        else:
            return render(request, 'reviews/review.html', {
                'form': form
    })

# def review(request):
    
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
        
#         if form.is_valid():
#             form.save()
            
#             return HttpResponseRedirect('thank_you')
    
#     else:
#         form = ReviewForm()
    
#     return render(request, 'reviews/review.html', {
#         'form': form
#     })


class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'This works!'
        return context
    
    
class ReviewListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews'
    
    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=3)
    #     return data
    
    
class SingleReview(DetailView):
    template_name = 'reviews/single_review.html'
    model = Review
    context_object_name = 'review'
