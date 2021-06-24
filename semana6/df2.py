import numpy as np
import pandas as pd
import io,os
RUTAEXCEL="D:/"

df = pd.read_excel(RUTAEXCEL +  "DatosRiesgoCredito.xlsx")
print(df)

df2 = pd.read_excel(RUTAEXCEL +  "DatosRiesgoCredito.xlsx", sheet_name="CreditosNegados")

#columnas de dataframe, imprime las columnas

df.columns


#Imprime el tipo de datos de cada columna, entero, decimal
df.dtypes

#Imprime el tipo de datos de cada columna, entero, decimal
df.info()


#Promedio de la edad de esos registros, las 2 inst hacen lo mismo
df.Edad.mean()
df['Edad'].mean()

# .describe() si un numero,entrega estadistica
df['Edad'].describe()


#el metodo .mean -> el promedio
df['Ingresos (U$)'].describe()

# Esta instruccion me mustra mas columnas, en este caso genero, edad
df[['Genero','Edad']]

# .groupby("Genero") -> agrupe por genero y saca el promedio
df[['Genero','Edad']].groupby("Genero").mean()

#.count() cuenta resgistros
df[['Genero','Edad']].groupby("Genero").count()


#.short organiza by (por)
df[['Genero','Edad']].sort_values(by="Edad")

# muestra solamente los datos donde la edad es mayor a 55
print(df2[df2['Edad'] > 55])

print(df2[df2['Edad'] > 55].groupby("Genero").count())

df3_resultado=df2[df2['Edad'] > 55]
print(df3_resultado)

df3_resultado.to_csv(RUTAEXCEL + "prueba.csv")
