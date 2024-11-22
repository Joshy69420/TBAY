#imports 
from flask import Flask
#run web application instance
app=Flask(__name__)
#tell it where to go
@app.route("/home")
def home():
    return "<h1>Tbay<h1>"
if __name__=='__main__': 
    app.run()  