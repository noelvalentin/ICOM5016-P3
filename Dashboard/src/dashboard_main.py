from flask import Flask
from flask_cors import CORS
from src.dashboard_handler import DashboardHandler

app = Flask(__name__)
CORS(app)

#-------------- Dashboard --------------#


@app.route('/PhotoMessagingApp/dashboard/trending', methods=['GET'])
def getTrendingTopics():
    return DashboardHandler().getTrendingTopics()


@app.route('/PhotoMessagingApp/dashboard/posts', methods=['GET'])
def getNumberOfPostsPerDay():
    return DashboardHandler().getPostsCount()


@app.route('/PhotoMessagingApp/dashboard/replies', methods=['GET'])
def getNumberOfRepliesPerDay():
    return DashboardHandler().repliesPerDay()


@app.route('/PhotoMessagingApp/dashboard/likes', methods=['GET'])
def getNumberOfLikesPerDay():
    return DashboardHandler().likesPerDay()


@app.route('/PhotoMessagingApp/dashboard/dislikes', methods=['GET'])
def getNumberOfDislikesPerDay():
    return DashboardHandler().dislikesPerDay()


if __name__ == '__main__':
    app.run()
