from flask import Flask, jsonify

ns = __import__("22_naver_shop")

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


@app.route("/get-price/<p_name>", methods=["POST", "GET"])
def get_price(p_name):
    result = ns.naver_price(p_name)

    return jsonify(result)

@app.route('/get-image-detect')
def get_image_detect():
    # 이미지 딥러닝모델 함수 실행
    return jsonify({'고양이'})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5001", debug=True)  # 127.0.0.1:5000

