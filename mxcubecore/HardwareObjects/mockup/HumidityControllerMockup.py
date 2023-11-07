#
#  Project: MXCuBE
#  https://github.com/mxcube
#
#  This file is part of MXCuBE software.
#
#  MXCuBE is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  MXCuBE is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU General Lesser Public License
#  along with MXCuBE. If not, see <http://www.gnu.org/licenses/>.

"""Mockup class for testing purposes"""

from mxcubecore.HardwareObjects.abstract.AbstractActuator import AbstractActuator

# Default humidity value (%)
DEFAULT_VALUE = 50
# Default humidity limits (%)
DEFAULT_LIMITS = (0, 100)


class HumidityControllerMockup(AbstractActuator):
    """Humidity Controller Mockup class"""
    def __init__(self, name):
        super().__init__(name)
        self.humidity = DEFAULT_VALUE
        self.set_limits(DEFAULT_LIMITS)
        print("jojoojojojojojojojoojojojojo")

    def get_value(self):
        return self.humidity

    def _set_value(self, value):
        self.humidity = value
