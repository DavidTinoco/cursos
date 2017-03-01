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

print len(raiz.xpath("cursos/curso"))


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

curso = unicode(raw_input("De qué curso desea saber sus teléfonos?: "))

existe = False
for c in raiz.xpath("//nombre"):
    if c.text == curso:
        print c.getparent().find("telefonos").text

if not existe:
    print "No existe dicho curso"
    
#5

categoria = raw_input("Escoja la categoría del curso que desea: ")

existe = False
for c in raiz.xpath("//categoria"):
    if c.text == categoria:
        existe = True
        print "El curso " + c.getparent().getparent().find("nombre").text + " tiene un horario de " + c.getparent().getparent().find("horario").text + " y su página web es: " + c.getparent().getparent().find("url").text

if not existe:
    print "No existe dicha categoría"        
