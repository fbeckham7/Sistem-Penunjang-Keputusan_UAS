from http import HTTPStatus

from flask import Flask, request
from flask_restful import Resource, Api 

from models import Iphone

app = Flask(__name__)
api = Api(app)        

class Recommendation(Resource):

    def post(self):
        criteria = request.get_json()
        kriteria_valid = ['brand','ram','battery','processor','kamera','harga']
        iphone = Iphone()

        if not criteria:
            return 'criteria is empty', HTTPStatus.BAD_REQUEST.value

        if not all([v in kriteria_valid for v in criteria]):
            return 'criteria is not found', HTTPStatus.NOT_FOUND.value

        recommendations = iphone.get_recs(criteria)
        results = [{"nama": iphone.iphone_data_dict[rec[0]], "skor": rec[1]} for rec in recommendations.items()]

        return {
            'alternatif': results
        }, HTTPStatus.OK.value


api.add_resource(Recommendation, '/recommendation')

if __name__ == '__main__':
    app.run(port='5005', debug=True)
