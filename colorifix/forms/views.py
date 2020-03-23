from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.db.models import Q, Max
from django.db import connection

from .models import Forms, Parameters, Options, Values

# Create your views here.
def index(request, form_id=0):
    all_forms = Forms.objects.all()

    if "options" in request.POST: form_id = request.POST["options"]
    selected_form = Forms.objects.get(unique_id=form_id) if int(form_id) > 0 else None

    return render(
        request,
        'forms/index.html',
        context={'all_forms': all_forms, 'selected_form': selected_form}
    )

def save_form(request, form_id):
    error_id = 0

    try:
        selected_form = Forms.objects.get(unique_id=form_id)
    
        for parameter in selected_form.parameters:
            new_entry = Values()
            new_entry.form_id = form_id
            new_entry.param_id = parameter.unique_id
            if parameter.param_type == "bool":
                new_entry.value = 1 if parameter.name in request.POST else 0
            else:
                new_entry.value = request.POST[parameter.name]
            new_entry.save()
    except:
        error_id = 1
    
    return HttpResponseRedirect(reverse('forms:index', args=(form_id,)))
    