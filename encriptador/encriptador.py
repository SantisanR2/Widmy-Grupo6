import hashlib

def generar_hash(texto):
    # Crea un objeto hash utilizando el algoritmo SHA256
    hash_object = hashlib.sha256(texto.encode('utf-8'))
    # Genera el hash en formato hexadecimal
    hash_hex = hash_object.hexdigest()
    # Devuelve el hash generado
    return hash_hex
