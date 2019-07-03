from django.shortcuts import render


def home(request):  # cria uma função
    return render(request, 'index.html')  # os parametros que retorna a função render()
