from flask import jsonify
from dao.replies import RepliesDAO

class ReplyHandler:
    def build_reply_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['posterid'] = row[1]
        result['originalpostid'] = row[2]
        result['date'] = row[3]
        result['message'] = row[4]
        result['photo'] = row[5]
        return result


    def build_like_dict(self,row):
        result={}
        result['lid'] = row[0]
        result['likerid'] = row[1]
        result['originalpostid'] = row[2]
        result['date'] = row[3]
        return result


    def build_dislike_dict(self,row):
        result = {}
        result['dlid'] = row[0]
        result['dislikerid'] = row[1]
        result['originalpostid'] = row[2]
        result['date'] = row[3]
        return result


    #def build_reply_attributes(self, rid, posterid, originalpostid, date, message, photo):
        #result = {}
        #result['rid'] = rid
        #result['posterid'] = posterid
        #result['originalpostid'] = originalpostid
        #result['date'] = date
        #result['message'] = message
        #result['photo'] = photo
        #return result

    #def build_like_attributes(self, lid, likerid, originalpostid, date)
        # result = {}
        # result['lid'] = lid
        # result['likerid'] = likerid
        # result['originalpostid'] = originalpostid
        # result['date'] = date
        # return result

    #def build_dislike_attributes(self, dlid, dislikerid, originalpostid, date)
        # result = {}
        # result['dlid'] = dlid
        # result['dislikerid'] = dislikerid
        # result['originalpostid'] = originalpostid
        # result['date'] = date
        # return result

    def getAllReplies(self):
        dao = RepliesDAO()
        replies_list = dao.getAllReplies()
        result_list = []
        for row in replies_list:
            result = self.build_reply_dict(row)
            result_list.append(result)
        return jsonify(Messsages=result_list)

    def getAllRepliesByUser(self, posterid):
        dao = RepliesDAO()
        replies_list = dao.getAllRepliesByUser(posterid)
        result_list = []
        for row in replies_list:
            result = self.build_reply_dict(row)
            result_list.append(result)
        return jsonify(Replies = result_list)

    def getReplyById(self, rid):
        dao = RepliesDAO()
        row = dao.getReplyById(rid)
        if not row:
            return jsonify(Error = "Message Not Found"), 404
        else:
            reply = self.build_reply_dict(row)
            return jsonify(Reply = reply)

    def getRepliesByDate(self, date):
        dao = RepliesDAO()
        replies_list = dao.getRepliesByDate(date)
        result_list = []
        for row in replies_list:
            result = self.build_reply_dict(row)
            result_list.append(result)
        return jsonify(Replies=result_list)


    def getRepliesOfPost(self, originalpostid):
        dao = RepliesDAO()
        replies_list = dao.getRepliesOfPost(originalpostid)
        result_list = []
        for row in replies_list:
            result = self.build_reply_dict(row)
            result_list.append(result)
        return jsonify(Replies=result_list)


    def getRepliesPerDayByUser(self, posterid, date):
        dao = RepliesDAO()
        replies_list = dao.getRepliesPerDayByUser(posterid, date)
        result_list = []
        for row in replies_list:
            result = self.build_reply_dict(row)
            result_list.append(result)
        return jsonify(Replies=result_list)


    def createReply(self):
        dao = RepliesDAO()
        result = dao.createReply()
        return result

    def deleteReply(self, rid):
        dao = RepliesDAO()
        if not dao.getReplyById(rid):
            return jsonify(Error = "Reply Not Found"), 404
        result = dao.deleteReply(rid)
        return result

    def updateReply(self, rid):
        dao = RepliesDAO()
        if not dao.getReplyById(rid):
            return jsonify(Error = "Reply Not Found"), 404
        result = dao.updateReply(rid)
        return result

    #LIKE FUNCTIONS HERE:

    def getLikesOfPost(self, originalpostid):
        dao = RepliesDAO()
        likes_list = dao.getLikesOfPost(originalpostid)
        result_list = []
        for row in likes_list:
            result = self.build_like_dict(row)
            result_list.append(result)
        return jsonify(Likes=result_list)

    def getLikeById(self,lid):
        dao = RepliesDAO()
        row = dao.getLikeById(lid)
        if not row:
            return jsonify(Error="Like Not Found"), 404
        else:
            like= self.build_like_dict(row)
            return jsonify(Like=like)

    def getLikesPerDay(self, date):
        dao = RepliesDAO()
        likes_list = dao.getLikesPerDay(date)
        result_list = []
        for row in likes_list:
            result = self.build_like_dict(row)
            result_list.append(result)
        return jsonify(Likes=result_list)

    def createLike(self):
        dao = RepliesDAO()
        result = dao.createLike()
        return result

    def updateLike(self, lid):
        dao = RepliesDAO()
        if not dao.getLikeById(lid):
            return jsonify(Error="Like Not Found"), 404
        result = dao.updateLike(lid)
        return result

    def deleteLike(self, lid):
        dao = RepliesDAO()
        if not dao.getLikeById(lid):
            return jsonify(Error="Like Not Found"), 404
        result = dao.deleteLike(lid)
        return result

    #DISLIKE FUNCTIONS

    def getDislikesOfPost(self, originalpostid):
        dao = RepliesDAO()
        dislikes_list = dao.getDislikesOfPost(originalpostid)
        result_list = []
        for row in dislikes_list:
            result = self.build_dislike_dict(row)
            result_list.append(result)
        return jsonify(Dislikes=result_list)

    def getDislikeById(self, dlid):
        dao = RepliesDAO()
        row = dao.getDislikeById(dlid)
        if not row:
            return jsonify(Error="Dislike Not Found"), 404
        else:
            dislike = self.build_dislike_dict(row)
            return jsonify(Dislike=dislike)

    def getDislikesPerDay(self, date):
        dao = RepliesDAO()
        dislikes_list = dao.getDislikesPerDay(date)
        result_list = []
        for row in dislikes_list:
            result = self.build_dislike_dict(row)
            result_list.append(result)
        return jsonify(Dislikes=result_list)

    def createDislike(self):
        dao = RepliesDAO()
        result = dao.createDislike()
        return result

    def updateDislike(self, dlid):
        dao = RepliesDAO()
        if not dao.getDislikeById(dlid):
            return jsonify(Error="Dislike Not Found"), 404
        result = dao.updateDislike(dlid)
        return result

    def deleteDislike(self, dlid):
        dao = RepliesDAO()
        if not dao.getDislikeById(dlid):
            return jsonify(Error="Dislike Not Found"), 404
        result = dao.deleteDislike(dlid)
        return result