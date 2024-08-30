import conditions
from exercise import Exercise

crunches = Exercise("Crunches",
                    "./resources/gifs/crunches.gif",
                    "./resources/starting_postures/crunches.png",
                    True, False, 10, 90, None, conditions.crunches)
pile_squats = Exercise("Pile squats",
                       "./resources/gifs/pile_squats.gif",
                       "./resources/starting_postures/pile_squats.png",
                       False, True, 10, 60, None, conditions.pile_squats)
lunges_right_leg = Exercise("Lunges right leg",
                            "./resources/gifs/lunges_right.gif",
                            "./resources/starting_postures/lunges_right.png",
                            True, True, 5, 60, None, conditions.lunges_right_leg)
lunges_left_leg = Exercise("Lunges left leg",
                           "./resources/gifs/lunges_left.gif",
                           "./resources/starting_postures/lunges_left.png",
                           True, True, 5, 60, None, conditions.lunges_left_leg)
side_lunges_right_leg = Exercise("Side lunges right leg",
                                 "./resources/gifs/side_lunges_right.gif",
                                 "./resources/starting_postures/side_lunges_right.png",
                                 False, True, 5, 60, None, conditions.side_lunges_right_leg)
side_lunges_left_leg = Exercise("Side lunges left leg",
                                "./resources/gifs/side_lunges_left.gif",
                                "./resources/starting_postures/side_lunges_left.png",
                                False, True, 5, 60, None, conditions.side_lunges_left_leg)
squats = Exercise("Squats",
                  "./resources/gifs/squats.gif",
                  "./resources/starting_postures/squats.png",
                  True, True, 10, 90, None, conditions.squats)
hip_stretch_left_leg = Exercise("Hip stretch left leg",
                                "./resources/gifs/hip_stretch_left.gif",
                                "./resources/starting_postures/hip_stretch_left.png",
                                True, True, 5, 60, None, conditions.hip_stretch_left_leg)
hip_stretch_right_leg = Exercise("Hip stretch right leg",
                                 "./resources/gifs/hip_stretch_right.gif",
                                 "./resources/starting_postures/hip_stretch_right.png",
                                 True, True, 5, 60, None, conditions.hip_stretch_right_leg)
good_morning_stretch = Exercise("Good morning stretch",
                                "./resources/gifs/good_morning.gif",
                                "./resources/starting_postures/good_morning.png",
                                True, True, 5, 45, None, conditions.good_morning_stretch)
press_up_back = Exercise("Press up back",
                         "./resources/gifs/press_up_back.gif",
                         "./resources/starting_postures/press_up_back.png",
                         True, True, 5, 60, None, conditions.press_up_back)
left_leg_elevation = Exercise("Left leg elevation",
                              "./resources/gifs/leg_elevation_left.gif",
                              "./resources/starting_postures/leg_elevation_left.png",
                              True, True, 5, 60, None, conditions.left_leg_elevation)
right_leg_elevation = Exercise("Right leg elevation",
                               "./resources/gifs/leg_elevation_right.gif",
                               "./resources/starting_postures/leg_elevation_right.png",
                               True, True, 5, 60, None, conditions.right_leg_elevation)
box_push_ups = Exercise("Box push ups",
                        "./resources/gifs/box_pushups.gif",
                        "./resources/starting_postures/bird_dog-box_push_ups-glute_kick.png",
                        True, False, 5, 60, None, conditions.box_push_ups)
cobra_stretch = Exercise("Cobra stretch",
                         "./resources/gifs/cobra_stretch.gif",
                         "./resources/starting_postures/cobra_stretch.png",
                         True, False, 5, 60, None, conditions.cobra_stretch)
crunch_kicks = Exercise("Crunch kicks",
                        "./resources/gifs/crunch_kicks.gif",
                        "./resources/starting_postures/crunch_kicks.png",
                        True, False, 5, 60, None, conditions.crunch_kicks)
leg_drops = Exercise("Leg drops",
                     "./resources/gifs/leg_drops.gif",
                     "./resources/starting_postures/leg_raise.png",
                     True, False, 5, 60, None, conditions.leg_drops)
military_push_ups = Exercise("Military push ups",
                             "./resources/gifs/military_push_ups.gif",
                             "./resources/starting_postures/military_push_ups.png",
                             True, False, 5, 60, None, conditions.military_push_ups)
superman = Exercise("Superman",
                    "./resources/gifs/superman.gif",
                    "./resources/starting_postures/superman.png",
                    True, False, 5, 60, None, conditions.superman)
side_bends = Exercise("Side bends",
                      "./resources/gifs/side_bends.gif",
                      "./resources/starting_postures/side_bends.png",
                      False, True, 5, 60, None, conditions.side_bends)
donkey_kicks = Exercise("Donkey kicks",
                        "./resources/gifs/donkey_kicks.gif",
                        "./resources/starting_postures/donkey_kicks.png",
                        True, False, 5, 60, None, conditions.donkey_kicks)
glute_kick_back = Exercise("Glute kick back",
                           "./resources/gifs/glute_kick_back.gif",
                           "./resources/starting_postures/bird_dog-box_push_ups-glute_kick.png",
                           True, False, 5, 60, None, conditions.glute_kick_back)
bicycle_crunches = Exercise("Bicycle crunches",
                            "./resources/gifs/bicycle_crunches.gif",
                            "./resources/starting_postures/bicycle_crunches.png",
                            True, False, 5, 60, None, conditions.bicycle_crunches)
bird_dog = Exercise("Bird dog",
                    "./resources/gifs/bird_dog.gif",
                    "./resources/starting_postures/bird_dog-box_push_ups-glute_kick.png",
                    True, False, 5, 60, None, conditions.bird_dog)
dead_bug = Exercise("Dead bug",
                    "./resources/gifs/dead_bug.gif",
                    "./resources/starting_postures/dead_bug.png",
                    True, False, 5, 60, None, conditions.dead_bug)
diagonal_plank = Exercise("Diagonal plank", "./resources/gifs/diagonal_plank.gif",
                          "./resources/starting_postures/military_push_ups.png",
                          True, False, 5, 60, None, conditions.diagonal_plank)
leg_raise = Exercise("Leg raise",
                     "./resources/gifs/leg_raise.gif",
                     "./resources/starting_postures/leg_raise.png",
                     True, False, 5, 60, None, conditions.leg_raise)
donkey_kicks_pulse_left = Exercise("Donkey kicks pulse left",
                                   "./resources/gifs/donkey_kicks_pulse_left.gif",
                                   "./resources/starting_postures/donkey_kicks.png",
                                   True, False, 5, 60, None, conditions.donkey_kicks_pulse_left)
donkey_kicks_pulse_right = Exercise("Donkey kicks pulse right",
                                    "./resources/gifs/donkey_kicks_pulse_right.gif",
                                    "./resources/starting_postures/donkey_kicks_right.png",
                                    True, False, 5, 60, None, conditions.donkey_kicks_pulse_right)
glute_kick_back_pulse_left = Exercise("Glute kick back pulse left",
                                      "./resources/gifs/glute_kickback_pulse_left.gif",
                                      "./resources/starting_postures/glute_pulse_left.png",
                                      True, False, 5, 60, None, conditions.glute_kick_back_pulse_left)
glute_kick_back_pulse_right = Exercise("Glute kick back pulse right",
                                       "./resources/gifs/glute_kickback_pulse_right.gif",
                                       "./resources/starting_postures/glute_pulse_right.png",
                                       True, False, 5, 60, None, conditions.glute_kick_back_pulse_right)
jumping_jacks = Exercise("Jumping jacks", "./resources/gifs/jumping_jacks.gif",
                         "./resources/starting_postures/jumping_jacks.png",
                         False, True, 5, 60, None, conditions.jumping_jacks)

exercise_list = [crunches, pile_squats, lunges_right_leg, lunges_left_leg, side_lunges_right_leg,
                 side_lunges_left_leg, squats, hip_stretch_left_leg, hip_stretch_right_leg, good_morning_stretch,
                 press_up_back, left_leg_elevation, right_leg_elevation, box_push_ups, cobra_stretch, crunch_kicks,
                 leg_drops, military_push_ups, superman, side_bends, donkey_kicks, glute_kick_back, bicycle_crunches,
                 bird_dog, dead_bug, diagonal_plank, leg_raise, donkey_kicks_pulse_left, donkey_kicks_pulse_right,
                 glute_kick_back_pulse_left, glute_kick_back_pulse_right, jumping_jacks]

sets = {
    'full_body_day_starter': [good_morning_stretch, jumping_jacks, squats,
                              bird_dog,
                              box_push_ups, glute_kick_back,
                              glute_kick_back_pulse_left,
                              glute_kick_back_pulse_right, superman,
                              side_lunges_left_leg,
                              side_lunges_right_leg, side_bends],
    'lower_back_work': [press_up_back, hip_stretch_left_leg,
                        hip_stretch_right_leg,
                        right_leg_elevation, left_leg_elevation,
                        leg_drops, leg_raise,
                        dead_bug, cobra_stretch],
    'core_work': [crunch_kicks, bicycle_crunches, diagonal_plank,
                  military_push_ups, donkey_kicks,
                  donkey_kicks_pulse_right, donkey_kicks_pulse_left,
                  bird_dog, superman, side_bends, jumping_jacks],
    'leg_work': [lunges_right_leg, lunges_left_leg, squats,
                 side_lunges_right_leg, side_lunges_left_leg,
                 pile_squats, glute_kick_back, glute_kick_back_pulse_left,
                 glute_kick_back_pulse_right, jumping_jacks]
}
