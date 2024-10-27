
from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)             # id ne sera présent que dans les réponses
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(load_only=True)       # Le mot de passe est requis en entrée mais non affiché en sortie

user_schema = UserSchema()
