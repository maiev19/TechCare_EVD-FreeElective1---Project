from datetime import date

from pyscript import document, window
from pyodide.ffi import create_proxy

get = document.getElementById
proxies = []   # we keep the event handlers here so Python doesn't delete them


def listen(element, event, function):
    proxy = create_proxy(function)
    proxies.append(proxy)
    element.addEventListener(event, proxy)


# show the current year in the footer
get("yr").textContent = str(date.today().year)


# ---------- mobile menu ----------
def toggle_menu(event):
    get("menu").classList.toggle("open")


listen(get("burger"), "click", toggle_menu)
