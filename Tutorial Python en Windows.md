# Tutorial de instalación de Python en Windows
## Instalando Python

 1. Descargar Python en la versión más estable disponible.
![Paso 1](/Im%C3%A1genes/Tutorial%20Python%20Windows/1.png)
 2. Abrir el instalador y verificar ambos campos disponibles.
![Paso 2](/Im%C3%A1genes/Tutorial%20Python%20Windows/4.png)
 3. Una vez completada la instalación, deshabilitar el límite de ruta máxima de Windows usando la función extra que ofrece el instalador de Python.
![Paso 3](/Im%C3%A1genes/Tutorial%20Python%20Windows/5.png)
 4. Abre cmd y ejecuta tanto el comando python, como pip3. Si el resultado es similar al de las imágenes, ambas funcionalidades se han instalado correctamente.
![Paso 4](/Im%C3%A1genes/Tutorial%20Python%20Windows/6.png)
![Paso 5](/Im%C3%A1genes/Tutorial%20Python%20Windows/7.png)
## Instalando Jupyter
 5. Con pip3 funcionando, basta con correr el siguiente comando que instalará jupyter para el usuario actual del sistema:
`pip3 install --user jupyter`
![Paso 5](/Im%C3%A1genes/Tutorial%20Python%20Windows/8.png)
 6. [OPCIONAL] Una vez finalizada la instalación, si aparecen mensaje de color amarillo como los de la imagen, deberás agregar la ruta de jupyter a la ruta general del sistema (*PATH*) copiando la ruta que está destacada, pero sin agregar las comillas.
![Paso 6](/Im%C3%A1genes/Tutorial%20Python%20Windows/9.png)
 7. [OPCIONAL] Abre las variables de entorno, y edita la variable *PATH* del usuario (si usas más de un usuario en el computador, opta por cambiar la variable del sistema).
![Paso 7](/Im%C3%A1genes/Tutorial%20Python%20Windows/11.png)
 8. [OPCIONAL] Una vez abierta la variable, agrega la nueva ruta de jupyter copiada en pasos anteriores con el botón **Nuevo**. Para finalizar, simplemente acepta en los 3 cuadros abiertos.
![Paso 8](/Im%C3%A1genes/Tutorial%20Python%20Windows/13.png)
 9. Una vez instalado correctamente jupyter, basta con cerrar y abrir la consola, y ejecutar para comprobar la instalación:
`jupyter notebook`
![Paso 9](/Im%C3%A1genes/Tutorial%20Python%20Windows/14.png)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTU5NzQ1ODk5OSwtMTI4NTY0Nzg4OSwxND
cwNDg0NzEzXX0=
-->