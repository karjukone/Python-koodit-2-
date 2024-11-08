from flask import Flask

app = Flask(__name__)

@app.route('/alkuluku/<int:luku>')
def onkoAlkuluku(luku):
    onAlku = True

    if luku < 2:
        onAlku = False

    for jakaja in range(2, luku):
        if luku % jakaja == 0:
            onAlku = False
            break
    
    vastaus = {
        "Number" : luku,
        "isPrime" : "en tiiä"
    }
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1')