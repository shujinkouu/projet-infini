from bs4 import BeautifulSoup
import webview

#html_doc = """<!doctype html>
#soup = BeautifulSoup(html_doc, 'html.parser')

with open("C:\\Users\\Asus\\Desktop\\OpenLayer\\test.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

webview.create_window("soup", html=soup.prettify())
webview.start()
