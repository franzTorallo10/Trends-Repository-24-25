from django.http import HttpResponse # type: ignore
from django.template import loader # type: ignore
from.models import Member

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers': mymembers,
    }
    
    return HttpResponse(template.render(context, request))