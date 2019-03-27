from flask import Flask
from flask import request
from flask import json as fjson
import json

app = Flask(__name__)

@app.route('/scraper', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_runScraper():
    if request.method == 'POST':
        terms = ""

        if request.headers['Content-Type'] == 'application/json':
            # expects json like so: 
            #   { 
            #       "new-terms" : ["laser", "orion"]
            #   }
            # make sure the content-type is application/json
            terms_raw = fjson.dumps(request.get_json())
            terms_dict = json.loads(terms_raw)
            
            terms = [e for e in terms_dict['new-terms']]
        
        print(terms)

        return "Added Terms: " + ', '.join(terms) + "\n"
    else:
        return "Use POST to add new terms thanks! :D\n"
    

if __name__ == '__main__':
    app.run()
