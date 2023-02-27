import asyncio
from django.http import HttpResponse
from django.views import View
import json
from artist.models import Artist

class Works(View):

    def get(self, request, *args, **kwargs):
        artist_name = request.GET.get('artist', None)
        work_type = request.GET.get('work_type', None)
        response = {}
        if artist:
            artist_obj = Artist.objects.filter(name=artist_name)
            for work_detail in artist_obj.works.all():
                response[work_detail.work_type] = work_detail.work_type
        if work_type:
            artist_list = []
            for artist in Artist.objects.filter(works__work_type=worke_type):
                artist_list.append(artist.name)
            response['artist_names'] = artist_list
        return HttpResponse(str(response))