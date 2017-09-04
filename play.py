from isolation.gamestate import *

gs0 = GameState()
gs0.print()
print(gs0.get_legal_moves())

gs1 = gs0.forecast_move((0,0))
gs1.print()
print(gs1.get_legal_moves())

gs2 = gs1.forecast_move((1,1))
gs2.print()
print(gs2.get_legal_moves())