from marshmallow import Schema, fields


class UserSchema(Schema):
    userNo = fields.String(required=True)
    authCode = fields.String(required=True)
    name = fields.String(required=True)
    surname = fields.String(required=True)
    birthDate = fields.String(required=True)
    phoneNumber = fields.String(required=True)
    email = fields.Email(required=True)
    selectedCard = fields.String(required=True)
    allCards = fields.List(fields.String(), required=True)
    balance = fields.Float(required=True)