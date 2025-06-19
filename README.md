# 🛰️ DNSEXFILTER

**DNSExfilter** es un script en Python diseñado para demostrar cómo se puede realizar **exfiltración de datos utilizando el protocolo DNS**. Simula el comportamiento de un malware que codifica información sensible en Base64 y la fragmenta en subdominios, enviando consultas DNS a un servidor bajo control del atacante.

Estas consultas aparentan ser legítimas, pero contienen fragmentos de datos que luego son reconstruidos en el servidor remoto. Esta técnica permite evadir medidas tradicionales de seguridad, ya que el tráfico DNS suele estar permitido y no siempre es inspeccionado profundamente.

> ⚠️ Esta herramienta tiene fines educativos y de concienciación en ciberseguridad. **No debe utilizarse fuera de entornos controlados o sin autorización.**

---

## 🚩 Características

- 🔐 Simulación de exfiltración de datos a través de DNS.
- 📦 Codificación en Base64 para transmitir información sensible.
- ✂️ Fragmentación automática del archivo según el límite de subdominios.
- 🧪 Tráfico DNS que aparenta ser legítimo.
- 🌐 Personalización del dominio bajo control del atacante.
- 📥 Captura y reconstrucción de datos en el servidor DNS.
- 📊 Salida detallada en consola con progreso y estadísticas.
- 🎯 Útil para pruebas de concepto, análisis forense o entrenamiento ofensivo.

---

## ⚙️ Requisitos

Asegúrate de contar con lo siguiente:

- Python 3
- Módulos estándar de Python: `socket`, `base64`, `random`, `time`
- Módulo adicional:
  ```bash
  pip install dnslib

## Herramienta externa sugerida (opcional para decodificación manual):
- https://www.base64decode.org/


## Instalación

- Clonar el repositorio
```bash
  git clone https://github.com/tuusuario/dnsexfilter.git
  cd dnsexfilter
  chmod +x Servidor_DNSExfilter.py Clientes_DNSexfilter.py
##

