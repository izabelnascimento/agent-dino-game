from Bird import Bird


class ModelBasedAgent:
    def __init__(self):
        self.state = {
            "obstacle_distance": float('inf'),
            "obstacle_height": 0,
            "dino_is_jumping": False
        }

    def update_state(self, obstacles, dinosaur):
        if obstacles:
            obstacle = obstacles[0]
            self.state["obstacle_distance"] = obstacle.rect.x - dinosaur.dino_rect.x
            self.state["obstacle_height"] = obstacle.rect.y
        else:
            self.state["obstacle_distance"] = float('inf')

        self.state["dino_is_jumping"] = dinosaur.dino_jump

    def act(self, dinosaur, obstacles):
        action = self.decide_action(obstacles)
        is_jumping = self.state["dino_is_jumping"]

        if action == "jump" and not is_jumping:
            dinosaur.dino_down = False
            dinosaur.dino_run = False
            dinosaur.dino_jump = True
        elif action == "down" and not is_jumping:
            dinosaur.dino_down = True
            dinosaur.dino_run = False
            dinosaur.dino_jump = False

    def decide_action(self, obstacles):
        if self.state["obstacle_distance"] >= 290:
            return ""
        obstacle = obstacles[0]
        if isinstance(obstacle, Bird):
            return "down" if self.state["obstacle_height"] < 300 else "jump"

        return "jump"


model_based_agent = ModelBasedAgent()


def model_based_agent_control(obstacles, dinosaur):
    model_based_agent.update_state(obstacles, dinosaur)
    model_based_agent.act(dinosaur, obstacles)
