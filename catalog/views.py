from django.shortcuts import render, get_object_or_404
from .models import Release

def release_list(request):
    releases = Release.objects.select_related('artist').all()
    return render(request, 'music/releass_list.html', {'releases': releases})

def release_detail(request, pk):
    release = get_object_or_404(Release.objects.prefetch_related('tracks'), pk=pk)
    return render(request,'music/release_detail.html', {'release': release})
