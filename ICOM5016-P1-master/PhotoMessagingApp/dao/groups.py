import psycopg2

class GroupsDAO:

    def __init__(self):
        connection_url = "dbname=mydb user=yo host=localhost password=password"
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
        cursor.execute(query, (gname, ownerID,))
        gid = cursor.fetchone()[0]
        self.conn.commit()
        return gid

'''
    def getGroupById(self, gid):
        result=[]
        if gid==30:
            result=[30,"Avengers","Steve Rogers"]

        elif gid==11:
            result=[11,"Los Extraterrestres","Wisin y Yandel"]
        elif gid== 9:
            result=[9,"All-Stars","Fulanito"]

        return result

    def getGroupByGroupName(self, gname):
        result=[]
        if gname=="Avengers":
            result = [[30, "Avengers", "Steve Rogers"]]
        elif gname=="Los Extraterrestres":
            result=[[11,"Los Extraterrestres","Wisin y Yandel"]]
        elif gname=="All-Stars":
            result=[[9,"All-Stars","Fulanito"]]

        return result

    def getAllGroupsByOwnerID(self, ownerID):
        result = [[10,"Basket"],[12,"Playa Sabado"]]
        return result
'''

'''
    def createGroup(self):
        result = "Group Succesfully Created."
        return result

    def deleteGroup(self, gid):
        result = "the group %d has been deleted" %(gid)
        return result

    def updateGroup(self, gid):
        result = "the group %d has been updated" %(gid)
        return result
'''
