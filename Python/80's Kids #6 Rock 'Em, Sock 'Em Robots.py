def fight(robot_1, robot_2, tactics):
    attacking_robot = robot_1 if robot_1["speed"] >= robot_2["speed"] else robot_2
    defending_robot = robot_2 if robot_1["speed"] >= robot_2["speed"] else robot_1
    while len(robot_1["tactics"]) + len(robot_2["tactics"]) > 0:
        defending_robot["health"] -= tactics[attacking_robot["tactics"].pop(0)] if len(attacking_robot["tactics"]) > 0 else 0
        if defending_robot["health"] <= 0:
            return "{} has won the fight.".format(attacking_robot["name"])
        temp = defending_robot
        defending_robot = attacking_robot
        attacking_robot = temp
    if robot_1["health"] == robot_2["health"]:
        return "The fight was a draw."
    return "{} has won the fight.".format(robot_1["name"] if robot_1["health"] > robot_2["health"] else robot_2["name"])