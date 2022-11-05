# {{cookiecutter.project_name}}
{{cookiecutter.short_description}}

![Django CI](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.directory_name}}/actions/workflows/django-test.yml/badge.svg)

License
-------

Distributed under the terms of the [{{cookiecutter.license}}](LICENSE) license,

Running in development mode
------
First install the dependencies
{% if cookiecutter.packaging == 'pip' %}
    pip install -r requirements/develop.txt
{% elif cookiecutter.packaging == 'poetry' %}
    poetry install
{% endif %}
Then run the development server

    python manage.py runserver --settings=config.settings.develop
