"""Module for pizza functions."""
def pizza_filling(size, *ingredientes):
    """Return the size and topping of a pizza.

    param size: Size of the pizza
    param ingredientes: Tuple with all the toppings
    """
    print(type(ingredientes))
    print("Cocinando pizza de " + str(size) + " pulgadas con los siguientes ingredientes:")
    for ing in ingredientes:
        print("- " + ing.capitalize())