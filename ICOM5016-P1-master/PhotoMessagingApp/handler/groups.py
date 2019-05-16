from flask import jsonify
from dao.groups import GroupsDAO


class GroupHandler:

    def build_group_chat_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['gid'] = row[1]
        result['gname'] = row[2]
        result['first_name'] = row[3]
        return result

#--------------- Phase 2 ---------------#

    def getAllGroups(self):
        dao = GroupsDAO()
        group_list = dao.getAllGroups()
        result_list = []
        for row in group_list:
            result = self.build_group_chat_dict(row)
            result_list.append(result)
        return jsonify(Groups=result_list)

#----------------- END -----------------#

    def createGroup(self, form):
        print("form: ", form)
        if len(form) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            gname = form['gname']
            ownerID = form['ownerID']

            if gname and ownerID:
                dao = GroupsDAO()
                gid = dao.createGroup(gname, ownerID)
                #result = self.build_user_info_dict(uid, first_name,  last_name, phone, email)
                return jsonify(Groups=gid), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def postToGroup(self, form):
        print("form: ", form)
        if len(form) < 0:
            return jsonify(Error="Malformed post request"), 400
        else:
            image = form['image']
            text = form['text']
            uid = form['uid']
            gid = form['gid']
            oid = form['oid']

            if text and uid:
                dao = GroupsDAO()
                result = dao.postToGroup(image, text, uid, gid, oid)
                # result = self.build_user_info_dict(uid, first_name,  last_name, phone, email)
                return jsonify(User=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def getMyGroups(self, uid):
        dao = GroupsDAO()

        group_list = dao.getMyGroups(uid)
        result_list = []
        for row in group_list:
            result = self.build_group_chat_dict(row)
            result_list.append(result)
        return jsonify(Groups=result_list)

    def deleteMember(self, gid, uid):
        dao = GroupsDAO()
        # if not dao.isMember(gid,uid):
        #   return jsonify(Error="Part not found."), 404
        # else:
        dao.deleteMember(gid, uid)
        return jsonify(DeleteStatus="OK"), 200

    def deleteGroup(self, gid):
        dao = GroupsDAO()
        # if not dao.isMember(gid,uid):
        #   return jsonify(Error="Part not found."), 404
        # else:
        dao.deleteGroup(gid)
        return jsonify(DeleteStatus="OK"), 200

    def addMember(self, form):
        print("form: ", form)
        if len(form) < 0:
            return jsonify(Error="Malformed post request"), 400
        else:
            gid = form['gid']
            uid = form['uid']

            if gid and uid:
                dao = GroupsDAO()
                dao.addMember(uid, gid)
                return jsonify(User="OK"), 200
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400


