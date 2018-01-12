############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

    # def __repr__(self):
    #     """Provide helpful output when printing"""

    #     repr_str = "<MelonType code={code} name={name}>"
    #     return repr_str.format(code=self.code, name=self.name)


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    melon1 = MelonType("musk", "1998", "green", True, True, "Muskmelon")
    pairing1 = melon1.add_pairing("Mint")

    melon2 = MelonType("cas", "2003", "orange", True, False, "Casaba")
    pairing2 = melon2.add_pairing("Strawberry")
    pairing2 = melon2.add_pairing("Mint")

    melon3 = MelonType("cren", "1996", "green", True, False, "Crenshaw")
    pairing3 = melon3.add_pairing("proscuitto")

    melon4 = MelonType("yw", "2013", "yellow", True, True, "Yellow Watermelon")
    pairing4 = melon4.add_pairing("ice-cream")


    all_melon_types.append(melon1)
    all_melon_types.append(melon2)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        name = melon.name
        pairing = " ".join(melon.pairings)
        print"{} goes well with {}".format(name, pairing)


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # melon_types is a list of melon objects

    melon_codes = {}

    for melon in melon_types:
        melon_codes[melon.code] = melon

    return melon_codes
    

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, code, shape_rating, color_rating, harvested_from, 
                harvested_by):
        self.code = code
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self. harvested_from = harvested_from
        self.harvested_by = harvested_by
        

    def is_sellable(self, shape_rating, color_rating, harvested_from):

        return self.shape_rating > 5 and color_rating > 5 and harvested_from != 3
        
        

    # def __repr__(self):
    #     """Provide helpful output when printing"""

    #     repr_str = "<MelonType code={code} name={name}>"
    #     return repr_str.format(code=self.code, name=self.harvested_by)

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    available_melons = []

    melon_1 = Melon("yw", 8, 7, 2, "Sheila")
    available_melons.append(melon_1)

    melon_2 = Melon("yw", 3, 4, 2, "Sheila")
    available_melons.append(melon_2)

    melon_3 = Melon("yw", 9, 8, 3, "Sheila")
    available_melons.append(melon_3)

    melon_4 = Melon("cas", 10, 6, 35, "Sheila")
    available_melons.append(melon_4)

    melon_5 = Melon("cren", 8, 9, 35, "Michael")
    available_melons.append(melon_5)

    melon_6 = Melon("cren", 8, 2, 35, "Michael")
    available_melons.append(melon_6)

    melon_7 = Melon("cren", 2, 3, 4, "Michael")
    available_melons.append(melon_7)

    melon_8 = Melon("musk", 6, 7, 4, "Michael")
    available_melons.append(melon_8)

    melon_9 = Melon("yw", 7, 10, 3, "Sheila")
    available_melons.append(melon_9)

    return available_melons

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        for_sale = 



make_melon_types()
melons = make_melon_types()
print_pairing_info(melons)
make_melon_type_lookup(melons)
make_melons(melons)
current_melons = make_melons(melons)
get_sellability_report(current_melons)