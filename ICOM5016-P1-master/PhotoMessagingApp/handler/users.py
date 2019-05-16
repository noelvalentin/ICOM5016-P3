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

    def addUserByEmail(self, form):
        print("form: ", form)
        if len(form) != 4:
            return jsonify(Error="Malformed post request"), 400
        else:
            uid = form['uid']
            first_name = form['first_name']
            last_name = form['last_name']
            email = form['email']


            if uid and first_name and last_name and email:
                dao = UsersDAO()
                result = dao.addUserByEmail(uid, first_name, last_name, email)
                # result = self.build_user_info_dict(uid, first_name,  last_name, phone, email)
                return jsonify(User=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def addUserByPhone(self, form):
        print("form: ", form)
        if len(form) != 4:
            return jsonify(Error="Malformed post request"), 400
        else:
            uid = form['uid']
            first_name = form['first_name']
            last_name = form['last_name']
            phone = form['phone']


            if uid and first_name and last_name and phone:
                dao = UsersDAO()
                result = dao.addUserByPhone(uid, first_name, last_name, phone)
                # result = self.build_user_info_dict(uid, first_name,  last_name, phone, email)
                return jsonify(User=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteContact(self, uid,cid):
        dao = UsersDAO()
        if not dao.getContact(uid,cid):
            return jsonify(Error="Part not found."), 404
        else:
            dao.deleteContact(uid,cid)
            return jsonify(DeleteStatus="OK"), 200


