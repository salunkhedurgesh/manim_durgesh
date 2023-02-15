from PhD_thesis.threeR.functions_threeR import make_paths
import pandas as pd


def my_det(t2, t3):
    inter_val = [0, t2, t3]
    # return -3 * (3 * cos(inter_val[2]) + 4) * (
    #             sin(inter_val[2]) * (2 + 4 * cos(inter_val[1])) - 2 * cos(inter_val[1]) * cos(inter_val[2]))

    return jac3R(inter_val, [0, 1, 0], [1, 2, 3 / 2], [np.pi / 2, np.pi / 2, 0]) * 8


def my_det6R(s, e, cur_iter=0, total_iter=50):
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

    point_record = [point1_comp, point2_comp, point3_comp, point4_comp, point5_comp, point6_comp, point7_comp,
                    point8_comp, point9_comp, point10_comp, point11_comp, point12_comp]
    # JACO
    d1s = 212
    d3s = -12
    d4s = -249.3
    d5s = -84.6
    d6s = -222.73
    a2s = 410

    # DH parameters of CRX-10ia/L robot are:
    d_list = [d1s, 0, d3s, d4s, d5s, d6s]
    a_list = [0, a2s, 0, 0, 0, 0]
    alpha_list = [PI / 2, PI, PI / 2, np.deg2rad(55), np.deg2rad(55), PI]
    d_list = [number / 100 for number in d_list]
    a_list = [number / 100 for number in a_list]

    theta_list = return_intermediate(np.array(point_record[s]), np.array(point_record[e]), cur_iter, total_iter)

    return static_pref_jacdet(theta_list, d_list, a_list, alpha_list)


class NegPlotT(ZoomedScene):
    CONFIG = {
        "axis_config": {
            "numbers_to_exclude": None
        }
    }

    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.06,
            zoomed_display_height=6,
            zoomed_display_width=10,
            image_frame_stroke_width=0.002,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
            },
            zoomed_camera_frame_starting_position=[-4.8, 0.18, 0],
            **kwargs
        )

    def construct(self):
        # object definition

        # Plotting the path
        path_length = 10
        df_n = pd.read_csv("D:\durghy_manim\Jaco\saved_data_neg_theta1.csv")
        df_n2 = pd.read_csv("D:\durghy_manim\Jaco\saved_data_theta1.csv")

        plane2 = NumberPlane(x_range=[0, path_length], y_range=[-3.2, 3.2], x_length=path_length, y_length=6.4,
                             background_line_style={
                                 "stroke_color": TEAL,
                                 "stroke_width": 0.1,
                                 "stroke_opacity": 0.6
                             }).scale(0.7).shift(LEFT * 2.5)

        plane2.x_axis.shift(DOWN * plane2.y_axis.get_length() / 2)
        plane2.add_coordinates(np.arange(0, path_length), range(-3, 4))
        plane2.coordinate_labels[1][0:3].shift(LEFT * 0.4)
        plane2.coordinate_labels[1][3:7].shift(LEFT * 0.35)
        x_label2 = Tex("path", font_size=30).next_to(plane2.x_axis, DOWN * 0.4).scale(0.8)
        y_label2 = Tex("$\\theta_1 (radians)$", font_size=30).next_to(plane2.y_axis).rotate(np.pi / 2).shift(
            LEFT * 1.5).scale(0.8)
        plane2.add(x_label2, y_label2)

        full_path = []
        full_path2 = []
        zoom_path = []
        zoom_path2 = []
        zoom_pathd = []
        zoom_pathd2 = []
        paths = make_paths(df_n, thresh=0.2)
        paths2 = make_paths(df_n2, thresh=0.1)
        print(len(paths))
        # t_str = []
        # t_iter = 0
        t1 = []

        for i2 in range(len(paths)):
            print(f"Length of path {i2} is {len(paths[i2])}")
            for i4 in np.arange(1, len(paths[i2]) - 1):
                i3 = paths[i2][0] - len(paths[i2]) + 1 + i4
                if i2 == 2:
                    zoom_path2.append(Line(plane2.c2p((i3 * path_length / 724), paths[i2][i4]),
                                           plane2.c2p(((i3 + 1) * path_length / 724), paths[i2][i4 + 1]),
                                           stroke_color=RED_C, stroke_width=5, stroke_opacity=0.6))
                    zoom_pathd2.append(Line(plane2.c2p((i3 * path_length / 724), paths[i2][i4]),
                                            plane2.c2p(((i3 + 1) * path_length / 724), paths[i2][i4 + 1]),
                                            stroke_color=RED_C, stroke_width=0.5, stroke_opacity=0.6))
                else:
                    full_path2.append(Line(plane2.c2p((i3 * path_length / 724), paths[i2][i4]),
                                           plane2.c2p(((i3 + 1) * path_length / 724), paths[i2][i4 + 1]),
                                           stroke_color=RED_C, stroke_width=5, stroke_opacity=0.6))
            if i2 == 3:
                t1.append(Tex("$T_1$").scale(0.8).move_to(full_path2[-1].get_end()).shift(RIGHT * 0.2))
            elif i2 == 1:
                t1.append(Tex("$T_5$").scale(0.8).move_to(full_path2[-1].get_end()).shift(LEFT * 2 + UP * 0.5))

        for i2 in range(len(paths2)):
            print(f"Length of path {i2} is {len(paths2[i2])}")
            for i4 in np.arange(1, len(paths2[i2]) - 1):
                i3 = paths2[i2][0] - len(paths2[i2]) + 1 + i4
                if i2 == 2:
                    zoom_path.append(Line(plane2.c2p((i3 * path_length / 724), paths2[i2][i4]),
                                          plane2.c2p(((i3 + 1) * path_length / 724), paths2[i2][i4 + 1]),
                                          stroke_color=BLUE_C, stroke_width=5, stroke_opacity=0.6))
                    zoom_pathd.append(Line(plane2.c2p((i3 * path_length / 724), paths2[i2][i4]),
                                           plane2.c2p(((i3 + 1) * path_length / 724), paths2[i2][i4 + 1]),
                                           stroke_color=BLUE_C, stroke_width=0.5, stroke_opacity=0.6))
                else:
                    full_path.append(Line(plane2.c2p((i3 * path_length / 724), paths2[i2][i4]),
                                          plane2.c2p(((i3 + 1) * path_length / 724), paths2[i2][i4 + 1]),
                                          stroke_color=BLUE_C, stroke_width=5, stroke_opacity=0.6))

            if i2 == 2:
                t1.append(Tex("$T_3, T_4$").scale(0.8).move_to(zoom_path[-1].get_end()).shift(RIGHT * 0.8))
            else:
                if i2 == 0:
                    t1.append(
                        Tex("$T_7, T_8$").scale(0.8).move_to(full_path[-1].get_end()).shift(RIGHT * 0.8 + UP * 0.2))
                if i2 == 1:
                    t1.append(Tex("$T_6$").scale(0.8).move_to(full_path[-1].get_end()).shift(LEFT * 2 + DOWN * 0.5))
                if i2 == 3:
                    t1.append(Tex("$T_2$").scale(0.8).move_to(full_path[-1].get_end()).shift(LEFT * 2 + DOWN * 0.5))

        point_plot = Dot(color=GREEN).move_to(plane2.c2p(0, paths[3][1]))
        point_plot2 = Dot(color=GREEN).move_to(plane2.c2p(0, paths[1][1]))
        point_plotN = Dot(color=GREEN).move_to(plane2.c2p(0, paths[4][1]))

        third_choice = Tex(
            r"""\begin{minipage}{5 cm} \centering Trajectories  $T_1$ and $T_5$ lead to a continuous path that 
            CANNOT be \emph{repeated} \end{minipage}""",
            font_size=36).to_edge(RIGHT)
        third_problem = Tex(
            r"""\begin{minipage}{5 cm} \centering These paths CANNOT be \emph{repeated} because the trajectory 
            ends at the start point of another trajectory which is not repeatable \end{minipage}""",
            font_size=36).to_edge(RIGHT)
        tp_bkg = BackgroundRectangle(third_problem, fill_opacity=1)
        tp_present = Group(tp_bkg, third_problem)

        # animations

        self.add(plane2, *zoom_path, *zoom_path2, *full_path, *full_path2)
        self.FadeIt(*full_path)
        self.play(*[FadeIn(k) for k in [t1[0], t1[1]]])
        self.add(TracedPath(point_plot.get_center, stroke_width=5, stroke_color=PURPLE_C))
        self.add(TracedPath(point_plot2.get_center, stroke_width=5, stroke_color=PURPLE_C))
        self.FadeInFadeOut(third_choice, wait_time=2)

        for i2 in np.arange(1, len(paths[3]) - 1, 8):
            self.play(Transform(point_plot, point_plot.move_to(
                plane2.c2p((i2 * path_length / 724), paths[3][i2])), run_time=0.05))
            self.play(Transform(point_plot2, point_plot2.move_to(
                plane2.c2p((i2 * path_length / 724), paths[1][i2])), run_time=0.05))

        self.add(TracedPath(point_plotN.get_center, stroke_width=5, stroke_color=PURPLE_C))
        self.remove(point_plot)
        for i2N in np.arange(1, len(paths[4]) - 1, 8):
            i2 = i2N + len(paths[3]) - 1
            self.play(Transform(point_plotN, point_plotN.move_to(
                plane2.c2p((i2 * path_length / 724), paths[4][i2N])), run_time=0.05))
            self.play(Transform(point_plot2, point_plot2.move_to(
                plane2.c2p((i2 * path_length / 724), paths[1][i2])), run_time=0.05))

        self.wait()
        self.FadeInFadeOut(tp_present, wait_time=5)

    def FadeIt(self, *inObject):
        self.play(*[Transform(k2, k2.copy().set_opacity(0.2)) for k2 in inObject])

    def FadeInFadeOut(self, *object_to_process, wait_time=3):
        self.play(FadeIn(*object_to_process))
        self.wait(wait_time)
        self.play(FadeOut(*object_to_process))


class PosPlotT(Scene):
    CONFIG = {
        "axis_config": {
            "numbers_to_exclude": None
        }
    }

    def construct(self):
        # object definition

        # Plotting the path
        path_length = 10
        df_n = pd.read_csv("D:\durghy_manim\Jaco\saved_data_theta1.csv")
        df_n2 = pd.read_csv("D:\durghy_manim\Jaco\saved_data_neg_theta1.csv")

        plane2 = NumberPlane(x_range=[0, path_length], y_range=[-3.2, 3.2], x_length=path_length, y_length=6.4,
                             background_line_style={
                                 "stroke_color": TEAL,
                                 "stroke_width": 0.1,
                                 "stroke_opacity": 0.6
                             }).scale(0.7).shift(LEFT * 2.5)

        plane2.x_axis.shift(DOWN * plane2.y_axis.get_length() / 2)
        plane2.add_coordinates(np.arange(0, path_length), range(-3, 4))
        plane2.coordinate_labels[1][0:3].shift(LEFT * 0.4)
        plane2.coordinate_labels[1][3:7].shift(LEFT * 0.35)
        x_label2 = Tex("path", font_size=30).next_to(plane2.x_axis, DOWN * 0.4).scale(0.8)
        y_label2 = Tex("$\\theta_1 (radians)$", font_size=30).next_to(plane2.y_axis).rotate(np.pi / 2).shift(
            LEFT * 1.5).scale(0.8)
        plane2.add(x_label2, y_label2)

        # full_path = []
        full_path2 = []
        paths = make_paths(df_n)

        first_x = (len(paths[2]) * path_length) / 724
        second_x = (len(paths[0]) * path_length) / 724
        third_x = ((len(paths[1]) - len(paths[4])) * path_length) / 724

        first_transition = DashedLine(plane2.c2p(first_x, -3.5), plane2.c2p(first_x, 3.5))
        first_nom = Tex("$(8 \\rightarrow 6)$", font_size=24).move_to(first_transition.get_end()).shift(LEFT * 0.5)
        second_transition = DashedLine(plane2.c2p(second_x, -3.5), plane2.c2p(second_x, 3.5))
        second_nom = Tex("$(6 \\rightarrow 4)$", font_size=24).move_to(second_transition.get_end()).shift(RIGHT * 0.5)
        third_transition = DashedLine(plane2.c2p(third_x, -3.5), plane2.c2p(third_x, 3.5))
        third_nom = Tex("$(4 \\rightarrow 8)$", font_size=24).move_to(third_transition.get_end())

        point_plot = Dot().move_to(plane2.c2p(0, paths[2][1]))
        point_plot2 = Dot().move_to(plane2.c2p(0, paths[0][1]))
        point_plot3 = Dot(color=GREEN).move_to(plane2.c2p(0, paths[1][1]))
        point_plot4 = Dot(color=GREEN).move_to(plane2.c2p(0, paths[3][1]))

        point_plotb = Circle(color=BLUE_C, radius=0.1).move_to(plane2.c2p(0, paths[2][1]))
        point_plot2b = Circle(color=BLUE_C, radius=0.1).move_to(plane2.c2p(0, paths[0][1]))
        point_plot3b = Circle(color=BLUE_C, radius=0.1).move_to(plane2.c2p(0, paths[1][1]))
        point_plot4b = Circle(color=BLUE_C, radius=0.1).move_to(plane2.c2p(0, paths[3][1]))
        print(len(paths))

        for i2 in range(len(paths)):
            print(f"Length of path {i2} is {len(paths[i2])}")
            for i4 in np.arange(1, len(paths[i2]) - 1):
                i3 = paths[i2][0] - len(paths[i2]) + 1 + i4
                full_path2.append(Line(plane2.c2p(i3 * path_length / 724, paths[i2][i4]),
                                       plane2.c2p((i3 + 1) * path_length / 724, paths[i2][i4 + 1]),
                                       stroke_color=BLUE_C, stroke_width=5, stroke_opacity=0.6))

        full_path22 = []
        paths2 = make_paths(df_n2, thresh=0.2)
        print(len(paths2))

        for i2 in range(len(paths2)):
            print(f"Length of path2 {i2} is {len(paths2[i2])}")
            for i4 in np.arange(1, len(paths2[i2]) - 1):
                i3 = paths2[i2][0] - len(paths2[i2]) + 1 + i4
                full_path22.append(Line(plane2.c2p(i3 * path_length / 724, paths2[i2][i4]),
                                        plane2.c2p((i3 + 1) * path_length / 724, paths2[i2][i4 + 1]),
                                        stroke_color=RED_C, stroke_width=5, stroke_opacity=0.6))

        four_choices = Tex(
            r"""\begin{minipage}{5 cm}\centering We have 4 IKS in the same aspect and we can start the 
            trajectory from any one of them \end{minipage}""",
            font_size=36).to_edge(RIGHT)
        first_choice = Tex(
            r"""\begin{minipage}{5 cm} \centering Let us start with IKS corresponding to $T_3$\end{minipage}""",
            font_size=36).to_edge(RIGHT)
        zeroth_problem = Tex(
            r"""\begin{minipage}{5 cm} \centering The path exits from a region with 8 IKS to enter a region with 
            6 IKS and thus lose 2 IKS (1 in each aspect) \end{minipage}""",
            font_size=36).to_edge(RIGHT)
        zp_bkg = BackgroundRectangle(zeroth_problem, fill_opacity=1)
        zp_present = Group(zp_bkg, zeroth_problem)
        first_problem = Tex(
            r"""\begin{minipage}{5 cm}We do not have a continuous path beyond this point and a sudden jump to 
            any other paths in the same aspect will take place \end{minipage}""",
            font_size=36).to_edge(RIGHT)
        fp_bkg = BackgroundRectangle(first_problem, fill_opacity=1)
        fp_present = Group(fp_bkg, first_problem)

        zeroth_problem2 = Tex(
            r"""\begin{minipage}{5 cm} \centering The path exits from a region with 6 IKS to enter a region 
            with 4 IKS and further loses 2 IKS (1 in each aspect) \end{minipage}""",
            font_size=36).to_edge(RIGHT)
        zp_bkg2 = BackgroundRectangle(zeroth_problem2, fill_opacity=1)
        zp_present2 = Group(zp_bkg2, zeroth_problem2)
        second_choice = Tex(
            r"""\begin{minipage}{5 cm} \centering Let us start with IKS corresponding to 
            $T_7$\end{minipage}""").to_edge(RIGHT)
        second_problem = Tex(
            r"""\begin{minipage}{5 cm}Same problem is encountered at this point and a sudden jump to any other paths 
            with a solution at next instance will take place \end{minipage}""", font_size=36).to_edge(RIGHT)
        sp_bkg = BackgroundRectangle(second_problem)
        sp_present = Group(sp_bkg, second_problem)

        third_choice = Tex(
            r"""\begin{minipage}{5 cm} \centering Trajectories  $T_2$ and $T_6$ lead to a continuous path 
            that can be \emph{repeated} \end{minipage}""", font_size=36).to_edge(RIGHT)
        third_problem = Tex(
            r"""\begin{minipage}{5 cm} \centering This path can be \emph{repeated} because the 
            trajectory ends with the same IKS it started with it \end{minipage}""", font_size=36).to_edge(RIGHT)
        tp_bkg = BackgroundRectangle(third_problem, fill_opacity=1)
        tp_present = Group(tp_bkg, third_problem)
        zeroth_problem3 = Tex(
            r"""\begin{minipage}{5 cm} \centering The path exits from a region with 4 IKS to enter a region
             with 8 IKS and thus gains 4 IKS (2 in each aspect) \end{minipage}""", font_size=36).to_edge(RIGHT)
        zp_bkg3 = BackgroundRectangle(zeroth_problem3, fill_opacity=1)
        zp_present3 = Group(zp_bkg3, zeroth_problem3)

        show_three = True

        # animations
        # self.add(*get_Background("Example trajectory of JACO robot"))
        self.add(plane2)
        self.play(*[FadeIn(k4) for k4 in full_path2])
        self.play(*[FadeIn(k4) for k4 in full_path22])

        self.FadeInFadeOut(four_choices)
        self.FadeIt(*full_path22)
        self.FadeInFadeOut(point_plotb, point_plot2b, point_plot3b, point_plot4b)

        self.wait()
        self.add(TracedPath(point_plot.get_center, stroke_width=5, stroke_color=GOLD_A))
        self.FadeInFadeOut(first_choice, wait_time=2)
        for i2 in np.arange(1, len(paths[2]) - 1, 2):
            self.play(Transform(point_plot, point_plot.move_to(
                plane2.c2p((i2 * path_length / 724), paths[2][i2])), run_time=0.2))
        self.play(Create(first_transition))
        self.play(FadeIn(first_nom))
        self.FadeInFadeOut(zp_present, wait_time=5)
        self.FadeInFadeOut(fp_present, wait_time=5)
        self.wait(2)
        point_plot.color = PURE_RED
        for i2 in range(11):
            nh = len(paths[2]) - 1
            eh = paths[3][nh] - paths[2][nh]
            self.play(Transform(point_plot, point_plot.move_to(
                plane2.c2p((nh * path_length / 724), paths[2][nh] + (eh * i2 / 10))), run_time=0.05))
        self.wait(2)
        self.add(TracedPath(point_plot2.get_center, stroke_width=5, stroke_color=RED_C, dissipating_time=0.2))
        self.FadeInFadeOut(second_choice, wait_time=2)
        for i2 in np.arange(1, len(paths[0]) - 1, 4):
            self.play(Transform(point_plot2, point_plot2.move_to(
                plane2.c2p((i2 * path_length / 724), paths[0][i2])), run_time=0.2))
        self.play(Create(second_transition))
        self.play(FadeIn(second_nom))
        self.FadeInFadeOut(zp_present2, wait_time=5)
        self.FadeInFadeOut(sp_present, wait_time=5)
        self.wait(2)

        self.add(TracedPath(point_plot3.get_center, stroke_width=5, stroke_color=GREEN))
        self.add(TracedPath(point_plot4.get_center, stroke_width=5, stroke_color=GREEN))
        self.FadeInFadeOut(third_choice, wait_time=2)
        for i2 in np.arange(1, len(paths[1]) - 1, 8):
            if i2 > 724 - 74 and show_three:
                show_three = False
                self.wait()
                self.play(Create(third_transition))
                self.wait()
                self.play(FadeIn(third_nom))
                self.FadeInFadeOut(zp_present3, wait_time=5)
            self.play(Transform(point_plot3, point_plot3.move_to(
                plane2.c2p((i2 * path_length / 724), paths[1][i2])), run_time=0.05))
            self.play(Transform(point_plot4, point_plot4.move_to(
                plane2.c2p((i2 * path_length / 724), paths[3][i2])), run_time=0.05))
        self.wait()
        self.FadeInFadeOut(tp_present, wait_time=5)

        self.wait(2)
        # self.clear()
        # complete_set1 = Group(plane2, point_plot, point_plot2, *full_path2, first_transition, second_transition)
        # self.add(complete_set1)
        # self.play(Transform(complete_set1, complete_set1.copy().scale(0.5).shift(LEFT * 4 + UP)))
        # self.wait(3)

    def FadeInFadeOut(self, *inObject, wait_time=3):
        self.play(FadeIn(*inObject))
        self.wait(wait_time)
        self.play(FadeOut(*inObject))

    def FadeIt(self, *inObject):
        self.play(*[Transform(k2, k2.copy().set_opacity(0.2)) for k2 in inObject])
