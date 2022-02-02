from __main__ import app

@app.route('/test', methods=['GET'])
def test():
    return 'get it works!'

@app.route('/test', methods=['POST'])
def post_test():
    return 'post it works!'

@app.route('/test', methods=['PUT'])
def put_test():
    return 'put it works!'