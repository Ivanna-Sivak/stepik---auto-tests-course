link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"


def test_add_to_basket_button(browser):
    try:
        browser.get(link)
        browser.find_element_by_css_selector(".btn-add-to-basket")
        result = True
    except:
        result = False
    assert result is True, "Button not found"
