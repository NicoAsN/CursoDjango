from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render


class persona(object):
    def __init__(self, nombre, apellido):

        self.nombre=nombre

        self.apellido=apellido

def saludo(request): #Primera vista

    p1=persona("Alumno Nicolas","Navarrete")

        #nombre = "Nicolas"
        #apellido = "Navarrete"

    temas_curso=["Plantillas","Modelos","Formularios","Vistas","Despliegue"]

    ahora=datetime.datetime.now()

        #doc_externo=open("D:/Pendrive/No borrar/Pildoras informaticas/CursoDjango/ProyectosDjango/Proyecto1/Proyecto1/Plantillas/miplantilla.html")

        #plt=Template(doc_externo.read())

        #doc_externo.close()

    #doc_externo=get_template('miplantilla.html')

        #ctx=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual": ahora, "temas":temas_curso})

    #documento=doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual": ahora, "temas":temas_curso})

    return render(request, 'miplantilla.html', {"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual": ahora, "temas":temas_curso})

def despedida(request): 

    return HttpResponse("Hasta luego alumnos Django")


def dameFecha(request):

    fecha_actual=datetime.datetime.now()

    documento="""<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    <h1>
    <body>
    <html>""" %fecha_actual

    return HttpResponse(documento)

def calculaEdad(request,edad, agno):

    #edadActual=18
    periodo=agno-2020
    edadFutura=edad+periodo
    documento="<html><body><h2>Ahora tienes %s pero en el año %s tendras %s años" %(edad, agno, edadFutura)

    return HttpResponse(documento)


def curso_c(request):

    fecha_actual=datetime.datetime.now()

    return render(request,"cursoC.html", {"dameFecha":fecha_actual})

def curso_css(request):

    fecha_actual=datetime.datetime.now()

    return render(request,"cursoCss.html", {"dameFecha":fecha_actual})