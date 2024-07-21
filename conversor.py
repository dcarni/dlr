import os

def rename_files_to_txt():
    # Obtiene la ruta de la carpeta donde se encuentra el script
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Itera sobre todos los archivos en la carpeta
    for filename in os.listdir(script_directory):
        # Ignora los directorios, solo procesa archivos
        if os.path.isfile(os.path.join(script_directory, filename)):
            # Obtiene el nombre base sin extensión
            base = os.path.splitext(filename)[0]
            # Construye el nuevo nombre con la extensión .txt
            new_name = base + ".txt"
            # Renombra el archivo
            os.rename(os.path.join(script_directory, filename), os.path.join(script_directory, new_name))
            print(f'Renamed: {filename} to {new_name}')

if __name__ == "__main__":
    rename_files_to_txt()
