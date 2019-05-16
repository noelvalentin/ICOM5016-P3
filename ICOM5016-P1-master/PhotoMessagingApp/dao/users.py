import psycopg2


class UsersDAO:

    def __init__(self):
        connection_url = "dbname=jeanmerced user=postgres password=password"
        self.conn = psycopg2._connect(connection_url)


#--------------- Phase 2 ---------------#

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select uid, first_name, last_name from Users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self, uid):
        cursor = self.conn.cursor()
        query = "select uid, first_name, last_name, phone, email from Users where uid = %s;"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result

    def getUserContactsById(self, uid):
        cursor = self.conn.cursor()
        query = "select uid, first_name, last_name from Users, (select cid from ContactList where uid = %s) as C where uid = cid;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMembersByGroupId(self, gid):
        cursor = self.conn.cursor()
        query = "select uid, first_name, last_name from Users natural inner join isMember where gid = %s"
        cursor.execute(query, (gid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOwnerByGroupId(self, gid):
        cursor = self.conn.cursor()
        query = "select uid, first_name, last_name from Users natural inner join ChatGroup Where gid = %s"
        cursor.execute(query, (gid,))
        result = cursor.fetchone()
        return result

    def getLikersByMessageId(self, mid):
        cursor = self.conn.cursor()
        query = "select uid, first_name, last_name, date from Users natural inner join Likes where mid = %s"
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getDislikersByMessageId(self, mid):
        cursor = self.conn.cursor()
        query = "select uid, first_name, last_name, date from Users natural inner join Dislikes where mid = %s"
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

#----------------- END -----------------#

    def insert(self, email, password, first_name, last_name, phone):
        cursor = self.conn.cursor()
        query = "insert into Users(email, password, first_name, last_name,phone) values (%s, %s, %s, %s, %s) returning uid;"
        cursor.execute(query, (email, password, first_name, last_name, phone,))
        uid = cursor.fetchone()[0]
        self.conn.commit()
        return uid

    def getUserByFirstName(self, firstName):
        cursor = self.conn.cursor()
        query = "select uid, first_name, last_name from Users  Where first_name = %s"
        cursor.execute(query, (firstName,))
        result = cursor.fetchone()
        return result

    def getUserByEmail(self, email):
        cursor = self.conn.cursor()
        query = "select uid, first_name, last_name,email from Users  Where email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        return result

    def login(self, email, password):
        cursor = self.conn.cursor()
        query = "select uid  from Users  Where email = %s and password= %s"
        cursor.execute(query, (email, password,))
        result = cursor.fetchone()
        return result

    def addUserByEmail(self, uid, first_name, last_name, email):
        cursor = self.conn.cursor()
        query = "insert into ContactList(uid,cid) values(%s,(select uid from Users where first_name=%s and last_name=%s and email=%s)) returning uid;"
        cursor.execute(query, (uid, first_name, last_name, email))
        result = cursor.fetchone()[0]
        self.conn.commit()
        return result

    def addUserByPhone(self, uid, first_name, last_name, phone):
        cursor = self.conn.cursor()
        query = "insert into ContactList(uid,cid) values(%s,(select uid from Users where first_name=%s and last_name=%s and phone=%s)) returning uid;"
        cursor.execute(query, (uid, first_name, last_name, phone))
        result = cursor.fetchone()[0]
        self.conn.commit()
        return result

    def deleteContact(self, uid, cid):
        cursor = self.conn.cursor()
        query = "delete from ContactList  where uid = %s and cid=%s;"
        cursor.execute(query, (uid, cid))
        self.conn.commit()
        return cid

    def getContact(self, uid, cid):
        cursor = self.conn.cursor()
        query = "select cid from ContactList  where uid = %s and cid=%s;"
        cursor.execute(query, (uid, cid))
        self.conn.commit()
        return cid

