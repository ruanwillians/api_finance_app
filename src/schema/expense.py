from marshmallow import Schema, fields


class ExpenseSchema(Schema):
    id = fields.Integer()
    value = fields.Float()
    description = fields.String()
    date = fields.Integer()
    category_id = fields.Integer()
    user_id = fields.Integer()
