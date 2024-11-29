
nombre_usuario = "Juan"
edad_usuario = 25
print(f"El usuario se llama {nombre_usuario} y tiene {edad_usuario} años.")


ciudad_origen = "Monterrey"
ciudad_destino = "Guadalajara"
ruta_viaje = f"El viaje será desde {ciudad_origen} hasta {ciudad_destino}."
print(ruta_viaje)


temperatura_actual = 22.5
humedad_relativa = 65
print(f"La temperatura actual es de {temperatura_actual}°C y la humedad relativa es del {humedad_relativa}%.")


temperatura_actual = 24.8
print(f"La temperatura ha cambiado. Ahora es de {temperatura_actual}°C y la humedad relativa sigue siendo del {humedad_relativa}%.")


nivel_alerta = "moderado"
if nivel_alerta == "bajo":
    print("No hay riesgos importantes. Continúa con tus actividades.")
elif nivel_alerta == "moderado":
    print("Mantente alerta. Toma precauciones si es necesario.")
elif nivel_alerta == "alto":
    print("Evita actividades al aire libre y sigue las instrucciones de seguridad.")
else:
    print("Nivel de alerta desconocido. Verifica la información.")
