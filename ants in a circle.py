

nmt_inputs = input().split()
 
N, M, T = int(nmt_inputs[0]), int(nmt_inputs[1]), int(nmt_inputs[2])
new_position_ants = []
 
 
def check_if_any_ant_present(ant_new_pos, current_direction):
    if ant_new_pos in new_position_ants:
        ant_new_pos = ant_new_pos - (current_direction)
        check_if_any_ant_present(ant_new_pos, -(current_direction))
    
    return ant_new_pos, current_direction
 
for i in range(M):
    ants_position_inputs = input().split()
    ant_pos, direction = int(ants_position_inputs[0]), int(ants_position_inputs[1])
    
    ant_pos = (ant_pos+T*direction)%N
    if ant_pos > N:
        ant_pos = 1
    elif ant_pos < 1:
        ant_pos = N
    # ant_new_pos, current_direction = check_if_any_ant_present(ant_pos+direction, direction)
    new_position_ants.append(ant_pos)
 
new_position_ants = map(lambda x: str(x), sorted(new_position_ants))
print(" ".join(new_position_ants).strip())
