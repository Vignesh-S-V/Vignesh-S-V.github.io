from manim import *
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
from gtts import gTTS
import os

# 1. அனிமேஷன் உருவாக்கும் பகுதி (Manim Scene)
class LavatharAnimation(Scene):
    def construct(self):
        # பின்னணி வண்ணம்
        self.camera.background_color = "#000000"

        # தலைப்பு அனிமேஷன்
        title = Text("LAVATHAR", font_size=72, color=GOLD)
        subtitle = Text("The Sun's Children", font_size=36, color=WHITE).next_to(title, DOWN)
        
        # தோன்றும் முறை
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))

        # சூரியன் மற்றும் பிளாஸ்மா அனிமேஷன் (உதாரணத்திற்கு)
        sun = Circle(radius=2, color=YELLOW, fill_opacity=0.8)
        sun.set_glow_factor(1)
        plasma_waves = Annulus(inner_radius=2, outer_radius=2.5, color=ORANGE, fill_opacity=0.5)
        
        self.play(Create(sun))
        self.play(sun.animate.scale(1.2), RateFuncs.wiggle(plasma_waves))
        
        # டெக்ஸ்ட் கன்டென்ட் அனிமேஷன்
        description = Text(
            "Inside the Sun's core at $15.7$ million Kelvin", 
            font_size=24, 
            t2c={"$15.7$": RED}
        )
        self.play(Write(description))
        self.wait(2)

# 2. டெக்ஸ்ட்டை ஒலியாக மாற்றும் செயல்பாடு
def create_voiceover(text, filename="voiceover.mp3"):
    tts = gTTS(text=text, lang='en') # அல்லது 'ta' தமிழுக்கு
    tts.save(filename)
    return filename

# 3. வீடியோ மற்றும் ஆடியோவை இணைக்கும் மெயின் பங்க்ஷன்
def generate_full_video(script_text):
    print("அனிமேஷன் உருவாக்கப்படுகிறது...")
    # Manim அனிமேஷனை இயக்குகிறது (கமாண்ட் லைன் மூலம்)
    os.system("manim -pql main.py LavatharAnimation")
    
    print("ஆடியோ உருவாக்கப்படுகிறது...")
    voice_file = create_voiceover(script_text)
    
    # இறுதி வீடியோவை உருவாக்குதல்
    # Manim உருவாக்கிய வீடியோ கோப்பை இங்கே இணைக்க வேண்டும்
    # (பொதுவாக media/videos/... என்ற ஃபோல்டரில் இருக்கும்)
    video_path = "media/videos/main/480p15/LavatharAnimation.mp4"
    
    if os.path.exists(video_path):
        video = VideoFileClip(video_path)
        audio = AudioFileClip(voice_file)
        final_video = video.set_audio(audio)
        final_video.write_videofile("lavathar_final_output.mp4", fps=24)
        print("வெற்றிகரமாக வீடியோ உருவாக்கப்பட்டது: lavathar_final_output.mp4")
    else:
        print("வீடியோ கோப்பு கண்டறியப்படவில்லை!")

# ஸ்கிரிப்ட் கன்டென்ட்
script_content = "Welcome to Sol City Prime. A civilization living inside the heart of fire."

if __name__ == "__main__":
    generate_full_video(script_content)