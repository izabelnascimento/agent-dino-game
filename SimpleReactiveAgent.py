from Bird import Bird


def simple_reactive_agent(obstacles, dinosaur):
    if obstacles:
        obstacle = obstacles[0]
        distance_to_obstacle = obstacle.rect.x - dinosaur.dino_rect.x

        if distance_to_obstacle < 290:
            if isinstance(obstacle, Bird):
                if obstacle.rect.y < 300:
                    if not dinosaur.dino_jump:
                        dinosaur.dino_duck = True
                        dinosaur.dino_run = False
                        dinosaur.dino_jump = False
                else:
                    if not dinosaur.dino_jump:
                        dinosaur.dino_duck = False
                        dinosaur.dino_run = False
                        dinosaur.dino_jump = True
            else:
                if not dinosaur.dino_jump:
                    dinosaur.dino_duck = False
                    dinosaur.dino_run = False
                    dinosaur.dino_jump = True
