from django.shortcuts import render
from .models import Presentation

def presentation_list(request):
    classes = {}
    for cls in ["5", "6", "7", "8", "9", "10", "11"]:
        presentations = Presentation.objects.filter(school_class=cls).order_by("-uploaded_at")
        if presentations.exists():
            classes[cls] = presentations

    return render(request, "presentations/list.html", {"classes": classes})
from django.shortcuts import render
from .models import Presentation

def presentation_list(request):
    query = request.GET.get("q")  # то, что ввёл пользователь в строке поиска

    if query:
        presentations = Presentation.objects.filter(title__icontains=query).order_by("-uploaded_at")
    else:
        presentations = Presentation.objects.all().order_by("-uploaded_at")

    return render(request, "presentations/list.html", {
        "presentations": presentations,
        "query": query
    })
