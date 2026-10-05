salario_bruto = float(input("Salario bruto: "))
porcentaje_impuestos = float(input("Porcentaje de impuestos: "))
deducciones = float(input("Deducciones adicionales: "))

impuesto = salario_bruto * (porcentaje_impuestos / 100)
salario_neto = salario_bruto - impuesto - deducciones

print("El salario neto es:", salario_neto)