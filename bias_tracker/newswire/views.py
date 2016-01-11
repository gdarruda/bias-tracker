# coding=utf-8

from django.shortcuts import render


def index(request):
    profiles = [dict(id="@estadaopolitica", name="Política Estadão",
                     description="Twitter oficial da editoria de Política do Estadão. Conheça também nossa página no Facebook"),
                dict(id="@folha_poder", name="Folha Poder",
                     description="Canal de diálogo com o leitor da editoria Poder do jornal Folha de S.Paulo")]

    return render(request, 'index.html', {"profiles": profiles})
