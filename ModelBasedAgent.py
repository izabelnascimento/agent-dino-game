from Bird import Bird


class ModelBasedAgent:
    def __init__(self):
        self.state = {
            "obstacle_distance": float('inf'),
            "obstacle_height": 0,
            "dino_y_position": 0,
            "dino_is_jumping": False,
            "time_since_last_jump": 0
        }

    def update_state(self, obstacles, dinosaur):
        if obstacles:
            obstacle = obstacles[0]
            self.state["obstacle_distance"] = obstacle.rect.x - dinosaur.dino_rect.x
            self.state["obstacle_height"] = obstacle.rect.y
        else:
            self.state["obstacle_distance"] = float('inf')

        self.state["dino_y_position"] = dinosaur.dino_rect.y
        self.state["dino_is_jumping"] = dinosaur.dino_jump
        self.state["time_since_last_jump"] += 1

    def act(self, dinosaur, obstacles):
        action = self.decide_action(obstacles)

        if action == "jump" and not dinosaur.dino_jump:
            dinosaur.dino_duck = False
            dinosaur.dino_run = False
            dinosaur.dino_jump = True
        elif action == "duck" and not dinosaur.dino_jump:
            dinosaur.dino_duck = True
            dinosaur.dino_run = False
            dinosaur.dino_jump = False

    def decide_action(self, obstacles):
        if self.state["obstacle_distance"] < 290:
            if isinstance(obstacles[0], Bird):
                if self.state["obstacle_height"] < 300:
                    return "duck"
                else:
                    return "jump"
            else:
                return "jump"
        else:
            return ""


model_based_agent = ModelBasedAgent()


def model_based_agent_control(obstacles, dinosaur):
    model_based_agent.update_state(obstacles, dinosaur)
    model_based_agent.act(dinosaur, obstacles)
