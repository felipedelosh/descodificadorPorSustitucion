"""
Decriptor loko
"""
# -⁻- coding: UTF-8 -*-
import os
from tkinter import *

class Decriptor:
    def __init__(self):
        self.rutaPY = str(os.path.dirname(os.path.abspath(__file__))) # En donde estoy padado
        self.pantalla = Tk()
        self.tela = Canvas(self.pantalla, width=900, height=720, bg="snow")
        self.lblBarnner = Label(self.tela, text="Esto fue creado por el loco para decifrar .txt por sustitución")
        self.lblNombreTxt = Label(self.tela, text="Ingrese el nombre del txt: ")
        self.txtNombreTXT = Entry(self.tela)
        self.btnCargarTexto = Button(self.tela, text="CargarTexto", command=self.cargarTexto)
        self.btnInstrucciones = Button(self.tela, text="Instrucciones", bg="green", command=self.mostrarInstrucciones)
        self.btnActualizarTexto = Button(self.tela, text="Actualizar", command=self.actualizartexto)
        self.txtTextoBruto = Text(self.tela, width=70)
        self.bannerPorcentaje = Label(self.tela, text="%De Coincidencia%")
        self.lblRemplazar = Label(self.tela, text="Reemplzar A -> B : ")
        self.txtReemplazarA = Entry(self.tela, width=6)
        self.txtReemplazarB = Entry(self.tela, width=6)
        self.btnReemplazarAB = Button(self.tela, text="reemplazarAB", command=self.reemplazarEnTextoAB)
        self.lblVerPalabrasSiElEspacioEs = Label(self.tela, text="Ver palabras si el espacio es: ")
        self.txtVerPalabrasSiElEspacioEs = Entry(self.tela, width=6)
        self.btnVerPalabrasSiElEspacioEs = Button(self.tela, text="Ver", command=self.verPalabrasSiElEspacioEsA)


        """Variables"""
        self.textoCargadoExitosamente = False
        self.textoEncriptado = "" # Aqui se guarda el texto original
        self.textoTemporal = ""

        self.pintarPantallaYMostrar()

    def pintarPantallaYMostrar(self):
        self.pantalla.title("DecriptorByFelipelosH")
        self.pantalla.geometry("900x720")

        self.tela.place(x=0, y=0)
        self.lblBarnner.place(x=280, y=10)
        self.lblNombreTxt.place(x=20, y=40)
        self.txtNombreTXT.place(x=200, y=40)
        self.btnCargarTexto.place(x=330, y=40)
        self.btnInstrucciones.place(x=800, y=20)
        self.bannerPorcentaje.place(x=600, y=80)
        self.txtTextoBruto.place(x=10, y=80)

        self.tela.create_line(10, 490, 890, 490)
        self.tela.create_line(10, 500, 890, 500)

        self.lblRemplazar.place(x=20, y=540)
        self.txtReemplazarA.place(x=140, y=542)
        self.txtReemplazarB.place(x=190, y=542)
        self.btnReemplazarAB.place(x=240, y=540)
        self.lblVerPalabrasSiElEspacioEs.place(x=20, y=590)
        self.txtVerPalabrasSiElEspacioEs.place(x=190, y=590)
        self.btnVerPalabrasSiElEspacioEs.place(x=240, y=588)

        


        self.pantalla.mainloop()

    def mostrarBotonActualizar(self):
        self.btnActualizarTexto.place(x=500, y=40)

    def cargarTexto(self):
        if self.validarTxtEntradaTexto():
            try:
                rutaTXT = self.rutaPY + "\\" + str(self.txtNombreTXT.get()) + ".txt"
                blockDeNotas = open(rutaTXT, "r", encoding="UTF-8")
                self.textoEncriptado = blockDeNotas.read()
                self.mostrarTextoEncriptado()
                blockDeNotas.close()
                self.mostrarBotonActualizar()
                self.textoCargadoExitosamente = True
            except:
                self.mostrarVentanaEmergente("Error Fatal", "No se puede abrir el archivo..."+str(self.txtNombreTXT.get()))
        else:
            self.mostrarVentanaEmergente("Error Fatal...", "Se necesita introducir el nombre del txt sin la extensión")


    def mostrarTextoEncriptado(self):
        self.txtTextoBruto.delete("1.0", END)
        self.txtTextoBruto.insert("1.0", self.textoEncriptado)
        self.actualizarEstadisticas()

    def actualizarEstadisticas(self):
        txt = "%Porcentaje de Aparición de Caracteres%\n\n"
        totalDeCaracteresDelTexto = len(self.textoEncriptado)
        estadisticaCaracteres = {}

        for i in self.textoEncriptado:
            if i in estadisticaCaracteres:
                estadisticaCaracteres[i] = estadisticaCaracteres[i] + 1 
            else:
                estadisticaCaracteres[i] = 1

        porcentajeCaracteres = []


        for i in estadisticaCaracteres:
            porcentaje = (estadisticaCaracteres[i]/totalDeCaracteresDelTexto)*100
            porcentaje = round(porcentaje, 4)
            porcentajeCaracteres.append((i, porcentaje))

        # Organizar por burbuja
        # CopiarElVector
        copyPor = []
        for i in porcentajeCaracteres:
            copyPor.append(i)

        temp = None
        for i in range(0, len(copyPor)-1):
            for j in range(0, len(copyPor)-i-1):
                if copyPor[j][1] < copyPor[j+1][1]:
                    temp = copyPor[j]
                    copyPor[j] = copyPor[j+1]
                    copyPor[j+1] = temp

        info = ""
        contador = 0
        for i in copyPor:
            if contador == 2:
                info = info + "\n"
                contador = 0

            info = info + "[" + str(i[0]) + "] =>" + str(i[1]) + "%" + " -- "
            contador = contador + 1

        txt = txt + info

        self.bannerPorcentaje['text'] = txt


    def reemplazarEnTextoAB(self):
        if self.textoCargadoExitosamente:
            if self.validarReemplazoTextoA():
                # Se reemplaza y se guarda en el temporal 
                self.textoTemporal = self.textoEncriptado.replace(self.txtReemplazarA.get(), self.txtReemplazarB.get())
                # Semuestra 
                self.mostrarVentanaEmergente("Reemplazando : "+self.txtReemplazarA.get()+" -> "+self.txtReemplazarB.get(), self.textoTemporal)



            else:
                self.mostrarVentanaEmergente("Error...", "para reemplzar un texto debe de introducir un patron inicial")
        else:
            self.mostrarVentanaEmergente("Error fatal... ", "Primero se debe de cargar un texto")

    def verPalabrasSiElEspacioEsA(self):
        if self.textoCargadoExitosamente:
            if self.validarVerPalabrasSiElEspacioEs():
                palabras = self.textoEncriptado.split(self.txtVerPalabrasSiElEspacioEs.get())


                txt = "" # Mensaje pricipal
                br = "---------------------------------\n" # Salto de linea bonito

                for i in palabras:
                    txt = txt + "\n" + i

                # Se pone el titulo y se muestran las posibles palabras
                txt = "Estas son todas las posibles palabras si el espacio es: " + "/" + self.txtVerPalabrasSiElEspacioEs.get() + "/" + "\n" + txt

                txt = br + txt + br

                # Se muestran las estadisticas

                txt = txt + "Posibles palabras: " + str(len(palabras)) + "\n" + br
 
                # Se muestran las coincidencias de palabras

                coincidencias = {}

                for i in palabras:
                    if i in coincidencias:
                        coincidencias[i] = coincidencias[i] + 1
                    else:
                        coincidencias[i] = 1

                # Se ordenan mediante burbuja
                # Organizar por burbuja
                # CopiarElVector
                copyPor = []
                for i in coincidencias:
                    copyPor.append((i, coincidencias[i]))

                temp = None
                for i in range(0, len(copyPor)-1):
                    for j in range(0, len(copyPor)-i-1):
                        if copyPor[j][1] < copyPor[j+1][1]:
                            temp = copyPor[j]
                            copyPor[j] = copyPor[j+1]
                            copyPor[j+1] = temp


                cantidadDePalabras = ""
                for i in copyPor:
                    cantidadDePalabras = cantidadDePalabras + i[0] + "  =>  " + str(i[1]) + "\n"
                

                txt = txt + cantidadDePalabras


                self.mostrarVentanaEmergente("Si el espacio es... + /" + self.txtVerPalabrasSiElEspacioEs.get(), txt)



            else:
                self.mostrarVentanaEmergente("Error...", "Introduzca un patrón ó caracter para ver si el espacio es...")
        else:
            self.mostrarVentanaEmergente("Error...", "Para realizar la acción de espaciado cargue un texto")



    def actualizartexto(self):
        self.txtTextoBruto.delete("1.0", END)
        self.textoEncriptado = self.textoTemporal
        self.txtTextoBruto.insert("1.0", self.textoEncriptado)
        self.actualizarEstadisticas()


    def mostrarVentanaEmergente(self, titulo, texto):
        ventanita = Toplevel()
        ventanita.geometry("800x600")
        ventanita.title(titulo)
        tela = Canvas(ventanita, width=800, height=600)
        tela.place(x=0, y=0)
        txt = Text(tela, width=96, height=35)
        txt.insert("1.0", texto)
        txt.place(x=10, y=10)

    def mostrarInstrucciones(self):
        titulo = "Instrucciones para Retrasados Mentales"

        texto = """

Este es el programa de desencriptado por sustitución del loko 2021

1 -> tiene que cargar el archivo.txt :
            Asegurece de tener el archivo.txt luego copie el nombre del archivo sin la extensión .txt 

2 -> Si el archivo cargo correctamente se mostrará en pantalla con las estadisticas de caracteres 

3 -> Para hacer el reemplazo de caracteres:

    * Si desea reemplazar un caracter o conjunto de caracteres introduzcalos en la casilla A y será   
    reemplazado por lo de la casilla B

    * Si desea eliminar los espacios en blanco: ingrese un espacio en blanco en la casilla A y nada en 
    la casilla B

    //Una vez reemplado proceda a actualizar el texto para dejarlo en ese estado.

4 -> Si ud supone que el espacio es el caracter ó patrón ... introduzcalo y este le mostrara como serian las posibles palabras.

        """

        self.mostrarVentanaEmergente(titulo, texto)

    def validarTxtEntradaTexto(self):
        return str(self.txtNombreTXT.get()).strip() != ""

    def validarReemplazoTextoA(self):
        return str(self.txtReemplazarA.get()) != ""

    def validarVerPalabrasSiElEspacioEs(self):
        return str(self.txtVerPalabrasSiElEspacioEs.get()) != ""
        


d = Decriptor()