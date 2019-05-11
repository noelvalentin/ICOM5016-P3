import psycopg2

class MessagesDAO:

    def __init__(self):
        connection_url = "dbname=mydb user=yo host=localhost password=password"
        self.conn = psycopg2._connect(connection_url)

#--------------- Phase 2 ---------------#

    def getAllMessages(self):
        cursor = self.conn.cursor()
        query = "select mid, image, text, date, uid, first_name from Message natural inner join Users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessagesByGroupId(self, gid):
        cursor = self.conn.cursor()
        query = "select mid, image, text, date, uid,first_name from Message natural inner join Users where gid = %s "
        cursor.execute(query, (gid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getLikesByMessageId(self, mid):
        cursor = self.conn.cursor()
        query = "select count(*) from Likes where mid = %s;"
        cursor.execute(query, (mid,))
        result = cursor.fetchone()
        return result

    def getDislikesByMessageId(self, mid):
        cursor = self.conn.cursor()
        query = "select count(*) from Dislikes where mid = %s;"
        cursor.execute(query, (mid,))
        result = cursor.fetchone()
        return result

    def getPostsCount(self):
        cursor = self.conn.cursor()
        query = "select count(*) from Message ;"
        cursor.execute(query,)
        result = cursor.fetchone()
        return result

    def getTrendingTopics(self):
        cursor = self.conn.cursor()
        query = "select tag, count(*) from Hashtag group by tag order by count desc"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

#----------------- END -----------------#

'''
    def getAllMessagesByUser(self, posterid):
        vacio = []
        if posterid == 2:
            result = [[1, 2, 14, "12/feb/2019", "cool message", "cool photo"],
                      [2, 2, 49, "13/aug/2040", "great message", "great photo"]]
        elif posterid == 3:
            result = [[5, 3, 12, "12/feb/2019", "cool message", "cool photo"],
                      [6, 3, 456, "13/aug/2040", "great message", "great photo"]]
        else:
            return vacio
        return result

    def getMessageById(self, mid):
        vacio = []
        if mid == 2:
            result = [2, 2, 14, "12/feb/2019", "cool message", "cool photo"]
        elif mid == 3:
            result = [3, 3, 12, "12/feb/2019", "cool message", "cool photo"]
        else:
            return vacio
        return result

    def getMessagesByDate(self, date):
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

    def getMessagesByGroupChat(self, groupchatid):
        vacio = []
        if groupchatid == 25:
            result = [[10, 20, 25, "14/feb/2019", "cool message", "cool photo"],
                      [20, 20, 25, "14/feb/2019", "great message", "great photo"]]
        elif groupchatid == 190:
            result = [[11, 21, 190, "18/feb/2040", "cool message", "cool photo"],
                      [243, 25, 190, "18/feb/2040", "great message", "great photo"]]
        else:
            return vacio
        return result

    def getTrendingTopics(self):
        result = "The trending topics are calculated here, and they are #Crazy"
        return result

    def getMessagesPerDayByUser(self, posterid, date):
        vacio = []
        if posterid == 25 & date == "14-feb-2019":
            result = [[10, 20, 25, "14/feb/2019", "cool message", "cool photo"],
                      [20, 20, 25, "14/feb/2019", "great message", "great photo"]]
        elif posterid == 190 & date == "18-feb-2040":
            result = [[11, 21, 190, "18/feb/2040", "cool message", "cool photo"],
                      [243, 25, 190, "18/feb/2040", "great message", "great photo"]]
        else:
            return vacio
        return result

    def getActiveUsers(self):
        result = "These are the most Active Users right now, they post many things every day."
        return result
'''

'''

    def deleteMessage(self, mid):
        result = "MESSAGE TERMINATED"
        return result

    def updateMessage(self, mid):
        result = "Message %d information has been updated" % (mid)
        return result

    def createMessage(self):
        result = "Your message has been created, woohoo"
        return result
'''
