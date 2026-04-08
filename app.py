from flask import Flask, render_template, request
import pickle 

app = Flask(__name__)

vector = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('phishing.pkl', 'rb'))


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        print(url)
        predict = model.predict(vector.transform([url]))
        print(predict)
        return render_template("index.html", predict = predict)
        

        
    else:
        return render_template("index.html")



if __name__== "__main__":
    app.run(debug=True) 
