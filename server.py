from flask import Flask, request, abort
import json, sys, random,time
import hotel, minimarket, spbu

app = Flask("Pertaland")

@app.route('/pertaland', methods=['GET'])
def pertaland():
    time.sleep(3)
    data = {}
    data['hotel'] = hotel.hotel(random.randint(0, 5), random.randint(0, 5), random.randint(113, 27879), random.randint(0, 7))
    data['minimarket'] = minimarket.minimarket(random.randint(0, 3), random.randint(0, 3), random.randint(5464, 19826), random.randint(3092, 21098), random.randint(0, 3))
    data['spbu'] = spbu.spbu(random.randint(954, 19865), random.randint(0, 2), random.randint(0, 5), random.randint(57, 998))

    return data

app.run(host='0.0.0.0', port=7777)
