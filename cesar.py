def cifra_cesar(texto, deslocamento, modo="criptografar"):
    """
    Implementa a Cifra de César para criptografar ou descriptografar um texto.

    Args:
        texto (str): O texto de entrada.
        deslocamento (int): O número de posições para deslocar.
        modo (str): Escolha "criptografar" ou "descriptografar".

    Returns:
        str: O texto resultante.
    """
    if modo == "descriptografar":
        deslocamento = -deslocamento

    resultado = ""
    for char in texto:
        if char.isalpha():  # Apenas caracteres alfabéticos serão processados
            base = ord('A') if char.isupper() else ord('a')
            novo_char = chr((ord(char) - base + deslocamento) % 26 + base)
            resultado += novo_char
        else:
            resultado += char  # Manter caracteres não alfabéticos inalterados
    return resultado
