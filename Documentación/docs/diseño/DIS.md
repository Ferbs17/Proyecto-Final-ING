# Diseño

## Pantalla Principal

![](/archivos/proyecto/TacoApp.png)

Optamos por un menu simple en donde se pueda identificar de manera intuitiva a que menu corresponde cada boton.

- Tortillas: Tortillerias registrada
- Carnes: Carniceria registrada
- Verduras: Verdulerias registrada
- Bebidas: Provedores de refresco y cervezas
- Otros: Cualquier otro puesto que no encaje en la categorias principales
- Añadir: Un submenu donde podras registrar un nuevo provedor

Cada uno de los botones ajusta su anchura de manera automatica y con una altura fija para no desbordar sobre el menu.

Cada boton cuenta con un icono escalable y una etiqueta que denomia sun nombre, al hacer clic sobre uno te dirijirá a su submenu correspondiente

## Submit Menu

![](/archivos/proyecto/TacoApp_2.png)

En este menu es donde el usuario ingresa los datos para registrar un nuevo local/provedor de materiales.

Cada objeto contiene las siguientes caracteristicas:

- Nombre
- Numero telefonico
- Direccion
- ID: Este es generado internamente al ingresar los 3 campos anteriores
  
Al final se encuentran los botones **Submit** y **Cancel**, el primero para registrar y subir los datos a una base de datos donde se creara un objeto con un **ID** unico para su posterior utilización, el segun simplemente eliminara lo que hayas ingresado en los campos anteriores y te regresara al menu principal

Cada campo se ajusta automaticamente de forma horizontal, y el campo **Dirección** puede admitir multiples lineas para direcciones muy largas

## View Menu

![](/archivos/proyecto/TacoApp_1.png)

Al ingresar al menu se conecta a la base de datos del menu que hayas seleccionado (Tortillas, Carne, Verduras, Bebidas, Otros) y por cada instancia en la base de datos se genera una tarjeta con el **Nombre**, **Telefono** y su **Dirección**.

Al hacer clic sobre cada tarjeta la expande para que poder visualizar por completo el campo de **Dirección**.

Todas las tarjetas estan en un *ScrollView* para poder deslizar el menu y observar que tarjetas estan ocultas sin desbordar el menu.

Al final en una esquina esta colocado de forma fija un boton para ir hacia el menu principal