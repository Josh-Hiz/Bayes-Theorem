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
        # Background
        config.background_color = BG

        # --- Title ---
        title = Text(
            "The core idea: updating beliefs with Bayes",
            font_size=44
        ).set_color_by_gradient(BLUE_B, TEAL_A)
        title.to_edge(UP, buff=0.6)
        self.play(FadeIn(title, shift=0.2 * UP), run_time=0.8)

        # --- Bayes' theorem (with isolated substrings) ---
        equation = MathTex(
            r"P(H \mid E)=", r"{P(E \mid H)P(H) \over P(E)}",
            substrings_to_isolate=[
                r"P(H \mid E)",   # posterior
                r"P(E \mid H)",   # likelihood
                r"P(H)",          # prior
                r"P(E)",          # evidence
            ],
            color=WHITE,
        ).scale(1.4)

        equation.move_to(ORIGIN)
        self.play(Write(equation), run_time=1.5)
        self.wait(0.5)

        # Grab references to the pieces we care about
        posterior = equation.get_part_by_tex(r"P(H \mid E)")
        likelihood = equation.get_part_by_tex(r"P(E \mid H)")
        prior = equation.get_part_by_tex(r"P(H)")
        evidence = equation.get_part_by_tex(r"P(E)")

        # Helper to animate “highlight + arrow + label” for one part
        def explain_part(mobj, label_text, expl_text, color,
                         position="below", wait_time=2.0):
            """
            position = "above": label+arrow above, equation nudged down
            position = "below": label+arrow below, equation nudged up
            """
            shift_vec = UP * 0.4 if position == "below" else DOWN * 0.4

            # Nudge the whole equation first to make space
            self.play(equation.animate.shift(shift_vec), run_time=1.0)

            # Label + explanation
            label = Text(label_text, font_size=32, weight="BOLD", color=color)
            expl = Text(expl_text, font_size=26)
            label_group = VGroup(label, expl).arrange(
                DOWN, aligned_edge=LEFT, buff=0.15
            )

            if position == "below":
                # Text below, arrow pointing up to the term
                label_group.next_to(equation, DOWN, buff=0.7)
                arrow = Arrow(
                    start=label_group.get_top(),
                    end=mobj.get_bottom(),
                    buff=0.12,
                    stroke_width=2.2,
                    max_tip_length_to_length_ratio=0.10,
                )
                text_shift_dir = UP
            else:
                # Text above, arrow pointing down to the term
                label_group.next_to(equation, UP, buff=0.7)
                arrow = Arrow(
                    start=label_group.get_bottom(),
                    end=mobj.get_top(),
                    buff=0.12,
                    stroke_width=2.2,
                    max_tip_length_to_length_ratio=0.10,
                )
                text_shift_dir = DOWN

            # Animate in: color the piece, grow arrow, fade in text
            self.play(
                mobj.animate.set_color(color),
                GrowArrow(arrow),
                FadeIn(label_group, shift=0.1 * text_shift_dir),
                run_time=1.5,
            )
            self.wait(wait_time)

            # De-emphasize + move equation back
            self.play(
                mobj.animate.set_color(WHITE),
                FadeOut(arrow),
                FadeOut(label_group),
                equation.animate.shift(-shift_vec),
                run_time=1.0,
            )

        # 1 Posterior (from above, push equation down)
        explain_part(
            posterior,
            "Posterior  P(H | E)",
            "Your updated belief in H after seeing the evidence E.",
            COLOR_POST,
            position="below",
        )

        # 2 Likelihood (from above)
        explain_part(
            likelihood,
            "Likelihood  P(E | H)",
            "How compatible the evidence E is with hypothesis H.",
            COLOR_LIKE,
            position="above",
        )

        # 3 Evidence / normalizing constant (from below, push equation up)
        explain_part(
            evidence,
            "Evidence  P(E)",
            "Overall probability of seeing E under all hypotheses.",
            COLOR_EVID,
            position="below",
        )

        # 4 Prior (from above)
        explain_part(
            prior,
            "Prior  P(H)",
            "What you believed about H before seeing E.",
            COLOR_PRIOR,
            position="above",
        )

        self.wait(0.5)
