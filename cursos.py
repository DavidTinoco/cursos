#-*- coding:utf-8 -*-

from lxml import etree

doc = etree.parse("cursos.xml")
raiz = doc.getroot()

#1

horas = int(raw_input("Introduzca el número de horas a las que debe ser superior el curso: "))

for c in raiz.xpath("//duracion"):
    if int(c.text.split(" ")[0]) > horas:
        print c.getparent().find("nombre").text

#2

pausa = raw_input("Pulse intro para continuar")

categorias = []

for c in raiz.xpath("//categoria"):
    categorias.append(c.text)

for c in set(categorias):
    cat = "count(//categoria[.=\"" + c + "\"])"
    n = raiz.xpath(cat)
    print "La categoría " + c.encode("utf-8") + " tiene " + str(int(n)) + " cursos"

#3

mes = raw_input("Indique qué mes desea comenzar un curso (01-12): ")

existe = False
for c in raiz.xpath("//fecha-de-inicio-previsto"):
    if c.text.split("-")[1] == mes:
        existe = True
        print c.getparent().find("nombre").text

if not existe:
    print "No hay cursos en el mes indicado"


#4

curso =raw_input("De qué curso desea saber sus teléfonos?: ")

existe = False
for c in raiz.xpath("//nombre"):
    if c.text.encode("utf-8") == curso:
        existe = True
        print c.getparent().find("telefonos").text

if not existe:
    print "No existe dicho curso"
    
#5

categoria = raw_input("Escoja la categoría del curso que desea: ")
nombre = "null"
horario = "null"
url = "null"


existe = False
for c in raiz.xpath("//categoria"):
    if c.text.encode("utf-8") == categoria:
        existe = True
        if c.getparent().getparent().find("nombre").text != None:
            nombre = c.getparent().getparent().find("nombre").text.encode("utf-8")
            
        if c.getparent().getparent().find("horario").text != None:
            horario = c.getparent().getparent().find("horario").text.encode("utf-8")

        if c.getparent().getparent().find("url").text != None:
            url = c.getparent().getparent().find("url").text.encode("utf-8")
            
        print "El curso " + nombre + " tiene un horario de " + horario + " y su página web es: " + url
        print

if not existe:
    print "No existe dicha categoría"        
