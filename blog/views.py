from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

def server_error(request):
    response = render_to_response('500.html', context_instance=RequestContext(request))
    response.status_code = 500
    return response

def bad_request(request):
    response = render_to_response('404.html', context_instance=RequestContext(request))
    response.status_code = 404
    return response

def post_list(request):
    return render(request, 'blog/post_list.html', {})