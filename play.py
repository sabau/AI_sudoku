from isolation.gs import *
import isolation.utils as u
from isolation.minimax import *

gs0 = GameState()
print(minimax_decision(gs0))
gs1 = gs0.forecast_move((0,0))
print(minimax_decision(gs1))

gs2 = gs1.forecast_move((1,0))
print(minimax_decision(gs2))
gs3 = gs2.forecast_move((0,1))
print(minimax_decision(gs3))

gs4 = gs3.forecast_move((1,1))
print(minimax_decision(gs4))


