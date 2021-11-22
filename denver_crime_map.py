from flask import Flask, render_template
from os.path import join as path_join


app = Flask(__name__)
local_path = "file://" + app.root_path
file_name = "crime_cats_201503"
data_file = path_join("/static", "data", "{}.topojson".format(file_name))
text_file = "/static/write-up.txt"
with open(path_join(app.root_path, "leaflet_token"), "r") as f:
    leaflet_token = f.read().strip()


@app.route("/")
def heatmap_page(name=None):
    return render_template(
        "proof-of-concept.html",
        token=leaflet_token,
        data=data_file,
        info_text=text_file,
        fname=file_name,
    )


if __name__ == "__main__":
    app.run()
