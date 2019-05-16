from flask import Flask, request
from src.handler.users import UserHandler
from src.handler.groups import GroupHandler
from src.handler.messages import MessageHandler


# Import Cross-Origin Resource Sharing to enable services on other ports
# on this machine or on other machines to access this app
from flask_cors import CORS

# Activate
app = Flask(__name__)

# Apply CORS to this app
CORS(app)


@app.route('/PhotoMessagingApp', methods=['GET'])
def greeting():
    return 'Hello, this is the Photo Messaging DB App!'

#--------------- Phase 2 ---------------#


@app.route('/PhotoMessagingApp/home', methods=['GET'])
def home():
    return 'Welcome to your homepage!'


@app.route('/PhotoMessagingApp/statistics/nposts', methods=['GET'])
def postsCounter():
    return MessageHandler().getPostsCount()


@app.route('/PhotoMessagingApp/statistics/replies', methods=['GET'])
def repliesPerDay():
    return MessageHandler().repliesPerDay()


@app.route('/PhotoMessagingApp/statistics/likes', methods=['GET'])
def likesPerDay():
    return MessageHandler().likesPerDay()


@app.route('/PhotoMessagingApp/statistics/dislikes', methods=['GET'])
def dislikesPerDay():
    return MessageHandler().dislikesPerDay()
# List of users in the system


@app.route('/PhotoMessagingApp/home/users', methods=['GET'])
def getAllUsers():
    return UserHandler().getAllUsers()


# Information on a given user with ID
@app.route('/PhotoMessagingApp/home/users/<int:uid>', methods=['GET'])
def getUserbyId(uid):
    return UserHandler().getUserById(uid)

# List of users in the contact list of user with ID


@app.route('/PhotoMessagingApp/home/users/<int:uid>/contacts', methods=['GET'])
def getUserContactsById(uid):
    return UserHandler().getUserContactsById(uid)

# List of messages in the system


@app.route('/PhotoMessagingApp/home/messages/replies/<int:oid>', methods=['GET'])
def getAllMessages(oid):
    return MessageHandler().getAllMessages(oid)

# List of chat groups in the system


@app.route('/PhotoMessagingApp/home/groups', methods=['GET'])
def getAllGroups():
    return GroupHandler().getAllGroups()

# Owner of a given chat group with ID


@app.route('/PhotoMessagingApp/home/groups/<int:gid>/owner', methods=['GET'])
def getOwnerByGroupId(gid):
    return UserHandler().getOwnerByGroupId(gid)

# List of users subscribed to a chat group with ID


@app.route('/PhotoMessagingApp/home/groups/<int:gid>/members', methods=['GET'])
def getMembersByGroupId(gid):
    return UserHandler().getMembersByGroupId(gid)

# List of messages posted to a chat group with ID


@app.route('/PhotoMessagingApp/home/groups/<int:gid>/messages', methods=['GET'])
def getMessagesByGroupId(gid):
    return MessageHandler().getMessagesByGroupId(gid)

# List of users who liked a message with ID


@app.route('/PhotoMessagingApp/home/messages/<int:gid>/likers', methods=['GET'])
def getLikersByMessageId(gid):
    return UserHandler().getLikersByMessageId(gid)

# List of users who disliked a message with ID


@app.route('/PhotoMessagingApp/home/messages/<int:gid>/dislikers', methods=['GET'])
def getDislikersByMessageId(gid):
    return UserHandler().getDislikersByMessageId(gid)

# Number of likes of message with ID


@app.route('/PhotoMessagingApp/home/messages/<int:mid>/likes', methods=['GET'])
def getLikesByMessageId(mid):
    return MessageHandler().getLikesByMessageId(mid)

# Number of dislikes of message with ID


@app.route('/PhotoMessagingApp/home/messages/<int:mid>/dislikes', methods=['GET'])
def getDislikesByMessageId(mid):
    return MessageHandler().getDislikesByMessageId(mid)


@app.route('/PhotoMessagingApp/home/trendingHash', methods=['GET'])
def trending():
    return MessageHandler().getTrendingTopics()


#----------------- END -----------------#


#######Create methods####
# Creating a new User
@app.route('/PhotoMessagingApp/signup', methods=['POST'])
def createUser():
    # cambie a request.json pq el form no estaba bregando
    # parece q estaba poseido por satanas ...
    # DEBUG a ver q trae el json q manda el cliente con la nueva pieza
    print("REQUEST: ", request.json)
    return UserHandler().createUser(request.json)


@app.route('/PhotoMessagingApp/group/create', methods=['POST'])
def createGroup():

    print("REQUEST: ", request.json)
    return GroupHandler().createGroup(request.json)

# Get user method by firstName


@app.route('/PhotoMessagingApp/home/users/firstName/<string:fName>', methods=['GET'])
def getUserByFirstName(fName):
    return UserHandler().getUserByFirstName(fName)


@app.route('/PhotoMessagingApp/home/users/email/<string:email>', methods=['GET'])
def getUserByEmail(email):
    return UserHandler().getUserByEmail(email)


@app.route('/PhotoMessagingApp/login/<string:email>/<string:password>', methods=['GET'])
def login(email, password):
    return UserHandler().login(email, password)


@app.route('/PhotoMessagingApp/addByEmail', methods=['POST'])
def addUserByEmail():
    return UserHandler().addUserByEmail(request.json)


@app.route('/PhotoMessagingApp/addByPhone', methods=['POST'])
def addUserByPhone():
    return UserHandler().addUserByPhone(request.json)


@app.route('/PhotoMessagingApp/deleteContact/<int:uid>/<int:cid>', methods=['DELETE'])
def deleteContact(uid, cid):
    return UserHandler().deleteContact(uid, cid)


@app.route('/PhotoMessagingApp/postToGroup', methods=['POST'])
def postToGroup():
    return GroupHandler().postToGroup(request.json)


@app.route('/PhotoMessagingApp/home/mygroups/<int:uid>', methods=['GET'])
def getMyGroups(uid):
    return GroupHandler().getMyGroups(uid)


@app.route('/PhotoMessagingApp/deleteMember/<int:gid>/<int:uid>', methods=['DELETE'])
def deleteMember(gid, uid):
    return GroupHandler().deleteMember(gid, uid)


@app.route('/PhotoMessagingApp/deleteGroup/<int:gid>', methods=['DELETE'])
def deleteGroup(gid):
    return GroupHandler().deleteGroup(gid)


@app.route('/PhotoMessagingApp/addMember', methods=['POST'])
def addMember():
    return GroupHandler().addMember(request.json)


@app.route('/PhotoMessagingApp/likeMessage', methods=['POST'])
def likeMessage():
    return MessageHandler().likeMessage(request.json)


@app.route('/PhotoMessagingApp/dislikeMessage', methods=['POST'])
def dislikeMessage():
    return MessageHandler().dislikeMessage(request.json)


@app.route('/PhotoMessagingApp/createHashtag', methods=['POST'])
def createHashtag():
    return MessageHandler().createHashtag(request.json)


if __name__ == '__main__':
    app.run()
