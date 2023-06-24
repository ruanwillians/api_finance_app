from marshmallow import Schema, fields


class Category_schema(Schema):
    id = fields.Integer()
    name = fields.String()
    description = fields.String()
    user_id = fields.Integer()
