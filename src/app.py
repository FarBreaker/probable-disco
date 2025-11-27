from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details')

def details():
    return jsonify({
        'time': datetime.datetime.now().strftime("%d-%m-%Y"),   
        'hostname': socket.gethostname(),
        'ci-mode': 'enabled',
    }),200

@app.route('/api/v1/healthz')

def health():
    return jsonify({
        'status':'up'
    }),200

@app.route('/api/v1/products')

def products():
    return jsonify({
        'products': [
            {
                'id': '1',
                'name': 'Sample Product 1',
                'description': 'This is a sample product description',
                'price': 29.99,
                'category': 'Electronics',
                'inStock': True,
                'imageUrl': 'https://example.com/image1.jpg'
            },
            {
                'id': '2',
                'name': 'Sample Product 2',
                'description': 'Another sample product',
                'price': 49.99,
                'category': 'Clothing',
                'inStock': False,
                'imageUrl': 'https://example.com/image2.jpg'
            },
            {
                'id': '3',
                'name': 'Sample Product 3',
                'description': 'Yet another product',
                'price': 19.99,
                'category': 'Books',
                'inStock': True
            }
        ],
        'total': 3,
        'page': 1
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)