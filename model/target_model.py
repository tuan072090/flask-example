from marshmallow import Schema, fields, pprint, validate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TargetModel(db.Model):
    __tablename__ = 'target'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80), nullable=False)
    typeId = db.Column(db.String(120), nullable=False)
    amountCommission = db.Column(db.Float,nullable=False)
    createdAt = db.Column(db.Integer, nullable=False)

    def __init__(self, type, typeId, amountCommission, createdAt):
        self.type = type
        self.typeId = typeId
        self.amountCommission = amountCommission
        self.createdAt = createdAt


class TargetSchema(Schema):
    id = fields.Int()
    type = fields.Str(validate=validate.OneOf(["deal", "place", "zalo"]),required=True)
    typeId = fields.Str(required=True)
    amountCommission = fields.Float(required=True)
    createdAt = fields.Int()