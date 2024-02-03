import os
import shutil
from datetime import datetime

def organizar_archivos(ruta, diccionario):
    for archivo in os.listdir(ruta):
        ruta_completa = os.path.join(ruta, archivo)

        if os.path.isfile(ruta_completa):
            # Obtener la extensión del archivo
            _, extension = os.path.splitext(archivo)

            # Buscar la carpeta correspondiente en el diccionario
            carpeta = None
            for key, extensions in diccionario.items():
                if extension in extensions:
                    carpeta = key
                    break

            # Si no se encuentra en ninguna categoría, se coloca en "Otros"
            carpeta = carpeta or "Otros"

            # Crear la carpeta si no existe
            carpeta_con_fecha = f"{carpeta}_{datetime.now().strftime('%d-%m-%Y')}"
            carpeta_ruta = os.path.join(ruta, carpeta_con_fecha)
            os.makedirs(carpeta_ruta, exist_ok=True)

            # Mover el archivo a la carpeta correspondiente
            shutil.move(ruta_completa, os.path.join(carpeta_ruta, archivo))

if __name__ == "__main__":
    ruta_a_organizar = r"C:\Users\ben_9\Desktop\Principal\01_Documentos\02_Universidad\Princesa"
    
    diccionario_configuracion = {
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"],
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"],
    "Doc_Word": [".doc", ".docx"],
    "Doc_Excel": [".xls", ".xlsx"],
    "Doc_PowerPoint": [".ppt", ".pptx"],
    "Doc_Texto": [".txt", ".md", ".csv"],
    "Doc_PDF": [".pdf"],
    "Doc_Audio": [".mp3", ".wav", ".flac", ".aac"],
    "Comprimidos": [".zip", ".rar", ".7z", ".tar"],
    "Otros": []  # Esta categoría incluirá cualquier extensión no especificada en las anteriores
    # Agrega más categorías y extensiones según tus necesidades
    }

    organizar_archivos(ruta_a_organizar, diccionario_configuracion)