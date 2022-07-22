force_side_dict = {}

command = input()

while command != "Lumpawaroo":
    if "|" in command:
        split_command = command.split(" | ")
        force_side, force_user = split_command
        present = False
        for value in force_side_dict.values():
            if force_user in value:
                present = True
                break
        if not present:
            if force_side not in force_side_dict.keys():
                force_side_dict[force_side] = [force_user]
            else:
                force_side_dict[force_side].append(force_user)
    else:
        split_command = command.split(" -> ")
        force_user, force_side = split_command
        present = False
        for key, value in force_side_dict.items():
            if force_user in value:
                present = True
                force_side_dict[key].pop(value.index(force_user))
                break
        if present:
            if force_side not in force_side_dict.keys():
                force_side_dict[force_side]= [force_user]
            else:
                force_side_dict[force_side].append(force_user)
        else:
            if force_side not in force_side_dict.keys():
                force_side_dict[force_side] = [force_user]
            else:
                force_side_dict[force_side].append(force_user)
    command = input()