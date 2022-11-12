
# question 1:

short_list_of_mountains = ["Verstovia", "Bear", "South Sister"]
def fourth_place(list_one: str ) -> str:
    """This is a function that returns the fourth item in a list.

    Args:
        list_one (str): a list with an index of 3 or greater

    Returns:
        str: the fourth item in the list or an error message for an index error if the list has an index less than 3
    """
    try:
        return list_one[3]
    except IndexError as E:
        print(E)

fourth_place(short_list_of_mountains)

# question 2:

subtracter_lambda = (lambda a, b: b - a)
print(subtracter_lambda(2, 4))

# question 3:

class Shoe:
    """The shoe object contains the size color and smell of a shoe

    Parameters
    ----------
    US_size: int
        The US size of a shoe
    color: str
        The color of the shoe
    smelly: bool
        If the shoe is smelly or not
    """
    def __init__(self, US_size: int, color: str, smelly: bool) -> str:
        self.US_size = US_size
        self.color = color
        self.smelly = smelly

    def euro_size(self):
        """The function converts the US shoe size to a European shoe size

        returns
        -------
        European shoe size: str
        """
        print(str(self.US_size + 33))

altra = Shoe(9,"blue", smelly=True)
altra.euro_size()
addidas = Shoe(11, "white", smelly=False)
addidas.euro_size()

# question 4:

def galaxy(name: str, *stuff: str, pluto_is_a_planet: True, **planets: str) -> str:
    """This is a function that returns a paragraph of galaxy facts.

    Args:
        name (str): name of the galaxy
        *stuff(str): Various items found in the galaxy
        pluto_is_a_planet (True): if pluto is a planet
        **planets(str): a dictionary where keys = the planet name and values = the planet color

    Returns:
        str: paragraph of galaxy facts
    """

    solar_stuff = ""
    for i in (stuff):
        if i == stuff[-1]:
            solar_stuff += f"and a {i}. "
        else:
            solar_stuff += f"{i}, "

    what_is_pluto = ""
    if pluto_is_a_planet == True:
        what_is_pluto = "and pluto!"
    else:
       what_is_pluto = "not including pluto!"
    
    planet_string = ""
    for k, v in planets.items():
        if k == list(planets.keys())[-1]:
            planet_string += f" and {k} is the color {v}."
        else:
            planet_string += f" {k} is the color {v},"

    print(f"The {name} galaxy contains a lot of stuff including {len(planets)} planets {what_is_pluto} Here are the other planets in the galaxy and their color:{planet_string} The {name} galaxy also contains {solar_stuff}")

galaxy("Milky Way", "asteroids", "dust", "solar system", pluto_is_a_planet=True, Mercury = "slate gray", Mars = "red")
