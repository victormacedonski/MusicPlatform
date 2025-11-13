from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.http import HttpResponse
from .models import Release

def release_list(request):
    releases = Release.objects.select_related('artist').all()

    # отладка
    try:
        template = get_template('catalog/release_list.html')
        print("найден шалон:", template.origin.name)
    except Exception as e:
        print("Ошибка", e)
        return HttpResponse(f"<h2>Шаблон не найден: {e}<h2>")

    return render(request, 'catalog/release_list.html', {'releases': releases})

def release_detail(request, pk):
    release = get_object_or_404(Release.objects.prefetch_related('tracks'), pk=pk)
    return render(request,'catalog/release_detail.html', {'release': release})
    