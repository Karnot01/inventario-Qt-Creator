import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from helpers import load_token, obtener_usuario_token, token_is_valid, url_api, delete_token
from routes import RouteManager

# Importamos la librería que nos permite manejar la API
import requests
# Libreria que convierte strings en diccionarios
import json

# Importamos el apartado gráfico del archivo "register.ui"
from ui_principal import Ui_PrincipalWindow

# Creamos una clase que contendrá la ventana que vamos a dibujar
class PrincipalWindow(QMainWindow):
    def __init__ (self, nombre_usuario='1', parent=None):
        super().__init__(parent)

        # Inicializo mi administrador de rutas
        self.route_manager = RouteManager()

        # Le creamos un atributo a mi clase llamada "correo_usuario"
        self.nombre_usuario = nombre_usuario

        # Ejecutamos la función que va a cargar el token
        token_actual = load_token()

        # Este atributo coontendrá todo el apartado gráfico
        self.ui = Ui_PrincipalWindow()
        # Lo inicializamos el apartado gráfico
        self.ui.setupUi(self)
        # Le decimos a la etiquetaque sobreescriba su contenido con el correo del usuario
        self.ui.mostrar_correo.setText(f'Bienvenido: {self.nombre_usuario}')
        # Obtener boton buscar, detectar que sea clikeado y buscar el producto
        self.ui.boton_buscar.clicked.connect(self.buscar)

        # Control de los checkBox
        # Cuando se inicie la app, el recuadro de ID vendrá seleccionado por defecto
        self.ui.check_id.setChecked(True)
        # Selección de checkbox
        self.ui.check_id.toggled.connect(self.check_id_presionado)
        self.ui.check_name.toggled.connect(self.check_name_presionado)

        # Cobntrol de cerrado de sesión
        self.ui.boton_cerrar.clicked.connect(self.cerrar_sesion)
        self.dirigir_a_login(token_actual)

    def check_id_presionado(self, checked):
        # Primer paso es verificar si un checkbox esta activado
        # Segundo paso es verificar si el otro checkbox esta presionado
        if checked and self.ui.check_name.isChecked():
            # Se desactiva el checkbox del name
            self.ui.check_name.setChecked(False)

    def check_name_presionado(self, checked):
        if checked and self.ui.check_id.isChecked():
            self.ui.check_id.setChecked(False)

    # Método para buscar un producto a través de la API
    def buscar_producto_id(self):

        id_producto = self.ui.buscador.text()

        # URL a la cual se hará la petición
        url = url_api + f"/objetos_almacen?id={id_producto}"

        token_actual = load_token()

        headers = {"Authorization": f"Bearer {token_actual}"}

        response = requests.get(url, headers=headers)

        print(response.content.decode('utf-8'))

        respuesta_json = json.loads(response.content.decode('utf-8'))

        print(type(respuesta_json))

        if "message" in respuesta_json:
            self.ui.nombre_producto.setText('No se encontró ningún producto')
            self.ui.cantidad_producto.setText('')

        elif "Cantidad" in respuesta_json:
            self.ui.nombre_producto.setText(f'Nombre: {respuesta_json["Nombre"]}')
            self.ui.cantidad_producto.setText(f'Cantidad: {respuesta_json["Cantidad"]}')

    # Nos va a ayudar a buscar el producto por su nombre en la API
    def buscar_producto_nombre(self):

        nombre_producto = self.ui.buscador.text()

        # URL para buscar producto por nombre
        url = url_api + f"/objetos_almacen?nombre={nombre_producto}"

        token_actual = load_token()

        headers = {"Authorization": f"Bearer {token_actual}"}

        response = requests.get(url, headers=headers)

        print(response.content.decode('utf-8'))

        respuesta_json = json.loads(response.content.decode('utf-8'))

        print(type(respuesta_json))

        if "message" in respuesta_json:
            self.ui.nombre_producto.setText('No se encontró ningún producto')
            self.ui.cantidad_producto.setText('')

        elif "Cantidad" in respuesta_json:
            self.ui.nombre_producto.setText(f'Nombre: {respuesta_json["Nombre"]}')
            self.ui.cantidad_producto.setText(f'Cantidad: {respuesta_json["Cantidad"]}')

    def buscar(self):
        if self.ui.check_id.isChecked():
            # Busca un producto por su ID
            self.buscar_producto_id()

        elif self.ui.check_name.isChecked():
            # Busca un producto por su nombre
            self.buscar_producto_nombre()

    def dirigir_a_login(self, token_actual):
        if token_actual != '' and token_is_valid(token_actual):
            # Obtenemos el usuario del token en el archivo
            self.nombre_usuario = obtener_usuario_token(token_actual)
            print('Existe un token')

        else:
            print('No hay token - El token expiró')
            self.route_manager.mandar_a_login(self)

            if token_actual != '' and token_is_valid(token_actual):
                # Obtenemos el usuario del token en el archivo
                self.nombre_usuario = obtener_usuario_token(token_actual)
                print('Existe un token')

            else:
                print('No hay token - El token expiró')
                self.route_manager.mandar_a_login(self)

    # Este método nos ayudará a cerrar sesión
    def cerrar_sesion(self):
        print ("Cerrando sesión")
        # Borrar el token existente
        delete_token()
        print('Token eliminado correctamente')
        # Mandamos al usuario a pantalla del login
        self.route_manager.mandar_a_login(self)

# Es un método mágico -> Verifica si el archivo se esta ejecutando de raíz
if __name__ == '__main__':
    # Inicializamos la aplicación (Ventana)
    app = QApplication(sys.argv)
