jaco_12 = [[-3.0191952827344787756, 2.0265415172157690932, 1.5350486992553454052, -2.1626194932343251791,
            -1.6387961597291277023, -3.0373170323363411905],
           [-2.8011342510990861938, 1.0419515380876648981, 1.6064640851831037555, 2.1825494141309144843,
            1.6363010904182574174, -0.051654111981807494544],
           [-2.4105613886595918514, 2.2701471862691480023, 1.1412365781468318664, 2.1127067792830139632,
            0.54074835441896843499, 2.1402500363454277108],
           [-2.2615404930394393604, 1.2092847417120512539, 2.0135536082150091136, -2.0545215101972614223,
            -2.0973276214580268327, 2.0153291069762690371],
           [-0.57792475574779925856, 1.2985317175103635476, 2.0000437963702875696, -0.88715246468441683639,
            2.1861317755538069622, 1.0513949106296589345],
           [-0.36569715674971116036, 2.3609329955345435962, 1.1796536018712167780, 0.72922275321998617329,
            -0.13334576430663003518, 0.79814158045260024825],
           [0, 2.1988160000000000928, 1.4647469999999998018,
            -0.49560030717958572452, 1.2834440000000000499, 0],
           [0.52356209993557222184, 1.0062743672613490190, 1.6842406052754134779, 0.43455737082592245790,
            -1.2544557857657716612, -3.0973289743789071578],
           [0.89367960179005738168, 0.83936943469765905322, 1.9362875641088886130, -0.63336931642593451130,
            -0.059578476562609662344, 2.5252292273018345856],
           [1.1252796748648838007, 1.8562040537860180602, 1.1622372631795855510, 0.79841338654100805323,
            -2.2530518923812322465, 2.2927848678423235002],
           [2.8322971945177137828, 1.9120864634057881469, 1.1188535351717668940, 2.0103695453107854957,
            1.9849735789052799717, 1.2958356974253442763],
           [2.9696536705636929376, 0.82629307176591709396, 2.0095377790434480553, -2.0728098536718961543,
            -0.68447046273614209025, 1.1371871228635316303]]

point1_comp = [-3.1201, 0.7082, 1.4904, 2.62, -1.9637, -1.8817]
point2_comp = [3.0675, 1.0545, 1.3090, 2.4283, -1.2305, -2.3002]
point3_comp = [2.9132, 0.2824, 1.9297, -2.1648, -2.9685, -2.7165]
point4_comp = [2.5338, 1.2022, 1.1149, 1.5839, 0.6030, 2.6322]
point5_comp = [2.4730, 0.0943, 2.0281, -1.4916, -2.4244, 2.4362]
point6_comp = [2.4335, 0.0936, 1.5741, 1.4311, 2.3452, 0.5391]
point7_comp = [-0.8579, 3.0408, 1.5721, -1.5912, 2.1625, 0.5390]
point8_comp = [-0.8046, 3.0466, 1.1135, 1.5103, -2.2697, 2.4394]
point9_comp = [-0.7501, 1.9399, 2.0268, -1.4270, 0.6212, 2.6291]
point10_comp = [-0.2812, 2.0346, 1.8631, -0.5833, -1.0917, -2.4130]
point11_comp = [-0.2456, 2.8156, 1.3090, 0.4882, -2.8301, -2.3003]
point12_comp = [-0.1583, 2.7025, 1.4699, -0.0656, -2.5402, -1.9078]


class CheckRobot(ThreeDScene):
    config.background_color = WHITE

    def construct(self):
        config.background_color = WHITE
        theta_list = [0, PI / 3, 0, 0, 0, 0]
        d_list = [210.2, -50, -62, -249.3, -84.6, -227.3]
        a_list = [0, 410, 0, 0, 0, 0]
        alpha_list = [PI / 2, PI, PI / 2, deg2rad(55), deg2rad(55), 0]
        d_list = [number / 100 for number in d_list]
        a_list = [number / 100 for number in a_list]

        self.camera.scale(1.5)
        self.camera.set_euler_angles(theta=-180 * DEGREES, phi=80 * DEGREES)

        rob_ins1 = get_RobotInstance(d_list, jaco_12[2], a_list, alpha_list, opacity=1, show_frame=True,
                                     adjust_frame=True)
        rob_ins2 = get_RobotInstance(d_list, jaco_12[5], a_list, alpha_list, opacity=1, show_frame=False)
        rob_ins3 = get_RobotInstance(d_list, jaco_12[8], a_list, alpha_list, opacity=1, show_frame=False)
        rob_ins4 = get_RobotInstance(d_list, jaco_12[11], a_list, alpha_list, opacity=1, show_frame=False)
        self.add(rob_ins1, rob_ins2, rob_ins3, rob_ins4)


class AnimateRobot2(ThreeDScene):
    def construct(self):
        d_list = [210.2, -50, -62, -249.3, -84.6, -227.3]
        a_list = [0, 410, 0, 0, 0, 0]
        alpha_list = [PI / 2, PI, PI / 2, deg2rad(55), deg2rad(55), 0]
        d_list = [number / 100 for number in d_list]
        a_list = [number / 100 for number in a_list]
        theta_list = adapt_2Pi(point1_comp)
        # theta_list_inter1 = adapt_2Pi([-0.85, 2.71573821e-02, 6.81434159e-02, 8.35356126e-01, 4.31228851e-04,
        # 2.46]) theta_list_inter2 = adapt_2Pi([-0.85, -1.47772586e+00, 1.19056044e+00, -1.47537815e+00,
        # -2.69837580e+00, 2.46])
        theta_list2 = adapt_2Pi(point5_comp)

        each_iteration = 50
        total_iterations = 100
        offset = -2
        # key_points = [theta_list, theta_list_inter1, theta_list_inter2, theta_list2]
        key_points = [theta_list, theta_list2]

        # theta_list = [0, PI / 2, -PI / 3, PI, 0, 0]
        if key_points is None or len(key_points) < 2:
            raise ValueError("The key points are either empty or only 1 configuration is mentioned\n"
                             "Please mention least 2 arrays of length 6 that will act as the start and end point"
                             "of the trajectory to plot")

        if len(key_points) == 2:
            intermediate_theta = get_interpolation_vector(key_points[0], key_points[1],
                                                          total_iterations=total_iterations,
                                                          each_iteration=each_iteration)
        else:
            via_points = []
            for vi in range(1, len(key_points) - 1):
                via_points.append(key_points[vi])
            intermediate_theta = get_interpolation_vector(key_points[0], key_points[-1],
                                                          via_points=via_points, total_iterations=total_iterations)

        ee_point_vec = []
        ee_trace = Group()

        self.camera.scale(1.5)
        self.camera.set_euler_angles(theta=120 * DEGREES, phi=80 * DEGREES)

        rob_ins = get_RobotInstance(d_list, key_points[0], a_list, alpha_list, offset=offset)
        ee_point, ee_R = get_FrameMatrix(d_list, key_points[0], a_list, alpha_list, 6, offset=offset)
        ee_point_vec.append(ee_point)

        self.add(rob_ins)
        self.add(get_RobotInstance(d_list, key_points[0], a_list, alpha_list, offset=offset,
                                   opacity=1))
        for anim_iter in range(1, len(intermediate_theta)):
            ee_point, ee_R = get_FrameMatrix(d_list, intermediate_theta[anim_iter], a_list, alpha_list,
                                             6, offset=offset)
            ee_point_vec.append(ee_point)
            ee_trace.add(Line3D(start=ee_point_vec[-2], end=ee_point, color=WHITE, thickness=0.05, fill_opacity=1))

            self.play(Transform(rob_ins, get_RobotInstance(d_list, intermediate_theta[anim_iter], a_list,
                                                           alpha_list, offset=offset)),
                      run_time=0.05)
            self.add(ee_trace)
            if np.mod(anim_iter, 100 / 2) == 0:
                ghost_instance = get_RobotInstance(d_list, intermediate_theta[anim_iter], a_list,
                                                   alpha_list, offset=offset, opacity=0.25, show_frame=True)
                self.add(ghost_instance)

        self.wait()
        self.play(self.camera.animate.set_euler_angles(theta=360 * DEGREES, phi=90 * DEGREES), run_time=5)
        self.wait()


class FirstLast(ThreeDScene):
    config.background_color = WHITE

    def construct(self):
        theta_list = [0, PI / 3, 0, 0, 0, 0]
        d_list = [210.2, -50, -62, -249.3, -84.6, -227.3]
        a_list = [0, 410, 0, 0, 0, 0]
        alpha_list = [PI / 2, PI, PI / 2, deg2rad(55), deg2rad(55), 0]
        d_list = [number / 100 for number in d_list]
        a_list = [number / 100 for number in a_list]

        self.camera.scale(1.5)
        self.camera.set_euler_angles(theta=105 * DEGREES, phi=80 * DEGREES)

        rob_ins1 = get_RobotInstance(d_list, point1_comp, a_list, alpha_list, opacity=1, show_frame=True,
                                     adjust_frame=True)
        rob_ins2 = get_RobotInstance(d_list, point5_comp, a_list, alpha_list, opacity=1, show_frame=False)
        self.add(rob_ins1, rob_ins2)


class Nspc(ThreeDScene):
    def construct(self):
        d_list = [210.2, -50, -62, -249.3, -84.6, -227.3]
        a_list = [0, 410, 0, 0, 0, 0]
        alpha_list = [PI / 2, PI, PI / 2, deg2rad(55), deg2rad(55), 0]
        d_list = [number / 100 for number in d_list]
        a_list = [number / 100 for number in a_list]
        theta_list = adapt_2Pi(point1_comp)
        # theta_list_inter1 = adapt_2Pi([-0.85, 2.71573821e-02, 6.81434159e-02, 8.35356126e-01, 4.31228851e-04,
        # 2.46]) theta_list_inter2 = adapt_2Pi([-0.85, -1.47772586e+00, 1.19056044e+00, -1.47537815e+00,
        # -2.69837580e+00, 2.46])
        theta_list2 = adapt_2Pi(point5_comp)

        each_iteration = 50
        total_iterations = 200
        offset = -2
        # key_points = [theta_list, theta_list_inter1, theta_list_inter2, theta_list2]
        key_points = [theta_list, theta_list2]

        # theta_list = [0, PI / 2, -PI / 3, PI, 0, 0]
        if key_points is None or len(key_points) < 2:
            raise ValueError("The key points are either empty or only 1 configuration is mentioned\n"
                             "Please mention least 2 arrays of length 6 that will act as the start and end point"
                             "of the trajectory to plot")

        if len(key_points) == 2:
            intermediate_theta = get_interpolation_vector(key_points[0], key_points[1],
                                                          total_iterations=total_iterations,
                                                          each_iteration=each_iteration)
        else:
            via_points = []
            for vi in range(1, len(key_points) - 1):
                via_points.append(key_points[vi])
            intermediate_theta = get_interpolation_vector(key_points[0], key_points[-1],
                                                          via_points=via_points, total_iterations=total_iterations)

        ee_point_vec = []
        ee_trace = Group()

        self.camera.scale(1.5)
        self.camera.set_euler_angles(theta=105 * DEGREES, phi=80 * DEGREES)

        rob_ins = get_RobotInstance(d_list, key_points[0], a_list, alpha_list, offset=offset, opacity=0.8)
        ee_point, ee_R = get_FrameMatrix(d_list, key_points[0], a_list, alpha_list, 6, offset=offset)
        ee_point_vec.append(ee_point)

        # self.add(rob_ins)
        # self.add(get_RobotInstance(d_list, key_points[0], a_list, alpha_list, offset=offset,
                                   # opacity=0.4))
        instance_des = 50
        self.add(get_RobotInstance(d_list, intermediate_theta[instance_des], a_list, alpha_list, offset=offset))
        # self.add(get_RobotInstance(d_list, key_points[1], a_list, alpha_list, offset=offset, opacity=1))

        for anim_iter in range(1, min(instance_des, len(intermediate_theta))):
            ee_point, ee_R = get_FrameMatrix(d_list, intermediate_theta[anim_iter], a_list, alpha_list,
                                             6, offset=offset)
            ee_point_vec.append(ee_point)
            ee_trace.add(Line3D(start=ee_point_vec[-2], end=ee_point, color=BLACK, thickness=0.05, fill_opacity=1))
            self.add(ee_trace)
            if np.mod(anim_iter, 100 / 0.2) == 0:
                ghost_instance = get_RobotInstance(d_list, intermediate_theta[anim_iter], a_list,
                                                   alpha_list, offset=offset, opacity=0.25, show_frame=True)
                self.add(ghost_instance)
