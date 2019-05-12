# -*- coding: utf-8 -*-

from Source.mission_input import mission_input
from Source.Main.save import save


mission = [
        [   "SPEND", [-1.0,-1.0, 20.0, 1]    ],
        [   "TAKEOFF", [-1.0, 0.5*1.4, 6, 0.03]    ],
        [   "ACCELERATE", [-1.0, -1.0, 0.8, 6]    ],
        [   "CLIMB", [-1.0, -1.0, 9000.0, 5]    ],
        [   "FLY_DISTANCE", [-1.0, -1.0, 740.0]    ],
        [   "DROP", [160.0]    ],
        [   "INSTANTANEOUS_TURN", [-1.0, -1.0, 1.0, 1.4, 6]    ],
        [   "ACCELERATE", [-1.0, -1.0, 0.8, 6]    ],
        [   "SUSTAINED_TURN", [-1.0, -1.0, 2.0, 6]    ],
        [   "DROP", [950.0]    ],
        [   "CLIMB", [-1.0, -1.0, 8000.0, 5]    ],
        [   "FLY_DISTANCE", [0.8, -1.0, 740.0]    ],
        [   "LOITER", [0.5, 5000.0, 20.0]    ]
        ]

mission_input = mission_input(mission)

save('mission_input.pydata', mission_input)
