edad = int(input("Edad: "))
tiene_dpi = input("¿Tiene DPI?: (s/n)").lower()

#AND
if edad>=18 and tiene_dpi=="s":
    print("Bienvendio puedes entrar")
elif edad>=18 or tiene_dpi=="n":
    print("Vale tienes 18 pero no traes DPI, te dejaremos entrar")
elif not(edad>18 and tiene_dpi=="s"):
    print("No puedes entrar")