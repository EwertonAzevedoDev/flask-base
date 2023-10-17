from website import mongo, bcrypt  # Importe as bibliotecas apropriadas

class User():
    def __init__(self, user_id, username, password, active=True):
        self.id = user_id
        self.username = username
        self.password = password
        self.active = active

    @staticmethod
    def get(user_id):
        # Consulte o MongoDB para obter um usuário pelo ID
        user_data = mongo.db.Users.find_one({"_id": user_id})
        if user_data:
            return User(
                user_id=user_data["_id"],
                username=user_data["username"],
                password=user_data["password"],
                active=user_data.get("active", True)
            )

    @staticmethod
    def get_by_username(username):
        # Consulte o MongoDB para obter um usuário pelo nome de usuário
        user_data = mongo.db.Users.find_one({"username": username})
        if user_data:
            return User(
                user_id=user_data["_id"],
                username=user_data["username"],
                password=user_data["password"],
                active=user_data.get("active", True)
            )

    
    def is_active(self):
        return self.active

    
    def is_authenticated(self):
        return True

    
    def is_anonymous(self):
        return False

    def check_password(self, password):
        # Use o Bcrypt para verificar a senha
        return bcrypt.check_password_hash(self.password, password)
