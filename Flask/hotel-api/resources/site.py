from flask_restful import Resource
from models.site import SiteModel


class Sites(Resource):

    def get(self):
        return {'sites': [site.json() for site in SiteModel.query.all()]} #return a list of all objects in SiteModel

class Site(Resource):

    def get(self, url):
        site = SiteModel.find_site(url)
        if site:
            return site.json()
        return {"message": "Site not found."}, 404 # not found

    def post(self, url):

        if SiteModel.find_site(url):
            return {"Message": f"Site '{url} 'already exists."}, 400 # bad request
        site = SiteModel(url)
        try:
            site.save_site()
        except:
            return {"message" : "An internal error occured trying to create a new site."}
        return site.json()

    def delete(self, url):
        site = SiteModel.find_site(url)
        if site:
            site.delete_site()
            return {"message": "Site deleted"}
        return {"message": "Site not found"}, 404