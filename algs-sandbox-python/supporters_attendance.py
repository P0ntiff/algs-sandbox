'''
TeamsSupporters map is given to you. There is also FolksAvailable-array who are Available in office today. List all the Teams who have 100% support available today

Sample 1:
TeamsToSupporterMap = {
    "Thunders" : ["David", "Catherine"]
}
FolksAvailable = ["Catherine", "David", "Sam"]

Output: ["Thunders"]

Sample 2:
TeamsToSupporterMap = {
    "Thunders" : ["David", "Catherine"],
    "Warriors": ["Rebooters", "Sam", "Thunders", "Team X"],
    "Rebooters": ["Thunders", "Sam"]
    "Team X": []
}
FolksAvailable =  ["Catherine","David","Sam"]

Output: ["Thunders","Warriors","Rebooters"]
'''

def teams_with_full_attendance(teams_to_supporters, folks_available):
    visited = {}
    output = []
    def visit(team):
        full_attendance = True
        if len(teams_to_supporters[team]) == 0:
            visited[team] = True 
            return
        for member in teams_to_supporters[team]:
            if member in visited:
                # checked this team already, see if they had full attendance
                full_attendance &= visited[member]
            else: 
                if member in teams_to_supporters: 
                    # must be a team we haven't seen, visit
                    visit(member)
                    full_attendance &= visited[member]
                else:   
                    # must be a supporter, just check if they're available
                    full_attendance &= member in folks_available
        visited[team] = full_attendance
    for team in teams_to_supporters:
        visit(team)
        if visited[team]: 
            output.append(team)
    return output



TeamsToSupporterMap = {
    "Thunders" : ["David"]
}
FolksAvailable =  ["Catherine","David","Sam"]

print(teams_with_full_attendance(TeamsToSupporterMap, FolksAvailable))