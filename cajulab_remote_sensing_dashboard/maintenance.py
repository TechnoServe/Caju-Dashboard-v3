from django.shortcuts import render

def maintenance(request):
    return render(request, "maintenance/maintenance.html", status=400)