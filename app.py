from flask import Flask, request, render_template
import random

app = Flask(__name__)

# Einsteigsseite, wird angezeigt mit 'http://127.0.0.1:5000
@app.route("/", methods=["get", "post"])
def index():
    w1 = random.randint(1,6)
    w2 = random.randint(1,6)
    print(w1)
    print(w2)
    
    print(request.form)
    if "wurfel1" in request.form:
        print("wurfel1")
        # Die Variable option wird in options.html verwendet
        text="Der Würfel Zeigt eine "+ str(w1)
        return render_template("index.html", text =text)
    elif "wurfel2" in request.form:
        print("wurfel2")
        # Die Variable option wird in options.html verwendet
        text="Die Würfel zeigen eine "+ str(w1)+" und eine "+ str(w2)
        return render_template("index.html", text=text)
    else:
        text= "Zuerst Würfeln"
        return render_template("index.html", text =text)
    



if __name__ == "__main__":
    app.run(debug=True)
