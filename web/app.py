from flask import Flask,jsonify,request
from flask_restful import Api,Resource

app=Flask(__name__)
api=Api(app)

def checkPostedData(postedData,fname):
    if(fname=="add" or fname=="sub" or fname=="mul"):
        if "x" not in postedData or "y" not in postedData:
            return 301 

        else:
            return 200
    elif(fname == "div"):
            if "x" not in postedData or "y" not in postedData:
                return 301
            elif int(postedData["y"]) == 0:
                return 302
            else:
                return 200
    

class Add(Resource):
    def post(self):
        #get data
        postedData=request.get_json()

        #verify validity of data
        status_code = checkPostedData(postedData,"add")
        if(status_code!=200):
            retJson = {
                "Message":"An error happened",
                "Status_code":status_code

            }
            return jsonify(retJson)

        

        x=postedData["x"]
        y=postedData["y"]
        x=int(x)
        y=int(y)
        ret=x+y

        #return data and status code
        retMap={
            "Message":ret,
            "Status Code":200
            }
        return jsonify(retMap)


    

class Subtract(Resource):
    def post(self):
        postedData=request.get_json()
        status_code=checkPostedData(postedData,"sub")
        if(status_code!=200):
            retJson = {
                "Message":"An error happened in ",
                "Status_code":status_code

            }
            return jsonify(retJson)

        x=postedData["x"]
        y=postedData["y"]
        ret=x-y
        retMap={
            "Message":ret,
            "status_code":200

        }
        return jsonify(retMap)

class Multiply(Resource):
    def post(self):
        postedData=request.get_json()
        status_code=checkPostedData(postedData,"mul")
        if(status_code!=200):
            retJson = {
                "Message":"An error happened",
                "Status_code":status_code

            }
            return jsonify(retJson)

        x=postedData["x"]
        y=postedData["y"]
        ret=x*y
        retMap={
            "Message":ret,
            "status_code":200

        }
        return jsonify(retMap)


class Divide(Resource):
    def post(self):
        postedData=request.get_json()
        status_code=checkPostedData(postedData,"div")
        if(status_code!=200):
            retJson = {
                "Message":"An error happened",
                "Status_code":status_code

            }
            return jsonify(retJson)

        x=postedData["x"]
        y=postedData["y"]
        ret=float(x/y)
        retMap={
            "Message":ret,
            "status_code":200

        }
        return jsonify(retMap)

api.add_resource(Add,"/add")
api.add_resource(Subtract,"/sub")
api.add_resource(Multiply,"/mul")
api.add_resource(Divide,"/div")

@app.route('/')
def hello_world():
    return "HELLLO WORLD"

@app.route('/himan')    
def himan():
    return "HI MAN !"


@app.route('/bye')
def bye():
    return "BYE"

@app.route('/add_two_nums',methods=["POST","GET"])
def adddd():
    dataDict=request.get_json()
    if "y" not in dataDict:
        return "ERROR",305
    x=dataDict["x"]
    y=dataDict["y"]

    z=x+y
    retJson={
        "z":z
    }
    return jsonify(retJson),200

if __name__=="__main__":
    app.run(host='0.0.0.0')
