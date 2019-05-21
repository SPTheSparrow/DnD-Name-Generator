
from bottle import Bottle
from bottle import run, debug, route, static_file, template, request
import random

@route('/')
def home():
    return static_file('index.html', root='static/')

@route('/generate')
def generateRoute():
    race = request.query["race"]
    return template('<h1>{{name}}!</h1>',name=generate(race))

names = {
   "human" : {
   	"first": ["Jon", "Theon", "Christopher", "Peter", "Tony", "Robin", "Maria", "Mary", "Lucy", "Karen", "Michael", "James", "Robert", "John"],
        "second" [" "]
   	"third": ["Smith", "Johnson", "William", "Jones", "Riverdale", "Moore", "Willson", "Miller", "Morales", "Parker", "Coleman", "Bennedect", "Price", "Reed"] 
   	}
   	 "elf" : {
   	"first" : ["A", "Be", "De", "El", "Fa", "Jo", "Ki", "La", "Ma", "Na", "O", "Pa", "Si", "Ta", "Va], 
   	"second" : ["bar", "ched", "dell", "far", "gran", "hal", "jen", "kel", "lim", "mor", "net", "penn", "quil", "quil", "rond", "sark", "shen", "tur", "vash", "yor", "zen"]
   	"third" :["a", "ac", "al", "am", "an", "ar", "ea", "el", "er", "ess", "ett", "ic", "id", "il", "in", "is", "or", "us"] 
   	} 
	} 
	
def generate(race) :
    name = random.choice(names[race]['first']) + random.choice(names[race]['second']) + random.choice(names[race]['third']) 
    return name
    	
app = Bottle()
app.route('/', method='GET')(home)
app.route('/generate', method='GET')(generateRoute)

run(app, host='localhost', port=8080)
