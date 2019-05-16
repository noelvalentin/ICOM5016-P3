from flask import jsonify
from src.dashboard_dao import DashboardDAO


class DashboardHandler:

    def build_stats_dict(self, row):
        result = {}
        result['info'] = row[0]
        result['count'] = row[1]
        return result

    #--------------- Phase 3 ---------------#

    def getPostsCount(self):
        dao = DashboardDAO()
        trending = dao.getPostsCount()
        result_list = []
        for row in trending:
            result = self.build_stats_dict(row)
            result_list.append(result)
        return jsonify(Result=result_list)

    def likesPerDay(self):
        dao = DashboardDAO()
        trending = dao.likesPerDay()
        result_list = []
        for row in trending:
            result = self.build_stats_dict(row)
            result_list.append(result)
        return jsonify(Result=result_list)

    def dislikesPerDay(self):
        dao = DashboardDAO()
        trending = dao.dislikesPerDay()
        result_list = []
        for row in trending:
            result = self.build_stats_dict(row)
            result_list.append(result)
        return jsonify(Result=result_list)

    def repliesPerDay(self):
        dao = DashboardDAO()
        trending = dao.repliesPerDay()
        result_list = []
        for row in trending:
            result = self.build_stats_dict(row)
            result_list.append(result)
        return jsonify(Result=result_list)

    def getTrendingTopics(self):
        dao = DashboardDAO()
        trending = dao.getTrendingTopics()
        result_list = []
        for row in trending:
            result = self.build_stats_dict(row)
            result_list.append(result)
        return jsonify(Result=result_list)
