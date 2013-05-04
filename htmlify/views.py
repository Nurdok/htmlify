"""Views."""
import re

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
    return render_to_response('htmlify.html', context)


def htmlify_line(line):
    pattern = r"^(\s*)[^\s]"
    match = re.match(pattern, line)
    if match:
        spaces = match.group(1)
        line = len(spaces) * '&nbsp;' + line[len(spaces):]
    return line


def htmlify_code(code):
    # TODO: replace < and > within the code
    # maintain whitespaces
    print code
    code = '<br/>\n'.join(htmlify_line(line) for line in code.split('\n'))

    # html tags
    code = "<pre><code>\n{}\n</code></pre>".format(code)
    return code
