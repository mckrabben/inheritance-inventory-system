from flask import Flask
from controllers.inventory_routes import inventory_routes

app = Flask(__name__)

# Register blueprints
app.register_blueprint(inventory_routes)

if __name__ == "__main__":
    app.run(debug=True)
