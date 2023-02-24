from manim import *


import manim.utils.paths
import pandas as pd



class Temp(Scene):
    def construct(self):
        # object definition
        a = Circle()

        # animations
        self.add(*get_Background("Temporary Slide"))
        self.add(a)


class GraphExample(Scene):
    CONFIG = {
        "axis_config": {
            "numbers_to_exclude": None
        }
    }

    def construct(self):
        # object definition

        # First graph with axes
        ax = Axes(
            x_range=[-3.2, 3.2],
            y_range=[-3.2, 3.2],
            exclude_origin_tick=True)
        ax.add_coordinates()
        ax.x_axis.shift(DOWN * 3.2)
        ax.y_axis.shift(LEFT * 3.2)

        # Second graph with Number Plane
        plane1 = NumberPlane(x_range=[-3.2, 3.2], y_range=[-3.2, 3.2], x_length=6.4, y_length=6.4,
                             background_line_style={
                                 "stroke_color": TEAL,
                                 "stroke_width": 0.1,
                                 "stroke_opacity": 0.6
                             }, x_axis_config={
                "exclude_origin_tick": False
            })
        plane1.x_axis.exclude_origin_tick = False
        plane1.add_coordinates(range(-3, 4), range(-3, 4))
        plane1.coordinate_labels[1][0:3].shift(LEFT * 0.5)
        plane1.coordinate_labels[1][3:7].shift(LEFT * 0.35)
        plane1.y_axis.shift(LEFT * 3.2)
        plane1.x_axis.shift(DOWN * 3.2)
        curve = plane1.plot_implicit_curve(lambda t2, t3: -3 * (3 * np.cos(t3) + 4) * (
                np.sin(t3) * (2 + 4 * np.cos(t2)) - 2 * np.cos(t2) * np.cos(t3)))
        # area = ax.get_area(graph=curve, x_range=(0, 2))

        # animations
        # self.add(ax, curve)
        self.add(plane1, curve)


class PlanePlot(Scene):
    CONFIG = {
        "axis_config": {
            "numbers_to_exclude": None
        }
    }

    def construct(self):
        # object definition

        # Graph with Number Plane
        plane1 = NumberPlane(x_range=[-3.2, 3.2], y_range=[-3.2, 3.2], x_length=6.4, y_length=6.4,
                             background_line_style={
                                 "stroke_color": TEAL,
                                 "stroke_width": 0.1,
                                 "stroke_opacity": 0.6
                             }, x_axis_config={
                "exclude_origin_tick": False
            })
        curve = plane1.plot_implicit_curve(lambda t2, t3: -3 * (3 * np.cos(t3) + 4) * (
                np.sin(t3) * (2 + 4 * np.cos(t2)) - 2 * np.cos(t2) * np.cos(t3)), color=DARK_BLUE)

        x_box = Line([-3.2, 3.2, 0], [3.2, 3.2, 0], stroke_width=plane1.x_axis.get_stroke_width())
        y_box = Line([3.2, -3.2, 0], [3.2, 3.2, 0], stroke_width=plane1.x_axis.get_stroke_width())
        plane1.y_axis.shift(LEFT * 3.2)
        plane1.x_axis.shift(DOWN * 3.2)
        plane1.add_coordinates(range(-3, 4), range(-3, 4))
        plane1.coordinate_labels[1][0:3].shift(LEFT * 0.5)
        plane1.coordinate_labels[1][3:7].shift(LEFT * 0.35)

        x_label = Tex("$\\theta_2$", font_size=48).next_to(plane1.x_axis, DOWN * 0.7)
        y_label = Tex("$\\theta_3$", font_size=48).next_to(plane1.y_axis, LEFT * 0.7)
        plane1.add(x_label, y_label)

        total_graph = VGroup(plane1, curve, x_box, y_box)

        neg_det = []
        pos_det = []
        for t2_i in np.arange(-3.2, 3.21, 0.05):
            for t3_i in np.arange(-3.2, 3.21, 0.05):
                if jac3R([0, t2_i, t3_i], [0, 1, 0], [1, 2, 3 / 2], [np.pi / 2, np.pi / 2, 0]) < 0:
                    neg_det.append(Dot(radius=0.025, color=RED).move_to(np.array([t2_i, t3_i, 0])))
                else:
                    pos_det.append(Dot(radius=0.025, color=GREEN).move_to(np.array([t2_i, t3_i, 0])))

        sing_text = Tex("Singularities \\\\ det$(\\mathbf{J}) = 0$", font_size=36).move_to(np.array([-0.25, 2.5, 0]))
        arrow1 = Arrow(start=sing_text.get_bottom(), end=[0, 0.6, 0])
        arrow2 = Arrow(start=sing_text.get_right(), end=[1.9, 2.25, 0])
        pos_det_text = Tex(r"""Aspect 1 (det$(\mathbf{J}) > 0$)""", font_size=36).move_to(np.array([0, -2, 0]))
        neg_det_text = Tex(r"""Aspect 2 (det$(\mathbf{J}) < 0$)""", font_size=36).move_to(np.array([0, 2, 0]))

        # animations
        self.add(total_graph)
        self.play(FadeIn(curve))
        self.wait()
        self.play(FadeIn(sing_text))
        self.play(*[Create(j) for j in [arrow1, arrow2]])
        self.wait(3)
        self.play(*[FadeOut(k) for k in [arrow1, arrow2, sing_text]])
        self.wait()
        self.play(FadeIn(pos_det_text))
        self.wait()
        self.play(FadeOut(pos_det_text))
        self.add(*pos_det)
        self.add(total_graph)
        self.wait()

        self.play(FadeIn(neg_det_text))
        self.wait()
        self.play(FadeOut(neg_det_text))
        self.add(*neg_det)
        self.add(total_graph)
        self.wait()
        self.clear()
        self.add(total_graph)
        self.play(ReplacementTransform(total_graph, total_graph.copy().scale(0.6).shift(LEFT*2.9 + UP * 0.05)))


def my_det(t2, t3):
    inter_val = [0, t2, t3]
    # return -3 * (3 * cos(inter_val[2]) + 4) * (
    #             sin(inter_val[2]) * (2 + 4 * cos(inter_val[1])) - 2 * cos(inter_val[1]) * cos(inter_val[2]))

    return jac3R(inter_val, [0, 1, 0], [1, 2, 3 / 2], [np.pi / 2, np.pi / 2, 0]) * 8


class PlanePlot2(Scene):
    CONFIG = {
        "axis_config": {
            "numbers_to_exclude": None
        }
    }

    def construct(self):
        # object definition

        # Graph with Number Plane
        plane1 = NumberPlane(x_range=[-3.2, 3.2], y_range=[-3.2, 3.2], x_length=6.4, y_length=6.4,
                             background_line_style={
                                 "stroke_color": TEAL,
                                 "stroke_width": 0.1,
                                 "stroke_opacity": 0.6
                             }, x_axis_config={
                "exclude_origin_tick": False
            }).add_coordinates(range(-3, 4), range(-3, 4)).shift(LEFT * 3).scale(0.6)
        curve = plane1.plot_implicit_curve(lambda t2, t3: -3 * (3 * np.cos(t3) + 4) * (
                np.sin(t3) * (2 + 4 * np.cos(t2)) - 2 * np.cos(t2) * np.cos(t3)), color=DARK_BLUE)
        # curve2 = plane1.plot_implicit_curve(lambda t2, t3: 3 * np.sin(t2) + 4 * np.cos(t3), color=DARK_BLUE)
        solution_set = [[-3, -0.5], [-0.742, 2.628], [-2.755775486, 2.099288504], [-0.3523366242, -2.014417810]]
        first_solution = Dot(radius=0.06, color=PURPLE).move_to(plane1.c2p(solution_set[0][0], solution_set[0][1]))
        first_solution2 = Dot(radius=0.06, color=PURPLE).move_to(plane1.c2p(solution_set[0][0], solution_set[0][1]))
        second_solution = Dot(radius=0.06, color=PURPLE).move_to(plane1.c2p(solution_set[1][0], solution_set[1][1]))
        third_solution = Dot(radius=0.06, color=PURPLE).move_to(plane1.c2p(solution_set[2][0], solution_set[2][1]))
        fourth_solution = Dot(radius=0.06, color=PURPLE).move_to(plane1.c2p(solution_set[3][0], solution_set[3][1]))
        pose_point = Dot(radius=0.1, color=RED).shift(RIGHT * 2)
        four_solution_text = Tex(r"""\begin{minipage}{5 cm}\centering The four IKS of a given pose in the workspace 
        \end{minipage}""", font_size=36).next_to(pose_point, DOWN)

        first_map = Dot(radius=0.06, color=PURPLE).move_to(plane1.c2p(solution_set[0][0], solution_set[0][1]))
        second_map = Dot(radius=0.06, color=PURPLE).move_to(plane1.c2p(solution_set[1][0], solution_set[1][1]))
        third_map = Dot(radius=0.06, color=PURPLE).move_to(plane1.c2p(solution_set[2][0], solution_set[2][1]))
        fourth_map = Dot(radius=0.06, color=PURPLE).move_to(plane1.c2p(solution_set[3][0], solution_set[3][1]))

        # point = Dot().move_to(plane1.c2p(0, 0))

        plane1.y_axis.shift(LEFT * plane1.x_axis.get_length() / 2)
        plane1.x_axis.shift(DOWN * plane1.y_axis.get_length() / 2)
        plane1.coordinate_labels[1][0:3].shift(LEFT * 0.5)
        plane1.coordinate_labels[1][3:7].shift(LEFT * 0.35)
        x_box = Line([plane1.x_axis.get_start()[0], plane1.y_axis.get_end()[1], 0],
                     [plane1.x_axis.get_end()[0], plane1.y_axis.get_end()[1], 0],
                     stroke_width=plane1.x_axis.get_stroke_width())
        y_box = Line([plane1.x_axis.get_end()[0], plane1.y_axis.get_start()[1], 0],
                     [plane1.x_axis.get_end()[0], plane1.y_axis.get_end()[1], 0],
                     stroke_width=plane1.x_axis.get_stroke_width())
        plane1.add(x_box, y_box)
        x_label = Tex("$\\theta_2$", font_size=30).next_to(plane1.x_axis, DOWN * 0.5)
        y_label = Tex("$\\theta_3$", font_size=30).next_to(plane1.y_axis, LEFT * 0.5)
        plane1.add(x_label, y_label)

        # NumberPlane 2
        plane2 = NumberPlane(x_range=[0, 50], y_range=[-50, 0], x_length=6.4, y_length=6.4,
                             background_line_style={
                                 "stroke_color": TEAL,
                                 "stroke_width": 0.1,
                                 "stroke_opacity": 0
                             }, ).add_coordinates(np.arange(0, 51, 10), np.arange(-50, 1, 10)).shift(RIGHT * 3).scale(
            0.6)
        plane2.coordinate_labels[1][0:len(plane2.coordinate_labels[1]) - 1].shift(LEFT * 0.45)
        plane2.coordinate_labels[1][len(plane2.coordinate_labels[1]) - 1].shift(LEFT * 0.35)
        plane2.coordinate_labels[0].shift(UP * 0.35)
        x_label2 = Tex("path", font_size=30).next_to(plane2.x_axis, UP * 0.45)
        y_label2 = Tex("$\\det(\\mathbf{J})$", font_size=30).next_to(plane2.y_axis).rotate(np.pi / 2).shift(LEFT*1.15)
        plane2.add(x_label2, y_label2)

        # print(f"p2c debug: {plane2.c2p(1, -40)}")
        det_point = Dot(color=LIGHT_BROWN).move_to(plane2.c2p(0, my_det(solution_set[0][0], solution_set[0][1])))
        # offset = first_solution.get_center()

        nscs_confirm = Tex(r"""\begin{minipage}{8cm}\centering The nonsingular change of solution can be confirmed 
        with the determinant value as it does not change signs\end{minipage}""", font_size=36).to_edge(DOWN, buff=0.5)

        # animations
        self.add(plane1)
        self.play(FadeIn(curve))
        self.wait()
        self.add(first_map, second_map, third_map, fourth_map, pose_point)
        self.add(four_solution_text)
        self.add(*[TracedPath(k.get_center, stroke_width=2, stroke_color=k2, dissipating_time=0.5,
                              stroke_opacity=0.6) for (k, k2) in zip([first_map, second_map, third_map, fourth_map],
                                                                     [ORANGE, YELLOW, BLUE, RED])])
        self.play(*[ReplacementTransform(i2, pose_point, run_time=2) for i2 in [first_map, second_map,
                                                                                third_map, fourth_map]])
        self.wait()
        self.clear()

        self.add(plane1, plane2)
        self.add(TracedPath(first_solution.get_center, stroke_width=2))
        self.add(TracedPath(det_point.get_center, stroke_width=4, stroke_color=LIGHT_BROWN))
        self.add(first_solution, second_solution, third_solution, fourth_solution, curve)
        self.add(nscs_confirm)
        for k in np.arange(0, 51):
            inter_point = return_intermediate(np.array(solution_set[0]), np.array(solution_set[1]), k, 50)
            self.add(first_solution2)
            self.play(ReplacementTransform(first_solution,
                                           first_solution.move_to(plane1.c2p(inter_point[0], inter_point[1]) + [
                                               plane1.x_axis.get_length() / 2, 0, 0])), run_time=0.02)
            self.play(ReplacementTransform(det_point,
                                           det_point.move_to(plane2.c2p(k, my_det(inter_point[0], inter_point[1])))),
                      run_time=0.03)
        self.wait()


class SingularityPlot(ThreeDScene):
    def construct(self):
        # object definition
        self.set_camera_orientation(phi=0 * DEGREES, theta=0 * DEGREES)

        # Graph with Number Plane
        axes = ThreeDAxes(x_range=[-3.2, 3.2], y_range=[-3.2, 3.2], z_range=[-3.2, 3.2], x_length=6.4, y_length=6.4,
                          z_length=6.4)
        # curve_eqn = lambda t2, t3: -3 * (3 * np.cos(t3) + 4) * (
        #         np.sin(t3) * (2 + 4 * np.cos(t2)) - 2 * np.cos(t2) * np.cos(t3)) / 18

        def param_trig(u, v):
            t2 = u
            t3 = v
            z = -3 * (3 * np.cos(t3) + 4) * (
                    np.sin(t3) * (2 + 4 * np.cos(t2)) - 2 * np.cos(t2) * np.cos(t3)) / 18
            return z

        trig_plane = axes.plot_surface(
            param_trig,
            resolution=(16, 16),
            u_range=(-3, 3),
            v_range=(-3, 3),
            colorscale=[BLUE, GREEN, YELLOW, ORANGE, RED],
        )

        # animations
        self.add(axes, trig_plane)
        # self.play(FadeIn(total_graph))
        # self.wait()
        # self.play(ReplacementTransform(total_graph, total_graph.copy().shift(LEFT*3).scale(0.5)), run_time=1)


class LinePlot(Scene):
    CONFIG = {
        "axis_config": {
            "numbers_to_exclude": None
        }
    }

    def construct(self):
        # object definition

        # Graph with Number Plane
        plane1 = NumberPlane(x_range=[-3.2, 3.2], y_range=[-3.2, 3.2], x_length=6.4, y_length=6.4,
                             background_line_style={
                                 "stroke_color": TEAL,
                                 "stroke_width": 0.1,
                                 "stroke_opacity": 0.6
                             })
        # curve = plane1.plot_implicit_curve(lambda t2, t3: -3 * (3 * np.cos(t3) + 4) * (
        #         np.sin(t3) * (2 + 4 * np.cos(t2)) - 2 * np.cos(t2) * np.cos(t3)), color=DARK_BLUE)
        # line_plot = plane1.plot_line_graph([0, 1, 2, 3], [0, 1, 2, 3], add_vertex_dots=False)

        # final_point = Dot().shift(LEFT)

        # x_box = Line([-3.2, 3.2, 0], [3.2, 3.2, 0], stroke_width=plane1.x_axis.get_stroke_width())
        # y_box = Line([3.2, -3.2, 0], [3.2, 3.2, 0], stroke_width=plane1.x_axis.get_stroke_width())
        plane1.y_axis.shift(LEFT * 3.2)
        plane1.x_axis.shift(DOWN * 3.2)
        plane1.add_coordinates(range(-3, 4), range(-3, 4))
        plane1.coordinate_labels[1][0:3].shift(LEFT * 0.5)
        plane1.coordinate_labels[1][3:7].shift(LEFT * 0.35)
        # total_graph = VGroup(plane1, curve, x_box, y_box, line_plot)

        # Plotting the path
        path_length = 10
        # df_n = pd.read_csv("D:\durghy_manim\Jaco\saved_data_theta1.csv")
        df_n = pd.read_csv("D:\durghy_manim\Jaco\saved_data_neg_theta1.csv")
        plane2 = NumberPlane(x_range=[0, path_length], y_range=[-3.2, 3.2], x_length=path_length, y_length=6.4,
                             background_line_style={
                                 "stroke_color": TEAL,
                                 "stroke_width": 0.1,
                                 "stroke_opacity": 0.6
                             })
        # plane2.y_axis.shift(LEFT * 3.2)
        plane2.x_axis.shift(DOWN * 3.2)
        plane2.add_coordinates(np.arange(0, path_length), range(-3, 4))
        plane2.coordinate_labels[1][0:3].shift(LEFT * 0.5)
        plane2.coordinate_labels[1][3:7].shift(LEFT * 0.35)
        # plane2.shift(LEFT*path_length/2)

        # point_plot = Dot().move_to(np.array([-path_length / 2, df_n.iloc[0, 3], 0]))
        full_path = []
        full_path2 = []
        for i2 in np.arange(0, len(df_n) - 3, 3):
            full_path.append(Line(np.array([df_n.iloc[i2, 1] * path_length / 724, df_n.iloc[i2, 3], 0]),
                                  np.array([df_n.iloc[i2 + 3, 1] * path_length / 724, df_n.iloc[i2 + 3, 3], 0]),
                                  stroke_color=GREEN_B).shift(LEFT * path_length / 2))

        for i2 in np.arange(0, len(df_n) - 3, 3):
            full_path2.append(Line(np.array([df_n.iloc[i2, 1] * path_length / 724, df_n.iloc[i2, 2], 0]),
                                   np.array([df_n.iloc[i2 + 3, 1] * path_length / 724, df_n.iloc[i2 + 3, 2], 0]),
                                   stroke_color=GREEN_A).shift(LEFT * path_length / 2))

        # animations
        # self.add(total_graph)
        # self.add(point_plot, final_point)
        self.add(*full_path, plane2, *full_path2)
        # self.add(TracedPath(point_plot.get_center)) for i2 in np.arange(0, len(df_n), 4): self.play(Transform(
        # point_plot, point_plot.copy().move_to(np.array([-5 + df_n.iloc[i2, 1] / 70, df_n.iloc[i2, 2], 0])),
        # run_time=0.005))
        # self.play(FadeIn(total_graph))
        # self.wait()
        # self.play(ReplacementTransform(total_graph, total_graph.copy().shift(LEFT*3).scale(0.5)), run_time=1)


class ClockwisePathExample(Scene):
    def construct(self):
        colors = [RED, GREEN, BLUE]

        starting_points = VGroup(
            *[
                Dot(LEFT + pos, color=inColor)
                for pos, inColor in zip([UP, DOWN, LEFT], colors)
            ]
        )

        finish_points = VGroup(
            *[
                Dot(RIGHT + pos, color=inColor)
                for pos, inColor in zip([ORIGIN, UP, DOWN], colors)
            ]
        )

        self.add(starting_points)
        self.add(finish_points)
        for dot in starting_points:
            self.add(TracedPath(dot.get_center, stroke_color=dot.get_color()))

        self.wait()
        self.play(
            Transform(
                starting_points,
                finish_points,
                path_func=manim.utils.paths.clockwise_path(),
                run_time=2,
            )
        )
        self.wait()


def make_paths(df):
    path_record = []

    for i2 in range(len(df)):
        # print(f"Index {i2} of the dataframe is being processed")
        elements = 0
        for j in range(len(df.columns) - 2):
            if pd.isna(df.iloc[i2, j + 2]):
                break
            else:
                elements += 1

            if i2 == 0:
                path_record.append([0, df.iloc[0, j + 2]])

        # if i2 > 50:
        #     print(f"The number of elements are {elements}")
        if i2 != 0:
            current_path_index = []
            match_found = []

            for j2 in range(len(path_record)):
                if path_record[j2][0] == i2 - 1:
                    current_path_index.append(j2)

            # print(path_record)
            # print(f"The number of elements are {elements}")

            for k in current_path_index:
                matching_list = None
                threshold = 0.1
                for k2 in range(elements):
                    d1 = abs(path_record[k][-1] - df.iloc[i2, k2 + 2])
                    if d1 < threshold:
                        threshold = d1
                        matching_list = [k, k2 + 2]
                        match_found.append(k2)
                if matching_list is not None:
                    path_record[matching_list[0]].append(df.iloc[i2, matching_list[1]])
                    path_record[matching_list[0]][0] = i2

            if len(match_found) != elements:
                for m in range(elements):
                    if m not in match_found:
                        path_record.append([i2, df.iloc[i2, m + 2]])

    return path_record


class PosPlot(Scene):
    CONFIG = {
        "axis_config": {
            "numbers_to_exclude": None
        }
    }

    def construct(self):
        # object definition

        # Plotting the path
        path_length = 10
        df_n = pd.read_csv("D:\durghy_manim\Jaco\saved_data_theta4.csv")

        plane2 = NumberPlane(x_range=[0, path_length], y_range=[-3.2, 3.2], x_length=path_length, y_length=6.4,
                             background_line_style={
                                 "stroke_color": TEAL,
                                 "stroke_width": 0.1,
                                 "stroke_opacity": 0.6
                             })
        # plane2.y_axis.shift(LEFT * 3.2)
        plane2.x_axis.shift(DOWN * 3.2)
        plane2.add_coordinates(np.arange(0, path_length), range(-3, 4))
        plane2.coordinate_labels[1][0:3].shift(LEFT * 0.5)
        plane2.coordinate_labels[1][3:7].shift(LEFT * 0.35)
        # plane2.shift(LEFT*path_length/2)

        # point_plot = Dot().move_to(np.array([-path_length / 2, df_n.iloc[0, 3], 0]))
        full_path = []
        # full_path2 = []
        paths = make_paths(df_n)
        # start_index = 0

        print(len(paths))
        # print(paths[i2])
        for i2 in range(len(paths)):
            for i4 in np.arange(1, len(paths[i2]) - 1):
                i3 = paths[i2][0] - len(paths[i2]) + 1 + i4
                full_path.append(Line(np.array([i3 * path_length / 724, paths[i2][i4], 0]),
                                      np.array([(i3 + 1) * path_length / 724, paths[i2][i4 + 1], 0]),
                                      stroke_color=GREEN).shift(LEFT * path_length / 2))

        # line2 = Line(np.array([0, 0, 0]), np.array([2, 1, 0]), stroke_color=GREEN_A).shift(LEFT*path_length / 2)
        # animations

        self.add(*full_path, plane2)
