from flask import Flask, render_template, request, jsonify
from utils.strength_check import check_strength, check_pwned
from utils.validate import is_blank, check_regex

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    password = request.form.get('password', '').strip()

    # 1. Check if blank or only spaces
    if is_blank(password):
        return jsonify({
            'ok': False,
            'msg': "You have not entered any password!",
            'strength': 0
        })
    
    # 2. Check regex errors, can show as suggestions if you want
    regex_issues = check_regex(password)
    # if regex_issues:
    #     return jsonify({
    #         'ok': False,
    #         'msg': ' '.join(regex_issues),
    #         'strength': 0
    #     })

    # 3. If regex passed, check strength, entropy, check for leaks
    strength, suggestions, entropy, strength_level = check_strength(password)
    pwned_count = check_pwned(password)

    return jsonify({
        'ok': True,
        'strength': strength,
        'strength_level': strength_level,
        'suggestions': suggestions,
        'entropy': entropy,
        'pwned': pwned_count
    })

if __name__ == "__main__":
    app.run(debug=True)
