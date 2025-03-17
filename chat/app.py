from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# دالة للرد على الرسائل
def chatbot_response(message):
    # يمكنك إضافة منطق الرد هنا
    if "مرحبا" in message:
        return "مرحبًا! كيف يمكنني مساعدتك؟"
    elif "كيف حالك" in message:
        return "أنا بخير، شكرًا لسؤالك!"
    else:
        return "لم أفهم ما تقصد. يمكنك إعادة صياغة السؤال؟"

# مسار للصفحة الرئيسية
@app.route('/')
def home():
    return render_template('index.html')

# مسار لاستقبال الرسائل وإرسال الردود
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    response = chatbot_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)