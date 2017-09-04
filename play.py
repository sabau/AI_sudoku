from isolation.gs import *
import isolation.utils as u

gs0 = GameState()
print(u.terminal_test(gs0))

gs1 = gs0.forecast_move((0,0))
print(u.terminal_test(gs1))
print(gs1.get_legal_moves())

gs2 = gs1.forecast_move((1,1))
print(u.terminal_test(gs2))
print(gs2.get_legal_moves())

gs3 = gs2.forecast_move((0,1))
print(u.terminal_test(gs3))
print(gs3.get_legal_moves())

gs4 = gs3.forecast_move((1,0))
print(u.terminal_test(gs4))


