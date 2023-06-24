from marshmallow import Schema, fields


class Movement_schema(Schema):
    id = fields.Integer()
    value = fields.Float()
    description = fields.String()
    date = fields.DateTime()
    category_id = fields.Integer()
    user_id = fields.Integer()
    type = fields.Integer()
