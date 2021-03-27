from tkinter import *
from tkinter import filedialog
import qrcode
from PIL import ImageTk, Image
from tkinter.messagebox import showwarning
import PyPDF2
from pyzbar.pyzbar import decode


root=Tk()
root.geometry('500x500')
my_menu=Menu(root)
root.config (menu=my_menu, bg="#d8fefe")
text_box=Text(root, height=30, width=50)
text_box.pack(pady=8)


def qrcoding():
    try:
        qr=qrcode.make(the_text)
        '''qr=qrcode.QRCode(version=40, error_correction=qrcode.constants.ERROR_CORRECT_H,
                         box_size=20,border=5)
        qr.add_data(the_text)
        qr.make(fit=True)
        img=qr.make_image(fill_color='blue', back_color='white')
        #En este caso no podemos personalizarlo porque la libreria QRCode que dispone hasta la version 40
        no permite determinado volumen de datos como de una pagina entera. Lo hacemos con el basico.'''

        qr.save('QR Code/qrcode.png')
        qr.show()
        '''picture= ImageTk.PhotoImage(Image.open('qrcode.png'))
        picture_label=Label(root, image=picture).place(x=15, y=20)'''
    except:
        
        showwarning(title='NADA PARA TRANSFORMAR',message='Debes abrir antes un .pdf o .txt y luego presionar en "Transformar a QR code"')   
        
def openpdf():
    global the_text
    open_my_pdf=filedialog.askopenfilename(initialdir='C:/Users/Willy/Documents/Python/text editor-converter QR/docs',title='Abrir archivos PDF:',
                                         filetype=(('Solo pdf','*.pdf'),('Cualquier archivo','*.*')))
    if open_my_pdf:
        pdf_selected=PyPDF2.PdfFileReader(open_my_pdf)
        first_page= pdf_selected.getPage(1)
        the_text=first_page.extractText()
        text_box.delete(1.0,END)
        text_box.insert(1.0, the_text)

def opentxt():
    global the_text
    global open_my_txt
    open_my_txt=filedialog.askopenfile(mode='r+',initialdir='C:/Users/Willy/Documents/Python/text editor-converter QR/docs',title='Abrir archivos txt:',
                                         filetype=(('Solo .txt','*.txt'),('Solo .pdf','*.pdf'),('Cualquier archivo','*.*')))
    if open_my_txt:
        the_text=open_my_txt.read()
        text_box.delete(1.0,END)
        text_box.insert(1.0, the_text)
        open_my_txt.close()
        
def createnew():
   
    cancelcontent()
    global filename
    filename=filedialog.asksaveasfile(mode='w',initialdir= 'C:/Users/Willy/Documents/Python/text editor-converter QR/docs', title='Titulo para guardar nuevo fichero:',
                                          filetype=(('Solo .txt','*.txt'),('Cualquier archivo','*.*')))
    if filename:
        showwarning(title='FICHERO CREADO', message='Ahora puedes editar y guardar el nuevo txt.')
        
def savenew():
    global the_text
    the_text=text_box.get(1.0, END)
    
    filename.writelines(the_text)
    filename.close()
    text_box.delete(1.0,END)
    

def save():
    global the_text
    the_text=text_box.get(1.0,END)
    file=open(open_my_txt.name,'w')
    file.writelines(the_text)
    file.close()
    text_box.delete(1.0,END)

def qrdecoding():
    open_my_qrcode=filedialog.askopenfilename (initialdir='C:/Users/Willy/Documents/Python/text editor-converter QR/QR Code', title='Elegir QR Code:',
                                              filetype=(('Solo codigo QR en .png', '*.png'),('Solo codigo QR en .jpg','*.jpg')))

  
    if open_my_qrcode:
        img=Image.open(open_my_qrcode)
        #img=Image.open('opening PDF/QR Code/ikea QR.png')
        result=decode(img)
        text_box.delete(1.0, END)
        text_box.insert(1.0, result)
        if result==[]:
            text_box.insert(1.0,'NO SE HA PODIDO REALIZAR.'+'\n'+ 'DEMASIADA EXTENSION DE DATOS A DESCODIFICAR.')

def cancelcontent():
    text_box.delete(1.0, END)

file_menu= Menu (my_menu, tearoff='False')
file2_menu= Menu (my_menu, tearoff='False')
file3_menu= Menu (my_menu, tearoff='False')

my_menu.add_cascade(label='Fichero PDF', menu=file_menu)
my_menu.add_cascade(label='Fichero txt', menu=file2_menu)
my_menu.add_cascade (label='Leer QR code', menu=file3_menu)

file_menu.add_cascade(label='Abrir', command=openpdf)
file_menu.add_cascade(label='Borrar', command=cancelcontent)
file_menu.add_cascade(label='Transformar a QR code',command= qrcoding)
file_menu.add_separator
file_menu.add_cascade(label='Salir', command=root.destroy)

file2_menu.add_cascade(label='Abrir', command=opentxt)
file2_menu.add_cascade(label='Guardar', command=save)
file2_menu.add_cascade(label='Crear nuevo txt', command=createnew)
file2_menu.add_cascade(label='Guardar el nuevo txt', command=savenew)
file2_menu.add_cascade(label='Transformar a QR code', command=qrcoding)

file3_menu.add_cascade(label='Abrir imagen QR code', command=qrdecoding)

root.mainloop()
