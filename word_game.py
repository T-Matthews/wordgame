#  from english_words import english_words_lower_alpha_set

from mimetypes import init
import random

wordlist=['Afghanistan','Albania','Algeria','American Samoa','Andorra',
'Angola','Anguilla','Antarctica','Antigua and Barbuda','Argentina','Armenia',
'Aruba','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh',
'Barbados','Belarus','Belgium','Belize','Benin','Bermuda','Bhutan','Bolivia',
'Bosnia and Herzegovina','Botswana','Bouvet Island','Brazil',
'Brunei Darussalam','Bulgaria','Burkina Faso','Burundi','Cambodia','Cameroon',
'Canada','Cape Verde','Cayman Islands','Central African Republic','Chad',
'Chile','China','Christmas Island','Colombia','Comoros','Congo','Cook Islands',
'Costa Rica','Ivory Coast', 'Croatia','Cuba','Cyprus','Czech Republic',
'Denmark','Djibouti','Dominica','Dominican Republic','East Timor','Ecuador',
'Egypt','El Salvador','Equatorial Guinea','Eritrea','Estonia','Ethiopia',
'Falkland Islands','Faroe Islands','Fiji','Finland','France','French Guiana',
'French Polynesia','Gabon','Gambia','Georgia','Germany','Ghana','Gibraltar',
'Greece','Greenland','Grenada','Guadeloupe','Guam','Guatemala','Guinea',
'Guinea-Bissau','Guyana','Haiti','Heard and McDonald Islands','Honduras',
'Hong Kong','Hungary','Iceland','India','Indonesia','Iran','Iraq','Ireland',
'Israel','Italy','Jamaica','Japan','Jordan','Kazakhstan','Kenya','Kiribati',
'North Korea','South Korea','Kuwait','Kyrgyzstan','Laos','Latvia','Lebanon',
'Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Macau',
'Macedonia','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta',
'Marshall Islands','Martinique','Mauritania','Mauritius','Mayotte','Mexico',
'Micronesia','Moldova','Monaco','Mongolia','Montserrat','Morocco','Mozambique',
'Myanmar','Namibia','Nauru','Nepal','Netherlands','New Caledonia',
'New Zealand','Nicaragua','Niger','Nigeria','Niue','Norfolk Island',
'Northern Mariana Islands','Norway','Oman','Pakistan','Palau','Panama',
'Papua New Guinea','Paraguay','Peru','Philippines','Pitcairn','Poland',
'Portugal','Puerto Rico','Qatar','Reunion','Romania','Russia','Rwanda',
'Saint Kitts and Nevis','Saint Lucia','Saint Vincent and The Grenadines',
'Samoa','San Marino','Saudi Arabia','Senegal','Seychelles','Sierra Leone',
'Singapore','Slovak Republic','Slovenia','Solomon Islands','Somalia',
'South Africa','Spain','Sri Lanka','St. Helena','Saint Pierre','Sudan',
'Suriname','Svalbard','Swaziland','Sweden','Switzerland','Syria','Taiwan',
'Tajikistan','Tanzania','Thailand','Togo','Tokelau', 'Tonga',
'Trinidad and Tobago','Tunisia','Turkey','Turkmenistan',
'Turks and Caicos Islands','Tuvalu','Uganda','Ukraine','United Arab Emirates',
'Great Britain', 'United States of America','Uruguay','Uzbekistan','Vanuatu',
'Vatican City','Venezuela','Viet Nam','British Virgin Islands',
'US Virgin Islands','Western Sahara','Yemen','Yugoslavia','Zaire','Zambia',
'Zimbabwe']
word = random.choice(wordlist).lower()
length=int(len(word))

class game:
    def __init__(self,word,length,guessed_ls=[],num_guessed=0,correct_ls=['_'],lives=7):
        self.word=word
        self.length=length
        self.guessed_ls=guessed_ls
        self.num_guessed=num_guessed
        self.correct_ls = correct_ls
        self.lives=lives
        
    def display(self):
        self.num_guessed=0
        self.correct_ls=[]
        for i in self.word:
            if i in self.guessed_ls:
                self.correct_ls.append(i)
                self.num_guessed+=1
            elif i ==" ":
                self.correct_ls.append('  ')
                print
            else:
                self.correct_ls.append('_')
        print('  '.join(self.correct_ls)+'\n')



    def guess(self):
            if self.num_guessed<((len(self.word))-(self.word.count(" "))):
                letter=input('What letter would you like to guess?\n').lower()
                if letter.isnumeric()==True or len(letter)>1:
                    print('\nYour input needs to be a single letter! Follow directions!\n')
                else:
                    if letter in self.guessed_ls:
                        print(f'You\'ve already guessed that value! Here are your guesses'+
                            f' so far:\n{self.guessed_ls}\n')
                    else:
                        self.guessed_ls.append(letter)

                        if letter in word:
                            print('Yep, good guess!\n')
                        else:
                            self.lives-=1
                            if self.lives==0:
                                print('Yikes! You ran out of guesses, better luck next time! The '
                f'correct country was {word}!')
                            
                            else:
                                print(f'Sorry, not in the word!\nYou have {self.lives} '
                                +'lives remaining!')
            else:
                print(f'Congrats! {self.word} is the correct country, '+
                'you\'ve won the game!')

def run():
    game1=game(word,length)
    play=input('Try guessing the name of a random country! '+
    'Want to play?\n [Y] Yes\n [N] No\n\n')
    if play.lower() == "y":
        while '_' in game1.correct_ls:
            if game1.lives==0:
                break 
            else:
                game1.display()
                game1.guess()
    else:
        print('Play the game next time by typing "Y"!')
       
run()