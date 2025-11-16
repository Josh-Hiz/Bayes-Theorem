from manim import *
import numpy as np

COLOR_POST = YELLOW_B
COLOR_LIKE = BLUE_B
COLOR_PRIOR = ORANGE
COLOR_EVID = PURPLE_B
BG = "#0e0e10"

class Scene1_TitleCard(Scene):
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

class Scene2_History(Scene):
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

class Scene3_WhatIsBayesianism(Scene):
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

        summary = Text(
            "In short:  P(H | E) = The probability that hypothesis H is true after seeing evidence E.",
            font_size=25,
            color=TEAL_A,
        )
        summary.to_edge(DOWN, buff=0.6)

        self.play(FadeIn(summary, shift=0.2 * UP), run_time=1.2)
        self.wait(2.0)


HYPOTHESIS_COLOR     = YELLOW
NOT_HYPOTHESIS_COLOR = GREY
EVIDENCE_COLOR1      = BLUE_C
EVIDENCE_COLOR2      = BLUE_E
NOT_EVIDENCE_COLOR1  = GREY
NOT_EVIDENCE_COLOR2  = GREY_D

ShowCreation = Create  # for old code compatibility


class SimpleBayesDiagram(VGroup):
    """
    Area diagram for Bayes:
      - Left column: H
      - Right column: ¬H
      - Bottom of each: E
      - Top of each: ¬E

    Now includes braces + MathTex labels and a .morph_to() helper
    to animate changing prior / likelihood / antilikelihood.
    """

    def __init__(
        self,
        prior=0.3,
        likelihood=0.7,
        antilikelihood=0.2,
        height=3.0,
        show_labels=True,
        **kwargs,
    ):
        super().__init__(**kwargs)

        # store parameters so morph_to() can reuse them
        self.prior = prior
        self.likelihood = likelihood
        self.antilikelihood = antilikelihood
        self.side_height = height

        width = height  # square for simplicity

        # --- Outer square ---
        outer = Square(side_length=height)
        outer.set_stroke(WHITE, 2)
        outer.set_fill(GREY_E, opacity=0.1)

        # --- Split into H (left) and ¬H (right) ---
        h_width = prior * width
        nh_width = width - h_width

        h_box = Rectangle(width=h_width, height=height)
        h_box.set_stroke(HYPOTHESIS_COLOR, 2)
        h_box.set_fill(opacity=0)

        nh_box = Rectangle(width=nh_width, height=height)
        nh_box.set_stroke(NOT_HYPOTHESIS_COLOR, 2)
        nh_box.set_fill(opacity=0)

        VGroup(h_box, nh_box).arrange(RIGHT, buff=0).move_to(outer)

        # --- Inside H: E (bottom) & ¬E (top) ---
        he_height = likelihood * height
        hne_height = height - he_height

        he_rect = Rectangle(width=h_width, height=he_height)
        he_rect.set_stroke(WHITE, 1)
        he_rect.set_fill(EVIDENCE_COLOR1, opacity=0.9)

        hne_rect = Rectangle(width=h_width, height=hne_height)
        hne_rect.set_stroke(WHITE, 1)
        hne_rect.set_fill(NOT_EVIDENCE_COLOR1, opacity=0.9)

        VGroup(he_rect, hne_rect).arrange(UP, buff=0).move_to(h_box)

        # --- Inside ¬H: E (bottom) & ¬E (top) ---
        nhe_height = antilikelihood * height
        nhne_height = height - nhe_height

        nhe_rect = Rectangle(width=nh_width, height=nhe_height)
        nhe_rect.set_stroke(WHITE, 1)
        nhe_rect.set_fill(EVIDENCE_COLOR2, opacity=0.9)

        nhne_rect = Rectangle(width=nh_width, height=nhne_height)
        nhne_rect.set_stroke(WHITE, 1)
        nhne_rect.set_fill(NOT_EVIDENCE_COLOR2, opacity=0.9)

        VGroup(nhe_rect, nhne_rect).arrange(UP, buff=0).move_to(nh_box)

        # --- store pieces as attributes ---
        self.outer = outer
        self.h_box = h_box
        self.nh_box = nh_box
        self.he_rect = he_rect
        self.hne_rect = hne_rect
        self.nhe_rect = nhe_rect
        self.nhne_rect = nhne_rect

        # base geometry
        self.add(outer, h_box, nh_box, he_rect, hne_rect, nhe_rect, nhne_rect)

        if show_labels:
            self._add_braces_and_labels()

    def _add_braces_and_labels(self):
        """Curly braces + MathTex labels for P(H), P(¬H), P(E|H), P(E|¬H)."""

        # Columns (H vs ¬H)
        h_column = VGroup(self.he_rect, self.hne_rect)
        nh_column = VGroup(self.nhe_rect, self.nhne_rect)

        # Horizontal braces under columns
        self.h_brace = Brace(h_column, DOWN, buff=0.08)
        self.nh_brace = Brace(nh_column, DOWN, buff=0.08)

        self.h_label = MathTex(r"P(H)").set_color(HYPOTHESIS_COLOR)
        self.h_label.next_to(self.h_brace, DOWN, buff=0.05)

        self.nh_label = MathTex(r"P(\neg H)").set_color(NOT_HYPOTHESIS_COLOR)
        self.nh_label.next_to(self.nh_brace, DOWN, buff=0.05)

        # Vertical braces on E strips
        self.he_brace = Brace(self.he_rect, LEFT, buff=0.08)
        self.nhe_brace = Brace(self.nhe_rect, RIGHT, buff=0.08)

        self.he_label = MathTex(r"P(E \mid H)").set_color(EVIDENCE_COLOR1)
        self.he_label.next_to(self.he_brace, LEFT, buff=0.05)

        self.nhe_label = MathTex(r"P(E \mid \neg H)").set_color(EVIDENCE_COLOR2)
        self.nhe_label.next_to(self.nhe_brace, RIGHT, buff=0.05)

        self.add(
            self.h_brace,
            self.nh_brace,
            self.he_brace,
            self.nhe_brace,
            self.h_label,
            self.nh_label,
            self.he_label,
            self.nhe_label,
        )

    # --- animation helper -------------------------------------------------
    def morph_to(self, prior=None, likelihood=None, antilikelihood=None):
        """
        Return a Transform that smoothly morphs this diagram
        to one with new (prior, likelihood, antilikelihood) values.
        """
        new = SimpleBayesDiagram(
            prior=prior if prior is not None else self.prior,
            likelihood=likelihood if likelihood is not None else self.likelihood,
            antilikelihood=antilikelihood if antilikelihood is not None else self.antilikelihood,
            height=self.side_height,
            show_labels=True,
        )
        new.move_to(self)  # keep it in the same place
        return Transform(self, new)
    
class SimpleProbabilityBar(VGroup):
    """
    Two-part bar representing a probability p and 1-p.
    To animate, build a new bar with new_bar_with_p() and Transform to it.
    """

    def __init__(
        self,
        p=0.5,
        width=5.0,
        height=0.4,
        color1=BLUE_D,
        color2=GREY_B,
        show_percent=True,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.p = p
        self.total_width = width
        self.height = height
        self.color1 = color1
        self.color2 = color2
        self.show_percent = show_percent

        w1 = p * width
        w2 = width - w1

        left = Rectangle(width=w1, height=height)
        left.set_fill(color1, opacity=1.0)
        left.set_stroke(WHITE, 1)

        right = Rectangle(width=w2, height=height)
        right.set_fill(color2, opacity=1.0)
        right.set_stroke(WHITE, 1)

        bar = VGroup(left, right).arrange(RIGHT, buff=0)
        self.left = left
        self.right = right
        self.add(bar)

        # Optional percentage labels
        self.left_label = None
        self.right_label = None
        if show_percent:
            left_label = MathTex(f"{int(round(p * 100))}\\%").scale(0.5)
            right_label = MathTex(f"{int(round((1 - p) * 100))}\\%").scale(0.5)
            left_label.move_to(left)
            right_label.move_to(right)
            self.left_label = left_label
            self.right_label = right_label
            self.add(left_label, right_label)

    def new_bar_with_p(self, new_p: float):
        new_bar = SimpleProbabilityBar(
            p=new_p,
            width=self.total_width,
            height=self.height,
            color1=self.color1,
            color2=self.color2,
            show_percent=self.show_percent,
        )
        new_bar.move_to(self)
        return new_bar
    
class Scene4_BayesVisualization(Scene):
    def construct(self):
        # Optional if you’re using a custom background color
        # self.camera.background_color = BG

        # --- Parameters -----------------------------------------------------
        prior = 0.30           # P(H)
        likelihood = 0.70      # P(E | H)
        antilikelihood = 0.20  # P(E | ¬H)

        posterior = (
            prior * likelihood
            / (prior * likelihood + (1 - prior) * antilikelihood)
        )

        # --- Title + small equation at the top ------------------------------
        title = Text(
            "Visualizing Bayes’ Theorem",
            font_size=40
        )
        title.to_edge(UP, buff=0.3)

        formula = MathTex(
            r"P(H \mid E) = "
            r"\frac{P(H)\,P(E \mid H)}"
            r"{P(H)\,P(E \mid H) + P(\neg H)\,P(E \mid \neg H)}"
        ).scale(0.6)
        formula.next_to(title, DOWN, buff=0.25)

        # Slightly gray the whole formula first, then re-color pieces later
        formula.set_color(GREY_B)
        formula.set_color_by_tex("P(H \\mid E)", WHITE)

        # --- Main diagram: shift a bit to the LEFT so there is room on right
        diagram = SimpleBayesDiagram(
            prior=prior,
            likelihood=likelihood,
            antilikelihood=antilikelihood,
            height=3.0,
            show_labels=True,
        )
        diagram.move_to(ORIGIN).shift(1.8 * LEFT + 0.2 * DOWN)

        # --- Bullet points (will appear on the RIGHT later) -----------------
        bullets = BulletedList(
            r"Area of each region = probability mass",
            r"Left column: $H$; right column: $\neg H$",
            r"Bottom colored strips: $E$ under $H$ and under $\neg H$",
            r"Posterior bar shows updated $P(H \mid E)$",
            font_size=23,
        )
        bullets.scale(0.85)
        bullets.set_width(5.5)               # keep them from running off screen
        bullets.next_to(diagram, RIGHT, buff=0.7)
        bullets.align_to(diagram, UP)
        bullets.to_edge(RIGHT, buff=0.6)

        # --- “Remember this” arrow like in the frames -----------------------
        remember_text = Text("Remember this", font_size=36)
        remember_text.next_to(diagram, RIGHT, buff=1.6).shift(0.2 * UP)

        remember_arrow = Arrow(
            start=remember_text.get_left() + 0.2 * LEFT,
            end=diagram.get_right(),
            buff=0.1,
            stroke_width=3,
        )

        # --- Intro: title, formula, diagram, remember-arrow -----------------
        self.play(FadeIn(title), Write(formula))
        self.play(FadeIn(diagram, shift=DOWN), run_time=2.0)

        # Surround the whole diagram once (the “1 × 1 square” idea)
        whole_box = SurroundingRectangle(diagram, buff=0.06, color=YELLOW)
        self.play(Create(whole_box))
        self.play(Write(remember_text), GrowArrow(remember_arrow))
        self.wait(0.8)

        # Remove that big box, keep the picture in mind
        self.play(FadeOut(whole_box))
        self.wait(0.2)

        # --- Highlight numerator: P(H) * P(E | H) ---------------------------
        num_rect = SurroundingRectangle(diagram.he_rect, buff=0.06, color=YELLOW)
        num_group = VGroup(
            formula.get_part_by_tex("P(H)"),
            formula.get_part_by_tex(r"P(E \mid H)"),
        )

        self.play(
            Create(num_rect),
            num_group.animate.set_color(YELLOW),
        )
        self.wait(0.6)

        # --- Highlight denominator region P(E) = P(H,E) + P(¬H,E) -----------
        denom_area_group = VGroup(diagram.he_rect, diagram.nhe_rect)
        denom_rect = SurroundingRectangle(denom_area_group, buff=0.06, color=BLUE)

        denom_group = VGroup(
            formula.get_part_by_tex("+"),
            formula.get_part_by_tex(r"P(\neg H)"),
            formula.get_part_by_tex(r"P(E \mid \neg H)"),
        )

        self.play(
            ReplacementTransform(num_rect, denom_rect),
            denom_group.animate.set_color(BLUE),
        )
        self.wait(0.6)
        self.play(FadeOut(denom_rect))

        # --- Swap “Remember this” for the explanatory bullets ---------------
        self.play(
            FadeOut(remember_arrow),
            FadeOut(remember_text),
        )
        self.play(FadeIn(bullets, shift=RIGHT, lag_ratio=0.15))
        self.wait(1.0)

        # --- Animate changing proportions in the diagram (optional demo) ----
        self.play(diagram.morph_to(prior=0.1), run_time=1.2)
        self.play(diagram.morph_to(prior=0.6), run_time=1.2)
        self.wait(0.2)

        self.play(diagram.morph_to(likelihood=0.4), run_time=1.2)
        self.play(diagram.morph_to(likelihood=0.7), run_time=1.2)
        self.wait(0.2)

        self.play(diagram.morph_to(antilikelihood=0.4), run_time=1.2)
        self.play(diagram.morph_to(antilikelihood=antilikelihood), run_time=1.2)
        self.wait(0.4)

        # --- Probability bar: prior -> posterior (right-hand “remember this”) ---
        prior_bar = SimpleProbabilityBar(p=prior, width=4.0, height=0.4)
        prior_bar.next_to(diagram, DOWN, buff=0.8)

        prior_label = Tex(r"Prior $P(H)$", font_size=30)
        prior_label.next_to(prior_bar, DOWN, buff=0.25)

        self.play(FadeIn(prior_bar), FadeIn(prior_label))
        self.wait(0.4)

        posterior_bar = prior_bar.new_bar_with_p(posterior)
        posterior_label = Tex(r"Posterior $P(H \mid E)$", font_size=30)
        posterior_label.move_to(prior_label)

        self.play(
            Transform(prior_bar, posterior_bar),
            Transform(prior_label, posterior_label),
            run_time=1.5,
        )
        self.wait(0.5)

        # Arrow calling out the posterior bar (analogous to last frames)
        bar_arrow = Arrow(
            start=posterior_bar.get_top() + UP * 0.5,
            end=posterior_bar.get_top(),
            buff=0.05,
            color=GREEN,
            stroke_width=3,
        )
        bar_text = Tex("This is $P(H \mid E)$", font_size=20)
        bar_text.next_to(bar_arrow, UP, buff=0.1)

        self.play(GrowArrow(bar_arrow), FadeIn(bar_text))
        self.wait(1.2)

        # --- Clean ending ---------------------------------------------------
        self.play(
            FadeOut(bar_arrow),
            FadeOut(bar_text),
            FadeOut(prior_bar),
            FadeOut(prior_label),
            FadeOut(diagram),
            FadeOut(formula),
            FadeOut(bullets),
            FadeOut(title),
        )
        self.wait(1.0)

HYPOTHESIS_COLOR     = YELLOW
NOT_HYPOTHESIS_COLOR = GREY
EVIDENCE_COLOR1      = BLUE_C   # light cyan
EVIDENCE_COLOR2      = BLUE_E   # darker teal
NOT_EVIDENCE_COLOR1  = GREY
NOT_EVIDENCE_COLOR2  = GREY_D
BG = "#0e0e10"

class BayesDiagram(VGroup):
    """
    Area diagram for Bayes:
      - Left column: H
      - Right column: ¬H
      - In each column, bottom = E, top = ¬E

    By default, the prior split (H vs ¬H) is hidden, and only the
    evidence-colored regions are visible (like your original).
    """

    def __init__(
        self,
        prior: float,
        likelihood: float,
        antilikelihood: float,
        height: float = 2.0,
        square_style: dict | None = None,
        rect_style: dict | None = None,
        hypothesis_color=HYPOTHESIS_COLOR,
        not_hypothesis_color=NOT_HYPOTHESIS_COLOR,
        evidence_color1=EVIDENCE_COLOR1,
        evidence_color2=EVIDENCE_COLOR2,
        not_evidence_color1=NOT_EVIDENCE_COLOR1,
        not_evidence_color2=NOT_EVIDENCE_COLOR2,
        prior_rect_direction=DOWN,
        **kwargs,
    ):
        super().__init__(**kwargs)

        # store parameters in case you want to extend this later
        self.prior = prior
        self.likelihood = likelihood
        self.antilikelihood = antilikelihood
        self.diagram_height = height
        self.prior_rect_direction = prior_rect_direction

        self.hypothesis_color = hypothesis_color
        self.not_hypothesis_color = not_hypothesis_color
        self.evidence_color1 = evidence_color1
        self.evidence_color2 = evidence_color2
        self.not_evidence_color1 = not_evidence_color1
        self.not_evidence_color2 = not_evidence_color2

        square_style = square_style or dict(
            fill_color=GREY_D,
            fill_opacity=1.0,
            stroke_color=WHITE,
            stroke_width=2,
        )
        rect_style = rect_style or dict(
            stroke_color=WHITE,
            stroke_width=1,
            fill_opacity=1.0,
        )

        # --- Outer square --------------------------------------------------
        outer = Square(side_length=height)
        outer.set_style(**square_style)

        width = height
        h_width = prior * width
        nh_width = width - h_width

        # --- H vs ¬H (columns) --------------------------------------------
        h_rect = Rectangle(width=h_width, height=height)
        h_rect.set_style(**rect_style)

        nh_rect = Rectangle(width=nh_width, height=height)
        nh_rect.set_style(**rect_style)

        VGroup(h_rect, nh_rect).arrange(RIGHT, buff=0).move_to(outer)

        # --- Inside H: E (bottom) & ¬E (top) ------------------------------
        he_height = likelihood * height
        hne_height = height - he_height

        he_rect = Rectangle(width=h_width, height=he_height)
        he_rect.set_style(**rect_style)

        hne_rect = Rectangle(width=h_width, height=hne_height)
        hne_rect.set_style(**rect_style)

        VGroup(he_rect, hne_rect).arrange(UP, buff=0).move_to(h_rect)

        # --- Inside ¬H: E (bottom) & ¬E (top) -----------------------------
        nhe_height = antilikelihood * height
        nhne_height = height - nhe_height

        nhe_rect = Rectangle(width=nh_width, height=nhe_height)
        nhe_rect.set_style(**rect_style)

        nhne_rect = Rectangle(width=nh_width, height=nhne_height)
        nhne_rect.set_style(**rect_style)

        VGroup(nhe_rect, nhne_rect).arrange(UP, buff=0).move_to(nh_rect)

        # --- Color fills ---------------------------------------------------
        h_rect.set_fill(hypothesis_color)
        nh_rect.set_fill(not_hypothesis_color)
        he_rect.set_fill(evidence_color1)
        hne_rect.set_fill(not_evidence_color1)
        nhe_rect.set_fill(evidence_color2)
        nhne_rect.set_fill(not_evidence_color2)

        # --- Save references ----------------------------------------------
        self.outer = outer
        self.h_rect = h_rect
        self.nh_rect = nh_rect
        self.he_rect = he_rect
        self.hne_rect = hne_rect
        self.nhe_rect = nhe_rect
        self.nhne_rect = nhne_rect

        self.hypothesis_split = VGroup(h_rect, nh_rect)
        self.evidence_split = VGroup(he_rect, hne_rect, nhe_rect, nhne_rect)

        # By default: show only evidence regions (like original)
        self.add(outer, self.hypothesis_split, self.evidence_split)
        outer.set_opacity(0)          # square invisible
        self.hypothesis_split.set_opacity(0)  # hide prior split

        # brace-related attrs (optional, used if you call add_brace_attrs)
        self.braces = None
        self.braces_buff = SMALL_BUFF

    # ------------------------------------------------------------------
    # Optional: braces for P(H), P(¬H), etc.
    # ------------------------------------------------------------------
    def add_brace_attrs(self, buff=SMALL_BUFF):
        braces = self.create_braces(buff)
        self.braces = braces
        self.braces_buff = buff

        attrs = [
            "h_brace",
            "nh_brace",
            "he_brace",
            "hne_brace",
            "nhe_brace",
            "nhne_brace",
        ]
        for brace, attr in zip(braces, attrs):
            setattr(self, attr, brace)

        self.add(braces)
        return self

    def create_braces(self, buff=SMALL_BUFF):
        kw = {"buff": buff}
        return VGroup(
            Brace(self.h_rect, self.prior_rect_direction, **kw),
            Brace(self.nh_rect, self.prior_rect_direction, **kw),
            Brace(self.he_rect, LEFT, **kw),
            Brace(self.hne_rect, LEFT, **kw),
            Brace(self.nhe_rect, RIGHT, **kw),
            Brace(self.nhne_rect, RIGHT, **kw),
        )

    def refresh_braces(self):
        if self.braces is not None:
            new_braces = self.create_braces(self.braces_buff)
            self.braces.become(new_braces)
        return self

    # The old manimlib pattern was self.play(diagram.set_prior, 0.5)
    # In Community Manim, prefer Transform + a new diagram, or your
    # SimpleBayesDiagram.morph_to(). These are kept mainly for completeness.

    def set_prior(self, new_prior: float):
        self.prior = new_prior
        # For static use: rebuild via a simple "become" from a fresh diagram
        new_diagram = BayesDiagram(
            prior=new_prior,
            likelihood=self.likelihood,
            antilikelihood=self.antilikelihood,
            height=self.diagram_height,
            hypothesis_color=self.hypothesis_color,
            not_hypothesis_color=self.not_hypothesis_color,
            evidence_color1=self.evidence_color1,
            evidence_color2=self.evidence_color2,
            not_evidence_color1=self.not_evidence_color1,
            not_evidence_color2=self.not_evidence_color2,
            prior_rect_direction=self.prior_rect_direction,
        )
        new_diagram.move_to(self)
        self.become(new_diagram)
        return self

    def general_set_likelihood(self, new_likelihood: float, low_rect, high_rect):
        height = self.diagram_height
        self.likelihood = new_likelihood

        low_rect.set_height(
            new_likelihood * height,
            stretch=True,
            about_edge=DOWN,
        )
        high_rect.set_height(
            (1 - new_likelihood) * height,
            stretch=True,
            about_edge=UP,
        )
        self.refresh_braces()
        return self

    def set_likelihood(self, new_likelihood: float):
        return self.general_set_likelihood(
            new_likelihood,
            self.he_rect,
            self.hne_rect,
        )

    def set_antilikelihood(self, new_antilikelihood: float):
        height = self.diagram_height
        self.antilikelihood = new_antilikelihood

        self.nhe_rect.set_height(
            new_antilikelihood * height,
            stretch=True,
            about_edge=DOWN,
        )
        self.nhne_rect.set_height(
            (1 - new_antilikelihood) * height,
            stretch=True,
            about_edge=UP,
        )
        self.refresh_braces()
        return self

    def copy(self):
        return super().copy()

# --------------------------------------------------------------------
# 1. Bayes formula helper
# --------------------------------------------------------------------
def get_bayes_formula(expand_denominator: bool = False) -> MathTex:
    """
    Returns a MathTex object with colored H, ¬H, E, plus:
        .posterior   -> P(H | E)
        .prior       -> all occurrences of P(H)
        .likelihood  -> all occurrences of P(E | H)
        .p_evidence  -> P(E) in the denominator
    """

    if expand_denominator:
        tex = (
            r"P(H \mid E) = "
            r"P(H)\,P(E \mid H)\over"
            r"{P(H)\,P(E \mid H) + P(\neg H)\,P(E \mid \neg H)}"
        )
    else:
        tex = (
            r"P(H \mid E) = "
            r"{P(H)\,P(E \mid H)\over P(E)}"
        )

    t2c = {
        r"H": HYPOTHESIS_COLOR,
        r"\neg H": NOT_HYPOTHESIS_COLOR,
        r"E": EVIDENCE_COLOR1,
    }

    formula = MathTex(
        tex,
        tex_to_color_map=t2c,
        substrings_to_isolate=[
            r"P(H \mid E)",
            r"P(H)",
            r"P(E \mid H)",
            r"P(E)",
        ],
    )

    # Handy attributes
    formula.posterior  = formula.get_part_by_tex(r"P(H \mid E)")
    formula.prior      = formula.get_parts_by_tex(r"P(H)")
    formula.likelihood = formula.get_parts_by_tex(r"P(E \mid H)")

    if expand_denominator:
        formula.p_evidence = formula.get_parts_by_tex(r"P(E)")
    else:
        formula.p_evidence = formula.get_part_by_tex(r"P(E)")

    return formula

def get_bayes_formula(expand_denominator: bool = False) -> MathTex:
    """
    Returns a MathTex object with:
        .posterior   -> P(H | E)
        .prior       -> all occurrences of P(H)
        .likelihood  -> all occurrences of P(E | H)
        .p_evidence  -> P(E) in the denominator

    All H's are yellow, all E's are blue.
    """

    if expand_denominator:
        tex = (
            r"P(H \mid E) = "
            r"P(H)\,P(E \mid H)\over"
            r"{P(H)\,P(E \mid H) + P(\neg H)\,P(E \mid \neg H)}"
        )
    else:
        tex = (
            r"P(H \mid E) = "
            r"{P(H)\,P(E \mid H)\over P(E)}"
        )

    formula = MathTex(
        tex,
        substrings_to_isolate=[
            r"P(H \mid E)",
            r"P(H)",
            r"P(E \mid H)",
            r"P(E)",
        ],
    )

    # --- Colors: everything white, then H/E colored, neg-sign grey ---
    formula.set_color(WHITE)
    formula.set_color_by_tex("H", HYPOTHESIS_COLOR)          # all H's yellow
    formula.set_color_by_tex("E", EVIDENCE_COLOR1)           # all E's blue
    formula.set_color_by_tex(r"\neg", NOT_EVIDENCE_COLOR2)   # the "¬" symbol grey

    # --- Handy attributes for later scenes (including Scene 5) ---
    formula.posterior  = formula.get_part_by_tex(r"P(H \mid E)")
    formula.prior      = formula.get_parts_by_tex(r"P(H)")
    formula.likelihood = formula.get_parts_by_tex(r"P(E \mid H)")

    if expand_denominator:
        formula.p_evidence = formula.get_parts_by_tex(r"P(E)")
    else:
        formula.p_evidence = formula.get_part_by_tex(r"P(E)")

    return formula


class Scene5_BayesEquationWithDiagrams(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text(
            "Bayes theorem",
            font_size=40,
            weight="BOLD"
        )

        # ---------- Left: Bayes formula ----------
        formula = get_bayes_formula(expand_denominator=False)
        formula.scale(1.4)
        formula.set_width(5.5)

        posterior  = formula.posterior
        prior      = formula.prior
        likelihood = formula.likelihood
        p_evidence = formula.p_evidence

        # ---------- Middle: "=" sign ----------
        eq_symbol = MathTex("=")
        eq_symbol.scale(1.6)

        # ---------- Right: Bayes diagrams as a fraction ----------
        prior_val    = 0.35
        like_val     = 0.6
        antilike_val = 0.2
        box_h        = 2.0

        top_diag = BayesDiagram(prior_val, like_val, antilike_val, height=box_h)
        bottom_diag = BayesDiagram(prior_val, like_val, antilike_val, height=box_h)

        # Match shading:
        # Top: only left-bottom (H & E) is cyan, everything else dark
        for r in [top_diag.he_rect, top_diag.hne_rect,
                  top_diag.nhe_rect, top_diag.nhne_rect]:
            r.set_fill(BLACK, opacity=1.0)
        top_diag.he_rect.set_fill(EVIDENCE_COLOR1, opacity=1.0)

        # Bottom: E-row – left cyan, right darker teal
        for r in [bottom_diag.he_rect, bottom_diag.hne_rect,
                  bottom_diag.nhe_rect, bottom_diag.nhne_rect]:
            r.set_fill(BLACK, opacity=1.0)
        bottom_diag.he_rect.set_fill(EVIDENCE_COLOR1, opacity=1.0)
        bottom_diag.nhe_rect.set_fill(EVIDENCE_COLOR2, opacity=1.0)

        frac_bar_diag = Line(LEFT, RIGHT, stroke_width=2.5, color=WHITE)
        frac_bar_diag.set_width(top_diag.get_width())

        diag_stack = VGroup(top_diag, frac_bar_diag, bottom_diag).arrange(
            DOWN, buff=0.3, aligned_edge=RIGHT
        )
        diag_stack.scale(1.3)

        # ---------- Overall centered layout ----------
        main_row = VGroup(formula, eq_symbol, diag_stack).arrange(
            RIGHT, buff=0.7
        )
        main_row.move_to(ORIGIN)

        title.next_to(main_row, UP, buff=0.1)

        # ---------- Base appearance ----------
        self.play(FadeIn(title, shift=0.2 * DOWN), run_time=0.7)
        self.play(Write(formula), run_time=1.6)
        self.play(
            FadeIn(eq_symbol),
            FadeIn(diag_stack, shift=0.2 * LEFT),
            run_time=1.0
        )
        self.wait(0.6)

        # ------------------------------------------------------------
        # STEP 1: Denominator / E highlight (blue)
        # ------------------------------------------------------------

        # Try to grab the 'E' inside P(H|E)
        try:
            posterior_E = posterior[-2]
        except Exception:
            posterior_E = posterior

        box_pE = SurroundingRectangle(p_evidence, buff=0.10, color=EVIDENCE_COLOR2)
        box_E_posterior = SurroundingRectangle(posterior_E, buff=0.10, color=EVIDENCE_COLOR2)

        # Denominator region in diagrams: bottom E row (H,E and ¬H,E)
        denom_region = VGroup(bottom_diag.he_rect, bottom_diag.nhe_rect)
        box_denom_region = SurroundingRectangle(
            denom_region, buff=0.04, color=EVIDENCE_COLOR2
        )

        e_label = Tex(r"\dots among cases where $E$ is true", font_size=30)
        e_label.next_to(posterior, DOWN, buff=0.8).align_to(posterior, LEFT)

        e_arrow = Arrow(
            start=e_label.get_top() + 0.15 * UP,
            end=posterior_E.get_bottom(),
            buff=0.05,
            stroke_width=2.4,
            max_tip_length_to_length_ratio=0.08,
        )

        self.play(
            Create(box_pE),
            Create(box_E_posterior),
            Create(box_denom_region),
            run_time=0.9,
        )
        self.play(
            GrowArrow(e_arrow),
            FadeIn(e_label, shift=0.1 * UP),
            run_time=0.9,
        )
        self.wait(1.4)

        self.play(
            FadeOut(box_pE),
            FadeOut(box_E_posterior),
            FadeOut(box_denom_region),
            FadeOut(e_arrow),
            FadeOut(e_label),
            run_time=0.8,
        )
        self.wait(0.4)

        # ------------------------------------------------------------
        # STEP 2: Numerator / H highlight (yellow)
        # ------------------------------------------------------------

        # Grab the 'H' inside P(H|E)
        try:
            posterior_H = posterior[2]
        except Exception:
            posterior_H = posterior

        # Numerator P(H) P(E|H)
        numerator_terms = VGroup(prior, likelihood)
        box_numerator_formula = SurroundingRectangle(
            numerator_terms, buff=0.10, color=YELLOW
        )

        # NEW: yellow box specifically around the H in P(H|E)
        box_H_posterior = SurroundingRectangle(
            posterior_H, buff=0.10, color=YELLOW
        )

        # Numerator region in diagrams: top's HE block
        numerator_region = top_diag.he_rect
        box_numerator_region = SurroundingRectangle(
            numerator_region, buff=0.04, color=YELLOW
        )

        h_label = Tex(r"How often is $H$ true", font_size=30)
        h_label.next_to(posterior, UP, buff=0.8).align_to(posterior, LEFT)

        h_arrow = Arrow(
            start=h_label.get_bottom() + 0.15 * DOWN,
            end=posterior_H.get_top(),
            buff=0.05,
            stroke_width=2.4,
            max_tip_length_to_length_ratio=0.08,
        )

        self.play(
            Create(box_numerator_formula),
            Create(box_H_posterior),
            Create(box_numerator_region),
            run_time=2.0,
        )
        self.play(
            GrowArrow(h_arrow),
            FadeIn(h_label, shift=0.1 * DOWN),
            run_time=2.0,
        )
        self.wait(2.0)

        self.play(
            FadeOut(box_numerator_formula),
            FadeOut(box_H_posterior),
            FadeOut(box_numerator_region),
            FadeOut(h_arrow),
            FadeOut(h_label),
            run_time=5.0,
        )
        self.wait(2.0)

class Scene6_MainTakeaways(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ----- Title + subtitle -----
        title = Text(
            "Main takeaways",
            font_size=48,
            weight="BOLD"
        )
        title.set_color_by_gradient(BLUE_B, TEAL_A)
        title.to_edge(UP, buff=0.8)

        subtitle = Text(
            "Bayes’ theorem as the geometry of changing beliefs",
            font_size=32
        ).set_color(TEAL_B)
        subtitle.next_to(title, DOWN, buff=0.4)

        # ----- 3 bullets: Bayesianism (philosophy & significance) -----
        bayesianism_bullets = BulletedList(
            "Bayesianism treats probabilities as degrees of belief, not just long-run frequencies.",
            "Rational agents should update those degrees of belief when new evidence arrives.",
            "It connects belief, fair betting odds, and scientific reasoning into one framework.",
            font_size=30,
        )
        bayesianism_bullets.set_color(TEAL_A)
        bayesianism_bullets.set_width(10)

        # ----- 3 bullets: Bayes’ theorem (the rule itself) -----
        bayes_rule_bullets = BulletedList(
            "Bayes’ theorem gives a precise rule for moving from prior to posterior.",
            "Geometrically, the posterior is “what fraction of the E-cases also have H”.",
            "As evidence carves up the space of possibilities, your credences shift smoothly.",
            font_size=30,
        )
        bayes_rule_bullets.set_color(TEAL_A)
        bayes_rule_bullets.set_width(10)

        # Group the two lists and center them on screen
        bullets_group = VGroup(bayesianism_bullets, bayes_rule_bullets).arrange(
            DOWN, buff=0.6, aligned_edge=LEFT
        )
        # Place under subtitle, then center horizontally
        bullets_group.next_to(subtitle, DOWN, buff=0.6)
        bullets_group.move_to(np.array([0, bullets_group.get_center()[1], 0]))

        # ----- Animations -----
        self.play(FadeIn(title, shift=0.2 * DOWN), run_time=0.7)
        self.play(FadeIn(subtitle, shift=0.1 * DOWN), run_time=0.6)

        all_bullets = list(bayesianism_bullets) + list(bayes_rule_bullets)
        self.play(
            LaggedStart(
                *[FadeIn(b, shift=0.1 * RIGHT) for b in all_bullets],
                lag_ratio=0.13,
                run_time=3.0,
            )
        )

        self.wait(2.0)



class Scene7_Thanks(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ----- Main thank-you text -----
        thanks = Text(
            "Thank you for watching!",
            font_size=60,
            weight="BOLD"
        )
        thanks.set_color_by_gradient(BLUE_B, TEAL_A)
        thanks.move_to(ORIGIN + 0.3 * UP)

        subtitle = Text(
            "Bayes' theorem: the geometry of changing beliefs",
            font_size=32
        ).set_color(TEAL_B)
        subtitle.next_to(thanks, DOWN, buff=0.5)

        # Simple closing animation
        self.play(FadeIn(thanks, scale=1.1), run_time=1.2)
        self.play(FadeIn(subtitle, shift=0.2 * UP), run_time=0.8)
        self.play(Flash(thanks, line_length=0.25, color=EVIDENCE_COLOR1, time_width=0.6),
                  run_time=0.6)
        self.wait(2.5)
