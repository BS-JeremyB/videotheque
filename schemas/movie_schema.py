
from marshmallow import Schema, fields
from schemas.director_schema import DirectorSchema

class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    director_id = fields.Int(required=True)
    director = fields.Nested(DirectorSchema, dump_only=True)  # Relation avec le réalisateur

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)
