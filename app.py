from flask import Flask, request, jsonify, render_template
from gradio_client import Client

app = Flask(__name__)

# 创建 Hugging Face Client 实例
client = Client("Richard3306/blip-image-api-chatbot")


@app.route('/')  # 路由1
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])  # 路由2
def chat():
    data = request.json
    user_message = data.get("message", "")

    # 调用 Hugging Face 的 API
    result = client.predict(
        message=user_message,
        system_message="You are a friendly Chatbot.",
        max_tokens=512,
        temperature=0.7,
        top_p=0.95,
        api_name="/chat"
    )
    print(f"User Message: {user_message}")  # 调试打印
    print(f"Bot Response: {result}")  # 调试打印
    return jsonify({"response": result})


if __name__ == '__main__':
    app.run(debug=True)