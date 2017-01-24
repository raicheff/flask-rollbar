#
# Flask-Rollbar
#
# Copyright (C) 2017 Boris Raicheff
# All rights reserved
#


import abc
import logging
import sys

import flask
import rollbar
import rollbar.contrib.flask


__version__ = '0.1.0'


logger = logging.getLogger('Flask-Rollbar')


class RollbarRequestMixin(object):
    """
    https://github.com/rollbar/rollbar-flask-example
    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def rollbar_person(self):
        return None


class Rollbar(object):
    """
    Flask-Rollbar

    https://rollbar.com/docs/notifier/pyrollbar/
    https://github.com/rollbar/rollbar-flask-example

    https://github.com/angstwad/flask-rollbar
    https://github.com/psykzz/flask-rollbar
    """

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app, **kwargs):

        enabled = app.config.get('ROLLBAR_ENABLED', not app.debug)
        if not enabled:
            return

        access_token = app.config.get('ROLLBAR_SERVER_TOKEN')
        if access_token is None:
            logger.warning('ROLLBAR_SERVER_TOKEN not set')
            return

        environment = app.config.get('ROLLBAR_ENVIRONMENT')
        if environment is None:
            logger.warning('ROLLBAR_ENVIRONMENT not set')

        def _data_hook(request, data):
            # https://rollbar.com/docs/api/items_post
            data['platform'] = sys.platform
            data['language'] = 'python'
            data['framework'] = 'flask'
            if request:
                data['context'] = str(request.url_rule)

        rollbar.BASE_DATA_HOOK = _data_hook

        rollbar.init(
            access_token,
            environment,
            root=app.root_path,
            allow_logging_basic_config=False,
            **kwargs
        )

        flask.got_request_exception.connect(rollbar.contrib.flask.report_exception, app)

    def __getattr__(self, name):
        return getattr(rollbar, name)


# EOF
