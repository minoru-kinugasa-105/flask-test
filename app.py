from flask import Flask, render_template
from flask_assets import Environment, Bundle
app = Flask(__name__)
assets = Environment(app)
assets.init_app(app)

scss = Bundle('scss/global.scss', filters='libsass', output='css/global.css')
assets.register('scss_all', scss)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/mp3-player')
def mp3_player():
    return render_template('mp3-player.html')

@app.route('/mp4-player')
def mp4_player():
    return render_template('mp4-player.html')

if __name__ == '__main__':
    with app.app_context():
        assets['scss_all'].build()
    app.run(host='0.0.0.0', port=12341, debug=True)