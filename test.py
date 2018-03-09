import nltk
import csv
import pandas
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.cross_validation import StratifiedKFold, cross_val_score, train_test_split
import string
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

from gtts import gTTS
import os

import imaplib
import email
import email.header
import time
import datetime
from threading import Thread


def split_into_lemmas_(sentence):
    wordnet_lemmatizer = WordNetLemmatizer()
    porter_stemmer = PorterStemmer()
    exclude = set(string.punctuation)
    sentence = ''.join(ch for ch in sentence if ch not in exclude)
    sentence= sentence.lower()
    tokens = nltk.word_tokenize(sentence)
    tokens=[porter_stemmer.stem(word) for word in tokens]
    return [wordnet_lemmatizer.lemmatize(word) for word in tokens]

def response(msg):

    tts = gTTS(text='you have a '+msg+'request', lang='en')
    tts.save("response.mp3")
    os.system("response.mp3")











def classify(mail):

    #transorfmming and filtering input data
    print (mail)
    bow4 = bow_transformer.transform([mail])

    mail=split_into_lemmas_(mail)
    tfidf4 = tfidf_transformer.transform(bow4)


    prediction=meeting_detector.predict(tfidf4)[0]
    print ('predicted:',prediction )
    if(prediction!='ham'):
        response(prediction)



#mail='i want to meet you and discuss with you'
#classify(mail)

#mail='Kindly change the time of the meeting'
#classify(mail)





# Use 'INBOX' to read inbox.  Note that whatever folder is specified,
# after successfully running this script all emails in that folder
# will be marked as read.


class MyThread(Thread):
    def __init__(self, mail):
        ''' Constructor. '''
        Thread.__init__(self)
        self.val = mail

    def run(self):
        while True:
            process_mailbox(self.val)
            #print ("loop completed")

            time.sleep(5)



def process_mailbox(mail):

    mail.list()
    mail.select('inbox')

    result, data = mail.uid('search', None, "UNSEEN")  # (ALL/UNSEEN)
    i = len(data[0].split())

    for x in range(i):
        latest_email_uid = data[0].split()[x]
        result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        # result, email_data = conn.store(num,'-FLAGS','\\Seen')
        # this might work to set flag to seen, if it doesn't already
        raw_email = email_data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)

        # Header Details
        date_tuple = email.utils.parsedate_tz(email_message['Date'])
        if date_tuple:
            local_date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
            local_message_date = "%s" % (str(local_date.strftime("%a, %d %b %Y %H:%M:%S")))
        email_from = str(email.header.make_header(email.header.decode_header(email_message['From'])))
        email_to = str(email.header.make_header(email.header.decode_header(email_message['To'])))
        subject = str(email.header.make_header(email.header.decode_header(email_message['Subject'])))

        # Body details
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)

                body=body.decode('utf-8')
                #classifying the upcoming mail
                print('--------------')
                print(body)
                classify(body)

            else:
                continue


#################################

messages = pandas.read_csv('dataSet', sep='\t', quoting=csv.QUOTE_NONE, names=["label", "message"])

msg_train, msg_test, label_train, label_test = train_test_split(messages['message'], messages['label'], test_size=0,
                                                                    random_state=0)

    # print(msg_train)


   # Training the Classifier
bow_transformer = CountVectorizer(analyzer=split_into_lemmas_).fit(msg_train)
bow_transformer.min_df = 0.5

print(len(bow_transformer.vocabulary_))

messages_bow = bow_transformer.transform(msg_train)
tfidf_transformer = TfidfTransformer().fit(messages_bow)
messages_tfidf = tfidf_transformer.transform(messages_bow)

    # providing data and labels to the classifier
meeting_detector = MultinomialNB().fit(messages_tfidf, label_train)

##########################################################

def run(email, pw):
    '''
    messages = pandas.read_csv('dataSet', sep='\t', quoting=csv.QUOTE_NONE, names=["label", "message"])

    msg_train, msg_test, label_train, label_test = train_test_split(messages['message'], messages['label'], test_size=0,
                                                                    random_state=0)

    # print(msg_train)


    # Training the Classifier
    bow_transformer = CountVectorizer(analyzer=split_into_lemmas_).fit(msg_train)
    bow_transformer.min_df = 0.5

    print(len(bow_transformer.vocabulary_))

    messages_bow = bow_transformer.transform(msg_train)
    tfidf_transformer = TfidfTransformer().fit(messages_bow)
    messages_tfidf = tfidf_transformer.transform(messages_bow)

    # providing data and labels to the classifier
    meeting_detector = MultinomialNB().fit(messages_tfidf, label_train)
'''

    EMAIL_ACCOUNT = "l144083@lhr.nu.edu.pk"
#    EMAIL_ACCOUNT = email
    PASSWORD = "15987415"
#    PASSWORD = pw

    mail = imaplib.IMAP4_SSL('imap.gmail.com')

    mail.login(EMAIL_ACCOUNT, PASSWORD)

    mail.list()
    mail.select('inbox')

    vehshithread=MyThread(mail)

    vehshithread.start()

    vehshithread.join()

import gui_1
import sys
from PyQt4 import QtCore, QtGui

if __name__ == "__main__":
#    global MainWindow

    print("start test.py")

    print("calling gui 1")
    app = QtGui.QApplication(sys.argv)

    MainWindow = QtGui.QMainWindow()
    ui = gui_1.Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show ()


#    Home = QtGui.QMainWindow()
#    w_ui = gui_2.Ui_Home()
#    w_ui.setupUi(Home)
#    Home.show()

#    sys.exit(app.exec_())

    sys.exit(app.exec_())

def SignUpBtnCall(email, pw):
    print("Home Screen")
    run(email,pw)

#testM=pandas.DataFrame({'index':msg_test.index, 'message':msg_test.values})
#testL=pandas.DataFrame({'index':label_test.index, 'label':label_test.values})


#bowww = bow_transformer.transform(msg_test)
#testtfidf = tfidf_transformer.transform(bowww)

#all_predictions = spam_detector.predict(testtfidf)
#print(msg_test.size)

#print ('accuracy', accuracy_score(label_test, all_predictions))
#print ('confusion matrix\n', confusion_matrix(label_test, all_predictions))
#print ('(row=expected, col=predicted)')

