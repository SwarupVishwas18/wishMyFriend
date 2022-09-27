from django.shortcuts import render, redirect
from gtts import gTTS
import os
from django.http import HttpResponse, FileResponse
# Create your views here.


def index(request):
    if request.method == 'POST':
            if request.POST.get('name') and request.POST.get('cat') and request.POST.get('flexRadioDefault'):
                mode = request.POST.get('flexRadioDefault')
                cat = request.POST.get('cat')
                if cat == 'bd':
                    text = "Very very happy birthday to you "+ request.POST.get('name') + ". Hope all your birthday wishes come true!"
                if cat == 'lu':
                    text = "Wish you a very good Luck "+ request.POST.get('name')
                if cat == 'co':
                    text = "Congratulation, " + request.POST.get('name')
                if cat == 'an':
                    text = "Happy Anniversary, " + request.POST.get('name')
                if cat == 'cr':
                    text = request.POST.get('name') + ", you have a call."
                if cat == 'cu':
                    text = request.POST.get('name')                
                    if len(text.split()) < 5:
                        return render(request, 'bday/index.html', context={'error': "There must be atleast 5 letters"})
                sl = False
                if mode == 'slow':
                    sl = True
                try:
                    aud = gTTS(text=text, lang='en', slow=sl)
                except:

                    return render(request, 'bday/index.html', context={'error': "Network Error"})
                else:
                    aud.save("static/speech.mp3")

                os.system("static/speech.mp3")
                return render(request, 'bday/index.html', context={'isPost': True})
                # file = open("static/speech.mp3", "rb").read() 
                # return HttpResponse(aud, 'audio/mpeg')

                # from django.templatetags.static import static
                # music = static('speech.mp3')
                # static/music/Billie Eilish - when the party\'s over (Viga Remix).mp3
                # return redirect(music)

                # return FileResponse(aud, as_attachment=True, filename='speech.mp3')
    else:
        print("Hello")
        return render(request, 'bday/index.html')
