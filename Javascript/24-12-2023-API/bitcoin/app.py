from flask import Flask, session, render_template
import requests

app = Flask(__name__)

app.secret_key="asdlkhjasdf,jkhdfkjhsdfkjhd"

COINDESK_URL="https://api.coindesk.com/v1/bpi/currentprice.json"

CAT_URL="https://catfact.ninja/fact"

@app.route('/')
def home():
     rate = requests.get(COINDESK_URL).json()
     fact=requests.get(CAT_URL).json()
     try:
          rates=session["rates"]
          rates.append(rate)
          session["rates"]=rates
     except:
          rates=[rate]
          session["rates"]=rates
     return render_template("rates.html", rates=rates, fact=fact)

if __name__ == '__main__':
    app.run(debug=True)