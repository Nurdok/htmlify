"""Views."""
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from htmlify.forms import HtmlifyForm


def htmlify(request):
    context = RequestContext(request)
    if request.method == 'GET':
        form = HtmlifyForm()
    elif request.method == 'POST':
        form = HtmlifyForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            html_code = htmlify_code(form.cleaned_data['code'])
            context.update({'htmlified': html_code})
    context.update({'form': form})
    print context
    return render_to_response('htmlify.html', context)


def htmlify_code(code):
    return code
