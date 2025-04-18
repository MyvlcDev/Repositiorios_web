import qrcode

# URL que deseas convertir en código QR
data = "https://myvlcsys.com"

# Crear el código QR
qr = qrcode.QRCode(
    version=1,  # Controla el tamaño del QR (1 es el menor tamaño)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nivel de corrección de errores (L, M, Q, H)
    box_size=10,  # Tamaño de cada caja del QR
    border=4,  # Tamaño del borde
)
qr.add_data(data)
qr.make(fit=True)

# Crear la imagen del QR
img = qr.make_image(fill_color="black", back_color="white")

# Guardar la imagen
img.save("myvlcsys_qr.png")

print("Código QR generado y guardado como myvlcsys_qr.png")