"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, City, Country
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)

#@api.route('/', methods=['POST', 'GET'])
#def handle_home():

#    response_body = {
#        "message": "Hello! I'm a message that came from the backend"
 #   }

 #   return jsonify(response_body), 200

def get_json(): # esta función es común para varias funciones (así se optimiza el código, mejor que repetir el mismo código en cada una de ellas)
    json = request.get_json()       # con esto cogemos el body que le enviamos para indicar qué país/ciudad es la que estamos creando
    
    if json is None:    # si no lo encuentra, tira este error (con esto ya tenemos la comprobación hecha para todas las funciones que usen este get_json())
        raise APIException("No se ha enviado un JSON o no se ha especificado en el header que se nos ha enviado un JSON") # lanzo una excepción que la aplicación captura y devuelve al usuario
   
    return json     # si lo encuentra, lo devuelve

# Quiero ver el listado de países:
@api.route('/countries', methods=['GET'])
def list_countries():
    countries = Country.query.all() # para listar los paises, primero tengo que cogerlos de la BBDD

    return jsonify(list(map(lambda country: country.serialize(), countries))), 200  # ahora devuelvo esos países que he buscado en la BBDD

# Quiero crear países nuevos:
@api.route('/countries/create', methods=['POST'])
def create_country():
    json = get_json()       # con esto cogemos el body que le enviamos para indicar qué país es (llamando a la función get_json())
    
    name = get_name(json) # cogemos el nombre del país que se ha escrito

    country = Country(name=name) # creamos el país que queremos dar de alta
    country.save()  # llamo a la función "save" (está en los modelos) para guardar el país en la BBDD

    return jsonify(country.serialize()), 200    # lo devuelvo

# Quiero listar sólo las ciudades de un país:
@api.route('/countries/<int:country_id>/cities', methods=['GET'])  
def list_cities_in_country(country_id):     # paso por parámetro el id del país en cuestión
    country = Country.query.get(country_id) # recojo el país

    return jsonify(list(map(lambda city: city.serialize(), country.cities))), 200  # ahora devuelvo las ciudades de ese país que he encontrado en la BBDD

# Quiero crear ciudades nuevas:
@api.route('/countries/<int:country_id>/cities/create', methods=['POST']) # con este endpoint obligo a crear ciudades DENTRO de un país
def create_city_in_country(country_id):
    json = get_json()       # con esto cogemos el body que le enviamos para indicar qué ciudad es (llamando a la función get_json())
       
    name = get_name(json)   

def get_name(json): # json tiene q pasarse por parámetro porque no es un objeto global que esté importado (como el request de la función get_json), sino que es local proveniente de get_json()
    name = json.get("name") # cogemos el nombre del país/ciudad que se ha escrito

    if name is None or name == "":
        raise APIException("El nombre es obligatorio") # lanzo una excepción que la aplicación captura y devuelve al usuario

    return name

# (A CONTINUACIÓN, LO QUE HICIMOS EL PRIMER DÍA)
    @api.route('/login', methods=['POST'])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(email = email).first()
    print(user.password)
    if(user.password != password or user is None):
        return "user not exist", 404
  
    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)


    response_body = {
        "message": "Token: Access Token"
    }

    return jsonify(response_body), 200

@api.route('/register', methods=['POST'])
def register():
    name = request.json.get("name", None)
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    city_id = request.json.get("city_id", None)
    user = User.query.filter_by(email = email).first()
    if(user):
        return "user exist", 400
    new_user = User(name = name, email = email, password = password, city_id = city_id)
    db.session.add(new_user)
    db.session.commit()
   
    #access_token = create_access_token(identity=email)
    #return jsonify(access_token=access_token), "User created successfully", 200


    response_body = {
        "message": "Hello! I'm a message that came from the backend"
    }

    return jsonify(response_body), 200

@api.route('/user', methods=['GET'])
def user_info():
    user = User.query.filter_by(id = User.id).first()

    response_body = {
        "message": "Hello! I'm a message that came from the backend"
    }

    return jsonify(response_body), 200