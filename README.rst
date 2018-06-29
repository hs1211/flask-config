===================
Flask Configuration
===================

From this https://damyanon.net/post/flask-series-configuration/ series, I make enhanced version config management in flask.
Whole project structure is so nice in my opinion. The structure is like following.

.. code-block:: text

    ├── Pipfile
    ├── Pipfile.lock
    ├── README.rst
    ├── app
    │   ├── __init__.py
    │   ├── about
    │   │   ├── __init__.py
    │   │   └── controller.py
    │   └── config.py
    ├── bin
    ├── config.cfg
    ├── docs
    ├── run.py
    └── tests
        └── __init__.py




How to setup this project?
--------------------------
We are using pipenv in this codebase. The followings are setup command.

.. code-block:: bash

    $ PIPENV_VENV_IN_PROJECT=true pipenv --three
    $ pipenv shell
    $ pipenv install


Way to set up configuration
---------------------------

1) EnvVar

.. code-block:: python

    app.config.from_envvar('FLASK_CONFIG')

    or

    stage = os.getenv('FLASK_CONFIG', 'local')

2) Object

.. code-block:: python

    app.config.from_object('module_name.DevelopmentConfig')

3) File

.. code-block:: python

    app.config.from_pyfile('config.cfg', silent=True)


