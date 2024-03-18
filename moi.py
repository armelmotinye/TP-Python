def convertir_en_celsius():
    """
# Convertit une température de Fahrenheit en Celsius en demandant à l'utilisateur d'entrer la température.
    
    Returns:
    # température équivalente en Celsius
    """
    while True:
        try:
            temp_fahrenheit = float(input("Entrez la température en Fahrenheit : "))
            celsius = (temp_fahrenheit - 32) * 5 / 9
            return celsius
            break
        except ValueError:
            print("Veuillez entrer une température valide.")

# Test de la fonction
temp_celsius = convertir_en_celsius()
print("Température en Celsius :", temp_celsius)
