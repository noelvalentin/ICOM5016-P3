import psycopg2


class MessagesDAO:

    def __init__(self):
        connection_url = "dbname=jeanmerced user=postgres password=password"
        self.conn = psycopg2._connect(connection_url)


#--------------- Phase 2 ---------------#

    def getAllMessages(self, oid):
        cursor = self.conn.cursor()
        query = "select mid, image, text, date, uid, first_name from Message natural inner join Users where oid=%s;"
        cursor.execute(query, (oid,))
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
        query = "select  date,count(date) from Message group by date order by count desc limit 5"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def likesPerDay(self):
        cursor = self.conn.cursor()
        query = "select date, count(*) from Likes group by date order by date limit 5"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def dislikesPerDay(self):
        cursor = self.conn.cursor()
        query = "select date, count(*) from Dislikes group by date order by date limit 5"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def repliesPerDay(self):
        cursor = self.conn.cursor()
        query = "select date, count(*) from Message where oid is not null group by date order by date limit 5"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTrendingTopics(self):
        cursor = self.conn.cursor()
        query = "select  tag ,count(*) as C from Hashtag natural inner join Tagged group by tag order by C desc limit 5"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def likeMessage(self, uid, mid):
        cursor = self.conn.cursor()
        query = "insert into Likes (uid, mid, date) values (%s, %s, current_date);"
        cursor.execute(query, (uid, mid))
        self.conn.commit()
        return mid

    def dislikeMessage(self, uid, mid):
        cursor = self.conn.cursor()
        query = "insert into Dislikes (uid, mid, date) values (%s, %s, current_date);"
        cursor.execute(query, (uid, mid))
        self.conn.commit()
        return mid

    def createHashtag(self, tag):
        cursor = self.conn.cursor()
        query = "insert into Hashtag (tag) values (%s);"
        query2 = "insert into Tagged (hid,mid) values ((select max(hid) from Hashtag),(select  max(mid) from Message));"
        cursor.execute(query, (tag,))
        cursor.execute(query2)
        self.conn.commit()
        return 0
#----------------- END -----------------#

