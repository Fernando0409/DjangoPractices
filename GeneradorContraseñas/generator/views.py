import random

from django.shortcuts import render
import random

# Create your views here.
def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def password(request):
    characteres = list('qwertyuiopasdfghjklzxcvbnm')
    generatePassword = ''

    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characteres.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('specialCh'):
        characteres.extend(list('!$%&?¿{}+'))
    if request.GET.get("numbers"):
        characteres.extend(list("1234567890"))

    for x in range(length):
        generatePassword += random.choice(characteres)
    #                                       Sintaxis para enviar una variable a una pagina
    return render(request, 'password.html', {'password': generatePassword})
