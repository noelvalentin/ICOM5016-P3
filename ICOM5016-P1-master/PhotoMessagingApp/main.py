from flask import Flask, jsonify, request
from handler.users import UserHandler
from handler.groups import GroupHandler
from handler.messages import MessageHandler

# Import Cross-Origin Resource Sharing to enable services on other ports on this machine or on other machines to access this app
from flask_cors import CORS, cross_origin

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
#Creating a new User
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

#Get user method by firstName

@app.route('/PhotoMessagingApp/home/users/firstName/<string:fName>', methods=['GET'])
def getUserByFirstName(fName):
     return UserHandler().getUserByFirstName(fName)

@app.route('/PhotoMessagingApp/home/users/email/<string:email>', methods=['GET'])
def getUserByEmail(email):
            return UserHandler().getUserByEmail(email)

@app.route('/PhotoMessagingApp/login/<string:email>/<string:password>', methods=['GET'])
def login(email,password):
     return UserHandler().login(email,password)

@app.route('/PhotoMessagingApp/addByEmail', methods=['POST'])
def addUserByEmail():
     return UserHandler().addUserByEmail(request.json)

@app.route('/PhotoMessagingApp/addByPhone', methods=['POST'])
def addUserByPhone():
     return UserHandler().addUserByPhone(request.json)


@app.route('/PhotoMessagingApp/deleteContact/<int:uid>/<int:cid>', methods=['DELETE'])
def deleteContact(uid,cid):
     return UserHandler().deleteContact(uid,cid)

@app.route('/PhotoMessagingApp/postToGroup', methods=['POST'])
def postToGroup():
     return GroupHandler().postToGroup(request.json)

@app.route('/PhotoMessagingApp/home/mygroups/<int:uid>', methods=['GET'])
def getMyGroups(uid):
            return GroupHandler().getMyGroups(uid)

@app.route('/PhotoMessagingApp/deleteMember/<int:gid>/<int:uid>', methods=['DELETE'])
def deleteMember(gid,uid):
            return GroupHandler().deleteMember(gid,uid)



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





@app.route('/PhotoMessagingApp/numReplies/<int:oid>', methods=['GET'])
def numReplies(oid):
    return MessageHandler().numReplies(oid)

'''
#############
#           #
#   USERS   #
#           #
#############

@app.route('/PhotoMessagingApp/signup', methods=['POST'])
def signup():
        return UserHandler().createUser()

@app.route('/PhotoMessagingApp/login', methods=['POST'])
def login():
        return UserHandler().userLogin()





@app.route('/PhotoMessagingApp/users', methods=['GET'])
def getAllUsers():
        return UserHandler().getAllUsers()


@app.route('/PhotoMessagingApp/users/<int:uid>', methods=['GET','DELETE','PUT'])
def getUserbyId(uid):
    if request.method == 'GET':
     return UserHandler().getUserById(uid)
    elif request.method=='DELETE':
     return UserHandler().deleteUser(uid)
    elif request.method=='PUT' :
     return UserHandler().updateUser(uid)
    else:
        return "Nothing"


@app.route('/PhotoMessagingApp/users/<int:id>/contacts', methods=['GET'])
def getAllUsersContacts(id):

        return UserHandler().getUserContactsById(id)


@app.route('/PhotoMessagingApp/users/firstName/<string:fName>', methods=['GET'])
def getUserByFirstName(fName):
     return UserHandler().getUserByFirstName(fName)


@app.route('/PhotoMessagingApp/users/lastName/<string:lName>', methods=['GET'])
def getUserByLastName(lName):
     return UserHandler().getUserByLastName(lName)

@app.route('/PhotoMessagingApp/users/phone/<int:phone>', methods=['GET'])
def getUserByPhone(phone):
     return UserHandler().getUserByPhone(phone)


@app.route('/PhotoMessagingApp/users/email/<string:email>', methods=['GET'])
def getUserByEmail(email):
            return UserHandler().getUserByEmail(email)



#############
#           #
#   GROUPS  #
#           #
#############





@app.route('/PhotoMessagingApp/groups', methods=['GET'])
def getAllGroups():
        return GroupHandler().getAllGroups()




@app.route('/PhotoMessagingApp/groups/<int:id>',methods=['GET','DELETE','PUT'])
def getGroupByID(id):
    if request.method== 'GET':
        return GroupHandler().getGroupById(id)
    elif request.method=='DELETE':
        return GroupHandler().deleteGroup(id)
    elif request.method=='PUT':
        return GroupHandler().updateGroup(id)
    else:
        return 200

@app.route('/PhotoMessagingApp/groups/<string:gname>', methods=['GET'])
def getGroupByGroupName(gname):
        return GroupHandler().getGroupByGroupName(gname)



@app.route('/PhotoMessagingApp/groups/owner/<int:id>', methods=['GET'])
def getAllGroupsByOwnerID(id):
        return GroupHandler().getAllGroupsByOwnerID(id)


@app.route('/PhotoMessagingApp/groups/<int:id>/members', methods=['GET'])
def getMembersByGroupId(id):
        return UserHandler().getMembersByGroupId(id)

@app.route('/PhotoMessagingApp/groups/<int:id>/owner', methods=['GET'])
def getOwnerByGroupId(id):
        return UserHandler().getOwnerByGroupId(id)





#############
#           #
#  MESSAGES #
#           #
#############
@app.route('/PhotoMessagingApp/messages', methods=['GET'])
def getAllMessages():
        return MessageHandler().getAllMessages()


@app.route('/PhotoMessagingApp/messages/user/<int:id>' , methods=['GET'])
def getAllMessagesByUser(id):
    return MessageHandler().getAllMessagesByUser(id)

@app.route('/PhotoMessagingApp/messages/<int:id>',methods=['GET','DELETE','PUT'])
def getMessageById(id):
    if request.method=='GET':
        return MessageHandler().getMessageById(id)
    elif request.method== 'DELETE':
        return MessageHandler().deleteMessage(id)
    elif request.method=='PUT':
        return MessageHandler().updateMessage(id)

@app.route('/PhotoMessagingApp/messages/<int:id>/likes' , methods=['GET'])
def getLikersByMessageId(id):
    return UserHandler().getLikersByMessageId(id)

@app.route('/PhotoMessagingApp/messages/<int:id>/dislikes' , methods=['GET'])
def getDislikersByMessageId(id):
    return UserHandler().getDislikersByMessageId(id)

@app.route('/PhotoMessagingApp/messages/date/<string:date>' , methods=['GET'])
def getMessagesByDate(date):
    return MessageHandler().getMessagesByDate(date)

@app.route('/PhotoMessagingApp/messages/group/<int:id>', methods=['GET'])
def getMessagesByGroupId(id):
    return MessageHandler().getMessagesByGroupId(id)

@app.route('/PhotoMessagingApp/messages/trending',  methods=['GET'])
def getTrendingTopics():
    return MessageHandler().getTrendingTopics()

@app.route('/PhotoMessagingApp/messages/user/<int:posterid>/<string:date>', methods=['GET'])
def getMessagesPerDayByUser(posterid,date):
    return MessageHandler().getMessagesPerDayByUser(posterid,date)

@app.route('/PhotoMessagingApp/messages/user/activeusers' , methods=['GET'])
def getActiveUsers():
    return MessageHandler().getActiveUsers()


#############
#           #
# REPLIES   #
#           #
#############
@app.route('/PhotoMessagingApp/messages/replies' , methods=['GET'])
def getAllReplies():
    return ReplyHandler().getAllReplies()

@app.route('/PhotoMessagingApp/messages/replies/user/<int:id>' ,  methods=['GET'])
def getAllRepliesByUser(id):
    return ReplyHandler().getAllRepliesByUser(id)

@app.route('/PhotoMessagingApp/messages/replies/<int:rid>',methods=['GET','PUT','DELETE'])
def getReplyById(rid):
    if request.method=='GET':
     return ReplyHandler().getReplyById(rid)
    elif request.method=='DELETE':
        return ReplyHandler().deleteReply(rid)
    elif request.method=='PUT':
        return ReplyHandler().updateReply(rid)

@app.route('/PhotoMessagingApp/messages/replies/date/<string:date>' , methods=['GET'])
def getRepliesByDate(date):
    return ReplyHandler().getRepliesByDate(date)

@app.route('/PhotoMessagingApp/messages/replies/post/<int:pid>' ,  methods=['GET'])
def getRepliesOfPost(pid):
    return ReplyHandler().getRepliesOfPost(pid)


@app.route('/PhotoMessagingApp/messages/replies/<int:uid>/<string:date>', methods=['GET'])
def getRepliesPerDayByUser(uid,date):
    return ReplyHandler().getRepliesPerDayByUser(uid,date)


@app.route('/PhotoMessagingApp/messages/create/replies' , methods=['POST'])
def createReply():
    return ReplyHandler().createReply()

#############
#           #
# LIKES     #
#           #
#############

@app.route('/PhotoMessagingApp/messages/likes/<int:postid>',  methods=['GET'])
def getLikesOfPost(postid):
    return ReplyHandler().getLikesOfPost(postid)

@app.route('/PhotoMessagingApp/messages/post/likes/<int:lid>',methods=['GET','PUT','DELETE'])
def getLikeById(lid):
    if request.method=='GET':
        return ReplyHandler().getLikeById(lid)
    elif request.method=='PUT':
        return ReplyHandler().updateLike(lid)
    elif request.method=='DELETE':
        return ReplyHandler().deleteLike(lid)

@app.route('/PhotoMessagingApp/messages/post/clike',  methods=['POST'])
def createLike():
    return ReplyHandler().createLike()

@app.route('/PhotoMessagingApp/messages/post/likes/<string:date>', methods=['GET'])
def getLikesPerDay(date):
        return ReplyHandler().getLikesPerDay(date)


#############
#           #
# DISLIKES  #
#           #
#############


@app.route('/PhotoMessagingApp/messages/dislikes/<int:postid>', methods=['GET'])
def getDislikesOfPost(postid):
    return ReplyHandler().getDislikesOfPost(postid)

@app.route('/PhotoMessagingApp/messages/post/dislikes/<int:lid>',methods=['GET','PUT','DELETE'])
def getDislikeById(lid):
    if request.method=='GET':
        return ReplyHandler().getDislikeById(lid)
    elif request.method=='PUT':
        return ReplyHandler().updateDislike(lid)
    elif request.method=='DELETE':
        return ReplyHandler().deleteDislike(lid)

@app.route('/PhotoMessagingApp/messages/post/cdislike' ,methods=['POST'])
def createDislike():
    return ReplyHandler().createDislike()

@app.route('/PhotoMessagingApp/messages/post/dislikes/<string:date>',  methods=['GET'])
def getDislikesPerDay(date):
        return ReplyHandler().getDislikesPerDay(date)

'''

if __name__ == '__main__':
    app.run()
