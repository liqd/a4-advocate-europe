from django.views import generic

from django.http import JsonResponse
from django.template import loader

class ImageUploadView(generic.View):

    def post(self, request, **kwargs):
        return JsonResponse({
            'result': {
                'imageChosen': {
                    'alt': 'Dogo',
                    'url': 'https://i.imgur.com/GBerpnx.jpg',
                    'style': 'centered'
                }
            }
        })


    def get(self, request, **kwargs):
        return JsonResponse({
            'html': loader.render_to_string('richtexts/upload_form.html', {}, request)
        })
