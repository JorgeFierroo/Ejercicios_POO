class Reserva:
    def __init__(self, nombre_del_pasajero, numero_de_vuelo, fecha):
        self.nombre_del_pasajero = nombre_del_pasajero
        self.numero_de_vuelo = numero_de_vuelo
        self.fecha = fecha

    def mostrar_detalle(self):
        return f"Reserva para {self.nombre_del_pasajero} en el vuelo {self.numero_de_vuelo} el {self.fecha}."

class ReservaEconomica(Reserva):
    def __init__(self, nombre_del_pasajero, numero_de_vuelo, fecha, asiento):
        super().__init__(nombre_del_pasajero, numero_de_vuelo, fecha)
        self.asiento = asiento 

    def mostrar_detalle(self):
        return f"Reserva Económica: {super().mostrar_detalle()} Asiento: {self.asiento}."

class ReservaBusiness(Reserva):
    def __init__(self, nombre_del_pasajero, numero_de_vuelo, fecha, acceso_vip):
        super().__init__(nombre_del_pasajero, numero_de_vuelo, fecha)
        self.acceso_vip = acceso_vip 

    def mostrar_detalle(self):
        return f"Reserva Business: {super().mostrar_detalle()} Acceso VIP: {'Sí' if self.acceso_vip else 'No'}."

class ReservaPrimeraClase(Reserva):
    def __init__(self, nombre_del_pasajero, numero_de_vuelo, fecha, beneficios):
        super().__init__(nombre_del_pasajero, numero_de_vuelo, fecha)
        self.beneficios = beneficios

    def mostrar_detalle(self):
        return f"Reserva Primera Clase: {super().mostrar_detalle()} Beneficios: {', '.join(self.beneficios)}."


# Ejemplo de uso
reserva1 = ReservaEconomica("Juan Pérez", "AB123", "13-09-2023", "42A")
reserva2 = ReservaBusiness("Ana Soto", "AB124", "14-09-2023", True)
reserva3 = ReservaPrimeraClase("Luisa Medina", "AB125", "15-09-2023", ["Champán", "Cama reclinable"])

reservaciones = [reserva1,reserva2,reserva3]

for i in(reservaciones):
    print(i.mostrar_detalle())