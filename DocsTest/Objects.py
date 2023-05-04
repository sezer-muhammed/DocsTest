import typing


class BaseObject:
    """
    BaseObject class represents a basic 3D object with various attributes.

    Attributes:
        name (str, optional): A unique name for the object.
        type (str, optional): The type or category the object belongs to.
        age (int, optional): The age of the object, represented as an integer.
        missing_age (int, optional): The missing age of the object, represented as an integer.
        position_x (float, optional): The x-coordinate of the object's position in 3D space.
        position_y (float, optional): The y-coordinate of the object's position in 3D space.
        position_z (float, optional): The z-coordinate of the object's position in 3D space.
        rotation_x (float, optional): The x-coordinate of the object's rotation in 3D space.
        rotation_y (float, optional): The y-coordinate of the object's rotation in 3D space.
        rotation_z (float, optional): The z-coordinate of the object's rotation in 3D space.
        scale_x (float, optional): The scaling factor for the object's size along the x-axis.
        scale_y (float, optional): The scaling factor for the object's size along the y-axis.
        scale_z (float, optional): The scaling factor for the object's size along the z-axis.

    Example:
        >>> obj = BaseObject(name="Cube", type="Geometry", age=1, missing_age=0,
                             position_x=0.0, position_y=0.0, position_z=0.0,
                             rotation_x=0.0, rotation_y=0.0, rotation_z=0.0,
                             scale_x=1.0, scale_y=1.0, scale_z=1.0)
    """

    def __init__(
        self,
        name=None,
        object_type=None,
        age=None,
        missing_age=None,
        position_x=None,
        position_y=None,
        position_z=None,
        rotation_x=None,
        rotation_y=None,
        rotation_z=None,
        scale_x=None,
        scale_y=None,
        scale_z=None,
    ) -> None:
        self.name = name
        self.object_type = object_type
        self.age = age
        self.missing_age = missing_age
        self.position_x = position_x
        self.position_y = position_y
        self.position_z = position_z
        self.rotation_x = rotation_x
        self.rotation_y = rotation_y
        self.rotation_z = rotation_z
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.scale_z = scale_z

    def update(self, parameters: typing.Dict[str, typing.Any]) -> None:
        """
        Update the object with the given parameters. The parameters should be a dictionary containing the
        specified keys and their corresponding types.

        Args:
            parameters (dict): A dictionary with the keys same name with attributes of the object and their corresponding types.

        Returns:
            None

        Raises:
            ValueError: If the value of a key is not the correct type.

        Examples:
            >>> parameters = {
                    'name': 'test',
                    'object_type': 'test',
                    'age': 1,
                    'missing_age': 1,
                    'position_x': 1,
                    'position_y': 1,
                    'position_z': 1,
                    'rotation_x': 1,
                    'rotation_y': 1,
                    'rotation_z': 1,
                    'scale_x': 1,
                    'scale_y': 1,
                    'scale_z': 1
                }
            >>> object.update(parameters)

            >>> parameters = {
                    'name': 'test',
                    'object_type': 'test',
                }
            >>> object.update(parameters)
        """

        for key, value in parameters.items():
            if key in ("name", "object_type"):
                if not isinstance(value, str):
                    raise ValueError("{key} should be a string")
            else:
                if not isinstance(value, (int, float)):
                    raise ValueError(f"{key} should be a number")

        self.name = parameters.get("name", self.name)
        self.object_type = parameters.get("object_type", self.object_type)
        self.age = parameters.get("age", self.age)
        self.missing_age = parameters.get("missing_age", self.missing_age)
        self.position_x = parameters.get("position_x", self.position_x)
        self.position_y = parameters.get("position_y", self.position_y)
        self.position_z = parameters.get("position_z", self.position_z)
        self.rotation_x = parameters.get("rotation_x", self.rotation_x)
        self.rotation_y = parameters.get("rotation_y", self.rotation_y)
        self.rotation_z = parameters.get("rotation_z", self.rotation_z)
        self.scale_x = parameters.get("scale_x", self.scale_x)
        self.scale_y = parameters.get("scale_y", self.scale_y)
        self.scale_z = parameters.get("scale_z", self.scale_z)

    def predict(self):
        """To be added"""
        raise NotImplementedError("Will be added later")
