import urllib.request, json
from flask import Flask, render_template, request              # import flask framework
app = Flask(__name__)             # create an app instance
@app.route("/<name>")              # route with URL variable /<name>
def hello_name(name):              # call method hello_name
    return "Hello "+ name          # which returns "hello + name  
@app.route("/")                
def hello():                    
    return render_template("index.html", datum=dict) 
@app.route("/about")
def about():
    name = request.args.get('name') if request.args.get('name') else "Hello World!" 
    return render_template("about.html", aboutName=name)   
    # We need to add the URL we will be using to fetch information from.
# Sometimes this means also sending some data like a key, but not for this one
url = "https://xkcd.com/info.0.json"
response = urllib.request.urlopen(url)
# Once we have the response we need to extract the data we want.
data = response.read()
dict = json.loads(data)
if __name__ == "__main__":        # when running python app.py
    app.run(debug=True)           #change app.run() to the following