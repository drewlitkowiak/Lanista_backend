import flask
from flask import request, jsonify
import Backend_Server as backend
from Videos import Videos

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


default_json = {
    "key": "value"
}


@app.route('/api/v1/example', methods=['GET'])
def api_home():
    return jsonify(default_json)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.errorhandler(401)
def authentication_error_html(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 401


@app.route('/api/v1/videos', methods=['GET'])
def videos_request():
    params = request.args

    video_id = params.get('id')

    if not video_id:
        return page_not_found(404)

    connection, cursor = backend.start()
    if connection is None or cursor is None:
        return authentication_error_html(401)

    cursor.execute("SELECT * FROM videos WHERE video_id = %s;", (video_id, ))

    result = cursor.fetchone()
    if result is None:
        return page_not_found(404)

    video = Videos((*result))

    cursor.close()
    connection.close()

    return jsonify(video.serialize())


if __name__ == '__main__':
    app.run()