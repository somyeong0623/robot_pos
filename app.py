from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient

# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.Serving_Robot
Order=db.Order
Kitchen=db.Kitchen

def CalNexts_o_id(self) :                 # self에는 Colection이름이 들어가면 됩니다.
    max = int()
    max = 0
    x = self.find().sort("o_id")
    for i in x:
        if i['o_id'] > max:
            max = i['o_id']
    return max + 1


#초기화면 보여주기
@app.route('/')
def home():
    return render_template('index_initial.html')

#메뉴화면 보여주기
@app.route('/pos')
def menu():
    return render_template('index.html')

# 초기화면 연결 확인
@app.route('/initial', methods=['GET'])
def show_initial():
    sample_receive = request.args.get('sample_give')
    print('초기화면 get 완료')
    return jsonify({'msg': '초기 화면 GET 완료!'})

# 초기화면 : 테이블번호, o_s_id받아와서 Order collection에 doc 추가.
@app.route('/initial', methods=['POST'])
def save_table_no():
    i = int()
    i = CalNexts_o_id(Order)
    table_no_receive = request.form['table_no_give']
    table_num=int(table_no_receive)

    # data=request.json
    # table_no_receive=jsonify(data)['table_no_give']
    print(table_num)
    doc={
        'o_id':i,
        'table_no':table_num,
        'menu':""
    }
    Order.insert_one(doc)
    return jsonify({'msg':'테이블번호가 저장되었습니다!!','o_id':i})



# 메뉴화면 연결 확인
@app.route('/menu', methods=['GET'])
def show_menu():
    sample_receive = request.args.get('sample_give')
    print(sample_receive)
    return jsonify({'msg': '메뉴화면 GET 연결 완료!'})

# 주문하기(POST) API
@app.route('/menu', methods=['POST'])
def save_order():
    # db.menu.update(
    #     {"o_s_id": i, "table_no": table_num},
    #     {
    #         "$push": {
    #             "menu": [
    #                 {"id": 3, "name": "짬뽕", "count": 1}
    #             ]
    #         }
    #     })

    return jsonify({'msg': '아ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ 잘 되니??????'})


# doc의 menu원소에 메뉴리스트{"name" "count"} 추가
@app.route('/payment', methods=['POST'])
def menu_payment():

    ##여기 o_id에 save_table_no의 함수에서 받아온 o_id 넣어줘야함...어케하냐..
    o_id:1
    menulist_receive = request.form['menulist_give']
    print(menulist_receive)
    # for i in menulist_receive:
    #     print(i["name"], i["count"])

    # doc={
    #     'menu_name': name_receive,
    #     'menu_count': count_receive
    # }
    #
    # db.menu.update(
    #     {"o_s_id":o_id},
    #     {
    #  "$push":{
    #         "menu":[
    #            {"name":"전주비빔밥","count":1}
    #         ]
    #     }
    # })

    return jsonify({'msg':'주문내역을 결제하러 가자! '})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)