from flask import current_app, Blueprint, render_template, request, jsonify, current_app

api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/embed", methods=["POST"])
def create_instruct_embed():
    try:
        data = request.get_json()
        if "text" not in data:
            return jsonify({"error": 'Missing "text" attribute'}), 400
        instruction = data.get("instruction", "")
        text = data["text"]
        response_data = {"text": text, "instruction": instruction}

        embed = current_app.config["instructor_svc"].generate_embedding(
            instruction, text
        )
        if embed is None:
            return jsonify({"error": "Failed to generate embedding"}), 500
        response_data["embedding"] = embed.tolist()[0]

        return jsonify(response_data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
