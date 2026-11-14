pytest_plugins = ["features.steps.cart_steps"]

from pytest_bdd import scenarios


scenarios("../features/cart.feature")