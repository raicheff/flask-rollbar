#
# Flask-Rollbar
#
# Copyright (C) 2017 Boris Raicheff
# All rights reserved
#


from setuptools import setup

from flask_rollbar import __version__


setup(
    name='Flask-Rollbar',
    version=__version__,
    description='Flask-Rollbar',
    author='Boris Raicheff',
    author_email='b@raicheff.com',
    url='https://github.com/raicheff/flask-rollbar',
    install_requires=('flask', 'rollbar'),
    py_modules=('flask_rollbar',),
)


# EOF
