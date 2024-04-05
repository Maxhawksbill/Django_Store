from multiprocessing.pool import ThreadPool

from selenium import webdriver


def test_valid_login():
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome()

    # Open localhost admin panel
    driver.get('http://localhost:8000/admin/')

    # Find input with name username
    username_element = driver.find_element(
        by='xpath',
        value='//input[@name="username"]'
    )

    username_element.send_keys('vitaliipavliuk')
    print("I've entered the username")

    # Find input with name password
    password_element = driver.find_element(
        by='xpath',
        value='//input[@name="password"]'
    )

    password_element.send_keys('gddgdd')
    print("I've entered the password")

    # Find the Login button
    login_button = driver.find_element(
        by='xpath',
        value='//input[@type="submit"]'
    )
    login_button.click()

    # Check that we are on chango admin
    welcome_text = driver.find_element(
        by='id', value='user-tools'
    ).text

    assert "welcome, vitaliipavliuk" in welcome_text.lower()
    print("I'm on the admin panel")

    print("I'm done")


def test_invalid_login():
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome()

    # Open localhost admin panel
    driver.get('http://localhost:8000/admin/')

    # Find input with name username
    username_element = driver.find_element(
        by='xpath', value='//input[@name="username"]')
    username_element.send_keys('vitaliipavliuk')
    print("I've entered the username")

    # Find input with name password
    password_element = driver.find_element(
        by='xpath', value='//input[@name="password"]')
    password_element.send_keys('gddgdd!')
    print("I've entered the password")

    # Find the Login button
    login_button = driver.find_element(
        by='xpath', value='//input[@type="submit"]')
    login_button.click()

    # Check that we are on django admin
    try:
        welcome_text = driver.find_element(by='id', value='user-tools').text
        raise AssertionError("I'm not supposed to be here")
    except BaseException:
        print("I'm not on the admin panel")

    print("I'm done")


if __name__ == '__main__':
    pool = ThreadPool(processes=2)

    results = []
    for func in [test_valid_login, test_invalid_login]:
        result = pool.apply_async(func)

        results.append(result)

    for result in results:
        result.get()

    pool.close()
