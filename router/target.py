from flask_restful import Resource
from flask import request, g
from model.target_model import TargetSchema,TargetModel
from marshmallow import ValidationError
from middleware.Authen import auth


class Target(Resource):

    @auth.login_required
    def get(self, **kwargs):

        print("g.current_user", g.current_user)

        target_id = kwargs.get("target_id")

        if not target_id:
            print("ko co id, return list")

            offset = request.args.get("offset")
            print("offset", offset)

            return {'message': 'show list target'}
        else:
            print("target_id", target_id)
            return {'message': 'show detail target ' + str(target_id)}

    def post(self):
        try:
            json_data = request.json

            target_schema = TargetSchema()
            result = target_schema.load(json_data)


            import calendar
            import time
            ts = calendar.timegm(time.gmtime())

            new_target = TargetModel(
                type=json_data["type"],
                typeId=json_data["typeId"],
                amountCommission=json_data["amountCommission"],
                createdAt=ts
            )

            from model.target_model import db
            db.session.add(new_target)
            db.session.commit()

            result = target_schema.dump(new_target)
            print("result...", result)

            return {'message': 'create success', "data": result}, 201

        except ValidationError as err:
            return {'message': err.messages}, 400

        except Exception as e:
            return {'message': e.args}, 500

    def put(self):
        return {'hello': 'world PUT'}
