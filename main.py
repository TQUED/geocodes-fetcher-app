"""
    Flask APP main module
"""
import datetime
import logging
import os

import pandas as pd
from flask import Flask, jsonify, request, send_file

import googlemaps

APP = Flask(__name__)
APP.config.from_object("config.Config")
LOG = logging.getLogger(__name__)
GMAPS_KEY = googlemaps.Client(key=APP.config["API_KEY"])


@APP.route("/")
@APP.route("/health")
def index():
    """
        health check endpoint
    """
    os.system("rm -f data/*")  # removing junks from working directory
    return jsonify({"status": "UP"})


@APP.route("/upload", methods=["POST"])
def upload_file():
    """
        endopoint to fetch the excel from user and
        return result excel with address cordinates
    """
    if "file" in request.files:
        try:
            upload_file_obj = request.files["file"]
            df_main = pd.read_excel(upload_file_obj, header=None)
            df_main.columns = ["Address"]
            df_main["Latitude"] = None
            df_main["Longitude"] = None
        except ValueError:  # empty excel file error handle
            return jsonify({"status": "Empty attachment,please check the excel!!! "})
        except Exception as err_obj:  # unexpected file format file error handle
            return jsonify({"status": f"{err_obj.__repr__()}"})

        for i in range(0, len(df_main), 1):
            geocode_result = GMAPS_KEY.geocode(df_main.iat[i, 0])
            try:
                lat = geocode_result[0]["geometry"]["location"]["lat"]
                lon = geocode_result[0]["geometry"]["location"]["lng"]
                df_main.iat[i, df_main.columns.get_loc("Latitude")] = lat
                df_main.iat[i, df_main.columns.get_loc("Longitude")] = lon
            except Exception:
                # set latitude and longitude as None on exception
                df_main.iat[i, df_main.columns.get_loc("Latitude")] = None
                df_main.iat[i, df_main.columns.get_loc("Longitude")] = None

        LOG.info("calculated dataframe is :- \n %s", df_main)
        output_filename = (
            f"data/my_file_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.xlsx"
        )
        df_main.to_excel(output_filename)
        return send_file(
            output_filename,
            attachment_filename=output_filename.split("/")[1],
            as_attachment=True,
        )

    # returns error when "file" param is not found
    return jsonify({"status": "URL parameter missing!!"})


if __name__ == "__main__":
    APP.run()
