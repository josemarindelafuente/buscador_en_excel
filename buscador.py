import pandas as pd


print("cargando archivo...")

archivo_excel = 'notas.xlsx'
hoja = 2
df = pd.read_excel(archivo_excel, sheet_name=hoja )

# Función para buscar la palabra en el archivo Excel
def buscar_palabra(palabra):
    resultados = df[df.apply(lambda row: row.astype(str).str.contains(palabra, case=False).any(), axis=1)]
    return resultados

while True:
    palabra = input("Ingrese una palabra para buscar (o 'salir' para terminar): ")
    
    if palabra.lower() == 'salir':
        print("Finalizando la búsqueda.")
        break
    
    resultados = buscar_palabra(palabra)
    
    if not resultados.empty:
        print("Resultado(s) encontrado(s):")
        print(resultados)
    else:
        print(f"No se encontró '{palabra}' en el archivo.")

