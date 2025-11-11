from manim import *
import numpy as np

COLOR_POST = YELLOW_B
COLOR_LIKE = BLUE_B
COLOR_PRIOR = ORANGE
COLOR_EVID = PURPLE_B
BG = "#0e0e10"

class SceneOne_TitleCard(Scene):
    def construct(self):
        config.background_color = BG

        title = Text("Bayesianism", weight="BOLD").scale(1.5)
        title.set_color_by_gradient(BLUE_B, TEAL_A)
        subtitle = Text("Bayes's theorem as the geometry of changing beliefs", font_size=36, color=TEAL_A)

        line1 = Text("Joshua Hizgiaev", font_size=40, color=TEAL_B)
        line2 = Text("HPL-112: Science and Metaphysics", font_size=36, color=TEAL_B)
        line3 = Text("A quick study of history, meaning, and visualization", font_size=32, color=TEAL_A)

        underline = Line(LEFT, RIGHT, color=TEAL_A).set_width(title.width * 1.06)

        top = VGroup(title, underline, subtitle).arrange(DOWN, buff=0.25)
        bottom = VGroup(line1, line2, line3).arrange(DOWN, buff=0.15)

        group = VGroup(top, bottom).arrange(DOWN, buff=0.6)
        group.move_to(ORIGIN)

        self.play(Write(title), run_time = 1.2)
        underline.next_to(title, DOWN, buff=0.18)
        self.play(Create(underline), run_time=0.6)
        self.play(FadeIn(subtitle, shift=0.2 * DOWN), run_time=0.8)
        self.wait(0.3)
        self.play(LaggedStart(
            FadeIn(line1, shift=0.2 * DOWN),
            FadeIn(line2, shift=0.2 * DOWN),
            FadeIn(line3, shift=0.2 * DOWN),
            lag_ratio=0.18, run_time=1.0
        ))
        self.wait(0.7)
        self.play(Flash(title, line_length=0.25, color=str(TEAL_C), time_width=0.6), run_time=0.6)
        
        # Added longer wait for pacing
        self.wait(4)

class SceneTwo_History(Scene):
    def construct(self):
        config.background_color = BG

        # --- Title ---
        title = Text(
            "A short history of Bayes",
            weight="BOLD"
        ).set_color_by_gradient(BLUE_B, TEAL_A)
        title.to_edge(UP, buff=0.6)

        # --- Image of Bayes on the right with a frame ---
        bayes_img = ImageMobject("HPL112/src/images/Thomas_Bayes.gif")
        bayes_img.set_height(3.5)
        bayes_img.to_edge(RIGHT, buff=1.0)

        frame = RoundedRectangle(
            corner_radius=0.2,
            height=bayes_img.height + 0.4,
            width=bayes_img.width + 0.4,
            color=TEAL_B,
            stroke_width=3
        )
        frame.move_to(bayes_img)

        caption = Text(
            "Thomas Bayes (1701-1761)",
            font_size=26,
            color=TEAL_B
        )
        caption.next_to(frame, DOWN, buff=0.25)

        # --- Bullet-point history on the left (multi-line, constrained) ---
        bullet_specs = [
            (
                "• 18th-century English minister whose work on\n"
                "  inverse probability was only published in 1763.",
                {"18th-century": COLOR_EVID, "1763": COLOR_EVID, "inverse probability": COLOR_POST}
            ),
            (
                "• Bayes's theorem gives a rule for updating a prior\n"
                "  belief about a hypothesis when new evidence arrives.",
                {"Bayes's theorem": COLOR_LIKE, "prior": COLOR_PRIOR, "evidence": COLOR_EVID}
            ),
            (
                "• 20th-century Bayesians like Ramsey and de Finetti\n"
                "  tied probability to fair betting rates and degrees of belief.",
                {"Ramsey": TEAL_B, "de Finetti": TEAL_B, "degrees of belief": COLOR_PRIOR}
            ),
            (
                "• Hacking, Howson & Urbach and Salmon used Bayesian\n"
                "  ideas to analyse scientific reasoning and rationality.",
                {"Hacking": TEAL_B, "Howson": TEAL_B, "Urbach": TEAL_B, "Salmon": TEAL_B}
            ),
            (
                "• Today, Bayesian ideas sit alongside frequentist methods\n"
                "  in statistics, and their debates fuel the 'statistics wars'.",
                {"Bayesian": COLOR_POST, "frequentist": COLOR_LIKE, "statistics wars": COLOR_EVID}
            ),
        ]

        bullet_lines = VGroup()
        for text, t2c in bullet_specs:
            line = Text(
                text,
                font_size=26,
                color=TEAL_B,
                line_spacing=0.35
            )
            line.set_color_by_t2c(t2c)
            bullet_lines.add(line)

        bullet_lines.arrange(DOWN, aligned_edge=LEFT, buff=0.35)

        # Constrain the bullet group to the left-side space
        # (frame_width minus image area and some margin)
        left_width = config.frame_width - bayes_img.width - 2.5
        if left_width > 0:
            bullet_lines.set_width(left_width)

        bullet_lines.to_edge(LEFT, buff=0.7)
        bullet_lines.shift(DOWN * 0.2)

        # --- Animations ---
        self.play(FadeIn(title, shift=0.2 * DOWN), run_time=0.9)
        self.play(
            FadeIn(bayes_img, shift=0.4 * LEFT),
            Create(frame),
            FadeIn(caption, shift=0.2 * DOWN),
            run_time=1.2
        )
        self.wait(0.3)

        self.play(
            LaggedStart(
                *[Write(line) for line in bullet_lines],
                lag_ratio=0.2,
                run_time=3.5
            )
        )

        self.wait(3)

class SceneThree_WhatIsBayesianism(Scene):
    def construct(self):
        config.background_color = BG

        # --- Title ---
        title = Text(
            "The core idea: updating beliefs with Bayes",
            font_size=44
        ).set_color_by_gradient(BLUE_B, TEAL_A)
        title.to_edge(UP, buff=0.6)
        self.play(FadeIn(title, shift=0.2 * UP), run_time=0.8)

        # --- Bayes' theorem (single TeX string) ---
        equation = MathTex(
            r"P(H \mid E) = \frac{P(E \mid H)\,P(H)}{P(E)}",
            color=WHITE
        ).scale(1.4)
        # Put the equation at the center of the screen
        equation.move_to(ORIGIN)
        self.play(Write(equation), run_time=1.8)
        self.wait(0.6)

        # Color parts after creation
        equation.set_color_by_tex(r"P(H \mid E)", COLOR_POST)
        equation.set_color_by_tex(r"P(E \mid H)", COLOR_LIKE)
        equation.set_color_by_tex(r"P(H)",        COLOR_PRIOR)
        equation.set_color_by_tex(r"P(E)",        COLOR_EVID)

        # Grab references to each part
        posterior = equation.get_part_by_tex(r"P(H \mid E)")
        likelihood = equation.get_part_by_tex(r"P(E \mid H)")
        # These strings occur twice; get_part_by_tex returns a VGroup
        prior_group = equation.get_part_by_tex(r"P(H)")
        prior = prior_group[-1] if isinstance(prior_group, VGroup) else prior_group
        evid_group = equation.get_part_by_tex(r"P(E)")
        evidence = evid_group[-1] if isinstance(evid_group, VGroup) else evid_group

        # Helper to show an arrow and label for a given part
        def annotate(part, color, title_text, *body_lines, direction=DOWN):
            # Arrow pointing from text to part
            if direction is DOWN:
                arrow = Arrow(
                    start=part.get_bottom() + DOWN * 1.2,
                    end=part.get_bottom(),
                    buff=0.05,
                    color=color
                )
                label_pos = arrow.get_start() + DOWN * 0.3
                shift_dir = 0.1 * DOWN
            else:  # UP
                arrow = Arrow(
                    start=part.get_top() + UP * 1.2,
                    end=part.get_top(),
                    buff=0.05,
                    color=color
                )
                label_pos = arrow.get_start() + UP * 0.3
                shift_dir = 0.1 * UP

            title_line = Text(title_text, color=color, font_size=28)
            extra_lines = [
                Text(txt, color=GREY_C, font_size=24) for txt in body_lines
            ]
            label = VGroup(title_line, *extra_lines).arrange(
                DOWN, aligned_edge=LEFT, buff=0.08
            )
            label.move_to(label_pos, aligned_edge=LEFT)

            self.play(
                GrowArrow(arrow),
                FadeIn(label, shift=shift_dir),
                run_time=0.8
            )
            self.wait(2)
            self.play(FadeOut(arrow), FadeOut(label), run_time=0.6)

        # 1. Posterior
        annotate(
            posterior,
            COLOR_POST,
            "Posterior: P(H | E)",
            "Updated belief in hypothesis H",
            "after seeing evidence E.",
            direction=DOWN
        )

        # 2. Likelihood
        annotate(
            likelihood,
            COLOR_LIKE,
            "Likelihood: P(E | H)",
            "How probable E is if H were true.",
            direction=UP
        )

        # 3. Prior
        annotate(
            prior,
            COLOR_PRIOR,
            "Prior: P(H)",
            "Initial belief in H before evidence.",
            direction=DOWN
        )

        # 4. Evidence / normalizer
        annotate(
            evidence,
            COLOR_EVID,
            "Evidence / normalizer: P(E)",
            "Overall probability of seeing E",
            "across all the hypotheses we consider.",
            direction=DOWN
        )

        # --- Final summary ---
        self.play(equation.animate.set_opacity(1), run_time=0.4)

        summary = MathTex(
            r"\text{Bayes' theorem: } \ Posterior \propto \ Likelihood \times Prior",
            tex_to_color_map={
                "Posterior": COLOR_POST,
                "Likelihood": COLOR_LIKE,
                "Prior": COLOR_PRIOR,
            }
        ).scale(0.9)
        summary.next_to(equation, DOWN, buff=0.9)

        self.play(FadeIn(summary, shift=0.2 * DOWN), run_time=1.0)
        self.wait(3)
