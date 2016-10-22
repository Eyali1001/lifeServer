
signup:
r = requests.post("https://e79e7715.ngrok.io/signup",data={'t':'p','u':'eyal mer','p':'1234','b':s,'a':16,'g':'m'})
adding diagnosis:
r = requests.post("https://dc018499.ngrok.io/",data={'u':'eyal mer','d':'very sick','c':'general'})

adding image to user:
r = requests.post("https://dc018499.ngrok.io/image",data={'u':'eyal mer','i':bitmap,'t':'post'})

getting image:
r = requests.post("https://dc018499.ngrok.io/image",data={'u':'eyal mer','t':'get'})
