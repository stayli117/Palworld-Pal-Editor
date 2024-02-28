import os
from pathlib import Path
import sys
import threading
import webbrowser
from flask import Flask, send_from_directory
from flaskwebgui import FlaskUI


from palworld_pal_editor.config import Config

from palworld_pal_editor.api import *

if getattr(sys, 'frozen', False):
    base_path = Path(sys._MEIPASS)
else:
    base_path = Path(__file__).parent

app = Flask(__name__, static_folder=base_path / "webui", static_url_path='/')
app.register_blueprint(player_blueprint, url_prefix='/api/player')
app.register_blueprint(pal_blueprint, url_prefix='/api/pal')
app.register_blueprint(save_blueprint, url_prefix='/api/save')

# Serve Web App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(f"{app.static_folder}/{path}"):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

def main():
    if Config.gui:
        # FlaskUI(app=app, server="flask").run()
        threading.Timer(1.25, lambda: webbrowser.open(f"http://127.0.0.1:{Config.port}") ).start()
    from waitress import serve
    # serve(app, host='0.0.0.0', port=8080)
    app.run(use_reloader=True, port=Config.port, threaded=True)