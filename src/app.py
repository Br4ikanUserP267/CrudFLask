from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import connection.connectionbd as connectionbd 
from product import Product

db = connectionbd.bdConnect()
app = Flask(__name__)

@app.route("/")
def home():
      products = db['products']
      productsRecived = products.find()
      return render_template('index.html',products=productsRecived)

#Method Post
@app.route('/products', methods=['POST'])



def addProduct():
    products = db['products']
    name = request.form['name']
    price = request.form['price']
    description = request.form['description']
    quantity = request.form['quantity']

    if name and price and description and  quantity:
        product = Product(name, price,description, quantity)
        products.insert_one(product.dbcollections())
        response = jsonify({
            'name' : name,
            'price' : price,
            'description' : description,
            'quantity' : quantity
        })
        return redirect(url_for('home'))
    else:
        return notFound()

#Method delete
@app.route('/delete/<string:product_name>')
def delete(product_name):
    products = db['products']
    products.delete_one({'name' : product_name})
    return redirect(url_for('home'))

#Method Put
@app.route('/edit/<string:product_name>', methods=['POST'])
def edit(product_name):
    products = db['products']
    name = request.form['name']
    price = request.form['price']
    description = request.form['description']
    quantity = request.form['quantity']

    if name and price and quantity:
        products.update_one({'name' : product_name},
        {'$set' :
         {'name' : name,
          'price' : price,
          'description':description,
          'quantity' : quantity}})

        response = jsonify({'message' : 'Producto ' + product_name + ' actualizado correctamente'})
        return redirect(url_for('home'))
    else:
        return notFound()

@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == "__main__":
    app.run(debug=True,port=8000)




