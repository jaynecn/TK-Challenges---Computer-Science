while True:
    print(new_player)
    print(new_player.current_room.description)
    
    user_input = (input("Where do you want to go? Type n, s, e or w: "))

    try:
        if user_input in user_movement:
            if user_input is 'n':
                assert new_player.current_room.n_to
                new_player.current_room = new_player.current_room.n_to
                print(new_player, 'this is the line i printed')
            elif user_input is 'w':
                assert new_player.current_room.w_to
                new_player.current_room = new_player.current_room.w_to
                print(new_player, 'this is the line i printed')
            elif user_input is 's':
                assert new_player.current_room.s_to
                new_player.current_room = new_player.current_room.s_to
                print(new_player, 'this is the line i printed')
            elif user_input is 'e':
                assert new_player.current_room.e_to
                new_player.current_room = new_player.current_room.e_to
                print(new_player, 'this is the line i printed')
            pass
        elif user_input is 'q':
            break
        else:
            print('invalid option')
        pass
    except ValueError:
        print(f'move not allowed')
    