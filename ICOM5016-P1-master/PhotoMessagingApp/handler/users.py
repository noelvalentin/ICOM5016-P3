from flask import jsonify
from dao.users import UsersDAO

class UserHandler:

    def buid_user_id_dict(self,row):
        result ={}
        result['uid'] = row[0]
        return result


    def build_user_info_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['first_name'] = row[1]
        result['last_name'] = row[2]
        result['phone'] = row[3]
        result['email'] = row[4]
        return result

    def build_user_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['first_name'] = row[1]
        result['last_name'] = row[2]
        return result

    def build_reaction_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['first_name'] = row[1]
        result['last_name'] = row[2]
        result['date'] = row[3]
        return result

#--------------- Phase 2 ---------------#

    def getAllUsers(self):
        dao = UsersDAO()
        users_list = dao.getAllUsers()
        result_list = []
        for row in users_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users = result_list)

    def getUserById(self, uid):
        dao = UsersDAO()
        row = dao.getUserById(uid)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            user = self.build_user_info_dict(row)
            return jsonify(User = user)

    def getUserContactsById(self, uid):
        dao = UsersDAO()
        contact_list = dao.getUserContactsById(uid)
        result_list = []
        for row in contact_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Contacts = result_list)

    def getMembersByGroupId(self, gid):
        dao = UsersDAO()
        member_list = dao.getMembersByGroupId(gid)
        result_list = []
        for row in member_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Members = result_list)

    def getOwnerByGroupId(self, gid):
        dao = UsersDAO()
        row = dao.getOwnerByGroupId(gid)
        if not row:
            return jsonify(Error = "Group Not Found"), 404
        else:
            owner = self.build_user_dict(row)
            return jsonify(Owner = owner)

    def getLikersByMessageId(self, mid):
        dao = UsersDAO()
        users_list = dao.getLikersByMessageId(mid)
        result_list = []
        for row in users_list:
            result = self.build_reaction_dict(row)
            result_list.append(result)
        return jsonify(Likers = result_list)

    def getDislikersByMessageId(self, mid):
        dao = UsersDAO()
        users_list = dao.getDislikersByMessageId(mid)
        result_list = []
        for row in users_list:
            result = self.build_reaction_dict(row)
            result_list.append(result)
        return jsonify(Dislikers = result_list)

#----------------- END -----------------#


    def createUser(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error = "Malformed post request"), 400
        else:
            email = form['email']
            password = form['password']
            first_name = form['first_name']
            last_name = form['last_name']
            phone= form['phone']
            if email and password and first_name and last_name and phone:
                dao = UsersDAO()
                uid = dao.insert(email, password, first_name, last_name,phone)
                #result = self.build_user_info_dict(uid, first_name,  last_name, phone, email)
                return jsonify(User=uid), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def getUserByFirstName(self, first_name):
        dao = UsersDAO()
        row = dao.getUserByFirstName(first_name)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User=user)

    def getUserByEmail(self, email):
        dao = UsersDAO()
        row = dao.getUserByEmail(email)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User=user)

    def login(self, email, password):
        dao = UsersDAO()
        row = dao.login(email, password)
        if not row:
            return jsonify(Error="Wrong email or password"), 404
        else:
            uid = self.buid_user_id_dict(row)
            return jsonify(User=uid)
'''
    def getUserByFirstName(self, first_name):
        dao = UsersDAO()
        row = dao.getUserByFirstName(first_name)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User = user)

    def getUserByLastName(self, last_name):
        dao = UsersDAO()
        row = dao.getUserByLastName(last_name)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User = user)

    def getUserByPhone(self, phone):
        dao = UsersDAO()
        row = dao.getUserByPhone(phone)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User = user)

    def getUserByEmail(self, email):
        dao = UsersDAO()
        row = dao.getUserByEmail(email)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User = user)

    #def getUserGroupsById(self, uid):
        #dao = UsersDAO()
        #group_list = dao.getUserGroupsById(uid)
        #result_list = []
        #for row in group_list:
            #result = self.build_user_groups_dict(row)
            #result_list.append(row)
        #return jsonify(Groups = result_list)
'''

'''
    def createUser(self):
        dao = UsersDAO()
        result = dao.createUser()
        return result

    def userLogin(self):
        dao=UsersDAO()
        result = dao.login()
        return result

    def deleteUser(self, uid):
        dao = UsersDAO()
        if not dao.getUserById(uid):
            return jsonify(Error = "User Not Found"), 404
        result = dao.deleteUser(uid)
        return result

    def updateUser(self, uid):
        dao = UsersDAO()
        if not dao.getUserById(uid):
            return jsonify(Error = "User Not Found"), 404
        result = dao.updateUser(uid)
        return result
'''
