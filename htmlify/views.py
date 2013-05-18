"""Views."""
import re

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from htmlify.forms import HtmlifyForm
from django.http import HttpResponse


def htmlify(request):
    context = RequestContext(request)
    if request.method == 'GET':
        form = HtmlifyForm()
    elif request.method == 'POST':
        form = HtmlifyForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            original_code = form.cleaned_data['code']
            html_code = htmlify_code(original_code)
            context.update({'htmlified': html_code,
                            'to_htmlify': original_code})
    context.update({'form': form})
    return render_to_response('htmlify.html', context)


def htmlify_ajax(request):
    if request == 'POST' or request.is_ajax():
        form = HtmlifyForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            original_code = form.cleaned_data['code']
            html_code = htmlify_code(original_code)
        else:
            return HttpResponse('Something went wrong...')
        return HttpResponse(html_code)
    return HttpResponse('bla')


def htmlify_line(line):
    pattern = r"^(\s*)[^\s]"
    match = re.match(pattern, line)
    if match:
        spaces = match.group(1)
        line = len(spaces) * '&nbsp;' + line[len(spaces):]
    return line


def htmlify_code(code):
    code = code.replace('&', '&amp;')
    code = code.replace('<', '&lt;')
    code = code.replace('>', '&gt;')

    # maintain whitespaces
    code = '\n'.join(htmlify_line(line) for line in code.split('\r\n'))

    # html tags
    code = "<pre><code>{}</code></pre>".format(code)
    return code
