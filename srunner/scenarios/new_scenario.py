
import carla
from typing import *
from srunner.scenarioconfigs.scenario_configuration import ScenarioConfiguration

import srunner.scenariomanager.scenarioatomics.atomic_trigger_conditions as conditions
from srunner.scenariomanager.carla_data_provider import CarlaDataProvider
from srunner.scenariomanager.timer import TimeOut
from srunner.scenariomanager.weather_sim import WeatherBehavior
from srunner.scenariomanager.scenarioatomics.atomic_behaviors import UpdateAllActorControls

from .basic_scenario import BasicScenario

class NewScenario(BasicScenario):
    """
    Some documentation on NewScenario
    :param world is the CARLA world
    :param ego_vehicles is a list of ego vehicles for this scenario
    :param config is the scenario configuration (ScenarioConfiguration)
    :param randomize can be used to select parameters randomly (optional, default=False)
    :param debug_mode can be used to provide more comprehensive console output (optional, default=False)
    :param criteria_enable can be used to disable/enable scenario evaluation based on test criteria (optional, default=True)
    :param timeout is the overall scenario timeout (optional, default=60 seconds)
    """

    # some ego vehicle parameters
    # some parameters for the other vehicles

    def __init__(self, 
            world: carla.World, 
            ego_vehicles: List[carla.Vehicle], 
            config: ScenarioConfiguration, 
            randomize=False, 
            debug_mode=False, 
            criteria_enable=True,
            timeout=60
        ):
        """
        Initialize all parameters required for NewScenario
        """

        # Call constructor of BasicScenario
        super(NewScenario, self).__init__(
          "NewScenario",
          ego_vehicles,
          config,
          world,
          debug_mode,
          criteria_enable=criteria_enable)


    def _create_behavior(self):
        """
        Setup the behavior for NewScenario
        """

    def _create_test_criteria(self):
        """
        Setup the evaluation criteria for NewScenario
        """