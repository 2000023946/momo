class Room:
    def __init__(self, name:str):
        self.name = name
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Room):
            return self.name == value.name
        return False
class Task:
    def ___init___(self, name:str):
        self.name = name
        self.isCompleted = False
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Task):
            return self.name == value.name and self.isCompleted == value.isCompleted
        return False
class Crewmate:
    def ___init___(self, name:str, color:str, acessories = ()):
        self.name = name
        self.color = color
        self.acessories = acessories
        self.isAlive = True
        self.tasksDone = 0
    def doTask(self, task):
        if not task.isCompleted:
            self.tasksDone+=1
            task.isCompleted = True
        else:
            return "Nothing to do here."
    def vote(self, AmongUs:object):
        for player in AmongUs.crewmates:
            if player.name[0] == self.name[0] and not len(player.name) == len(self.name) and player.isAlive:
                return player.name[0]
        for player in AmongUs.imposters:
            if player.name[0] == self.name[0] and not len(player.name) == len(self.name) and player.isAlive:   
                return player.name[0]
    def callMeeting(self, AmongUs:object):
        result = {}
        for player in AmongUs.crewmates + AmongUs.imposters:
            if player.isAlive:
                voted = self.vote(AmongUs)
                if voted:
                    result[voted] = result.get(voted, 0) + 1
        max = float('-inf')
        player = None
        for key in result.keys():
            if result[key] > max:
                player = key
                max = result[key]
        player.isAlive = False
        if isinstance(player, Imposter):
            return f"{player.name} was An Imposter."
        return f"{player.name} was not An Imposter"
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Crewmate):
            return self.name == value.name and self.color == value.color and self.acessories == value.acessories:
        return False
class Imposter:
    def __init__(self, name:str, color:str, acessories = ()):
        self.name = name
        self.color = color
        self.acessories = acessories
        self.isAlive = True
        eliminateCount = 0
    def eliminate(self, player):
        if isinstance(player, Imposter):
            return "They're on your team -__-"
        elif isinstance(player, Crewmate):
            player.isAlive = False
            Imposter.eliminateCount +=1
    def vote(self, AmongUs:object):
        for player in AmongUs.crewmates:
            if player.name[0] == self.name[0] and not len(player.name) == len(self.name) and player.isAlive:
                return player.name[0]
        for player in AmongUs.imposters:
            if player.name[0] == self.name[0] and not len(player.name) == len(self.name) and player.isAlive:   
                return player.name[0]
    def __str__(self) -> str:
        return f"My name is {self.name} and I'm an imposter"
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Imposter):
            return self.name == value.name and self.color == value.color and self.acessories == value.acessories:
        return False
class AmongUs:
    def __init__(self, maxPlayers:int, rooms:dict, crewmates:list, imposters:list) -> None:
        self.maxPlayers = maxPlayers
        self.rooms = rooms
        self.crewmates = crewmates
        self.imposters = imposters
    def registerPlayer(self, value:object):
        if len(self.crewmates) + len(self.imposters) >= self.maxPlayers:
            return "Lobby is full."
        for player in self.crewmates:
            if player.name == value.name:
                return f"Player with name: {player.name} exsists."
        for player in self.imposters:
            if player.name == value.name:
                return f"Player with name: {player.name} exsists."
        if isinstance(player, Crewmate):
            self.crewmates.append(player)
        if isinstance(player, Imposter):
            self.imposters.append(player)
    def registerTask(self, task:object, room: object):
        for key in self.rooms.keys():
            for value in self.rooms[key]:
                if value.__eq__(task):
                    return "This task has already been registered."
        if not room.name in self.rooms:
            self.rooms[room.name] = [task]
        else:
            curTasks = self.rooms[room.name]
            curTasks.append(task)
            self.rooms[room.name] = curTasks
    def gameOver(self):
        crewAliveCount = 0
        impostAliveCount = 0
        for crewmate in self.crewmates:
            if crewmate.isAlive:
                crewAliveCount +=1
        for imposter in self.imposters:
            if imposter.isAlive:
                impostAliveCount +=1
        if crewAliveCount == 0:
            return "Defeat! All crewmates have been eliminated."
        if impostAliveCount == 0:
            return "Victory! All imposters have been eliminated."
        return "Game is not over yet!"
        


