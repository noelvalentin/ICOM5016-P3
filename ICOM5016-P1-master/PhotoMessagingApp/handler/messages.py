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

    def build_message_reaction_dict(self,row):
        result ={}
        result['number_of_reactions'] = row[0]
        return result

#--------------- Phase 2 ---------------#

    def getAllMessages(self):
        dao = MessagesDAO()
        messages_list = dao.getAllMessages()
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
        row = dao.getPostsCount()
        if not row:
            return jsonify(Error = "Message Not Found"), 404
        else:
            likes= self.build_message_reaction_dict(row)
            return jsonify(Number = likes)

    def getTrendingTopics(self):
        dao = MessagesDAO()
        result = dao.getTrendingTopics()
        return result

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
