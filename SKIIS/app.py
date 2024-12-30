from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests

# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/SKILLOVER"
mongo = PyMongo(app)

@app.route('/api/posts', methods=['GET'])
def get_posts():
    """
    Fetch posts from the FLOW collection. Supports optional filtering by category and search query.
    """
    try:
        # ig we can get the query param
        category = request.args.get('category')  
        search_query = request.args.get('search')  
        
        # Build the MongoDB query
        query = {}
        if category:
            query["category"] = {"$regex": category, "$options": "i"}  
        if search_query:
            query["$or"] = [
                {"title": {"$regex": search_query, "$options": "i"}},  
                {"description": {"$regex": search_query, "$options": "i"}}  
            ]

        
        posts = mongo.db.FLOW.find(query)  

        # Convert the MongoDB cursor to a list of dictionaries
        data = [
            {
                "id": str(post["_id"]),
                "title": post.get("title", ""),
                "description": post.get("description", ""),
                "category": post.get("category", "")
            }
            for post in posts
        ]

        return jsonify(data), 200  
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500  

@app.route('/api/debug', methods=['GET'])
def debug_mongo():
    """
    Debug route to verify MongoDB connection and list databases.
    Access restricted to debug mode.
    """
    if not app.debug:
        return jsonify({"success": False, "message": "Access denied"}), 403
    try:
        db_names = mongo.cx.list_database_names()  
        return jsonify({"success": True, "databases": db_names}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
