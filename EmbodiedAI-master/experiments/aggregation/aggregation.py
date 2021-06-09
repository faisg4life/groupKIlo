from experiments.aggregation.cockroach import Cockroach
from experiments.aggregation.config import config
from simulation.utils import *
from simulation.swarm import Swarm


class Aggregations(Swarm):
    """ """
    
    def __init__(self, screen_size) -> None:
        """
        This function is the initializer of the class Aggregations.
        :param screen_size:
        """
        super(Aggregations, self).__init__(screen_size)
        self.object_loc = config["aggregation"]["outside"]

    def initialize(self, num_agents: int) -> None:
        """
        Initialize the whole swarm, creating and adding the obstacle objects, and the agent, placing them inside of the
        screen and avoiding the obstacles.
        :param num_agents: int:

        """

        # add obstacle/-s to the environment if present
        if config["aggregation"]["obstacles"]:
            object_loc = config["base"]["object_location"]

            if config["aggregation"]["outside"]:
                scale = [300, 300]
            else:
                scale = [800, 800]

            filename = "experiments/flocking/images/redd.png"
            filename2 = "experiments/aggregation/images/greyc1.png"
               
            

            self.objects.add_object(
                file=filename, pos=object_loc, scale=scale, obj_type="obstacle"
            )
            self.objects.add_object(
                file=filename2, pos=object_loc, scale=[100, 100], obj_type="site"
            )

            min_x, max_x = area(object_loc[0], scale[0])
            min_y, max_y = area(object_loc[1], scale[1])

        # add agents to the environment
        for index, agent in enumerate(range(num_agents)):
            coordinates = generate_coordinates(self.screen)

            # if obstacles present re-estimate the corrdinates
            if config["aggregation"]["obstacles"]:
                if config["aggregation"]["outside"]:
                    while (
                            max_x >= coordinates[0] >= min_x
                            and max_y >= coordinates[1] >= min_y
                    ):
                        coordinates = generate_coordinates(self.screen)
                else:
                    while (
                        coordinates[0] >= max_x
                        or coordinates[0] <= min_x
                        or coordinates[1] >= max_y
                        or coordinates[1] <= min_y
                    ):
                        coordinates = generate_coordinates(self.screen)

            self.add_agent(Cockroach(pos=np.array(coordinates), v=None, aggregation=self, index=index))
    pass
