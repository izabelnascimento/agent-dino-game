from Bird import Bird


def simple_reactive_agent(obstacles, dinosaur):
    if not obstacles:
        return

    obstacle = obstacles[0]
    distance_to_obstacle = obstacle.rect.x - dinosaur.dino_rect.x

    if distance_to_obstacle >= 290 or dinosaur.dino_jump:
        return

    if isinstance(obstacle, Bird):
        if obstacle.rect.y < 300:
            dinosaur.dino_down = True
            dinosaur.dino_run = False
            dinosaur.dino_jump = False
        else:
            dinosaur.dino_down = False
            dinosaur.dino_run = False
            dinosaur.dino_jump = True
    else:
        dinosaur.dino_down = False
        dinosaur.dino_run = False
        dinosaur.dino_jump = True
