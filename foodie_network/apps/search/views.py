from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q

User = get_user_model()
# Create your views here.
@login_required
def user_search(request):
    if 'q' in request.GET :
         query = request.GET.get('q')
         # results = {}
         users = User.objects.filter(Q(first_name__icontains = query) | Q(last_name__icontains = query))
         return render (request, 'search/results.html', {'users':users})
    return render(request, 'search/error.html')
