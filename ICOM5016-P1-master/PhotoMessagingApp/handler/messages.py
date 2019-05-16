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

    def build_hashtag_dict(self, row):
        result = {}
        result['tag'] = row[0]
        result['count'] = row[1]
        return result

    def build_stats_dict(self, row):
        result = {}
        result['date'] = row[0]
        result['count'] = row[1]
        return result

#--------------- Phase 2 ---------------#

    def getAllMessages(self, oid):
        dao = MessagesDAO()
        messages_list = dao.getAllMessages(oid)
        result_list = []
        for row in messages_list:
            result = self.build_message_dict(row)
            result_list.append(result)
        return jsonify(Messages=result_list)

    def getMessagesByGroupId(self, gid):
        dao = MessagesDAO()
        messages_list = dao.getMessagesByGroupId(gid)
        result_list = []
        for row in messages_list:
            result = self.build_message_dict(row)
            result_list.append(result)
        return jsonify(Messages=result_list)

    def getLikesByMessageId(self, mid):
        dao = MessagesDAO()
        row = dao.getLikesByMessageId(mid)
        if not row:
            return jsonify(Error="Message Not Found"), 404
        else:
            likes = self.build_message_reaction_dict(row)
            return jsonify(Likes=likes)

    def getDislikesByMessageId(self, mid):
        dao = MessagesDAO()
        row = dao.getDislikesByMessageId(mid)
        if not row:
            return jsonify(Error="Message Not Found"), 404
        else:
            dislikes = self.build_message_reaction_dict(row)
            return jsonify(Dislikes=dislikes)

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
                dao = MessagesDAO()
                dao.likeMessage(uid, mid)
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
            tag = form['tag']

            if tag:
                dao = MessagesDAO()
                dao.createHashtag(tag)
                return jsonify(User="OK"), 200
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400
#----------------- END -----------------#
