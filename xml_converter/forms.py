from django import forms


class SubmissionForm(forms.Form):
    file = forms.FileField(label='Upload an XML file')