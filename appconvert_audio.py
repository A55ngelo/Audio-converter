import os
from pydub import AudioSegment
Extensiones_de_audio = ('.m4a', '.mp3', '.wav', '.ogg', '.flac', '.wma', '.aac')

def convertir_carpeta():
    print('|----------CONVERTIDOR DE AUDIO----------|')
    carpeta_origen = input("Ingresa la ruta de tu audio (o carpeta de audios a convertir): ").strip().strip('"')
    formato_deseado = input("Seleccione un formato que desees (ejm: mp3, wav): ").lower().strip()
    carpeta_destino = os.path.join(carpeta_origen, f"Convertido(s)_a_{formato_deseado}")
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)
        print(f"Carpeta creada: {carpeta_destino}")
        
    archivos_convertidos = 0
    errores = 0
    
    print("\n--- Iniciando conversión ---")
    
    for archivo in os.listdir(carpeta_origen):
        if archivo.lower().endswith(Extensiones_de_audio):
            ruta_completa = os.path.join(carpeta_origen, archivo)
            
            nombre_base = os.path.splitext(archivo)[0]
            nombre_final = f"{nombre_base}.{formato_deseado}"
            ruta_salida = os.path.join(carpeta_destino, nombre_final)
            
            print(f"Procesando: {archivo}", end="\r")
            
            try:
                audio = AudioSegment.from_file(ruta_completa)
                audio.export(ruta_salida, format=formato_deseado)
                print(f"Terminado: {nombre_final}" + " "*10)
                archivos_convertidos += 1
            except FileNotFoundError as e:
                print(f"No se encontró el archivo {archivo}: {e}")
                errores += 1
            except PermissionError as e:
                print(f"Sin permisos para leer/escribir {archivo}: {e}")
                errores += 1
            except Exception as e:
                print(f"Error de conversión con el archivo {archivo}: {e}")
                errores += 1
                
    print("\n" + "="*30)
    print("Resumen:")
    print(f"-Total convertidos: {archivos_convertidos}")
    print(f"-Errores: {errores}")
    print(f"-Encuentra tus archivos en: {carpeta_destino}")
    print("="*30)
    
if __name__ == "__main__":
    convertir_carpeta()