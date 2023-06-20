from marshmallow import Schema, fields


class user_schema(Schema):
    id = fields.Integer()
    balance = fields.Float()
    name = fields.String()
    email = fields.String()


class Meta:
    exclude = ('password')
