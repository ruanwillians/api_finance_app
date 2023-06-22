from database import create_app, db
from src.controller.expense import expense_bp
from src.controller.user import user_bp
from src.controller.login import login_bp
from src.controller.categories import category_bp
from flask_jwt_extended import JWTManager
from flask_cors import CORS


app = create_app()
CORS(app)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = "senha"
app.register_blueprint(expense_bp)
app.register_blueprint(user_bp)
app.register_blueprint(login_bp)
app.register_blueprint(category_bp)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
