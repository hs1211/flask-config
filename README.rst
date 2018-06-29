===================
Flask Configuration
===================


How to setup this project?
==========================
We are using pipenv in this codebase. The followings are setup command.

.. code-block:: bash
    $ PIPENV_VENV_IN_PROJECT=true pipenv --three
    $ pipenv shell
    $ pipenv install


Way to set up configuration
===========================

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


