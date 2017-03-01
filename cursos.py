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

pausa = raw_input
