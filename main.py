import pandas as pd
import matplotlib.pyplot as plt
import re
import geocoder
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from wordcloud import WordCloud
from tkinter import *
from PIL import ImageTk ,Image



df = pd.read_csv('spam.csv',encoding='latin-1')
df = df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis = 1)

df.rename(columns = {'v1':'labels', 'v2':'message'}, inplace=True)
df.drop_duplicates(inplace=True)
df['label'] = df['labels'].map({'ham': 0, 'spam': 1})
df.drop(['labels'], axis=1, inplace=True)


import string


def preprocess_text(message):
    """
    Takes in a string of text, then performs the following:
    1. Remove all punctuation
    2. Remove all stopwords
    3. Returns a list of the cleaned text

    """
    # Check characters to see if they are in punctuation
    without_punc = [char for char in message if char not in string.punctuation]

    # Join the characters again to form the string.
    without_punc = ''.join(without_punc)

    # Now just remove any stopwords
    return [word for word in without_punc.split() if word.lower() not in stopwords.words('english')]

df['message'].head().apply(preprocess_text)



# spam_words = ' '.join(list(df[df['label'] == 1]['message']))
# spam_wc = WordCloud(width = 512,height = 512).generate(spam_words)
# plt.figure(figsize = (10, 8), facecolor = 'k')
# plt.imshow(spam_wc)
# plt.show()
#
# from wordcloud import WordCloud
#
# ham_words = ' '.join(list(df[df['label'] == 0]['message']))
# ham_wc = WordCloud(width = 512,height = 512).generate(ham_words)
# plt.figure(figsize = (10, 8), facecolor = 'k')
# plt.imshow(ham_wc)
# plt.show()


from sklearn.feature_extraction.text import CountVectorizer
x = df['message']
y = df['label']
cv = CountVectorizer()
x= cv.fit_transform(x)


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=0)


from sklearn.naive_bayes import MultinomialNB
classifier = MultinomialNB().fit(x_train, y_train)


from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
pred = classifier.predict(x_test)
# print(classification_report(y_test, pred))
# print()
# print('Confusion Matrix:\n',confusion_matrix(y_test, pred))
# print()
print('Accuracy : ',accuracy_score(y_test, pred))


# print the predictions
print(classifier.predict(x_test))

# print the actual values
print(y_test.values)


count=0
def sms():
    global count
    count+=1
    if count>=2:
        on_click()
    # creating a list of labels
    lab = ['not spam', 'spam']

    # perform tokenization
    x = cv.transform([e.get()]).toarray()

    # predict the text
    p = classifier.predict(x)

    # convert the words in string with the help of list
    s = [str(i) for i in p]
    a = int("".join(s))

    # show out the final result

    res = str("This is " + lab[a])
    # if len(res) >0:
    #     res.replace(res)

    global classification
    global bg1
    if lab[a]=='spam':
        bg1 = PhotoImage(file="pngwing.com (2).png")
        label1 = Label(root, image=bg1)
        label1.place(x=190, y=430)
        classification = Label(root, text=res, font=('helvetica', 30 , 'bold'), fg="red")
        classification.place(x=320,y=455)
    else:
        bg1 = PhotoImage(file="pngwing.com (1).png")
        label1 = Label(root, image=bg1)
        label1.place(x=190, y=430)
        classification = Label(root, text=res, font=('helvetica', 30, 'bold'), fg="green")
        classification.place(x=320,y=455)




def on_click():
    classification.destroy()
    # label1.destroy()

# ***************************ip Address code for gmail ********************************************

# opening and reading the file
with open("textip.txt") as fh:
    fstring = fh.readlines()
# declaring the regex pattern for IP addresses
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

lst = []
for line in fstring:
    lst.append(pattern.search(line))

res = []
for val in lst:
    if val != None :
        res.append(val)
# print(res)


mynm=str(res)
a= re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', mynm).group()

# *****************************************************************************************************
def location():
    ip = geocoder.ip(str(a))
    global l1,l2,l3,l4,l5,l6
    win=Toplevel(root)
    win.geometry("700x600")
    win.config(background="#dae6f6")
    value="#E80787"
    head = Label(win, text='IP Address Information', font=('Arial', 30, 'bold',), bg="#001DFA", fg="white")
    head.pack(pady=40, fill=X)
    l1 = Label(win, text=(a), font=('Helvetica', 40, 'bold'), fg='black',bg="#dae6f6")
    l1.pack(pady=20)
    l2=Label(win,text=("Country----->",ip.country),font=('Arial', 25 , 'bold'), fg = value,bg="#dae6f6")
    l2.pack()
    l3=Label(win,text=("City-------->",ip.city),font=('Arial', 25 , 'bold'), fg = value,bg="#dae6f6")
    l3.pack()
    l4=Label(win,text=("State------>",ip.state),font=('Arial', 25 , 'bold'), fg = value,bg="#dae6f6")
    l4.pack()
    l5=Label(win,text=("Longitude---->",ip.latlng),font=('Arial', 25 , 'bold'), fg = value,bg="#dae6f6")
    l5.pack()
    l6=Label(win,text=("Address--->",ip.address),font=('Arial', 25 , 'bold'), fg = value,bg="#dae6f6")
    l6.pack()

def click(event):
    e.config(state=NORMAL)
    e.delete(0,END)


root = Tk()
root.title('Feature Based Spam Email And IP Detector ')
root.geometry('800x700')
bg = PhotoImage(file="pk.png")
label1 = Label(root, image = bg)
label1.place(x = 0, y = 0)

head = Label(root, text='Email Spam Message Predictor',font=('Arial', 30 , 'bold',),bg="purple",fg="white")
head.pack(pady=40,fill=X)
e = Entry(root, width=800,borderwidth=5,font=('Arial 28'))
e.insert(0,"Enter message here")
e.config(state=DISABLED)
e.bind("<Button-1>",click)
e.pack(padx=15, pady=20)
b1 = Button(root, text = 'Predict', font=('Arial', 30 , 'bold'), fg = 'white', bg = 'red', command = sms,borderwidth=10)
b1.place(x=200,y=250)
b = Button(root, text = 'Location', font=('Arial', 30 , 'bold'), fg = 'white', bg = '#00FA3E', command =location,borderwidth=10)
b.place(x=450,y=250)
# b1=Button(root, text="Clear", font=('Arial', 40 , 'bold'),fg = 'white', bg = 'black',command=on_click,borderwidth=10)
# b1.place(x=550,y=150)
# b1.pack(padx=10,pady=20)
root.mainloop()
