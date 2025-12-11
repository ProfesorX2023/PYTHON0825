import os
import shutil
from pathlib import Path


def organizar_archivos_centralizado(rutas_origen, ruta_destino):
    """
    Organiza archivos de múltiples ubicaciones en un único conjunto de carpetas

    Args:
        rutas_origen: Lista de rutas desde donde tomar archivos
        ruta_destino: Ruta donde se crearán las carpetas organizadas
    """
    # Diccionario con categorías y sus extensiones
    categorias = {
        "Imagenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico", ".tiff"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".m4v"],
        "Documentos": [".pdf", ".doc", ".docx", ".txt", ".odt", ".rtf", ".tex", ".xlsx", ".xls", ".pptx", ".ppt"],
        "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a"],
        "Comprimidos": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"],
        "Ejecutables": [".exe", ".msi", ".bat", ".sh", ".app", ".deb", ".rpm"],
        "Codigo": [".py", ".java", ".cpp", ".c", ".js", ".html", ".css", ".php", ".rb", ".go", ".rs"],
        "Diseno": [".psd", ".ai", ".sketch", ".fig", ".xd", ".indd"],
        "Datos": [".csv", ".json", ".xml", ".sql", ".db", ".sqlite"],
        "Fuentes": [".ttf", ".otf", ".woff", ".woff2"],
        "Otros": []
    }

    # Crear carpeta de destino principal si no existe
    os.makedirs(ruta_destino, exist_ok=True)

    # Crear subcarpetas de categorías en el destino
    for carpeta in categorias.keys():
        os.makedirs(os.path.join(ruta_destino, carpeta), exist_ok=True)

    archivos_movidos = 0
    errores = []
    archivos_por_origen = {}

    # Procesar cada ruta de origen
    for ruta_origen in rutas_origen:
        if not os.path.exists(ruta_origen):
            print(f"⚠️  Ruta no encontrada: {ruta_origen}")
            continue

        archivos_por_origen[ruta_origen] = 0
        print(f"\n📂 Procesando: {ruta_origen}")
        print("-" * 50)

        try:
            for item in os.listdir(ruta_origen):
                ruta_item = os.path.join(ruta_origen, item)

                # Ignorar carpetas y archivos ocultos
                if os.path.isdir(ruta_item) or item.startswith('.'):
                    continue

                # Obtener extension del archivo
                extension = Path(item).suffix.lower()
                movido = False

                # Buscar en que categoria va el archivo
                for categoria, extensiones in categorias.items():
                    if categoria == "Otros":
                        continue

                    if extension in extensiones:
                        try:
                            destino = os.path.join(ruta_destino, categoria, item)

                            # Manejar archivos duplicados
                            if os.path.exists(destino):
                                nombre, ext = os.path.splitext(item)
                                contador = 1
                                while os.path.exists(destino):
                                    nuevo_nombre = f"{nombre}_{contador}{ext}"
                                    destino = os.path.join(ruta_destino, categoria, nuevo_nombre)
                                    contador += 1

                            shutil.move(ruta_item, destino)
                            archivos_movidos += 1
                            archivos_por_origen[ruta_origen] += 1
                            movido = True
                            print(f"  ✓ {item} → {categoria}/")
                            break
                        except Exception as e:
                            errores.append(f"Error moviendo {item}: {str(e)}")

                # Si no se movio, va a "Otros"
                if not movido and extension:
                    try:
                        destino = os.path.join(ruta_destino, "Otros", item)

                        # Manejar duplicados en Otros tambien
                        if os.path.exists(destino):
                            nombre, ext = os.path.splitext(item)
                            contador = 1
                            while os.path.exists(destino):
                                nuevo_nombre = f"{nombre}_{contador}{ext}"
                                destino = os.path.join(ruta_destino, "Otros", nuevo_nombre)
                                contador += 1

                        shutil.move(ruta_item, destino)
                        archivos_movidos += 1
                        archivos_por_origen[ruta_origen] += 1
                        print(f"  ✓ {item} → Otros/")
                    except Exception as e:
                        errores.append(f"Error moviendo {item}: {str(e)}")

        except Exception as e:
            errores.append(f"Error al acceder a {ruta_origen}: {str(e)}")

    # Resumen final
    print("\n" + "=" * 50)
    print("📊 RESUMEN")
    print("=" * 50)
    print(f"📍 Destino: {ruta_destino}")
    print(f"📁 Total de archivos organizados: {archivos_movidos}")

    print("\nArchivos por origen:")
    for origen, cantidad in archivos_por_origen.items():
        nombre_origen = os.path.basename(origen)
        print(f"  • {nombre_origen}: {cantidad} archivos")

    if errores:
        print(f"\n⚠️  {len(errores)} errores encontrados:")
        for error in errores:
            print(f"  - {error}")

    # Eliminar carpetas vacias
    for carpeta in categorias.keys():
        ruta_carpeta = os.path.join(ruta_destino, carpeta)
        if os.path.exists(ruta_carpeta) and not os.listdir(ruta_carpeta):
            os.rmdir(ruta_carpeta)
            print(f"🗑️  Carpeta vacia eliminada: {carpeta}/")

    print("\n✅ Organizacion completada")


if __name__ == "__main__":
    # ============================================================
    # CONFIGURACION - Modificar segun tus necesidades
    # ============================================================

    # Rutas de origen (de donde tomar los archivos)
    rutas_origen = [
        "C:\\Users\\Fibonacci-pc\\Downloads",
        "C:\\Users\\Fibonacci-pc\\Desktop",
        "C:\\Users\\Fibonacci-pc\\Documents",
        "C:\\Users\\Fibonacci-pc\\Pictures",
        "C:\\Users\\Fibonacci-pc\\Videos"
    ]

    # Ruta de destino unica (donde se crearan las carpetas organizadas)
    # Puedes cambiar esta ruta a donde prefieras
    ruta_destino = "C:\\Users\\Fibonacci-pc\\Archivos_Organizados"

    # ============================================================

    print("🗂️  ORGANIZADOR CENTRALIZADO DE ARCHIVOS")
    print("=" * 50)
    print(f"📍 Destino: {ruta_destino}")
    print(f"📂 Origenes: {len(rutas_origen)} ubicaciones")
    print("=" * 50)

    organizar_archivos_centralizado(rutas_origen, ruta_destino)
