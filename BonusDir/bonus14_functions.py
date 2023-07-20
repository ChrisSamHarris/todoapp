
def parse(feetInch):
    raw_val = feetInch.split()
    feet = float(raw_val[0])
    inches = float(raw_val[1])
    return feet, inches

def convert(feet, inches):
    meters = round(((feet * 0.3048) + (inches * 0.0254)),2)
    return meters