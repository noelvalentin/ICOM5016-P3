from flask import jsonify
from dao.messages import MessagesDAO

class MessageHandler:

    def build_message_dict(self, row):
        result = {}
        result['mid'] = row[0]
        result['image'] = row[1]
        result['text'] = row[2]
        result['date'] = row[3]
        result['uid'] = row[4]
        result['first_name'] = row[5]
        #result['oid'] = row[6]
        return result

    def build_message_reaction_dict(self, row):
        result = {}
        result['number_of_reactions'] = row[0]
        return result

    def build_hashtag_dict(self,row):
        result ={}
        result['tag'] = row[0]
        result['count']=row[1]
        return result

    def build_stats_dict(self,row):
        result ={}
        result['date'] = row[0]
        result['count']=row[1]
        return result

#--------------- Phase 2 ---------------#

    def getAllMessages(self,oid):
        dao = MessagesDAO()
        messages_list = dao.getAllMessages(oid)
        result_list = []
        for row in messages_list:
            result = self.build_message_dict(row)
            result_list.append(result)
        return jsonify(Messages = result_list)

    def getMessagesByGroupId(self, gid):
        dao = MessagesDAO()
        messages_list = dao.getMessagesByGroupId(gid)
        result_list = []
        for row in messages_list:
            result = self.build_message_dict(row)
            result_list.append(result)
        return jsonify(Messages = result_list)

    def getLikesByMessageId(self, mid):
        dao = MessagesDAO()
        row = dao.getLikesByMessageId(mid)
        if not row:
            return jsonify(Error = "Message Not Found"), 404
        else:
            likes= self.build_message_reaction_dict(row)
            return jsonify(Likes = likes)

    def getDislikesByMessageId(self, mid):
        dao = MessagesDAO()
        row = dao.getDislikesByMessageId(mid)
        if not row:
            return jsonify(Error = "Message Not Found"), 404
        else:
            dislikes = self.build_message_reaction_dict(row)
            return jsonify(Dislikes = dislikes)

    def getPostsCount(self):
        dao = MessagesDAO()
        trending = dao.getPostsCount()
        result_list = []
        for row in trending:
            result = self.build_stats_dict(row)
            result_list.append(result)
        return jsonify(Messages=result_list)

    def likesPerDay(self):
        dao = MessagesDAO()
        trending = dao.likesPerDay()
        result_list = []
        for row in trending:
            result = self.build_stats_dict(row)
            result_list.append(result)
        return jsonify(Messages=result_list)

    def dislikesPerDay(self):
        dao = MessagesDAO()
        trending = dao.dislikesPerDay()
        result_list = []
        for row in trending:
            result = self.build_stats_dict(row)
            result_list.append(result)
        return jsonify(Messages=result_list)

    def repliesPerDay(self):
        dao = MessagesDAO()
        trending = dao.repliesPerDay()
        result_list = []
        for row in trending:
            result = self.build_stats_dict(row)
            result_list.append(result)
        return jsonify(Messages=result_list)

    def getTrendingTopics(self):
        dao = MessagesDAO()
        trending = dao.getTrendingTopics()
        result_list = []
        for row in trending:
            result = self.build_hashtag_dict(row)
            result_list.append(result)
        return jsonify(Messages=result_list)


    def likeMessage(self, form):
        print("form: ", form)
        if len(form) < 0:
            return jsonify(Error="Malformed post request"), 400
        else:
            uid = form['uid']
            mid = form['mid']

            if uid and mid:
                dao =MessagesDAO()
                dao.likeMessage(uid,mid)
                return jsonify(User="OK"), 200
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400


    def dislikeMessage(self, form):
        print("form: ", form)
        if len(form) < 0:
            return jsonify(Error="Malformed post request"), 400
        else:
            uid = form['uid']
            mid = form['mid']

            if uid and mid:
                dao = MessagesDAO()
                dao.dislikeMessage(uid, mid)
                return jsonify(User="OK"), 200
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400


    def createHashtag(self, form):
        print("form: ", form)
        if len(form) < 0:
            return jsonify(Error="Malformed post request"), 400
        else:
            tag = form['tag'];


            if tag :
                dao = MessagesDAO()
                dao.createHashtag(tag)
                return jsonify(User="OK"), 200
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def numReplies(self, oid):
        dao = MessagesDAO()
        row = dao.numReplies(oid)
        if not row:
            return jsonify(OK="Message Not Found")
        else:
            dislikes = self.build_message_reaction_dict(row)
            return jsonify(Dislikes=dislikes)

#----------------- END -----------------#

'''
    def getAllMessagesByUser(self, posterid):
        dao = MessagesDAO()
        messages_list = dao.getAllMessagesByUser(posterid)
        result_list = []
        for row in messages_list:
            result = self.build_message_dict(row)
            result_list.append(result)
        return jsonify(Messsages = result_list)

    def getMessageById(self, mid):
        dao = MessagesDAO()
        row = dao.getMessageById(mid)
        if not row:
            return jsonify(Error = "Message Not Found"), 404
        else:
            message = self.build_message_dict(row)
            return jsonify(Message = message)

    def getMessagesByDate(self, date):
        dao = MessagesDAO()
        messages_list = dao.getMessagesByDate(date)
        result_list = []
        for row in messages_list:
            result = self.build_message_dict(row)
            result_list.append(result)
        return jsonify(Messsages = result_list)


    def getTrendingTopics(self):
        dao = MessagesDAO()
        result = dao.getTrendingTopics()
        return result

    def getMessagesPerDayByUser(self, posterid, date):
        dao = MessagesDAO()
        messages_list = dao.getMessagesPerDayByUser(posterid, date)
        result_list = []
        for row in messages_list:
            result = self.build_message_dict(row)
            result_list.append(result)
        return jsonify(Messsages = result_list)

    def getActiveUsers(self):
        dao = MessagesDAO()
        result = dao.getActiveUsers()
        return result
'''

'''
    def createMessage(self):
        dao = MessagesDAO()
        result = dao.createMessage()
        return result

    def deleteMessage(self, mid):
        dao = MessagesDAO()
        if not dao.getMessageById(mid):
            return jsonify(Error = "Message Not Found"), 404
        result = dao.deleteMessage(mid)
        return result

    def updateMessage(self, mid):
        dao = MessagesDAO()
        if not dao.getMessageById(mid):
            return jsonify(Error = "Message Not Found"), 404
        result = dao.updateMessage(mid)
        return result
'''
