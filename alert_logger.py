import logging
import subprocess
import ipaddress

# Configuración del archivo de registro
logging.basicConfig(
    filename="alertas_seguridad.log",
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# Función para registrar alertas
def registrar_alerta(ip, evento):
    mensaje = f"IP: {ip} - Evento: {evento}"

    logging.warning(mensaje)

    print("\n¡ALERTA DE SEGURIDAD!")
    print(mensaje)


# Función para bloquear una IP sospechosa
def bloquear_ip(ip):
    try:
        ipaddress.ip_address(ip)

        subprocess.run(
            ["sudo", "ufw", "deny", "from", ip],
            check=True
        )

        print("IP bloqueada:", ip)
        logging.warning(f"IP bloqueada: {ip}")

    except ValueError:
        print("La dirección IP no es válida")

    except FileNotFoundError:
        print("UFW no está disponible en este sistema")

    except subprocess.CalledProcessError:
        print("No se pudo bloquear la IP")


# Programa principal
if __name__ == "__main__":

    print("Sistema de Alertas de Seguridad")

    ip = input("Ingrese la IP sospechosa: ")

    evento = input("Ingrese el evento detectado: ")

    registrar_alerta(ip, evento)

    bloquear = input("\n¿Desea bloquear esta IP? (si/no): ")

    if bloquear.lower() == "si":
        bloquear_ip(ip)
    else:
        print("No se bloqueó ninguna IP")
