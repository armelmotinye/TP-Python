def convertir_en_celsius (temperature_fah):
    temperature_celsius = (temperature_fah - 32) * 5/9
    return temperature_celsius
temp_degrefah = 104
temp_celsius = convertir_en_celsius(temp_degrefah)
print(("la temperature"), temp_degrefah, "degre fah est equivalent a", temp_celsius, "degres celsius")

