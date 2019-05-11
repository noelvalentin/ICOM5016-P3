from flask import jsonify
from dao.groups import GroupsDAO

class GroupHandler:

    def build_group_chat_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['gid'] = row[1]
        result['gname'] = row[2]
        result['first_name']=row[3]
        return result

#--------------- Phase 2 ---------------#

    def getAllGroups(self):
        dao = GroupsDAO()
        group_list = dao.getAllGroups()
        result_list = []
        for row in group_list:
            result = self.build_group_chat_dict(row)
            result_list.append(result)
        return jsonify(Groups = result_list)

#----------------- END -----------------#

    def createGroup(self, form):
        print("form: ", form)
        if len(form) != 2:
            return jsonify(Error = "Malformed post request"), 400
        else:
            gname = form['gname']
            ownerID = form['ownerID']

            if gname and ownerID :
                dao = GroupsDAO()
                gid = dao.createGroup(gname, ownerID)
                #result = self.build_user_info_dict(uid, first_name,  last_name, phone, email)
                return jsonify(Groups=gid), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

'''
    def getGroupById(self, gid):
        dao = GroupsDAO()
        row = dao.getGroupById(gid)
        if not row:
            return jsonify(Error = "Group Not Found"), 404
        else:
            group = self.build_group_chat_dict(row)
            return jsonify(Group = group)

    def getGroupByGroupName(self, gname):
        dao = GroupsDAO()
        group_list = dao.getGroupByGroupName(gname)
        result_list = []
        for row in group_list:
            result = self.build_group_chat_dict(row)
            result_list.append(result)
        return jsonify(Groups = result_list)

    def getAllGroupsByOwnerID(self, ownerID):
        dao = GroupsDAO()
        group_list = dao.getAllGroupsByOwnerID(ownerID)
        result_list = []
        for row in group_list:
            result = self.build_group_dict(row)
            result_list.append(result)
        return jsonify(Groups = result_list)
'''

'''
    def createGroup(self):
        dao = GroupsDAO()
        result = dao.createGroup()
        return result

    def deleteGroup(self, gid):
        dao = GroupsDAO()
        if not dao.getGroupById(gid):
            return jsonify(Error="Group not found."), 404
        result = dao.deleteGroup(gid)
        return result

    def updateGroup(self, gid):
        dao = GroupsDAO()
        if not dao.getGroupById(gid):
            return jsonify(Error="Group not found."), 404
        result = dao.updateGroup(gid)
        return result
'''
