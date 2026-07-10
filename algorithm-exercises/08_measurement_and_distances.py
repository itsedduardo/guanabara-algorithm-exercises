# Exercise 8 from Guanabara's Algorithm workbook!
# Build a program which reads a distance in meters and show it's relatives values in other measurement. 
# Units: km, hm, dam, m, dm, cm, mm

def unit_convertor(meter):
    kilometer = meter / 1000
    hectometer = meter / 100
    decameter = meter / 10
    decimeter = meter * 10
    centimeter = meter * 100
    millimeter = meter * 1000
    print(
        f"kilometer: {kilometer}, "
        f"hectometer: {hectometer}, "
        f"decameter: {decameter}, "
        f"decimeter: {decimeter}, "
        f"centimeter: {centimeter}, "
        f"millimeter: {millimeter} "
    )

meter = float(input("Write a distance in meters: "))
unit_convertor(meter)
