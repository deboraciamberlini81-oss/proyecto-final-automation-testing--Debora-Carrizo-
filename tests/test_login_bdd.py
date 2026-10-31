
pytest_plugins = ["features.steps.login_steps"]

from pytest_bdd import scenarios


scenarios("../features/login.feature")
