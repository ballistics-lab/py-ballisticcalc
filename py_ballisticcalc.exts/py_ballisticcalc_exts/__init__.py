__author__ = "o-murphy"
__copyright__ = (
    "Copyright 2023 Dmytro Yaroshenko (https://github.com/o-murphy)",
    "Copyright 2024 David Bookstaber (https://github.com/dbookstaber)"
)

__credits__ = ["o-murphy", "dbookstaber"]

from .euler_engine import CythonizedEulerIntegrationEngine
from .rk4_engine import CythonizedRK4IntegrationEngine
# from .vector import Vector
from .trajectory_data import TrajectoryData

__all__ = (
    'CythonizedEulerIntegrationEngine',
    'CythonizedRK4IntegrationEngine',
    # 'Vector',
    'TrajectoryData',
)
