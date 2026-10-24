import subprocess

ip = input("Ingrese la direccion IP a scanear de la MV: ")

print("Scaneando direccion IP :", ip)
print("IP objetivo: ", ip)

resultado = subprocess.run(
    ["nmap", "-sS", ip],
    capture_output=True,
    text=True
)

print("\n===== Resultado del Escaneo ======")
print(resultado.stdout)