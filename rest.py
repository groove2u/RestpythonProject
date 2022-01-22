from flask import Flask, request, jsonify

from api import restCallAPI
import datetime

app = Flask(__name__)
api = restCallAPI()


@app.route('/hello_world') #test api
def hello_world():
    return 'Hello, World!'

@app.route('/echo_call/<param>') #get echo api
def get_echo_call(param):
    return jsonify({"param": param})

@app.route('/echo_call', methods=['POST']) #post echo api
def post_echo_call():
    param = request.get_json()
    return jsonify(param)

#분석서버가 분석하고 있는 cctv목록을 리턴한다.
@app.route('/analysis/cctvs', methods=['GET']) #post echo api
def list():
    cctvsList = []
    for value in api.list :
        cctvId = value['cctvId']
        cctvsList.append(cctvId)

    returnParam = dict();

    returnParam['cctvs'] = cctvsList
    returnParam['status'] = 200
    returnParam['message'] = "OK"

    returnParam = getDefaultParam(returnParam)



    return jsonify(returnParam)


#CCTV 추가
@app.route('/analysis/cctvs/<param>', methods=['POST'])
def insert(param):

    data = api.getCCTVInfo(param)

    cctvsList = []

    isExist = 0
    curId = data['cctvId']
    for value in api.list :
        cctvId = value['cctvId']

        cctvsList.append(cctvId)

        if curId != cctvId :
            print("cctv info add cctvId="+str(cctvId))
            isExist = 0
        else :
            print("cctv info is exist cctvId=" + str(cctvId))
            isExist = 1

    if isExist == 0 :
        api.list.append(data)
        cctvsList.append(curId)


    returnParam = dict();

    returnParam['cctvs'] = cctvsList
    if isExist == 0 :
        returnParam['status'] = 200
        returnParam['message'] = "OK"
    else :
        returnParam['status'] = 201
        returnParam['message'] = "exist already"

    returnParam = getDefaultParam(returnParam)

    return jsonify(returnParam)

    #return jsonify({"param": data})

#CCTV 변경
@app.route('/analysis/cctvs/<param>', methods=['PUT'])
def modify(param):

    data = api.getCCTVInfo(param)

    cctvsList = []

    isExist = 0
    curId = data['cctvId']
    for value in api.list :
        cctvId = value['cctvId']

        cctvsList.append(cctvId)

        if curId != cctvId :
            print("cctv info add cctvId="+str(cctvId))
            isExist = 0
        else :
            value = data
            print("cctv info is exist cctvId=" + str(cctvId))
            isExist = 1


    returnParam = dict();

    returnParam['cctvs'] = cctvsList
    if isExist == 1 :
        returnParam['status'] = 200
        returnParam['message'] = "OK"
    else :
        returnParam['status'] = 201
        returnParam['message'] = "cctvId not found"

    returnParam = getDefaultParam(returnParam)

    return jsonify(returnParam)

#CCTV 삭제
@app.route('/analysis/cctvs/<param>', methods=['DELETE'])
def delete(param):

    #list = list()

    data = dict();

    data['mode'] = "delete"
    data['param'] = param

    return jsonify(data)


def getDefaultParam(param) :

    param['path'] = request.full_path
    param['timestamp'] =  datetime.datetime.now()
    return param

if __name__ == "__main__":
    app.run()