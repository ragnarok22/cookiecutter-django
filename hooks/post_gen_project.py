import os
import secrets
import shutil

PROJECT_PATH = os.getcwd()

REMOVE_PATHS = [
    '{% if cookiecutter.packaging != "pip" %} requirements {% endif %}',
    '{% if cookiecutter.packaging != "poetry" %} poetry.lock {% endif %}',
    '{% if cookiecutter.packaging != "poetry" %} pyproject.toml {% endif %}',
]


def generate_secret() -> str:
    """
    Return a 50 character random string usable as a SECRET_KEY setting value.
    """

    def get_random_string(length, allowed_chars):
        """
        Return a securely generated random string.
        The bit length of the returned value can be calculated with the formula:
            log_2(len(allowed_chars)^length)
        For example, with default `allowed_chars` (26+26+10), this gives:
          * length: 12, bit length =~ 71 bits
          * length: 22, bit length =~ 131 bits
        """
        return "".join(secrets.choice(allowed_chars) for _ in range(length))

    chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"
    return get_random_string(50, chars)


for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)

env_file = '.env'
content = f"""DJANGO_SETTINGS_MODULE=config.settings.production
SECRET_KEY={generate_secret()}
DB_NAME=postgres
DB_HOST=postgres
DB_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

"""

with open(os.path.join(PROJECT_PATH, env_file), "w") as file:
    file.write(content)
