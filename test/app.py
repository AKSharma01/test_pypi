from flask.views import MethodView

class my(MethodView):
    def get(self):
        return jsonify({
            'data' : 'test'
        })
