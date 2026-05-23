from flask import Flask, render_template, request, jsonify
import uuid
from triage_tree import build_triage_tree, TreeNode

app = Flask(__name__)

triage_tree = build_triage_tree()
user_sessions = {}

@app.route('/')
def index():
    session_id = str(uuid.uuid4())
    user_sessions[session_id] = {'current_node_id': id(triage_tree)}
    return render_template('index.html', session_id=session_id)

@app.route('/ask')
def ask_question():
    session_id = request.args.get('session_id')
    answer = request.args.get('answer')

    if session_id not in user_sessions:
        return jsonify({'status': 'error', 'message': 'Invalid session'}), 400

    current_node_id = user_sessions[session_id]['current_node_id']
    current_node = find_node_by_id(triage_tree, current_node_id)

    if not current_node:
        return jsonify({'status': 'error', 'message': 'Node not found for session'}), 500

    if answer:
        if answer == 'yes':
            next_node = current_node.right
        elif answer == 'no':
            next_node = current_node.left
        else:
            return jsonify({'status': 'error', 'message': 'Invalid answer'}), 400

        if next_node is None:
            return jsonify({'status': 'error', 'message': 'Reached end of undefined path'}), 500
        
        user_sessions[session_id]['current_node_id'] = id(next_node)
        current_node = next_node

    if current_node.value:
        return jsonify({'status': 'result', 'result': current_node.value})
    else:
        return jsonify({'status': 'question', 'question': current_node.feature})

@app.route('/reset_session')
def reset_session():
    session_id = str(uuid.uuid4())
    user_sessions[session_id] = {'current_node_id': id(triage_tree)}
    return jsonify({'status': 'success', 'new_session_id': session_id})

def find_node_by_id(root, target_id):
    if root is None:
        return None
    if id(root) == target_id:
        return root
    left_result = find_node_by_id(root.left, target_id)
    if left_result:
        return left_result
    return find_node_by_id(root.right, target_id)

if __name__ == '__main__':
    app.run(debug=True)
