from marshmallow import Schema, fields

class BuilderSchema(Schema):
    id = fields.Int(required=True)
    deck_name = fields.Str()
    