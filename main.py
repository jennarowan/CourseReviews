import justpy as jp

def app():

    webpage = jp.QuasarPage(dark = True)
    
    h1 = jp.QDiv(a = webpage, text = "Analysis of Course Reviews", classes = "text-h2 text-center q-pt-md text-bold")
    p1 = jp.QDiv(a = webpage, text = "These graphs represent course review analysis", classes = "text-body-1 text-center q-pt-lg")
    
    return webpage

jp.justpy(app)