from django.shortcuts import render

def settings(request):
    context = {
        "token1": "Поздравляем с новым началом!",
        "token2": "Каждый день — это новая возможность.",
        "token3": "Смело идите к своим мечтам.",
        "token4": "Ваши усилия обязательно принесут плоды.",
        "token5": "Каждый шаг — это шаг к успеху.",
        "token6": "Не забывайте о своих целях.",
        "token7": "Верьте в себя и всё получится.",
        "token8": "Жизнь полна удивительных моментов!",
    }

    return render(request, "index.html", context=context)

def eshkere(request):
    context = {
        "title": "У нас нехватка боеприпасов",
        "title2": "Шайгу, Герасимов — где боеприпасы?",
        "title3": "Ислам, Агай, с Днем учителя.",
        "title4": "Эщкере.",
        "title5": "5-6 или 7-8.",
    }
    return render(request, "index.html", context=context)

