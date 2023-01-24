import math
import numpy.linalg as la
from manim import *
from robot_functions import *
from icra_supplementary import *
from master_thesis_functions import *
from maple_functions import *
from icra_functions import *
import pandas as pd


class AnimateRobot(ThreeDScene):
    def construct(self):

        # JACO
        d1s = 212
        d3s = -12
        d4s = -249.3
        d5s = -84.6
        d6s = -222.73
        a2s = 410

        # DH parameters of CRX-10ia/L robot are:
        d_list = [d1s, 50, 50 + d3s, d4s, d5s, d6s]
        a_list = [0, a2s, 0, 0, 0, 0]
        alpha_list = [PI / 2, PI, PI / 2, np.deg2rad(55), np.deg2rad(55), PI]
        d_list = [number / 100 for number in d_list]
        a_list = [number / 100 for number in a_list]
        point1_comp = [-3.1201, 0.7082, 1.4904, 2.62, -1.9637, -1.8817]
        point5_comp = [2.4730, 0.0943, 2.0281, -1.4916, -2.4244, 2.4362]

        theta_list = adapt_2Pi(point1_comp)
        theta_list2 = adapt_2Pi(point5_comp)

        each_iteration = 50
        total_iterations = 50
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
        self.camera.set_euler_angles(theta=120 * DEGREES, phi=90 * DEGREES)

        rob_ins = get_RobotInstance(d_list, key_points[0], a_list, alpha_list, offset=offset)
        ee_point, ee_R = get_FrameMatrix(d_list, key_points[0], a_list, alpha_list, 6, offset=offset)
        ee_point_vec.append(ee_point)

        # self.add(rob_ins)
        self.add(get_RobotInstance(d_list, key_points[0], a_list, alpha_list, offset=offset,
                                   opacity=0.25, show_frame=True))
        for anim_iter in range(1, len(intermediate_theta)):
            ee_point, ee_R = get_FrameMatrix(d_list, intermediate_theta[anim_iter], a_list, alpha_list,
                                             6, offset=offset)
            ee_point_vec.append(ee_point)
            ee_trace.add(
                Line3D(start=ee_point_vec[-2], end=ee_point_vec[-1], color=WHITE, thickness=0.05, fill_opacity=1))

            self.play(Transform(rob_ins, get_RobotInstance(d_list, intermediate_theta[anim_iter], a_list,
                                                           alpha_list, offset=offset, show_frame=True)), run_time=0.05)
            self.add(ee_trace)

        self.wait()
        self.play(self.camera.animate.set_euler_angles(theta=360 * DEGREES, phi=90 * DEGREES), run_time=5)
        self.wait()


class AnimateRegular3(ThreeDScene):
    def construct(self):

        # JACO
        d1s = 212
        d3s = -12
        d4s = -249.3
        d5s = -84.6
        d6s = -222.73
        a2s = 410

        # DH parameters of CRX-10ia/L robot are:
        d_list = [d1s, 50, 50 + d3s, d4s, d5s, d6s]
        a_list = [0, a2s, 0, 0, 0, 0]
        alpha_list = [PI / 2, PI, PI / 2, np.deg2rad(55), np.deg2rad(55), PI]
        d_list = [number / 100 for number in d_list]
        a_list = [number / 100 for number in a_list]

        df_n = pd.read_csv("D:\durghy_manim\Jaco\saved_data_theta1.csv")
        paths = make_paths(df_n, thresh=0.1)

        offset = -2
        ee_point_vec = []
        ee_trace = Group()

        self.camera.scale(1.5)
        self.camera.set_euler_angles(theta=120 * DEGREES, phi=90 * DEGREES)

        first_set = np.array(get_solution(1, paths[1][1], 1))
        rob_ins = get_RobotInstance(d_list, first_set, a_list, alpha_list, offset=offset)
        ee_point, ee_R = get_FrameMatrix(d_list, first_set, a_list, alpha_list, 6, offset=offset)
        ee_point_vec.append(ee_point)

        self.add(rob_ins)
        self.add(get_RobotInstance(d_list, first_set, a_list, alpha_list, offset=offset,
                                   opacity=0.25, show_frame=True))
        for anim_iter in range(1, len(paths[1]), 8):
            inter_set = np.array(get_solution(anim_iter, paths[1][anim_iter], 1))
            ee_point, ee_R = get_FrameMatrix(d_list, inter_set, a_list, alpha_list, 6, offset=offset)
            ee_point_vec.append(ee_point)
            ee_trace.add(Dot().move_to(ee_point_vec[-1]))
            # ee_trace.add(
            #     Line3D(start=ee_point_vec[-2], end=ee_point_vec[-1], color=WHITE, thickness=0.05, fill_opacity=1))

        self.add(ee_trace)

        for anim_iter in range(1, len(paths[1]), 8):
            inter_set = np.array(get_solution(anim_iter, paths[1][anim_iter], 1))
            self.play(Transform(rob_ins, get_RobotInstance(d_list, inter_set, a_list,
                                                           alpha_list, offset=offset, show_frame=True)), run_time=0.05)


class AnimateError(ThreeDScene):
    def construct(self):

        # JACO
        d1s = 212
        d3s = -12
        d4s = -249.3
        d5s = -84.6
        d6s = -222.73
        a2s = 410

        # DH parameters of CRX-10ia/L robot are:
        d_list = [d1s, 50, 50 + d3s, d4s, d5s, d6s]
        a_list = [0, a2s, 0, 0, 0, 0]
        alpha_list = [PI / 2, PI, PI / 2, np.deg2rad(55), np.deg2rad(55), PI]
        d_list = [number / 100 for number in d_list]
        a_list = [number / 100 for number in a_list]

        df_n = pd.read_csv("D:\durghy_manim\Jaco\saved_data_theta1.csv")
        paths = make_paths(df_n, thresh=0.1)
        point1_comp = np.array(get_solution(len(paths[2]) - 1, paths[2][len(paths[2]) - 1], 1))
        point5_comp = np.array(get_solution(len(paths[2]) - 1, paths[3][len(paths[2]) - 1], 1))
        start_point = np.array(get_solution(1, paths[2][1], 1))
        theta_list = adapt_2Pi(point1_comp)
        theta_list2 = adapt_2Pi(point5_comp)

        each_iteration = 10
        total_iterations = 10
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
        self.camera.set_euler_angles(theta=120 * DEGREES, phi=90 * DEGREES)

        rob_ins = get_RobotInstance(d_list, key_points[0], a_list, alpha_list, offset=offset, link_color=RED,
                                    joint_color=RED)
        ee_point, ee_R = get_FrameMatrix(d_list, key_points[0], a_list, alpha_list, 6, offset=offset)
        ee_point_vec.append(ee_point)

        self.add(rob_ins)
        self.add(
            get_RobotInstance(d_list, start_point, a_list, alpha_list, offset=offset, opacity=0.25, show_frame=True))

        fee_point_vec = []
        full_ee_trace = Group()
        for anim_iter in range(1, len(paths[1]), 8):
            inter_set = np.array(get_solution(anim_iter, paths[1][anim_iter], 1))
            fee_point, fee_R = get_FrameMatrix(d_list, inter_set, a_list, alpha_list, 6, offset=offset)
            fee_point_vec.append(fee_point)
            full_ee_trace.add(Dot().move_to(fee_point_vec[-1]))
            # ee_trace.add(
            #     Line3D(start=ee_point_vec[-2], end=ee_point_vec[-1], color=WHITE, thickness=0.05, fill_opacity=1))

        self.add(full_ee_trace)

        for anim_iter in range(1, len(intermediate_theta)):
            ee_point, ee_R = get_FrameMatrix(d_list, intermediate_theta[anim_iter], a_list, alpha_list,
                                             6, offset=offset)
            ee_point_vec.append(ee_point)
            ee_trace.add(
                Line3D(start=ee_point_vec[-2], end=ee_point_vec[-1], color=WHITE, thickness=0.05, fill_opacity=1))

            self.play(Transform(rob_ins, get_RobotInstance(d_list, intermediate_theta[anim_iter], a_list,
                                                           alpha_list, offset=offset, show_frame=True, link_color=RED,
                                                           joint_color=RED)), run_time=0.05)
            self.add(ee_trace)
        self.wait(2)


class AnimateNSCS(ThreeDScene):
    def construct(self):

        # JACO
        d1s = 212
        d3s = -12
        d4s = -249.3
        d5s = -84.6
        d6s = -222.73
        a2s = 410

        # DH parameters of CRX-10ia/L robot are:
        d_list = [d1s, 50, 50 + d3s, d4s, d5s, d6s]
        a_list = [0, a2s, 0, 0, 0, 0]
        alpha_list = [PI / 2, PI, PI / 2, np.deg2rad(55), np.deg2rad(55), PI]
        d_list = [number / 100 for number in d_list]
        a_list = [number / 100 for number in a_list]

        df_n = pd.read_csv("D:\durghy_manim\Jaco\saved_data_neg_theta1.csv")
        paths2 = make_paths(df_n, thresh=0.1)

        offset = -2
        ee_point_vec = []
        ee_trace = Group()

        self.camera.scale(1.5)
        self.camera.set_euler_angles(theta=120 * DEGREES, phi=90 * DEGREES)

        first_set = np.array(get_solution(1, paths2[1][1], -1))
        rob_ins = get_RobotInstance(d_list, first_set, a_list, alpha_list, offset=offset)
        ee_point, ee_R = get_FrameMatrix(d_list, first_set, a_list, alpha_list, 6, offset=offset)
        ee_point_vec.append(ee_point)

        self.add(rob_ins)
        self.add(get_RobotInstance(d_list, first_set, a_list, alpha_list, offset=offset,
                                   opacity=0.25, show_frame=True))
        for anim_iter in range(1, len(paths2[1]), 8):
            inter_set = np.array(get_solution(anim_iter, paths2[1][anim_iter], -1))
            ee_point, ee_R = get_FrameMatrix(d_list, inter_set, a_list, alpha_list, 6, offset=offset)
            ee_point_vec.append(ee_point)
            ee_trace.add(Dot().move_to(ee_point_vec[-1]))
            # ee_trace.add(
            #     Line3D(start=ee_point_vec[-2], end=ee_point_vec[-1], color=WHITE, thickness=0.05, fill_opacity=1))

        self.add(ee_trace)

        for anim_iter in range(1, len(paths2[1]), 8):
            inter_set = np.array(get_solution(anim_iter, paths2[1][anim_iter], -1))
            self.play(Transform(rob_ins, get_RobotInstance(d_list, inter_set, a_list,
                                                           alpha_list, offset=offset, show_frame=True)), run_time=0.05)


class AnimateErrorB(ThreeDScene):
    def construct(self):

        # JACO
        d1s = 212
        d3s = -12
        d4s = -249.3
        d5s = -84.6
        d6s = -222.73
        a2s = 410

        # DH parameters of CRX-10ia/L robot are:
        d_list = [d1s, 50, 50 + d3s, d4s, d5s, d6s]
        a_list = [0, a2s, 0, 0, 0, 0]
        alpha_list = [PI / 2, PI, PI / 2, np.deg2rad(55), np.deg2rad(55), PI]
        d_list = [number / 100 for number in d_list]
        a_list = [number / 100 for number in a_list]

        df_n = pd.read_csv("D:\durghy_manim\Jaco\saved_data_neg_theta1.csv")
        paths2 = make_paths(df_n, thresh=0.1)

        offset = -2
        ee_point_vec = []
        ee_trace = Group()

        self.camera.scale(1.5)
        self.camera.set_euler_angles(theta=120 * DEGREES, phi=90 * DEGREES)

        first_set = np.array(get_solution(1, paths2[2][1], 1))
        rob_ins = get_RobotInstance(d_list, first_set, a_list, alpha_list, offset=offset)
        ee_point, ee_R = get_FrameMatrix(d_list, first_set, a_list, alpha_list, 6, offset=offset)
        ee_point_vec.append(ee_point)

        self.add(rob_ins)
        self.add(get_RobotInstance(d_list, first_set, a_list, alpha_list, offset=offset,
                                   opacity=0.25, show_frame=True))
        for anim_iter in range(1, len(paths2[1]), 8):
            inter_set = np.array(get_solution(anim_iter, paths2[1][anim_iter], 1))
            ee_point, ee_R = get_FrameMatrix(d_list, inter_set, a_list, alpha_list, 6, offset=offset)
            ee_point_vec.append(ee_point)
            ee_trace.add(Dot().move_to(ee_point_vec[-1]))
            # ee_trace.add(
            #     Line3D(start=ee_point_vec[-2], end=ee_point_vec[-1], color=WHITE, thickness=0.05, fill_opacity=1))

        self.add(ee_trace)

        for anim_iter in range(1, len(paths2[2]), 2):
            inter_set = np.array(get_solution(anim_iter, paths2[2][anim_iter], 1))
            self.play(Transform(rob_ins, get_RobotInstance(d_list, inter_set, a_list,
                                                           alpha_list, offset=offset, show_frame=True)), run_time=0.05)


class AnimateRobot_Gen3(ThreeDScene):
    def construct(self):

        # JACO
        d1s = 243.3
        d3s = -10
        d4s = 245
        d5s = 57
        d6s = 235
        a2s = 280

        # DH parameters of CRX-10ia/L robot are:
        d_list = [d1s, 50, 50 + d3s, d4s, d5s, d6s]
        a_list = [0, a2s, 0, 0, 0, 0]
        alpha_list = [PI / 2, PI, PI / 2, PI / 2, PI / 2, 0]
        d_list = [number / 100 for number in d_list]
        a_list = [number / 100 for number in a_list]

        complete_Gen3 = [
            [-3.0957214639684576374, 0.73659696691185828074, 1.9391099341028583335, 0.070313846112917641969,
             2.0680884076334382010, 0.0065825947502313444317],
            [-3.0956496787383107800, 0.37791329895568898075, 1.1717906904378385883, 0.061979478014806370961,
             1.6603223840801924586, 0.034666529187635168232],
            [-0.25239826198661576460, 2.7662127592910404277, 1.8934646524550722466, 0.28889906853108808143,
             -1.6989629482654834792, 2.9441319521777652317],
            [-0.25064381059515068042, 2.4025837526096178103, 1.1046615048332583192, 0.33295035303083506793,
             -2.1048828746225802082, 2.8090757400829476652],
            [-0.00014593249696239682335, 2.4292072578424904390, 1.2575703506167638962, -3.0333467365363221843,
             2.0335300516176949130, -0.038229883548617964316],
            [0, 2.7447370124781413207, 1.9315400265882999568, -3.0443300004005360668, 1.6769479859597166483, 0],
            [2.9336210536897171368, 0.39427994740575947708, 1.2867515912465796900, -2.8848880611194523530,
             -1.7272006044926790768, 2.9721466496382713029],
            [2.9348478476558204318, 0.71526543800550275669, 1.9822544364234219116, -2.8498950327084032609,
             -2.0883784091406518551, 2.8663726830333717845]]

        point1_comp = [-3.1201, 0.7082, 1.4904, 2.62, -1.9637, -1.8817]
        point5_comp = [2.4730, 0.0943, 2.0281, -1.4916, -2.4244, 2.4362]

        theta_list = adapt_2Pi(complete_Gen3[0])
        theta_list2 = adapt_2Pi(complete_Gen3[2])
        theta_list_inter1 = [(complete_Gen3[0][0] + complete_Gen3[2][0]) / 2, -0.05595581, 0.85521189, 1.0820465,
                             0.46155794, (complete_Gen3[0][5] + complete_Gen3[2][5]) / 2]

        each_iteration = 50
        total_iterations = 100
        offset = -2
        key_points = [theta_list, theta_list_inter1, theta_list2]
        # key_points = [theta_list, theta_list2]

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
        self.camera.set_euler_angles(theta=-112 * DEGREES, phi=90 * DEGREES)

        rob_ins = get_RobotInstance(d_list, key_points[0], a_list, alpha_list, offset=offset)
        ee_point, ee_R = get_FrameMatrix(d_list, key_points[0], a_list, alpha_list, 6, offset=offset)
        ee_point_vec.append(ee_point)

        self.add(rob_ins)
        self.add(get_RobotInstance(d_list, key_points[0], a_list, alpha_list, offset=offset,
                                   opacity=0.25, show_frame=True))
        for anim_iter in range(1, len(intermediate_theta)):
            ee_point, ee_R = get_FrameMatrix(d_list, intermediate_theta[anim_iter], a_list, alpha_list,
                                             6, offset=offset)
            ee_point_vec.append(ee_point)
            ee_trace.add(
                Line3D(start=ee_point_vec[-2], end=ee_point_vec[-1], color=WHITE, thickness=0.05, fill_opacity=1))

            self.play(Transform(rob_ins, get_RobotInstance(d_list, intermediate_theta[anim_iter], a_list,
                                                           alpha_list, offset=offset, show_frame=True)), run_time=0.05)
            self.add(ee_trace)

        self.wait(2)
        self.play(self.camera.animate.set_euler_angles(theta=(-112 + 180) * DEGREES, phi=90 * DEGREES), run_time=5)
        self.play(self.camera.animate.set_euler_angles(theta=(-112 + 360) * DEGREES, phi=90 * DEGREES), run_time=5)
        self.wait()


class PlotRobot(ThreeDScene):
    def construct(self):

        # DH parameters:
        d_list = [0, 0, 0, 0.10915, 0.09465, 0.1]
        a_list = [-0.425, 0, -0.39225, 0, 0.08, 0]
        alpha_list = [1, -1, 0, 1, -1, 0]

        # Set 2
        d_list = [0, 0, 0, 0.10915, 0.09465, 0.1]
        a_list = [0, -0.425, -0.39225, 0.08, 0, 0]
        alpha_list = [1, -1, 0, 1, -1, 0]

        # Set 3
        d_list = [0, 0, 0, 0.10915, 0.09465, 0]
        a_list = [0, -0.425, -0.39225, 0, 0, 0]
        alpha_list = [1, 0, 0, 1, -1, 0]

        # Set 3
        d_list = [0, 0.10915, 0, 0.10915, 0.09465, 0]
        a_list = [0, 0, -0.39225, -0.425, 0, 0]
        alpha_list = [1, 0, 0, 0, -1, 0]

        # Set 4
        # d_list = [0, 0.10915, 0, 0.10915, 0.09465, 0]
        # a_list = [0.10515, 0, -0.39225, 0, -0.425, 0]
        # alpha_list = [0, 1, 0, -1, 0, 0]

        for iter_plot in range(len(d_list)):
            d_list[iter_plot] = d_list[iter_plot] * 10
            a_list[iter_plot] = a_list[iter_plot] * 10
            alpha_list[iter_plot] = alpha_list[iter_plot] * PI / 2

        point1_comp = [PI + PI / 3, 0, 0, 0, 0, 0]
        offset = -2
        self.camera.scale(1.5)
        self.camera.set_euler_angles(theta=120 * DEGREES, phi=90 * DEGREES)

        # self.add(rob_ins)
        self.add(get_RobotInstance(d_list, point1_comp, a_list, alpha_list, offset=offset, show_frame=True))
