"""
This code shows how to implment a from_fiule method to initialize a class

The advantage is that we can initialize the class in multiple ways this way depending on the circumstances

Credit goes to Lukas Fröhlich, where I saw this the first time.
"""

import yaml


class SampleClass(object):
    def __init__(self, parameter1, parameter2, config):
        """Sample class initializer.

        Parameters
        ----------
        parameter1 : type
            sample_parameter 1.
        parameter2 : type
            sample parameter 2.
        config : dict
            The configuration dictionary for the class.
        """
        self.parameter1 = parameter1
        self.parameter2 = parameter2

        self.config = config

    @classmethod
    def from_file(cls, config_file: str):
        """Initialize a sample class instance from a config file.
        Parameters
        ----------
        config_file : str
            The config file (full path, relative or absolute).
        Returns
        -------
        :class:`SampleClass`
            An instance of the BayesianOptimization class.
        """
        # Read config from file
        try:
            with open(config_file, "r") as f:
                config = yaml.load(f, Loader=yaml.FullLoader)

        except FileNotFoundError:
            print("The config file ({config_file}) you specified does not exist.")

            # In ROS one should use the following code snippet to log an error:
            '''
            rospy.logerr(
                f"The config file ({config_file}) you specified does not exist."
            )
            '''
            exit(1)

        # Construct class instance based on the config
        return cls(
            parameter1=config["parameter1"],
            parameter2=config["parameter2"],
            config=config,
        )