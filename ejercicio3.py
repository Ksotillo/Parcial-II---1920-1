class Drive():
    def __init__(self):
        self.archivos = []
        self.limite_en_gb = 15

   def crear(self, archivo):
        self.archivos.append(archivo)
        print('Se creo un archivo')

    def cargar(self, archivo):
        self.archivos.append(archivo)
        print('Se cargó un archivo')

    def editar(self, nombre_archivo):
        archivo = next((archivo for archivo in self.archivos if archivo.nombre == nombre_archivo), None)
        print('Se va a editar el siguiente archivo:', nombre_archivo)
        archivo.editar()

    def descargar(self, nombre_archivo):
        archivo = next((archivo for archivo in self.archivos if archivo.nombre == nombre_archivo), None)
        print('Se va a descargar el siguiente archivo:', nombre_archivo)
        archivo.descargar()

    def compartir(self, nombre_archivo, usuarios):
        archivo = next((archivo for archivo in self.archivos if archivo.nombre == nombre_archivo), None)
        for usuario in usuarios:
            archivo.compartir(usuario)
        print('Se han agregado los colaboradores al siguiente archivo:', nombre_archivo)

    def eliminar(self, nombre_archivo):
        for i, archivo in self.archivos:
            if archivo.nombre == nombre_archivo:
                self.archivos.remove(i)
                break
        print('Se ha eliminado el siguiente archivo:', nombre_archivo)

class Archivo():
    def __init__(self, nombre, autor, fecha_creacion, colaboradores):
        self.nombre = nombre
        self.autor = autor
        self.fecha_creacion = fecha_creacion
        self.colaboradores = colaboradores

    def editar(self):
        print('El archivo se está editando')

    def descargar(self):
        print('El archivo se está descargando')

    def compartir(self, colaborador):
        self.colaboradores.append(colaborador)
        print('El archivo ha sido compartido con ', colaborador)

class Documento(Archivo):
    def __init__(self, nombre, autor, fecha_creacion, colaboradores, margenes = '3 cm', cant_pag = '1'):
        Archivo(nombre, autor, fecha_creacion, colaboradores)
        self.margenes = margenes
        self.cant_pag = cant_pag

    def convertir(self, formato, drive):
        if formato == 'DOCX':
            print('Documento convertido a DOCX')
        elif formato == 'PDF':
            print('Documento convertido a PDF')
            pdf = Documento_PDF(self.nombre, self.autor, self.fecha_creacion, self.colaboradores, 'documento')
            drive.cargar(pdf)
        else:
            print('Formato no permitido')

class Presentacion(Archivo):
    def __init__(self, nombre, autor, fecha_creacion, colaboradores, tema = 'default', cant_diapo = '1'):
        Archivo(nombre, autor, fecha_creacion, colaboradores)
        self.tema = tema
        self.cant_diapo = cant_diapo

    def convertir(self, formato, drive):
        if formato == 'PPTX':
            print('Documento convertido a PPTX')
        elif formato == 'PDF':
            print('Documento convertido a PDF')
            pdf = Documento_PDF(self.nombre, self.autor, self.fecha_creacion, self.colaboradores, 'presentación')
            drive.cargar(pdf)
        else:
            print('Formato no permitido')

    def iniciar_presentacion(self):
        print('La presentación ha iniciado')

class Documento_PDF(Archivo):
    def __init__(self, nombre, autor, fecha_creacion, colaboradores, convertido_de):
        Archivo(nombre, autor, fecha_creacion, colaboradores)
        self.convertido_de = convertido_de

    def subrayar(self, texto):
        #
        #
        #
        print('Texto subrayado')

    def fusionar(self, pdfs):
        print('El archivo se ha fusionado con los PDFs indicados')

class Hoja_Calculo(Archivo):
    def __init__(self, nombre, autor, fecha_creacion, colaboradores, cant_hojas = '1', maxF= 1000, maxC = 1000):
        Archivo(nombre, autor, fecha_creacion, colaboradores)
        self.cant_hojas = cant_hojas
        self.maxF = maxF
        self.maxC = maxC


    def crear_grafico(self, datos):
        print('Se ha creado el grafico con los siguientes datos: ', datos)


class Sistema_Correo():
    def __init__(self):
        self.cuentas = []
        self.correos = []

    def crear_cuenta(self, cuenta):
        self.cuentas.append(cuenta)
        print('Cuenta creada exitosamente')

class Cuenta():
    def __init__(self, username, direccion, es_prof = False):
        self.username = username
        self.direccion = direccion
        self.es_prof = es_prof
        self.enviados = []
        self.recibidos = []
        self.borradores = []

    def leer(self, asunto_correo):
        correo = next((correo for correo in self.recibidos if correo.nombre == asunto_correo), None)
        print('A continuación se muestra el correo especificado:')
        correo.mostar()

    def enviar(self, correo):
        self.enviados.append(correo)
        print('Correo enviado exitosamente')

    def recibir(self, correo):
        self.recibidos.append(correo)
        print('Nuevo correo recibido: ', correo.asunto)

class Correo():
    def __init__(self, remitente, destinatario, asunto, contenido, archivos_adjuntos =[], fecha_envio):
        self.remitente = remitente
        self.destinatario = destinatario
        self.asunto = asunto
        self.contenido = contenido
        self.archivos_adjuntos = archivos_adjuntos
        self.fecha_envio = fecha_envio

    def insertar_imagen(self, imagen):
        print('Imagen insertada correctamente')

    def insertar_enlace(self, enlace):
        print('Enlace insertado correctamente')

    def insertar_emoji(self, emoji):
        print('Emoji insertado correctamente')

    def insertar_archivo_drive(self, archivo):
        print('Archivo de Drive insertado correctamente')

    def adjuntar_archivo(self, archivo):
        self.archivos_adjuntos.append(archivo)
        print('Archivo adjuntado correctamente')

class Classroom():
    def __init__(self):
        self.clases = []

    def crear_clase(self, clase):
        self.clases.append(clase)
        print('Clase creada correctamente')

class Clase():
    def __init__(self, profesor, estudiantes, preparador = None, aula, fecha_inicio, fecha_culminacion):
        self.profesor = profesor
        self.estudiantes = estudiantes
        self.preparador = preparador
        self.aula = aula
        self.fecha_inicio = fecha_inicio
        self.fecha_culminacion = fecha_culminacion

    def agregar_material(self, material):
        print('Material agregado correctamente a la clase')

    def editar_material(self, material):
        print('Material editado correctamente a la clase')

    def eliminar_material(self, material):
        print('Material eliminado correctamente a la clase')