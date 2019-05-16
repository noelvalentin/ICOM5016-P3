import psycopg2


class GroupsDAO:

    def __init__(self):
        connection_url = "dbname=jeanmerced user=postgres password=password"
        self.conn = psycopg2._connect(connection_url)


#--------------- Phase 2 ---------------#

    def getAllGroups(self):
        cursor = self.conn.cursor()
        query = "select uid,gid,gname,first_name from ChatGroup natural inner join Users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

#----------------- END -----------------#

    def createGroup(self, gname, ownerID):
        cursor = self.conn.cursor()
        query = "insert into ChatGroup(gname, uid) values (%s, %s) returning gid;"
        query2 = "insert into isMember (uid,gid) values( %s,(select gid from chatGroup where gname=%s))"
        cursor.execute(query, (gname, ownerID,))
        cursor.execute(query2, (ownerID, gname))
        #gid = cursor.fetchone()[0]
        self.conn.commit()
        return 0

    def postToGroup(self, image, text, uid, gid, oid):
        cursor = self.conn.cursor()
        query = "insert into Message(image, text, date, uid,gid,oid) values(%s,%s,current_date,%s,%s,%s) returning uid;"
        cursor.execute(query, (image, text, uid, gid, oid))
        result = cursor.fetchone()[0]
        self.conn.commit()
        return result

    def getMyGroups(self, uid):
        cursor = self.conn.cursor()
        query = "select uid,gid,gname,first_name from chatGroup natural inner join ((select   gid  from isMember where uid=%s)) as tabla natural inner join Users;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def deleteMember(self, gid, uid):
        cursor = self.conn.cursor()
        query = "delete from isMember  where gid = %s and uid=%s;"
        cursor.execute(query, (gid, uid))
        self.conn.commit()
        return uid

    def deleteGroup(self, gid):
        cursor = self.conn.cursor()
        query = "delete from isMember  where gid = %s;"
        query2 = "delete from Message where gid=%s;"
        query3 = "delete from ChatGroup where gid=%s;"
        cursor.execute(query, (gid,))
        cursor.execute(query2, (gid,))
        cursor.execute(query3, (gid,))
        self.conn.commit()
        return 0

    def addMember(self, uid, gid):
        cursor = self.conn.cursor()
        query = "insert into isMember (uid, gid) values (%s, %s);"
        cursor.execute(query, (uid, gid))
        self.conn.commit()
        return uid

