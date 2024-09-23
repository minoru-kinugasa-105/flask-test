from flask import Flask, render_template
from flask_assets import Environment, Bundle
import os
import shutil

app = Flask(__name__)
assets = Environment(app)
assets.init_app(app)

# SCSSの設定
scss = Bundle('scss/global.scss', filters='libsass', output='static/css/global.css')
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

def generate_static_files(output_dir='static_output'):
    # 出力ディレクトリを作成
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    # HTMLファイルを生成
    html_files = ['home.html', 'mp3-player.html', 'mp4-player.html']
    for html_file in html_files:
        rendered_html = render_template(html_file)
        with open(os.path.join(output_dir, html_file), 'w') as f:
            f.write(rendered_html)

    # CSSを静的出力ディレクトリにコピー
    shutil.copytree('static', os.path.join(output_dir, 'static'), dirs_exist_ok=True)

if __name__ == '__main__':
    # SCSSをビルド
    with app.app_context():
        assets['scss_all'].build()
        generate_static_files()

    app.run(host='0.0.0.0', port=12341, debug=True)
