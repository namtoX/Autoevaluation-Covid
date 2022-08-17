from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
Window.fullscreen = False
Window.size = (460, 660)
kv = """
#:import Clock kivy.clock.Clock
ScreenManager:
    FirstScreen:
    UploadScreen:
    Signup:
    hello:
    Aboutus:
    UploadScreen1:
    UploadScreen2:      
    UploadScreen3:
    UploadScreen4:
    UploadScreen5: 
    ResultScreen1:
    ResultScreen2:
    LoadingScreen:
<FirstScreen>:   
    name : 'FirstScreen'
    
    Image:
        source : 'haa.jpg'   
    MDLabel:
        text:f"[font=Arial]B I E N V E N U E ![/font]"
        markup: True
        pos_hint: {"center_x": 0.5, "center_y": 0.94}
        text_color :0, 0, 0, 1
        font_style: "H4"
        opacity: 0.85
<UploadScreen>:   
    name : 'upload'
    Image:
        source : 'back1.png'         
    MDRoundFlatButton:
        text : 'Créer un compte'
        pos_hint: {'center_x':0.5,'center_y':0.07}
        md_bg_color : (252/255, 129/255, 141/255, 1)
        text_color: (1, 1, 1, 1)
        on_press: 
            root.manager.current = 'signup' 
    MDIconButton
        icon: 'about.png'
        pos_hint: {"center_x": 0.065, "center_y":0.06}
        user_font_size: '25sp'
        on_press:
            root.manager.current = 'aboutus'

<Aboutus>:   
    name : 'aboutus'
    Image:
        source : 'aboutus.png'
        allow_stretch: True
        user_font_size: '25sp' 
    MDIconButton
        icon: 'main.png'
        pos_hint: {"center_x": 0.06, "center_y":0.06}
        user_font_size: '25sp'
        on_press: root.manager.current = 'upload'
<Signup>:   
    name : 'signup'
    Image:
        source : 'sign.png'
        allow_stretch: True
        user_font_size: '25sp'
    MDTextField:
        id: email
        icon_right: "email"
        hint_text: 'Email'
        helper_text: "e.g: adam@domain"
        helper_text_mode: "on_focus"
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        current_hint_text_color: 0, 0, 0, 1
        color_module:  'Custom'
        size_hint_x: 0.8
    MDTextField:
        id: name
        hint_text: 'Nom'
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        current_hint_text_color: 0, 0, 0, 1
        color_module:  'Custom'
        size_hint_x: 0.8
    MDTextField:
        id: password
        icon_right: 'lock'
        hint_text: 'Mot clé'
        helper_text: "e.g: ********"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        helper_text_mode: "on_focus"
        current_hint_text_color: 0, 0, 0, 1
        size_hint_x: 0.8
        password: True
    MDTextField:
        id: gender
        hint_text: 'Genre'
        helper_text: "e.g: Homme ou femme"
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        helper_text_mode: "on_focus"
        current_hint_text_color: 0, 0, 0, 1
        color_module:  'Custom'
        size_hint_x: 0.8
    MDTextField:
        id: age
        hint_text: 'Age'
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        current_hint_text_color: 0, 0, 0, 1
        color_module:  'Custom'
        size_hint_x: 0.8
    MDIconButton:
        icon:'gmail.png'
        pos_hint: {"center_x": 0.3, "center_y":0.184}
        
    MDIconButton:
        icon:'ig.png'
        pos_hint: {"center_x": .5, "center_y":0.15}
        on_press:
            app.ig()
    MDIconButton:
        icon:'fb.png'
        pos_hint: {"center_x": .7, "center_y":0.11}
    MDRoundFlatButton:
        text : 'Soumettre'
        pos_hint: {'center_x':0.77,'center_y':0.22}
        md_bg_color : (252/255, 129/255, 141/255, 1)
        text_color: (1, 1, 1, 1)
        on_press: 
            root.manager.current = 'hello'
    MDIconButton
        icon: 'main.png'
        pos_hint: {"center_x": 0.06, "center_y":0.06}
        user_font_size: '25sp'
        on_press: root.manager.current = 'upload'
<Hello>:   
    name : 'hello'
    Image:
        source : 'termes.png'
    MDRoundFlatButton:
        text : 'Commencez'
        pos_hint: {'center_x':0.5,'center_y':0.07}
        md_bg_color : (1, 155/255, 155/255, 1)
        text_color: (1, 1, 1, 1)
        on_press: 
            root.manager.current = 'upload1'
    MDIconButton
        icon: 'main.png'
        pos_hint: {"center_x": 0.06, "center_y":0.05}
        user_font_size: '25sp'
        on_press: root.manager.current = 'signup'
<UploadScreen1>:   
    name : 'upload1'
    MDScreen :
        Image:
            source : 'fatigue.png'
            allow_stretch: True
        MDIconButton
            icon: 'no.png'
            pos_hint: {"center_x": 0.75, "center_y":0.25}
            user_font_size: '25sp'
            on_press: root.manager.current = 'upload2'  
        MDIconButton
            icon: 'main.png'
            pos_hint: {"center_x": 0.06, "center_y":0.06}
            user_font_size: '25sp'
            on_press: root.manager.current = 'upload'
        MDIconButton
            icon: 'yes.png'
            pos_hint: {"center_x": 0.25, "center_y":0.25}
            user_font_size: '25sp'
            on_press: root.manager.current = 'upload2' 
            on_press: app.yes1()
<UploadScreen2>:
    name : 'upload2'
    MDScreen :
        Image:
            source : 'breath.png'
            allow_stretch: True
        MDIconButton
            icon: 'no.png'
            pos_hint: {"center_x": 0.75, "center_y":0.25}
            user_font_size: '25sp' 
            on_press: root.manager.current = 'upload3'
        
        MDIconButton
            icon: 'yes.png'
            pos_hint: {"center_x": 0.25, "center_y":0.25}
            user_font_size: '25sp'
            on_press: app.yes2()
            on_press: root.manager.current = 'upload3'
        MDIconButton
            icon: 'main.png'
            pos_hint: {"center_x": 0.06, "center_y":0.06}
            user_font_size: '25sp'
            on_press: root.manager.current = 'upload1'
<UploadScreen3>:
    name : 'upload3'
    MDScreen :
        Image:
            source : 'fever.png'
            allow_stretch: True
        MDIconButton
            icon: 'no.png'
            pos_hint: {"center_x": 0.75, "center_y":0.25}
            user_font_size: '25sp' 
            on_press: root.manager.current = 'upload4'
        MDIconButton
            icon: 'yes.png'
            pos_hint: {"center_x": 0.25, "center_y":0.25}
            user_font_size: '25sp'
            on_press: app.yes3()
            on_press: root.manager.current = 'upload4'
        MDIconButton
            icon: 'main.png'
            pos_hint: {"center_x": 0.06, "center_y":0.06}
            user_font_size: '25sp'
            on_press: root.manager.current = 'upload2'
<UploadScreen4>:
    name : 'upload4'
    MDScreen :
        Image:
            source : 'cough.png'
            allow_stretch: True
        MDIconButton:
            icon: 'no.png'
            pos_hint: {"center_x": 0.75, "center_y":0.25}
            user_font_size: '25sp' 
            on_press: root.manager.current = 'upload5'
        MDIconButton
            icon: 'yes.png'
            pos_hint: {"center_x": 0.25, "center_y":0.25}
            user_font_size: '25sp'
            on_press: app.yes4()
            on_press: root.manager.current = 'upload5'
        MDIconButton
            icon: 'main.png'
            pos_hint: {"center_x": 0.06, "center_y":0.06}
            user_font_size: '25sp'
            on_press: root.manager.current = 'upload3'
<UploadScreen5>: 
    name : 'upload5'
    MDScreen :
        Image:
            source : 'taste.png'
            allow_stretch: True
        MDIconButton
            icon: 'no.png'
            pos_hint: {"center_x": 0.75, "center_y":0.25}
            user_font_size: '25sp' 
            on_press:  
                root.manager.current = 'load'
                
        MDIconButton
            icon: 'yes.png'
            pos_hint: {"center_x": 0.25, "center_y":0.25}
            user_font_size: '25sp'
            on_press: 
                app.yes5()
                root.manager.current = 'load'
        MDIconButton
            icon: 'main.png'
            pos_hint: {"center_x": 0.06, "center_y":0.06}
            user_font_size: '25sp'
            on_press: root.manager.current = 'upload4'
<ResultScreen1>:      
    name : 'result1'
    MDScreen :
        Image:
            source: "bad.png"
        MDIconButton
            icon: 'close.png'
            pos_hint: {"center_x": 0.94, "center_y":0.97}
            user_font_size: '25sp'
            on_press: app.close()
<ResultScreen2>:       
    name : 'result2'
    MDScreen :    
        Image:
            source: "bon.png"
        MDIconButton
            icon: 'close.png'
            pos_hint: {"center_x": 0.94, "center_y":0.97}
            user_font_size: '25sp'
            on_press: app.close()
<LoadingScreen>:
    name : 'load'
    MDScreen :
        Image:
            source : 'loading.png'
        Image:
            source : 'load.gif'
            pos_hint: {'center_x':.5,'center_y':0.09}
            anim_delay : 0
            allow_stretch : True        
"""
class UploadScreen(Screen):
    pass
class FirstScreen(Screen):
    def switch(self, *args):
        self.parent.current = 'upload'
    def on_enter(self, *args):
        Clock.schedule_once(self.switch, 4)
class Signup(Screen):
    pass
class hello(Screen):
    pass
class Aboutus(Screen):
    pass
class UploadScreen1(Screen):
    pass
class UploadScreen2(Screen):
    pass
class UploadScreen3(Screen):
    pass
class UploadScreen4(Screen):
    pass
class UploadScreen5(Screen):
    pass
class LoadingScreen(Screen):
    def switch(self, *args):
        self.parent.current = 'result1'            
    def on_enter(self, *args):
        Clock.schedule_once(self.switch, 6)
class ResultScreen1(Screen):
    pass
class ResultScreen2(Screen):
    pass
# Create the screen manager
sm = ScreenManager()
sm.add_widget(UploadScreen(name='FirstScreen'))
sm.add_widget(UploadScreen(name='upload'))
sm.add_widget(UploadScreen(name='signup'))
sm.add_widget(UploadScreen1(name='aboutus'))
sm.add_widget(UploadScreen(name='hello'))
sm.add_widget(UploadScreen1(name='upload1'))
sm.add_widget(UploadScreen2(name='upload2'))
sm.add_widget(UploadScreen3(name='upload3'))
sm.add_widget(UploadScreen4(name='upload4'))
sm.add_widget(UploadScreen5(name='upload5'))
sm.add_widget(ResultScreen1(name='result1'))
sm.add_widget(ResultScreen2(name='result2'))
sm.add_widget(LoadingScreen(name='load'))

class Predictor(MDApp):
    clickcount = 0
    def build(self):
        screen = Builder.load_string(kv)
        return screen
    def close(self):
        Window.close()
    def ig(self):
        from selenium import webdriver
        webdriver = webdriver.Firefox()
        webdriver.get('https://www.instagram.com/p._.redictor/')
    def yes1(self):
        self.clickcount += 45
    def yes2(self):
        self.clickcount += 31
    def yes3(self):
        self.clickcount += 83
    def yes4(self):
        self.clickcount += 82
    def yes5(self):
        self.clickcount += 40
        



if __name__ == "__main__":

    Predictor().run()
#symptoms :
