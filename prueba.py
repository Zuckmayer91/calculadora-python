class SistemaEntregaAlimentos:
    def __init__(self):
        # Inicializar variables necesarias
        self.registro_pedidos = []
        self.porcentaje_descuento_grande = 10
        self.porcentaje_descuento_pequeno = 5

    def agregar_pedido(self, detalles_pedido):
        """ Agrega detalles del pedido de comida al registro de pedidos.
        Args:
            - detalles_pedido (dict): Detalles del pedido de comida.
        """
        # Completar el código aquí
        self.registro_pedidos.append(detalles_pedido)

    def actualizar_estado(self, numero_pedido, estado):
        """ Actualiza el estado de recogida y entrega del pedido.
        Args:
            - numero_pedido (int): Número de pedido.
            - estado (str): Nuevo estado del pedido (por ejemplo, 'Recogido', 'Entregado').
        """
        # Completar el código aquí
        for pedido in self.registro_pedidos:
            if pedido["numero_pedido"] == numero_pedido:
                pedido["estado"] = estado

    def modificar_pedido(self, numero_pedido, nuevos_articulos):
        """ Modifica los artículos del pedido solo si el pedido no se recoge.
        Args:
            - numero_pedido (int): Número de pedido.
            - nuevos_articulos (list): Nuevos artículos del pedido.
        """
        # Completar el código aquí
        for pedido in self.registro_pedidos:
            if pedido["numero_pedido"] == numero_pedido and pedido["estado"] != "Recogido":
                pedido["articulos"] = nuevos_articulos

    def cancelar_pedido(self, numero_pedido):
        """ Cancela el pedido si el pedido no se recoge.
        Args:
            - numero_pedido (int): Número de pedido.
        """
        # Completar el código aquí
        for pedido in self.registro_pedidos:
            if pedido["numero_pedido"] == numero_pedido and pedido["estado"] != "Recogido":
                self.registro_pedidos.remove(pedido)

    def generar_factura(self, numero_pedido, total):
        """ Genera una factura total según los detalles proporcionados.
        Args:
            - numero_pedido (int): Número de pedido.
            - total (float): Monto total del pedido.
        Returns:
            - str: Factura generada según las condiciones dadas.
        """
        # Completar el código aquí
        for pedido in self.registro_pedidos:
            if pedido["numero_pedido"] == numero_pedido:
                if total > 1000:
                    factura_total = total + (0.1 * total)
                else:
                    factura_total = total + (0.05 * total)
                return f"Factura para el pedido {numero_pedido}: ${factura_total}"

# Pruebas
sistema = SistemaEntregaAlimentos()

# Prueba 1
sistema.agregar_pedido({"numero_pedido": 1, "articulos": ["Pizza", "Refresco"], "estado": "Pendiente"})
sistema.actualizar_estado(1, "Recogido")
sistema.modificar_pedido(1, ["Hamburguesa", "Papas"])
print(sistema.generar_factura(1, 1200)) # Debería imprimir: "Factura para el pedido 1: $1080.0"

# Prueba 2
sistema.agregar_pedido({"numero_pedido": 2, "articulos": ["Ensalada", "Agua"], "estado": "Pendiente"})
sistema.cancelar_pedido(2)
print(sistema.generar_factura(2, 800)) # Debería imprimir: "Factura para el pedido 2: $760.0"
