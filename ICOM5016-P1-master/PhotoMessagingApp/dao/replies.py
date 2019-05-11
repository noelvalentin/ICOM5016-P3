class RepliesDAO:

    def getAllReplies(self):
        result = [[1, 12, 14, "18/dec/2019", "cool reply message", "perfect reaction photo"],
                  [2, 23, 49, "19/may/2048", "great reply", "amazing photo"]]
        return result

    def getAllRepliesByUser(self, posterid):
        vacio = []
        if posterid == 2:
            result = [[1, 2, 14, "18/dec/2019", "cool reply message", "perfect reaction photo"],
                      [2, 2, 49, "19/may/2048", "great reply", "amazing photo"]]
        elif posterid == 30:
            result = [[5, 30, 12, "12/feb/2019", "cool message", "cool photo"],
                      [6, 30, 456, "13/aug/2040", "great message", "great photo"]]
        else:
            return vacio
        return result

    def getReplyById(self, rid):
        vacio = []
        if rid == 2:
            result = [2, 2, 14, "12/feb/2019", "cool message", "cool photo"]
        elif rid == 3:
            result = [3, 3, 12, "12/feb/2019", "cool message", "cool photo"]
        else:
            return vacio
        return result

    def getRepliesByDate(self, date):
        vacio = []
        if date == "14-feb-2019":
            result = [[10, 20, 140, "14/feb/2019", "cool message", "cool photo"],
                      [20, 20, 490, "14/feb/2019", "great message", "great photo"]]
        elif date == "18-feb-2040":
            result = [[11, 21, 1412, "18/feb/2040", "cool message", "cool photo"],
                      [243, 25, 429, "18/feb/2040", "great message", "great photo"]]
        else:
            return vacio
        return result

    def getRepliesOfPost(self, originalpostid):
        vacio = []
        if originalpostid == 25:
            result = [[10, 20, 25, "14/feb/2019", "cool message", "cool photo"],
                      [20, 20, 25, "14/feb/2019", "great message", "great photo"]]
        elif originalpostid == 190:
            result = [[11, 21, 190, "18/feb/2040", "cool message", "cool photo"],
                      [243, 25, 190, "18/feb/2040", "great message", "great photo"]]
        else:
            return vacio
        return result


    def getRepliesPerDayByUser(self, posterid, date):
        vacio = []
        if posterid == 25 & date == "14-feb-2019":         #Is this the way to do it?
            result = [[10, 20, 25, "14/feb/2019", "cool message", "cool photo"],
                      [20, 20, 25, "14/feb/2019", "great message", "great photo"]]
        elif posterid == 190 & date == "18-feb-2040":
            result = [[11, 21, 190, "18/feb/2040", "cool message", "cool photo"],
                      [243, 25, 190, "18/feb/2040", "great message", "great photo"]]
        else:
            return vacio
        return result


    def deleteReply(self, rid):
        result = "REPLY MURDERED"
        return result

    def updateReply(self,rid):
        result = "Reply with ID %d : information has been updated" % (rid)
        return result

    def createReply(self):
        result = "Your reply has been created, woohoo"
        return result

    #LIKE FUNCTIONS HERE

    def getLikesOfPost(self,originalpostid):
        vacio = []
        if originalpostid == 215:
            result = [[10, 20, 215, "17/nov/2034"],
                      [20, 20, 215, "24/dec/2056"]]
        elif originalpostid == 190:
            result = [[11, 21, 190, "23/aug/2060"],
                      [243, 25, 190, "20/jan/2047"]]
        else:
            return vacio
        return result

    def getLikeById(self, lid):
        vacio = []
        if lid == 258:
            result = [258, 2, 14, "12/feb/2019"]
        elif lid == 3:
            result = [358, 3, 12, "12/feb/2019"]
        else:
            return vacio
        return result

    def getLikesPerDay(self, date):
        vacio = []
        if date == "14-feb-2019":
            result = [[10, 20, 140, "14/feb/2019"],
                      [20, 20, 490, "14/feb/2019"]]
        elif date == "18-feb-2040":
            result = [[11, 21, 1412, "18/feb/2040"],
                      [243, 25, 429, "18/feb/2040"]]
        else:
            return vacio
        return result

    def createLike(self):
        result = "You have liked this post."
        return result

    def updateLike(self, lid):
        result = "Like has been updated."
        return result

    def deleteLike(self,lid):
        result = "LIKE HAS BEEN UNDONE. UNLIKED."
        return result

    #DISLIKE FUNCTIONS

    def getDislikesOfPost(self, originalpostid):
        vacio = []
        if originalpostid == 215:
            result = [[10, 20, 215, "17/nov/2034"],
                      [20, 20, 215, "24/dec/2056"]]
        elif originalpostid == 190:
            result = [[11, 21, 190, "23/aug/2060"],
                      [243, 25, 190, "20/jan/2047"]]
        else:
            return vacio
        return result

    def getDislikeById(self, dlid):
        vacio = []
        if dlid == 258:
            result = [258, 2, 14, "12/feb/2019"]
        elif dlid == 3:
            result = [358, 3, 12, "12/feb/2019"]
        else:
            return vacio
        return result

    def getDislikesPerDay(self, date):
        vacio = []
        if date == "14-feb-2019":
            result = [[10, 20, 140, "14/feb/2019"],
                      [20, 20, 490, "14/feb/2019"]]
        elif date == "18-feb-2040":
            result = [[11, 21, 1412, "18/feb/2040"],
                      [243, 25, 429, "18/feb/2040"]]
        else:
            return vacio
        return result

    def createDislike(self):
        result = "You have disliked this post."
        return result

    def updateDislike(self, dlid):
        result = "Dislike has been updated."
        return result

    def deleteDislike(self, dlid):
        result = "DISLIKE HAS BEEN UNDONE. UN-DISLIKED."
        return result