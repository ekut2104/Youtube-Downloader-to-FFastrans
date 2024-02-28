import requests
# import logging
from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

# Налаштування логування
# logging.basicConfig(filename='app.log', level=logging.INFO)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process_form', methods=['POST'])
def process_form():
    url = request.form.get('url')
    name = request.form.get('name')

    # print(url, name)
    result = your_function(url, name)

    # Логування результату
    # logging.info(f"Job ID: {result}")

    return render_template('index.html', result=result)


def your_function(link, name):
    # URL, на який ви хочете відправити POST-запит
    uriFFastrns = "http://127.0.0.1:65445/api/v2/jobs/20240227-1127-3050-5846-5bb41ee0b7d4"

    # Дані, які ви хочете відправити
    data = {
        "wf_id": "20240212-1845-1856-29f8-a1f679481c54",
        "inputfile": link,
        "start_proc": "",
        "priority": "1",
        # "variables": [
        #     {
        #         "name": 's_video_name',
        #         "data": "name"
        #     },
        #     {
        #         "name": 's_channel_name',
        #         "data": "channel",
        #     },
        # ]
    }

    # Відправлення POST-запиту з JSON-даними
    response = requests.post(uriFFastrns, json=data)

    # Перевірка на успішний відгук
    if response.status_code == 200:
        print("POST request was successful")
        return response.json()
    if response.status_code == 202:
        print("Your request in process", response.status_code, response.text)
        return response.json()
    else:
        print("Error during POST request:", response.status_code, response.text)
        return response.json()


if __name__ == '__main__':
    app.run(debug=True)
