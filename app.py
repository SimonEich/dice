from flask import Flask, request, render_template
import random

app = Flask(__name__)

# Einsteigsseite, wird angezeigt mit 'http://127.0.0.1:5000
@app.route("/", methods=["get", "post"])
def index():
#Create two random numbers from 1 to 6.
    w1 = random.randint(1,6)
    w2 = random.randint(1,6)
 
    print(w1)
    print(w2)
    
    print(request.form)
    #If wurfel1 is pushed there gonna be showed the following text. One dice will be thrown.
    if "wurfel1" in request.form:
        print("wurfel1")
        text="Der Würfel Zeigt eine "+ str(w1)
        return render_template("index.html", text =text)
    #If wurfel2is pushed there gonna be showed the following text. Two dice will be thrown.
    elif "wurfel2" in request.form:
        print("wurfel2")
        text="Die Würfel zeigen eine "+ str(w1)+" und eine "+ str(w2)
        return render_template("index.html", text=text)
    #The App starts with the text "Zuerst Würfeln". This text gonna be changed with the predominate text options.
    else:
        text= "Zuerst Würfeln"
        return render_template("index.html", text =text)
    



if __name__ == "__main__":
    app.run(debug=True)
