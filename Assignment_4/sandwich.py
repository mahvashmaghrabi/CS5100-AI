import re


class Sandwich:
    def __init__(self, breads=None, spreads=None, ingredients=[], options=[], exceptions=[]):
        self.breads = breads
        self.spreads = spreads
        self.ingredients = ingredients
        self.options = options
        self.exceptions = exceptions

    def __str__(self):
        return "Bread-type: " + self.breads + "\n" + "Spread: " + self.spreads + "\n" + "Options: " + ', '.join(self.options) + "\n" + "Exceptions: " + ', '.join(self.exceptions) + "\n" +\
               "Usual Ingredients: " + ', '.join(self.ingredients)

def find_sandwich(text):
    
    match = re.search(r"\bmahvash's veggie\b", text)
    match2 = re.search(r"\bbeef club\b", text)
    match3 = re.search(r"\bspecial chicken\b", text)
    match4 = re.search(r"\bbaked cheese\b", text)
    if match:
        return "Mahvash's Veggie Sandwich"
    elif match2:
        return "Beef Club Sandwich"
    elif match3:
        return "Special Chicken Sandwich"
    elif match4:
        return "Baked Cheese Sandwich"
    return None

def find_bread(text, order):
    ##find bread
    bread1 = re.search(r"\bwheat\b", text)
    if bread1:
        order.breads = "wheat"
    bread2 = re.search(r"\brye\b", text)
    if bread2:
        order.breads = "rye"
    bread3 = re.search(r"\bitalian\b", text)
    if bread3:
        order.breads = "italian"

def find_spread(text, order):
    ##find spread
    spread1 = re.search(r"\bmayo\b", text)
    if spread1:
        order.spreads = "mayo"
    spread2 = re.search(r"\bbutter\b", text)
    if spread2:
        order.spreads = "butter"
    spread3 = re.search(r"\bmustard\b", text)
    if spread3:
        order.spreads = "mustard"
    spread4 = re.search(r"\bmayonnaise\b", text)
    if spread4:
        order.spreads = "mayo"


def find_options(text, order):
    ##find options
    options1 = re.search(r"\bgrilled\b", text)
    if options1:
        order.options.append("grilled")
    options2 = re.search(r"\bsalt and pepper\b", text)
    if options2:
        order.options.append("salt and pepper")
    options3 = re.search(r"\bcut in half\b", text)
    if options3:
        order.options.append("cut in half")


def find_exceptions(text, order):
    ##find exceptions
    exceptions1 = re.search(r"\bhold the mayo\b", text)
    if exceptions1:
        order.exceptions.append("hold the mayo")
    exceptions2 = re.search(r"\bno onions\b", text)
    if exceptions2:
        order.exceptions.append("no onions")
    exceptions3 = re.search(r"\bno pickles\b", text)
    if exceptions3:
        order.exceptions.append("no pickles")
    exceptions4 = re.search(r"\bdo not add pickles\b", text)
    if exceptions4:
        order.exceptions.append("no pickles")
    exceptions5 = re.search(r"\bno mayonnaise\b", text)
    if exceptions5:
        order.exceptions.append("hold the mayo")
    exceptions6 = re.search(r"\bremove the onions\b", text)
    if exceptions6:
        order.exceptions.append("no onions")


def understand(text, order):
    find_bread(text, order)
    find_spread(text, order)
    find_options(text, order)
    find_exceptions(text, order)


def main():
    breads = ["wheat", "rye", "italian"]
    spreads = ["mayo", "butter", "mustard"]
    options = ["grilled", "salt and pepper", "cut in half"]
    exceptions = ["hold the mayo", "no onions", "no pickles"]
    menu = {
        "Mahvash's Veggie Sandwich": Sandwich("keto", "pesto", ["carrots", "tomatoes", "cucumbers"], options, exceptions),
        "Beef Club Sandwich": Sandwich("white ", "cream", ["beef", "tomatoes", "lettuce"], options, exceptions),
        "Special Chicken Sandwich": Sandwich("french", "ketchup", ["chicken", "cheese", "lettuce"], options, exceptions),
        "Baked Cheese Sandwich": Sandwich("brown", "avocado", ["cheese", "jalapenos", "tomatoes"], options, exceptions)
    }
    print("Welcome to the Sandwich Club")
    order = Sandwich()
    default = None
    name = None
    text = input("What would you like to have ? ")
    text = text.lower()
    match = re.search("menu", text)
    if match:
         # print([k + ":" + str(v) for k, v in menu.items()])
         for key, value in menu.items():
             print(key, ' : ', value)

    while (name == None):
        name = find_sandwich(text)
        if (name == None):
            text = input("What would you like to have ? ")

    default = menu[name]
    order.ingredients = default.ingredients
    while (order.breads == None):
        understand(text, order)
        if (order.breads == None):
            text = input("This sandwich usually comes with " + default.breads + " bread"
                         + ". we have following options" + str(breads))
            if text == "":
                order.breads = default.breads

    while (order.spreads == None):
        understand(text, order)
        if (order.spreads == None):
            text = input("this sandwich usually comes with " + default.spreads + " spread"
                         + ". we have following options" + str(spreads))
            if text == "":
                order.spreads = default.spreads

    while not order.options:
        # understand(text, order)
        if not order.options:
            text = input("We have following options to choose from" + str(options))
            if text == "":
                break
        understand(text, order)

    while not order.exceptions:
        # understand(text, order)
        if not order.exceptions:
            text = input("You can choose any exceptions if you want" + str(exceptions))
            if text == "":
                break
        understand(text, order)

    print("Name of sandwich : " + name)
    print(order)
    opt = input('Do you want to order anything else?')
    opt = str(opt).lower()
    if (opt == 'yes'):
        main()


if __name__ == "__main__":
    main()
