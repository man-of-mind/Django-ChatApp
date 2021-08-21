from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import Room, Message

# Create your views here.
def home(request):
    return render(request, 'homepage.html')


def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {'username': username, 'room': room, 
    'room_details': room_details})


def send(request):
    print('i am here')
    message = request.POST.get('message')
    room_id = request.POST.get('room_id')
    username = request.POST.get('username')
    new_message = Message.objects.create(message=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')


def checkroom(request):
    room = request.POST.get('room_name')
    username = request.POST.get('username')
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)


def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({'messages': list(messages.values())})
