import conditions
from exercise import Exercise
from utils import Utils

crunches = Exercise("Crunches",
                    Utils.current_dir + "\\resources\\gifs\\crunches.gif",
                    Utils.current_dir + "\\resources\\starting_postures\\crunches.png",
                    True, False, 10, 90, None, conditions.crunches)
pile_squats = Exercise("Pile squats",
                       Utils.current_dir + "\\resources\\gifs\\pile_squats.gif",
                       Utils.current_dir + "\\resources\\starting_postures\\pile_squats.png",
                       False, True, 10, 60, None, conditions.pile_squats)
lunges_right_leg = Exercise("Lunges right leg",
                            Utils.current_dir + "\\resources\\gifs\\lunges_right.gif",
                            Utils.current_dir + "\\resources\\starting_postures\\lunges_right.png",
                            True, True, 5, 60, None, conditions.lunges_right_leg)
lunges_left_leg = Exercise("Lunges left leg",
                           Utils.current_dir + "\\resources\\gifs\\lunges_left.gif",
                           Utils.current_dir + "\\resources\\starting_postures\\lunges_left.png",
                           True, True, 5, 60, None, conditions.lunges_left_leg)
side_lunges_right_leg = Exercise("Side lunges right leg",
                                 Utils.current_dir + "\\resources\\gifs\\side_lunges_right.gif",
                                 Utils.current_dir + "\\resources\\starting_postures\\side_lunges_right.png",
                                 False, True, 5, 60, None, conditions.side_lunges_right_leg)
side_lunges_left_leg = Exercise("Side lunges left leg",
                                Utils.current_dir + "\\resources\\gifs\\side_lunges_left.gif",
                                Utils.current_dir + "\\resources\\starting_postures\\side_lunges_left.png",
                                False, True, 5, 60, None, conditions.side_lunges_left_leg)
squats = Exercise("Squats",
                  Utils.current_dir + "\\resources\\gifs\\squats.gif",
                  Utils.current_dir + "\\resources\\starting_postures\\squats.png",
                  True, True, 10, 90, None, conditions.squats)
hip_stretch_left_leg = Exercise("Hip stretch left leg",
                                Utils.current_dir + "\\resources\\gifs\\hip_stretch_left.gif",
                                Utils.current_dir + "\\resources\\starting_postures\\hip_stretch_left.png",
                                True, True, 5, 60, None, conditions.hip_stretch_left_leg)
hip_stretch_right_leg = Exercise("Hip stretch right leg",
                                 Utils.current_dir + "\\resources\\gifs\\hip_stretch_right.gif",
                                 Utils.current_dir + "\\resources\\starting_postures\\hip_stretch_right.png",
                                 True, True, 5, 60, None, conditions.hip_stretch_right_leg)
good_morning_stretch = Exercise("Good morning stretch",
                                Utils.current_dir + "\\resources\\gifs\\good_morning.gif",
                                Utils.current_dir + "\\resources\\starting_postures\\good_morning.png",
                                True, True, 5, 45, None, conditions.good_morning_stretch)
press_up_back = Exercise("Press up back",
                         Utils.current_dir + "\\resources\\gifs\\press_up_back.gif",
                         Utils.current_dir + "\\resources\\starting_postures\\press_up_back.png",
                         True, True, 5, 60, None, conditions.press_up_back)
left_leg_elevation = Exercise("Left leg elevation",
                              Utils.current_dir + "\\resources\\gifs\\leg_elevation_left.gif",
                              Utils.current_dir + "\\resources\\starting_postures\\leg_elevation_left.png",
                              True, True, 5, 60, None, conditions.left_leg_elevation)
right_leg_elevation = Exercise("Right leg elevation",
                               Utils.current_dir + "\\resources\\gifs\\leg_elevation_right.gif",
                               Utils.current_dir + "\\resources\\starting_postures\\leg_elevation_right.png",
                               True, True, 5, 60, None, conditions.right_leg_elevation)
box_push_ups = Exercise("Box push ups",
                        Utils.current_dir + "\\resources\\gifs\\box_pushups.gif",
                        Utils.current_dir + "\\resources\\starting_postures\\bird_dog-box_push_ups-glute_kick.png",
                        True, False, 5, 60, None, conditions.box_push_ups)
cobra_stretch = Exercise("Cobra stretch",
                         Utils.current_dir + "\\resources\\gifs\\cobra_stretch.gif",
                         Utils.current_dir + "\\resources\\starting_postures\\cobra_stretch.png",
                         True, False, 5, 60, None, conditions.cobra_stretch)
crunch_kicks = Exercise("Crunch kicks",
                        Utils.current_dir + "\\resources\\gifs\\crunch_kicks.gif",
                        Utils.current_dir + "\\resources\\starting_postures\\crunch_kicks.png",
                        True, False, 5, 60, None, conditions.crunch_kicks)
leg_drops = Exercise("Leg drops",
                     Utils.current_dir + "\\resources\\gifs\\leg_drops.gif",
                     Utils.current_dir + "\\resources\\starting_postures\\leg_raise.png",
                     True, False, 5, 60, None, conditions.leg_drops)
military_push_ups = Exercise("Military push ups",
                             Utils.current_dir + "\\resources\\gifs\\military_push_ups.gif",
                             Utils.current_dir + "\\resources\\starting_postures\\military_push_ups.png",
                             True, False, 5, 60, None, conditions.military_push_ups)
superman = Exercise("Superman",
                    Utils.current_dir + "\\resources\\gifs\\superman.gif",
                    Utils.current_dir + "\\resources\\starting_postures\\superman.png",
                    True, False, 5, 60, None, conditions.superman)
side_bends = Exercise("Side bends",
                      Utils.current_dir + "\\resources\\gifs\\side_bends.gif",
                      Utils.current_dir + "\\resources\\starting_postures\\side_bends.png",
                      False, True, 5, 60, None, conditions.side_bends)
donkey_kicks = Exercise("Donkey kicks",
                        Utils.current_dir + "\\resources\\gifs\\donkey_kicks.gif",
                        Utils.current_dir + "\\resources\\starting_postures\\donkey_kicks.png",
                        True, False, 5, 60, None, conditions.donkey_kicks)
glute_kick_back = Exercise("Glute kick back",
                           Utils.current_dir + "\\resources\\gifs\\glute_kick_back.gif",
                           Utils.current_dir + "\\resources\\starting_postures\\bird_dog-box_push_ups-glute_kick.png",
                           True, False, 5, 60, None, conditions.glute_kick_back)
bicycle_crunches = Exercise("Bicycle crunches",
                            Utils.current_dir + "\\resources\\gifs\\bicycle_crunches.gif",
                            Utils.current_dir + "\\resources\\starting_postures\\bicycle_crunches.png",
                            True, False, 5, 60, None, conditions.bicycle_crunches)
bird_dog = Exercise("Bird dog",
                    Utils.current_dir + "\\resources\\gifs\\bird_dog.gif",
                    Utils.current_dir + "\\resources\\starting_postures\\bird_dog-box_push_ups-glute_kick.png",
                    True, False, 5, 60, None, conditions.bird_dog)
dead_bug = Exercise("Dead bug",
                    Utils.current_dir + "\\resources\\gifs\\dead_bug.gif",
                    Utils.current_dir + "\\resources\\starting_postures\\dead_bug.png",
                    True, False, 5, 60, None, conditions.dead_bug)
diagonal_plank = Exercise("Diagonal plank", Utils.current_dir + "\\resources\\gifs\\diagonal_plank.gif",
                          Utils.current_dir + "\\resources\\starting_postures\\military_push_ups.png",
                          True, False, 5, 60, None, conditions.diagonal_plank)
leg_raise = Exercise("Leg raise",
                     Utils.current_dir + "\\resources\\gifs\\leg_raise.gif",
                     Utils.current_dir + "\\resources\\starting_postures\\leg_raise.png",
                     True, False, 5, 60, None, conditions.leg_raise)
donkey_kicks_pulse_left = Exercise("Donkey kicks pulse left",
                                   Utils.current_dir + "\\resources\\gifs\\donkey_kicks_pulse_left.gif",
                                   Utils.current_dir + "\\resources\\starting_postures\\donkey_kicks.png",
                                   True, False, 5, 60, None, conditions.donkey_kicks_pulse_left)
donkey_kicks_pulse_right = Exercise("Donkey kicks pulse right",
                                    Utils.current_dir + "\\resources\\gifs\\donkey_kicks_pulse_right.gif",
                                    Utils.current_dir + "\\resources\\starting_postures\\donkey_kicks_right.png",
                                    True, False, 5, 60, None, conditions.donkey_kicks_pulse_right)
glute_kick_back_pulse_left = Exercise("Glute kick back pulse left",
                                      Utils.current_dir + "\\resources\\gifs\\glute_kickback_pulse_left.gif",
                                      Utils.current_dir + "\\resources\\starting_postures\\glute_pulse_left.png",
                                      True, False, 5, 60, None, conditions.glute_kick_back_pulse_left)
glute_kick_back_pulse_right = Exercise("Glute kick back pulse right",
                                       Utils.current_dir + "\\resources\\gifs\\glute_kickback_pulse_right.gif",
                                       Utils.current_dir + "\\resources\\starting_postures\\glute_pulse_right.png",
                                       True, False, 5, 60, None, conditions.glute_kick_back_pulse_right)
jumping_jacks = Exercise("Jumping jacks", Utils.current_dir + "\\resources\\gifs\\jumping_jacks.gif",
                         Utils.current_dir + "\\resources\\starting_postures\\jumping_jacks.png",
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
