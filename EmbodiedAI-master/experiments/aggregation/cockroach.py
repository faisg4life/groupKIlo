from experiments.aggregation.config import config
from simulation.agent import Agent
from simulation.utils import *


class Cockroach(Agent):
    """ """
    def __init__(
            self, pos, v, aggregation, index: int, image: str = "experiments/aggregation/images/ant.png"
    ) -> None:
        """
        Args:
        ----
            pos:
            v:
            flock:
            index (int):
            image (str): Defaults to "experiments/flocking/images/normal-boid.png"
        """
        super(Cockroach, self).__init__(
            pos,
            v,
            image,
            max_speed=config["agent"]["max_speed"],
            min_speed=config["agent"]["min_speed"],
            mass=config["agent"]["mass"],
            width=config["agent"]["width"],
            height=config["agent"]["height"],
            dT=config["agent"]["dt"],
            index=index
        )

        self.aggregation = aggregation
        

    def change_state(self):
        #change from one state to another by finite_state_machine (assignment 0)
        return
    
    def site_behavior(self, cockroach: Agent, neighbors: list) -> Tuple[float, float, float]:
        radius_view = config["cockroach"]["radius_view"] # see's neighbors
        for neigh in neighbors:
            neighbor_sum += neigh
            
        # model probability based on n neighbors 

        # join given T timesteps

        # Still state

        # count number of agents observed after D timesteps

        # probability Pleave based on n neighbors 

        # transition to wander state after D timestep
        
    def update_actions(self):
        
           for obstacle in self.aggregation.objects.obstacles:
            collide = pygame.sprite.collide_mask(self, obstacle)
            if bool(collide):
                self.avoid_obstacle()
                
            for site in self.aggregation.objects.sites:
             collide = pygame.sprite.collide_mask(self, site)
             if bool(collide):
                print("taco's")

            return
    
    # def update_actions(self) -> None:
    #     """
    #     Every change between frames happens here. This function is called by the method "update" in the class Swarm,
    #     for every agent/object. Here, it is checked if there is an obstacle in collision (in which case it avoids it by
    #     going to the opposite direction), align force, cohesion force and separate force between the agent and its neighbors
    #     is calculated, and the steering force and direction of the agent are updated
    #     """

    #     # avoid any obstacles in the environment
    #     for obstacle in self.aggregation.objects.obstacles:
    #         collide = pygame.sprite.collide_mask(self, obstacle)
    #         if bool(collide):
    #             self.avoid_obstacle()

    #     align_force, cohesion_force, separate_force = self.site_behavior()

    #     # combine the vectors in one
    #     steering_force = (
    #             align_force * config["boid"]["alignment_weight"]
    #             + cohesion_force * config["boid"]["cohesion_weight"]
    #             + separate_force * config["boid"]["separation_weight"]
    #     )

    #     # adjust the direction of the boid
    #     self.steering += truncate(
    #         steering_force / self.mass, config["boid"]["max_force"]
    #     )