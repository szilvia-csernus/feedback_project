from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating"
        }
        error_messages = {
            "user_name": {
                "required": "Your name is required",
                "max_length": "Please enter a shorter name"
            },
            "review_text": {
                "required": "Your feedback is required",
                "max_length": "Please enter a shorter feedback"
            },
            "rating": {
                "required": "Your rating is required"
            }
        }