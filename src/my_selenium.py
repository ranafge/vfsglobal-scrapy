from selenium import webdriver

# Create a WebDriver instance for Chrome
driver = webdriver.Chrome()

# Example: Open a webpage
driver.get("https://www.example.com")

# Example: Print the title of the webpage
print(driver.title)

# Example: Close the browser
driver.quit()