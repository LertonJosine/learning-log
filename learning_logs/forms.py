from dataclasses import field
from django import forms
from learning_logs.models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labesl = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}