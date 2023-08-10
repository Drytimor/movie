from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'

        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'feedback': 'Отзыв',
            'rating': 'Рейтинг',
        }

        error_messages = {
            'name': {
                'min_length': 'Слишком мало символов,должно быть не меньше %(limit_value)d',
                'max_length': 'Слишком много символов, должно быть не больше %(limit_value)d',
                'required': 'Обязательно к заполнению'
            },
            'surname': {
                'min_length': 'Слишком мало символов,должно быть не меньше %(limit_value)d',
                'max_length': 'Слишком много символов, должно быть не больше %(limit_value)d',
                'required': 'Обязательно к заполнению'
            },
            'rating': {
                'min_value': 'Слишком мало символов,должно быть не меньше %(limit_value)d',
                'max_value': 'Слишком много символов, должно быть не больше %(limit_value)d',
                'required': 'Обязательно к заполнению'
            }
        }



