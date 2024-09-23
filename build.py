import os
from app import app, assets

with app.app_context():
    assets['scss_all'].build()
    if not os.path.exists('static_output'):
        os.makedirs('static_output')
    # ここで静的ファイルを生成する処理を追加します
