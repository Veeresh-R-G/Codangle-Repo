from termcolor import colored 
import emoji 
 
print('Hey, will you be the INPUT to my life with YES! \nI will make your life colorful and add magic to it as OUTPUT till your last breath!') 
print('I will give you memories and cherishable moments to live with!') 
print('I will make your life easier too!') 
print('Forget to tell about me, I am intelligent. You do not have to declare your emotions(input type) to me like you declare to others(languages).') 
print('I am easier to learn! I am faster and now into everything. \nAnd I am growing fast too! \nPeople love me these days alot.') 
print('You have two options: Yes or No.') 
print(emoji.emojize('Take a minute to think before saying No. Coz you will be regretting for not entering in my life! :wink:\n',use_aliases=True)) 
inp = input('If you love to enter in my life. Please enter Yes (Remember, I am senstive. Enter exactly as I mentioned):') 
 
if inp == 'Yes': 
     
    name = input('Now enter your name. I will show you how much I am fond of you! : ') 
    heart= ('\n'.join([''.join([(name[(x-y) % len(name)]  
                             if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ')  
                            for x in range(-30, 30)]) for y in range(30, -30, -1)])) 
    print(emoji.emojize(':kissing_heart:',use_aliases=True)) 
    print(colored(heart , 'red')) 
     
elif inp == 'No': 
    print(emoji.emojize('I am Heart Broken :cry:',use_aliases=True)) 
     
else: 
    print(emoji.emojize('Sorry, I can not understand your Emotion. I told you I am sensitive(case-senstive), now I am unable understand your thoughts :confused:', use_aliases=True)) 