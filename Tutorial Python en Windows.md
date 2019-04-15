# Tutorial de instalación de Python en Windows
## Instalando Python

 1. Descargar Python en la versión más estable disponible.
![Paso 1](/Im%C3%A1genes/Tutorial%20Python%20Windows/1.png)
 2. Abrir el instalador y verificar ambos campos disponibles.
![Paso 2](/Im%C3%A1genes/Tutorial%20Python%20Windows/4.png)
 3. Una vez completada la instalación, deshabilitar el límite de ruta máxima de Windows usando la función extra que ofrece el instalador de Python.
 4. Abre cmd y ejecuta tanto el comando python, como pip3. Si el resultado es similar al de las imágenes, ambas funcionalidades se han instalado correctamente.
## Instalando Jupyter
 5. Con pip3 funcionando, basta con correr el siguiente comando que instalará jupyter para el usuario actual del sistema:
`pip3 install --user jupyter`
 6. [OPCIONAL] Una vez finalizada la instalación, si aparecen mensaje de color amarillo como los de la imagen, deberás agregar la ruta de jupyter a la ruta general del sistema (*PATH*).
 7. [OPCIONAL] Abre las variables de entorno, y edita la variable *PATH* del usuario (si usas más de un usuario en el computador, opta por cambiar la variable del sistema).
 8. [OPCIONAL] Una vez abierta la variable, agrega la nueva ruta de jupyter copiada en pasos anteriores con el botón **Nuevo**. Para finalizar, simplemente acepta en los 3 cuadros abiertos.
 9. Una vez instalado correctamente jupyter, basta con cerrar y abrir la consola, y ejecutar para comprobar la instalación:
`jupyter notebook`
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTM0MzMwNDc0NywtMTI4NTY0Nzg4OSwxND
cwNDg0NzEzXX0=
-->