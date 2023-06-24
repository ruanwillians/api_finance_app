from marshmallow import Schema, fields


class User_schema(Schema):
    id = fields.Integer()
    balance = fields.Float()
    name = fields.String()
    email = fields.String()
    available = fields.Float()


class Meta:
    exclude = ('password')
