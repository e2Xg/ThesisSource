# -*- coding: utf-8 -*-

from Source.point_performance_input import point_performance_input
from Source.Main.save import save


point_performance = [
        [   "INSTANTANEOUS_TURN", [0.5, 0.0, 1.4, 6, 50.0]    ],
        [   "MAXIMUM_MACH_NUMBER", [9000.0, 6, 50.0]    ],
        [   "SUPERCRUISE_MACH_NUMBER", [9000.0, 5, 50.0]    ],
        [   "SUSTAINED_TURN", [0.5, 0.0, 6, 50.0]    ]
        ]

point_performance_input = point_performance_input(point_performance)

save('point_performance_input.pydata', point_performance_input)
