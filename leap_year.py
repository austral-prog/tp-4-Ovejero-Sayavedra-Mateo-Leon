def leap_year():
    year = int(input("Ingrese un año: "))
    is_leap = year %4 == 0 and year%100 != 0 or 3(year %400 == 0)
    if is_leap:
        print(f"El año {year} es bisiesto")
    else:
        print(f"El año {year} no es bisiesto")
