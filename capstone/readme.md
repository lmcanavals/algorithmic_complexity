# Complejidad Algorítmica

## Trabajo Parcial

### Descripción

El trabajo parcial consiste en resolver el problema de enrutamiento de vehículos
o VRP, en su versión para múltiples puntos de distribución.

[Video explicativo](https://youtu.be/OKMssWdC0I0)

El objetivo es buscar un balance entre el tiempo y costo de entrega. Un ejemplo
del problema es el caso de los supermercados, los cuales reciben pedidos por su
aplicación web o móvil, luego deben planificar la distribución considerando
minimizar el costo de operación de los vehículos y el tiempo de distribución
ya que a mayor demora en el tiempo de entrega, menor satisfacción por parte de
sus clientes lo cual puede significar una pérdida por perder clientes
desatisfechos.

Para simplificar el problema se plantea que la ciudad donde se distribuye tiene
una distribución perfectamente rectangular, similar a la ciudad de Manhattan.

### Requisitos

* El dataset debe contener:
	* Entre 50 y 100 puntos de distribución (almacenes).
	* Entre 2500 y 5000 puntos de entrega.
	* Una cantidad ilimitada de vehículos en cada punto de distribución.
	* Costo por tiempo y distancia por cada vehículo.
* Cada punto de distribución y punto de entrega, está definido por una posición
X, Y correspondiente a un punto en la ciudad.

### Entregas

* Crear un repositorio en Github con el nombre todo en minúsculas con el código de la
  sección, el item (tf, se usará el mismo para ambos trabajos TP y TF) y finalmente
  los códigos de los estudiantes sin la **u**, por ejemplo:
  `cc41_tf_202011111_202012222_202013333_201924444`
* Elaborar un plan de actividades con responsables y fechas usando los Issues.
* En la semana 7 deberá presentar lo siguente:
	* Un dataset con las especificaciones dadas.
	* El espacio de búsqueda del problema.
	* Un análisis preliminar de la complejidad de los algoritmos de cada miembro.
	* Un reporte de actividades.

Todos los documentos y archivos deberán estar contenidos en el repositorio, los
elementos escritos deben estar en formato Markdown.

