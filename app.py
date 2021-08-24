from flask import Flask

import WallpaperManager

app = Flask(__name__)


@app.route('/')
def send_color():
    return WallpaperManager.get_current_wallpapers_color()


if __name__ == '__main__':
    app.run()
