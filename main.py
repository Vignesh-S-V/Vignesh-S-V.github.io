from manim import *

class LavatharEpic(Scene):
    def construct(self):
        # பின்னணி அமைப்பு
        self.camera.background_color = "#000000"

        # --- ACT 1: PARADISE IN FIRE ---
        title1 = Text("ACT 1: PARADISE IN FIRE", color=RED, font_size=48)
        self.play(Write(title1))
        self.play(FadeOut(title1))

        # சூரியன் மற்றும் நகரம் (Sol City Prime)
        sun_surface = Annulus(inner_radius=2.5, outer_radius=3.5, color=ORANGE, fill_opacity=0.4)
        city_dome = Circle(radius=1.5, color=BLUE_B, fill_opacity=0.2)
        city_label = Text("SOL CITY PRIME - 502nd YEAR", font_size=32, color=GOLD).to_edge(UP)
        
        self.play(Create(sun_surface))
        self.play(FadeIn(city_dome), Write(city_label))
        self.wait(2)
        self.play(FadeOut(VGroup(sun_surface, city_dome, city_label)))

        # --- ACT 2: THE UNRAVELING ---
        title2 = Text("ACT 2: THE UNRAVELING", color=ORANGE, font_size=48)
        self.play(Write(title2))
        self.play(FadeOut(title2))

        # காந்தப்புல மாற்றம் (Magnetic Shift)
        warning = Text("MAGNETIC RECALIBRATION DETECTED", color=RED).to_edge(UP)
        sun_angry = Circle(radius=2, color=RED, fill_opacity=0.8)
        flashes = Flash(sun_angry, color=RED, num_lines=30, flash_radius=2.5)
        
        self.play(Write(warning), Create(sun_angry))
        self.play(sun_angry.animate.scale(1.3), flashes, run_time=2)
        self.wait(1)
        self.play(FadeOut(VGroup(warning, sun_angry)))

        # --- ACT 3: THE INFERNO (The Great Escape) ---
        title3 = Text("ACT 3: THE INFERNO", color=RED_E, font_size=48)
        self.play(Write(title3))
        self.play(FadeOut(title3))

        # 12 விண்கலங்கள் தப்பித்தல்
        fleet_text = Text("12 EVACUATION SHIPS DEPARTING", font_size=30).to_edge(UP)
        ships = VGroup(*[Triangle(color=WHITE).scale(0.15).shift(DOWN*2 + RIGHT*x) for x in range(-3, 4)])
        explosion = Star(color=YELLOW, fill_opacity=1).scale(4)

        self.play(Write(fleet_text))
        self.play(Create(ships))
        self.play(ships.animate.shift(UP*8), FadeIn(explosion), run_time=4)
        self.wait(1)
        self.play(FadeOut(VGroup(fleet_text, ships, explosion)))

        # --- ACT 4: THE RETURN ---
        title4 = Text("ACT 4: THE RETURN", color=GREEN, font_size=48)
        self.play(Write(title4))
        self.play(FadeOut(title4))

        # 500 ஆண்டுகளுக்குப் பிறகு பூமி
        earth = Circle(radius=2, color=BLUE, fill_opacity=0.7)
        greenery = Annulus(inner_radius=0, outer_radius=2, color=GREEN, fill_opacity=0.4)
        quote = Text("We all return to light.", font_size=36, color=GOLD)

        self.play(Create(earth))
        self.play(FadeIn(greenery))
        self.wait(1)
        self.play(ReplacementTransform(VGroup(earth, greenery), quote))
        self.play(Indicate(quote))
        self.wait(3)

        # இறுதித் தலைப்பு
        end_credits = Text("LAVATHAR", font_size=60, color=GOLD)
        self.play(FadeIn(end_credits))
        self.play(end_credits.animate.scale(0.5).to_edge(UP))
