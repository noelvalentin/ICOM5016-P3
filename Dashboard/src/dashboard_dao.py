import psycopg2


class DashboardDAO:

    def __init__(self):
        connection_url = "dbname=jeanmerced user=postgres password=password"
        self.conn = psycopg2._connect(connection_url)

#--------------- Phase 3 ---------------#

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
