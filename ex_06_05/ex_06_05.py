text = "X-DSPAM-Confidence:    0.8475"
fltText = text.find(':')
print(float(text[fltText+1:].lstrip()))