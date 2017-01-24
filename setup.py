#
# Flask-Rollbar
#
# Copyright (C) 2017 Boris Raicheff
# All rights reserved
#


from setuptools import setup


setup(
    name='Flask-Rollbar',
    version='0.1.0',
    description='Flask-Rollbar',
    author='Boris Raicheff',
    author_email='b@raicheff.com',
    url='https://github.com/raicheff/flask-rollbar',
    install_requires=('flask', 'rollbar'),
    py_modules=('flask_rollbar',),
)


# EOF
