import json

with open("new_response.json") as file:
    raw_data = json.load(file)


class Member:

    def __init__(self, user: dict):
        self.id = user["id"]
        fullname = user["fullname"]
        fullname = str(fullname)

        self.full_name = fullname
        self.first_name = fullname.split(" ")[0]
        self.last_name = fullname.split(" ")[1]


class MemberList:
    def __init__(self, user_list: dict):
        non_contacts = user_list["data"]["noncontacts"]
        counter = 0
        for user in non_contacts:
            counter = counter + 1
            user = Member(user)
            print(counter, user.full_name)



test = MemberList(raw_data)


            

