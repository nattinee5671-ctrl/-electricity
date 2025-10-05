# app_name/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import QAPdf
import os

def qa_page(request):
    return render(request, 'qa_rooms.html')

@csrf_exempt
def upload_pdf(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        floor = request.POST.get('floor')
        room_number = request.POST.get('room_number')
        section = request.POST.get('section')

        if not all([file, floor, room_number, section]):
            return JsonResponse({'error': 'ข้อมูลไม่ครบ'}, status=400)

        QAPdf.objects.create(
            floor=floor,
            room_number=room_number,
            section=section,
            file=file
        )
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Method not allowed'}, status=405)


def list_pdfs(request, floor, room_number, section):
    pdfs = QAPdf.objects.filter(
        floor=floor,
        room_number=room_number,
        section=section
    )
    files = [
        {
            'name': os.path.basename(p.file.name),
            'url': f'{settings.MEDIA_URL}{p.file.name}'
        } for p in pdfs
    ]
    return JsonResponse({'pdfs': files})
