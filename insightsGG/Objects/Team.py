"""
    File: insightsGG/Objects/Team.py
    Author: Aud#9488
    Desc: This file contains the class for creating insights Team objects
"""
#import json for pretty print
import json

#Import self libraries
import insightsGG.Objects


class Team:
    def __init__(self, ParentClass, InsightsTeam):
        #Setup reference to parent class
        self.Parent = ParentClass

        #Setup identifications
        self.Id      = InsightsTeam["team"]["id"]
        self.Name    = InsightsTeam["team"]["name"]

        #Setup meta data
        self.Picture     = InsightsTeam["team"]["picture"]
        self.Description = InsightsTeam["team"]["description"]
        self.Owner       = insightsGG.Objects.User(InsightsTeam["team"]["owner"])

        #Setup team specifics
        self.Privileges = InsightsTeam["privileges"] #wtf is this?
        self.Roles      = []

        #Push in roles
        for Roles in InsightsTeam["roles"]:
            self.Roles.append(insightsGG.Objects.Role(Roles))

    #Fetch videoes on this team
    def GetVideos(self):
        return self.Parent.GrabTeamVodList(self.Id, 100)

    """
        == Functions that help the user ==
    """
    #Add custom print out
    def __str__(self):
        PrettyPrinted = self.toJSON()

        print(PrettyPrinted)

        for TeamRoles in self.Roles:
            PrettyPrinted["Roles"].append(TeamRoles.__dict__)

        return json.dumps(PrettyPrinted, indent=4, sort_keys=False)


    #Add Custom JSON
    def toJSON(self):
        PrettyPrinted = {
            "Id"          : self.Id,
            "Name"        : self.Name,
            "Description" : self.Description,
            "Owner"       : self.Owner.__dict__,
            "Roles"       : [],
            "Privileges"  : self.Privileges
        }

        return PrettyPrinted