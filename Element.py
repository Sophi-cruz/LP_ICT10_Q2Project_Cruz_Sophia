from pyscript import display, document  # type: ignore


non_metals = {
    'Hydrogen': ('H', 'Hydrogen', 1, 1.008),
    'Helium': ('He', 'Helium', 2, 4.0026),
    'Lithium': ('Li', 'Lithium', 3, 6.94),
    'Beryllium': ('Be', 'Beryllium', 4, 9.0122),
    'Boron': ('B', 'Boron', 5, 10.81),
    'Carbon': ('C', 'Carbon', 6, 12.011),
    'Nitrogen': ('N', 'Nitrogen', 7, 14.007),
    'Oxygen': ('O', 'Oxygen', 8, 15.999),
    'Fluorine': ('F', 'Fluorine', 9, 18.998),
    'Neon': ('Ne', 'Neon', 10, 20.180),
}


def get_element_info(event=None):
    document.getElementById('result').innerHTML = ""
    element1 = document.getElementById('element-input').value.strip().title()


    result = non_metals.get(
        element1,
        ('Element not found', '-', '-', '-')
    )


    document.getElementById('result').innerHTML = f"""
    <b>Symbol:</b> {result[0]}<br>
    <b>Element:</b> {result[1]}<br>
    <b>Atomic Number:</b> {result[2]}<br>
    <b>Atomic Mass:</b> {result[3]}<br>
    """