from flask import abort, jsonify, url_for, request
from flask.ext.classy import FlaskView, route
from jinja2 import TemplateNotFound

from catalog.api.lookup import get_action

class APIView(FlaskView):

    def index(self):
        return self.version(1)

    @route('/<version>')
    def version(self, version=1):
        if version > 3:
            abort(404)
        return jsonify(version=version)

    @route('/action')
    @route('/<version>/action')
    def action(self, version=3):
        return jsonify(version=3)

    @route('/action/<func>', endpoint='action_api')
    @route('/<version>/action/<func>', endpoint='action_api')
    def action(self, func, version=3):

        action_fn = get_action(func)
        if not action_fn:
            err = self._error_message("Action not found", "Missing API call")
            resp = self._fail(func, err)
            return jsonify(resp)

        data = self._get_parameters()

        try:
            result = action_fn(data)
            resp = self._success(func)
            resp['result'] = result
        except Exception, e:
            err =  self._error_message(e.messsage, "Unexpected error")
            resp = self._fail(func, err)

        return jsonify(resp)

    def _get_parameters(self):
        if request.method == "GET":
            return request.args.copy()
        elif request.method == "POST":
            pass

    def _success_fail(self, success, action):
        return {
            "success": success,
            "help": self._help_url(action),
        }

    def _success(self, action):
        return self._success_fail(True, action)

    def _fail(self, action, error):
        resp = self._success_fail(False, action)
        del resp['help']
        resp['error'] = error
        return resp

    def _help_url(self, action):
        return url_for("action_api", version=3, func="help_show", _external=True) + "?name={}".format(action)

    def _error_message(self, msg, type):
        return {"message": msg, "__type": type}
