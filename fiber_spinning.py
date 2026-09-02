from manim import *

# Define consistent color palette for industrial components
ExtruderColor = GRAY_B
MeltColor = YELLOW
CoolAirColor = BLUE_A
FilamentColor = WHITE
BathColor = BLUE_D
SolventGasColor = RED_B

# ==========================================
# SCENE 1: Introduction (0:00 - 0:15)
# ==========================================
class Scene1Intro(Scene):
    def construct(self):
        title = Text("Spinning Processes in Textile Manufacturing", font_size=36, weight=BOLD)
        title.to_edge(UP, buff=0.8)
        self.play(Write(title))

        # Spinneret micro-holes diagram
        spinneret = Rectangle(width=4.0, height=0.6, color=GRAY, fill_opacity=0.8)
        spinneret.move_to(UP * 1.5)
        spinneret_label = Text("Spinneret Plate", font_size=20, color=GRAY_A).next_to(spinneret, RIGHT)

        # Micro-holes lines
        holes = VGroup(*[
            Line(spinneret.get_bottom() + LEFT * 1.5 + RIGHT * i * 0.75, 
                 spinneret.get_bottom() + LEFT * 1.5 + RIGHT * i * 0.75 + DOWN * 0.3, 
                 color=BLACK, stroke_width=4)
            for i in range(5)
        ])

        # Extruding filaments animation
        filaments = VGroup(*[
            Line(spinneret.get_bottom() + LEFT * 1.5 + RIGHT * i * 0.75, 
                 DOWN * 3.0 + LEFT * 1.5 + RIGHT * i * 0.75, 
                 color=WHITE, stroke_width=2.5)
            for i in range(5)
        ])

        self.play(Create(spinneret), FadeIn(spinneret_label))
        self.play(Create(holes))
        self.play(Create(filaments, run_time=3))
        self.wait(1)


# ==========================================
# SCENE 2: Melt Spinning Process (0:15 - 0:55)
# ==========================================
class Scene2MeltSpinning(Scene):
    def construct(self):
        # Section Header
        title = Text("Melt Spinning Process", font_size=30, color=BLUE).to_edge(UP)
        takeaway = Text("Melt Spinning: Thermoplastics (Polyester, Nylon). No solvents required.", 
                         font_size=18, color=YELLOW).to_edge(DOWN)
        self.add(title, takeaway)

        # Extruder & Hopper Schematic
        hopper = Polygon([-1, 3, 0], [1, 3, 0], [0.3, 1.8, 0], [-0.3, 1.8, 0], color=ExtruderColor, fill_opacity=0.3)
        hopper_label = Text("Extruder Hopper", font_size=16).next_to(hopper, RIGHT)
        
        barrel = Rectangle(width=1.2, height=2.0, color=ExtruderColor, fill_opacity=0.4).next_to(hopper, DOWN, buff=0)
        spinneret = Rectangle(width=2.0, height=0.3, color=GRAY_A, fill_opacity=0.9).next_to(barrel, DOWN, buff=0)
        spinneret_label = Text("Spinneret", font_size=16).next_to(spinneret, RIGHT)

        # Cooling quench cabinet box
        quench = Rectangle(width=3.0, height=2.5, color=BLUE_E, fill_opacity=0.2).next_to(spinneret, DOWN, buff=0.1)
        quench_label = Text("Cool Air Quench", font_size=16, color=BLUE_B).next_to(quench, RIGHT)

        # Take-up Winder
        winder = Circle(radius=0.5, color=GRAY_A, fill_opacity=0.5).next_to(quench, DOWN, buff=0.5)
        winder_label = Text("Take-up Winder", font_size=16).next_to(winder, RIGHT)

        self.play(Create(hopper), Create(barrel), Create(spinneret), Create(quench), Create(winder))
        self.play(Write(hopper_label), Write(spinneret_label), Write(quench_label), Write(winder_label))

        # Filament Extrusion Flow
        filaments = VGroup(*[
            Line(spinneret.get_bottom() + LEFT * 0.4 + RIGHT * i * 0.4, 
                 winder.get_top(), color=WHITE, stroke_width=2)
            for i in range(3)
        ])

        cool_air_arrows = VGroup(*[
            Arrow(quench.get_left() + UP * (0.8 - i * 0.8), quench.get_left() + RIGHT * 1.5 + UP * (0.8 - i * 0.8), color=BLUE_A)
            for i in range(3)
        ])

        self.play(Create(filaments, run_time=2))
        self.play(Create(cool_air_arrows))
        self.play(Rotate(winder, angle=2*PI, run_time=2))
        self.wait(1)


# ==========================================
# SCENE 3: Solution Spinning Overview (0:55 - 1:05)
# ==========================================
class Scene3SolutionOverview(Scene):
    def construct(self):
        title = Text("Solution Spinning Overview", font_size=32, color=BLUE).to_edge(UP)
        
        info_box = Rectangle(width=10.0, height=3.5, color=GRAY_B, fill_opacity=0.1)
        text1 = Text("For polymers that decompose before melting (e.g., Acrylic, Rayon).", font_size=20)
        text2 = Text("Solution Spinning: Polymer is dissolved in a solvent to form a 'dope' before extrusion.", 
                     font_size=20, color=YELLOW)
        
        content = VGroup(text1, text2).arrange(DOWN, buff=0.5).move_to(info_box.get_center())

        self.play(Write(title))
        self.play(Create(info_box), Write(content))
        self.wait(2)


# ==========================================
# SCENE 4: Wet Spinning Process (1:05 - 1:40)
# ==========================================
class Scene4WetSpinning(Scene):
    def construct(self):
        title = Text("Wet Spinning Process", font_size=30, color=BLUE).to_edge(UP)
        takeaway = Text("Wet Spinning: Solidification via chemical coagulation bath. Ideal for Acrylic and Rayon.", 
                         font_size=16, color=YELLOW).to_edge(DOWN)
        self.add(title, takeaway)

        # Coagulation Bath Container
        bath = Rectangle(width=7.0, height=2.5, color=BLUE_D, fill_opacity=0.4).move_to(DOWN * 0.5)
        bath_label = Text("Coagulation Bath (Liquid Non-Solvent)", font_size=16, color=BLUE_B).next_to(bath, DOWN)

        # Submerged Spinneret
        pipe = Rectangle(width=0.4, height=2.0, color=GRAY_B, fill_opacity=0.8).move_to(LEFT * 2.8 + UP * 0.5)
        spinneret = Rectangle(width=0.8, height=0.4, color=GRAY_A, fill_opacity=0.9).next_to(pipe, DOWN, buff=0)
        spinneret_label = Text("Submerged Spinneret", font_size=14).next_to(spinneret, UP + LEFT, buff=0.1)

        # Rollers
        roller1 = Circle(radius=0.4, color=GRAY_A, fill_opacity=0.5).move_to(RIGHT * 2.5 + DOWN * 0.5)
        roller2 = Circle(radius=0.4, color=GRAY_A, fill_opacity=0.5).move_to(RIGHT * 3.5 + UP * 1.5)

        # Filament path through bath and around rollers
        path = VMobject(color=WHITE, stroke_width=2.5)
        path.set_points_as_corners([
            spinneret.get_right(),
            roller1.get_bottom(),
            roller2.get_right()
        ])

        self.play(Create(bath), Write(bath_label))
        self.play(Create(pipe), Create(spinneret), Write(spinneret_label))
        self.play(Create(roller1), Create(roller2))
        self.play(Create(path, run_time=3))
        self.wait(1)


# ==========================================
# SCENE 5: Dry Spinning Process (1:40 - 2:15)
# ==========================================
class Scene5DrySpinning(Scene):
    def construct(self):
        title = Text("Dry Spinning Process", font_size=30, color=BLUE).to_edge(UP)
        takeaway = Text("Dry Spinning: Solidification via warm air solvent evaporation (Spandex, Acetate).", 
                         font_size=16, color=YELLOW).to_edge(DOWN)
        self.add(title, takeaway)

        # Column Chamber
        column = Rectangle(width=2.5, height=5.0, color=GRAY_B, fill_opacity=0.2).move_to(LEFT * 1.5)
        col_label = Text("Heated Drying Column", font_size=16).next_to(column, LEFT)

        # Hot air arrows (entering from sides)
        air_in = Arrow(column.get_left() + DOWN * 1.5 + LEFT * 1.0, column.get_left() + DOWN * 1.5, color=RED)
        air_label = Text("Hot Air Stream", font_size=14, color=RED).next_to(air_in, LEFT)
        
        vapor_out = Arrow(column.get_right() + UP * 1.5, column.get_right() + UP * 1.5 + RIGHT * 1.0, color=ORANGE)
        vapor_label = Text("Solvent Vapor Recovery", font_size=14, color=ORANGE).next_to(vapor_out, RIGHT)

        # Filaments flowing inside column
        filaments = Line(column.get_top() + DOWN * 0.3, column.get_bottom() + DOWN * 1.0, color=WHITE, stroke_width=3)
        winder = Circle(radius=0.4, color=GRAY_A, fill_opacity=0.5).move_to(column.get_bottom() + DOWN * 1.0 + RIGHT * 0.4)

        self.play(Create(column), Write(col_label))
        self.play(Create(air_in), Write(air_label), Create(vapor_out), Write(vapor_label))
        self.play(Create(filaments, run_time=2), Create(winder))
        self.wait(1)


# ==========================================
# SCENE 6: Dry-Jet Wet Spinning Process (2:15 - 2:45)
# ==========================================
class Scene6DryJetWetSpinning(Scene):
    def construct(self):
        title = Text("Dry-Jet Wet Spinning Process", font_size=30, color=BLUE).to_edge(UP)
        takeaway = Text("Dry-Jet Wet Spinning: Combines air gap stretching with wet coagulation (Kevlar, Lyocell).", 
                         font_size=16, color=YELLOW).to_edge(DOWN)
        self.add(title, takeaway)

        # Spinneret at top
        spinneret = Rectangle(width=2.0, height=0.5, color=GRAY_A, fill_opacity=0.8).move_to(UP * 1.5)
        spin_label = Text("Spinneret Face", font_size=16).next_to(spinneret, RIGHT)

        # Coagulation bath below with explicit gap
        bath = Rectangle(width=6.0, height=2.5, color=BLUE_D, fill_opacity=0.4).move_to(DOWN * 1.2)
        bath_label = Text("Coagulation Bath", font_size=16, color=BLUE_B).next_to(bath, RIGHT)

        # Air Gap Highlighting
        air_gap_zone = Rectangle(width=2.5, height=0.8, color=RED, fill_opacity=0.2).move_to(UP * 0.5)
        air_gap_arrow = Arrow(air_gap_zone.get_left() + LEFT * 1.5, air_gap_zone.get_left(), color=RED)
        air_gap_text = Text("Air Gap (5-10 mm)\nHigh Molecular Alignment", font_size=14, color=RED).next_to(air_gap_arrow, LEFT)

        # Filaments crossing the gap into bath
        filaments = VGroup(*[
            Line(spinneret.get_bottom() + LEFT * 0.6 + RIGHT * i * 0.6, 
                 bath.get_bottom() + LEFT * 0.6 + RIGHT * i * 0.6, 
                 color=WHITE, stroke_width=2.5)
            for i in range(3)
        ])

        self.play(Create(spinneret), Write(spin_label))
        self.play(Create(bath), Write(bath_label))
        self.play(Create(air_gap_zone), Create(air_gap_arrow), Write(air_gap_text))
        self.play(Create(filaments, run_time=2))
        self.wait(1)


# ==========================================
# SCENE 7: Comparative Summary & Conclusion (2:45 - 3:00)
# ==========================================
class Scene7ComparativeSummary(Scene):
    def construct(self):
        title = Text("Summary of Textile Fiber Spinning Technologies", font_size=28, weight=BOLD).to_edge(UP)
        self.add(title)

        # Grid Panels
        panels = VGroup(
            VGroup(Rectangle(width=5.5, height=2.2, color=GRAY_C), Text("Melt Spinning:\nSolidification by Cooling", font_size=16, color=WHITE)),
            VGroup(Rectangle(width=5.5, height=2.2, color=GRAY_C), Text("Wet Spinning:\nSolidification by Chemical Bath", font_size=16, color=WHITE)),
            VGroup(Rectangle(width=5.5, height=2.2, color=GRAY_C), Text("Dry Spinning:\nSolidification by Evaporation", font_size=16, color=WHITE)),
            VGroup(Rectangle(width=5.5, height=2.2, color=GRAY_C), Text("Dry-Jet Wet Spinning:\nAir Gap + Chemical Bath", font_size=16, color=WHITE))
        )

        for p in panels:
            p[0].set_fill(GRAY_E, opacity=0.3)
            p[1].move_to(p[0].get_center())

        panels.arrange_in_grid(rows=2, cols=2, buff=0.4).move_to(DOWN * 0.3)

        self.play(Create(panels, run_time=3))
        self.wait(2)
