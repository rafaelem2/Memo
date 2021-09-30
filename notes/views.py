from django.shortcuts import render, redirect
from .models import Note


def createNote(note):
    note_item = Note(note=note)

    note_item.save()


def index(request):
    if request.method == 'POST':
        note = request.POST.get('note')
        createNote(note)

        return redirect('index')
    else:
        last_note = Note.objects.last()

        return render(request, 'notes/index.html',
                      {'last_note': last_note})

def delete(request):
    id = request.POST.get('id')
    note = Note.objects.get(id=id)
    note.delete()

    return redirect('index')

def edit(request,id):
    title = request.POST.get('titulo')
    content = request.POST.get('detalhes')
    note = Note.objects.get(id=id)
    note.title = title
    note.content = content
    note.save()

    return redirect('index')