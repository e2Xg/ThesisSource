# -*- coding: utf-8 -*-

from Source.mission_input import mission_input
from Source.Main.save import save


mission = [
        [   "TAKEOFF", [-1.0, 0.5*1.4, 6, 0.03]    ],
        [   "ACCELERATE", [-1.0, -1.0, 0.9, 6]    ],
        [   "CLIMB", [-1.0, -1.0, 9000.0, 5]    ],
        [   "FLY_DISTANCE", [-1.0, -1.0, 600.0]    ],
        [   "ACCELERATE", [-1.0, -1.0, 1.4, 6]    ],
        [   "FLY_SETTING", [-1.0, -1.0, 50.0, 5]    ],
        [   "ACCELERATE", [-1.0, -1.0, 1.2, 6]    ],
        [   "SUSTAINED_TURN", [-1.0, -1.0, 2.0, 6]    ],
        #[   "INSTANTANEOUS_TURN", [-1.0, -1.0, 1.0, 1.4, 6]    ],
        [   "DROP", [948.0+180.0]    ],
        [   "ACCELERATE", [-1.0, -1.0, 1.4, 6]    ],
        [   "CLIMB", [-1.0, -1.0, 9000.0, 5]    ],
        [   "FLY_SETTING", [-1.0, -1.0, 50.0, 5]    ],
        [   "ACCELERATE", [-1.0, -1.0, 0.9, 1]    ],
        [   "FLY_DISTANCE", [-1.0, -1.0, 600.0]    ],
        [   "LOITER", [0.5, 3048.0, 20.0]    ]
        ]

mission_input = mission_input(mission)

save('mission_input.pydata', mission_input)
