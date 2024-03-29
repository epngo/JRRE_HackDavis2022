from flask import Flask, render_template,redirect,url_for,request,session,flash

import os
import sys
import re
import time

import PyPDF2
import NNforBookClass
app = Flask(__name__)
app.secret_key = "a"

@app.route('/')
def index():
    return render_template('greenhouse.html')


@app.route('/result',methods = ['POST', 'GET'])



def result():
   if request.method == 'POST':
      result = request.form
      # just to get the values easily
      readinglevel = request.values.get('readinglevel')
      BookRating = request.values.get('BookRating')
      BookName  = request.values.get('BookName')
      BookPDF = request.values.get('BookPDF')
      NNDec = request.values.get('NN')
      Classification =request.values.get('Classification')
      print(readinglevel) # use result ig and put the data here. 
      print(BookRating)
      print(BookName)
      print(BookPDF)

      wordLength = []
      pdfFileObj = open(BookPDF, 'rb')
      pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
      pages = pdfReader.numPages
      for i in range(pages):
          pdfFileObj = open(BookPDF, 'rb')
          pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
          pageObj = pdfReader.getPage(i)
          data = pageObj.extractText()
          text = data
          texts = len(text.split())
          totalwords = texts + 1
          wordLength.append(len(text))

      time.sleep(1)
      print(totalwords)
      avgWordLength = sum(wordLength) / totalwords
      print(avgWordLength)

      returnEntry = [float(BookRating),[totalwords,avgWordLength]]
      # append returnEntry
      NNforBookClass.allReturns.append(returnEntry)
      

      for a in range(len(NNforBookClass.allReturns)):
        
        NNforBookClass.varAvgArr[a] = NNforBookClass.getAvgInArraySpot(a)
        if( NNDec =="YES" or NNDec =="yes"):
            weightsTemp = NNforBookClass.perceptron(NNforBookClass.currentWeights,NNforBookClass.allReturns)
            NNforBookClass.currentWeights = weightsTemp

        if(Classification == "YES" or Classification =="yes"):
             rating = 0
             for z in range(len(NNforBookClass.currentWeights)):
                rating = rating + NNforBookClass.currentWeights[z]*returnEntry[1][z]



      print("Rating is ",rating)
      return render_template("result.html",result = range(rating))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')