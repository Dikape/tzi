from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def firstpage(request):
    return HttpResponse("wewqewqwqeewqewqwwqewew")