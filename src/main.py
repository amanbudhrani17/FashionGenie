

'''This is the main Flask Server File where we are calling our various AI Models and '''
import os
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import requests
import urllib.request
import model
from pyngrok import ngrok
from PIL import Image

import products


app = Flask("myapp")
api = Api(app)
# CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/recommended_products', methods=['POST'])
def process_string():
    data = request.get_json()
    input_string = data.get('input_string')
    print(input_string)
    urllib.request.urlretrieve(input_string, "download.jpg")
    path = "/home/btech/nityanand.mathur/aman/grid/backend/download"
    try:
        n_path = path+".jpg"
        image = Image.open(n_path)
        print('/n/n/n')
        print(n_path)
        print('/n/n/n')
        return model.getSimilar(n_path)
    except Exception:
       
        urllib.request.urlretrieve(input_string, "download.png")
        try:
            n_path = path+".png"
            image = Image.open(n_path)
            print('/n/n/n')
            print(n_path)
            print('/n/n/n')
            return model.getSimilar(n_path)
        except Exception:
            urllib.request.urlretrieve(input_string, "download.jpeg")
            n_path = path+".jpeg"
            image = Image.open(n_path)
            print('/n/n/n')
            print(n_path)
            print('/n/n/n')
            return model.getSimilar(n_path)


    return []


@app.route('/get_products/<category>', methods=['GET'])
def get_products(category):
    return products.getProducts(category)

# @app.route('/generate_image', methods=['POST'])
# def generated_images():
#     data = request.get_json()
#     input_string = data.get('string')
#     l = [
#         'https://drive.google.com/file/d/1ywPRhD3_LuiqheqF0rcQtiETLHyd6bNY/view?usp=sharing',
#         'https://drive.google.com/file/d/1lknXDWi_DANbCGgXJdlsnN9gQUinrZi5/view?usp=sharing',
#         'https://drive.google.com/file/d/1CiOhDROwjcaiqx0wHKFGLiJrNOwe6cVL/view?usp=sharing',
#         'https://drive.google.com/file/d/1CiOhDROwjcaiqx0wHKFGLiJrNOwe6cVL/view?usp=sharing',
#         'https://drive.google.com/file/d/1CiOhDROwjcaiqx0wHKFGLiJrNOwe6cVL/view?usp=sharing'
#     ]
#     return l

def get_location_from_ip(ip):
    print(ip)
    response = requests.get(f"http://ipinfo.io/{ip}/json")
    data = response.json()
    return data.get('city'), data.get('region'), data.get('country')

@app.route('/get_location', methods=['GET'])
def get_location():
    client_ip = request.remote_addr
    city, region, country = get_location_from_ip(client_ip)
    return f"City: {city}, Region: {region}, Country: {country}"


def download_image(url, save_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print("Image downloaded successfully!")
        else:
            print("Failed to download image.")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")


def delete_image(file_path):
    try:
        os.remove(file_path)
        print("Image deleted successfully!")
    except OSError as e:
        print(f"Error deleting image: {e}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    public_url = ngrok.connect(addr="http://127.0.0.1:5000")
    print("Ngrok URL:", public_url)
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
