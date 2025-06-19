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
  ```
- Herramienta externa sugerida (opcional para decodificación manual):
  - https://www.base64decode.org/

---

## 📦 Instalación

1. Clona el repositorio y navega al directorio:

   ```bash
   git clone https://github.com/tuusuario/dnsexfilter.git
   cd dnsexfilter
   chmod +x Servidor_DNSExfilter.py Clientes_DNSexfilter.py
   ```

2. Instala las dependencias:

   ```bash
   pip install dnslib
   ```

3. Verifica el uso del puerto 53 (requiere privilegios de superusuario en muchos sistemas):

   ```bash
   sudo lsof -i :53
   ```

---

## ▶️ Uso

### 🖥️ Lado del servidor (máquina atacante)

Inicia el servidor malicioso:

```bash
sudo python3 Servidor_DNSExfilter.py
```

- Escucha en el puerto 53.
- Extrae los fragmentos codificados de las consultas DNS.
- Muestra los datos recibidos en consola.
- Decodifica manualmente con herramientas externas si se desea ver el contenido del archivo.

> ⚠️ El servidor **debe iniciarse antes** que el cliente.

---

### 📤 Lado del cliente

Edita el archivo `Clientes_DNSexfilter.py` si deseas cambiar el nombre del archivo o el dominio.

Ejecuta el script:

```bash
python3 Clientes_DNSexfilter.py
```

- Lee el archivo `secreto.txt`.
- Fragmenta y codifica en Base64 cada parte.
- Envía consultas DNS tipo A a intervalos definidos por `RETARDO`.
- Las consultas se verán así:

  ```
  YWJjZGVmZ2g.1.oculto.com
  ```

---

## 📌 Notas Éticas y Limitaciones

- Esta herramienta es solo para **entornos de laboratorio**.
- No está permitida su ejecución contra sistemas sin consentimiento explícito.
- Utilízala únicamente con propósitos éticos, educativos y de investigación.
- Su uso indebido puede constituir una violación legal.

---

## 📚 Recursos

- [RFC 1035 - DNS Specification](https://tools.ietf.org/html/rfc1035)
- [OWASP - Data Exfiltration](https://owasp.org/www-community/attacks/Data_Exfiltration)
- [Base64 Decode Tool](https://www.base64decode.org/)

---

## 🧠 Autor

Desarrollado como PoC para entrenamientos ofensivos y análisis de amenazas en ciberseguridad. Si deseas contribuir, reportar mejoras o compartir ideas, ¡los PRs son bienvenidos!

---
