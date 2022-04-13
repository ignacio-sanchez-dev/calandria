from django.http import JsonResponse
from django.shortcuts import render

from .convert import xml_to_dict
from .forms import SubmissionForm


def upload_page(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = request.FILES.get('file')
            response = xml_to_dict(submission)
            if response:
                return JsonResponse(response, content_type='application/json')
            else:
                return JsonResponse({}, status=400, content_type='application/json')


    form = SubmissionForm()
    return render(request, "upload_page.html", {'form': form})
