import time
import unittest
import bcrypt
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from provider_vault_django_app.models import Users
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class RegisterTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        """
        Runs once before all tests.
        """
        super().setUpClass()
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        cls.browser = webdriver.Chrome(options=chrome_options)

    @classmethod
    def tearDownClass(cls):
        """
        Runs once after all tests.
        """
        cls.browser.quit()
        super().tearDownClass()

    def setUp(self):
        """
        Runs before each test.
        Clears all input fields.
        """
        self.browser.get(f"{self.live_server_url}/register/")

    def test_password_first_check_no_character(self):
        """Check if password is minimum length of 8 characters"""
        password_input = self.browser.find_element(By.ID, "password")
        password_check_msg = self.browser.find_element(By.ID, "password_check_msg")

        password_input.send_keys("the")
        time.sleep(0.5)
        self.assertEqual(
            "Password must be at least 8 characters long!", password_check_msg.text
        )

    def test_password_first_check_eight_characters(self):
        """Check if password is minimum length of 8 characters"""
        password_input = self.browser.find_element(By.ID, "password")
        password_check_msg = self.browser.find_element(By.ID, "password_check_msg")

        password_input.send_keys("Password")
        time.sleep(0.5)
        self.assertNotEqual(
            "Password must be at least 8 characters long!", password_check_msg.text
        )

    def test_password_second_check_all_lowercase(self):
        """Check if password contains both uppercase and lowercase letters"""
        password_input = self.browser.find_element(By.ID, "password")
        password_check_msg = self.browser.find_element(By.ID, "password_check_msg")

        password_input.send_keys("password1!")
        time.sleep(0.5)
        self.assertEqual(
            "Password must contain both uppercase and lowercase letters!",
            password_check_msg.text,
        )

    def test_password_second_check_all_uppercase(self):
        """Check if password contains both uppercase and lowercase letters"""
        password_input = self.browser.find_element(By.ID, "password")
        password_check_msg = self.browser.find_element(By.ID, "password_check_msg")

        password_input.send_keys("PASSWORD1!")
        time.sleep(0.5)
        self.assertEqual(
            "Password must contain both uppercase and lowercase letters!",
            password_check_msg.text,
        )

    def test_password_second_check_mixed_case(self):
        """Check if password contains both uppercase and lowercase letters"""
        password_input = self.browser.find_element(By.ID, "password")
        password_check_msg = self.browser.find_element(By.ID, "password_check_msg")

        password_input.send_keys("Password1!")
        time.sleep(0.5)
        self.assertNotEqual(
            "Password must contain both uppercase and lowercase letters!",
            password_check_msg.text,
        )

    def test_password_third_check_no_number(self):
        """Check if password includes at least one number"""
        password_input = self.browser.find_element(By.ID, "password")
        password_check_msg = self.browser.find_element(By.ID, "password_check_msg")

        password_input.send_keys("Password!")
        time.sleep(0.5)
        self.assertEqual(
            "Password must include at least one number!", password_check_msg.text
        )

    def test_password_third_check_with_number(self):
        """Check if password includes at least one number"""
        password_input = self.browser.find_element(By.ID, "password")
        password_check_msg = self.browser.find_element(By.ID, "password_check_msg")

        password_input.send_keys("Password1!")
        time.sleep(0.5)
        self.assertNotEqual(
            "Password must include at least one number!", password_check_msg.text
        )

    def test_password_fourth_check_no_special_character(self):
        """Check if password includes at least one special character (!@#$%^&*)"""
        password_input = self.browser.find_element(By.ID, "password")
        password_check_msg = self.browser.find_element(By.ID, "password_check_msg")

        password_input.send_keys("Password1")
        time.sleep(0.5)
        self.assertEqual(
            "Password must include at least one special character (!@#$%^&*)!",
            password_check_msg.text,
        )

    def test_password_fourth_check_with_special_character_not_listed(self):
        """Check if password includes at least one special character (!@#$%^&*)"""
        password_input = self.browser.find_element(By.ID, "password")
        password_check_msg = self.browser.find_element(By.ID, "password_check_msg")

        password_input.send_keys("Password1+")
        time.sleep(0.5)
        self.assertEqual(
            "Password must include at least one special character (!@#$%^&*)!",
            password_check_msg.text,
        )

    def test_password_fourth_check_with_special_character(self):
        """Check if password includes at least one special character (!@#$%^&*)"""
        password_input = self.browser.find_element(By.ID, "password")
        password_check_msg = self.browser.find_element(By.ID, "password_check_msg")

        password_input.send_keys("Password1!")
        time.sleep(0.5)
        self.assertNotEqual(
            "Password must include at least one special character (!@#$%^&*)!",
            password_check_msg.text,
        )

    def test_password_all_checks_pass(self):
        """Check if password meets all criteria"""
        password_input = self.browser.find_element(By.ID, "password")
        password_check_msg = self.browser.find_element(By.ID, "password_check_msg")

        password_input.send_keys("Password1!")
        time.sleep(0.5)
        self.assertEqual("", password_check_msg.text)

    def test_passwords_mismatch(self):
        """Check if passwords do not match"""
        password_input = self.browser.find_element(By.ID, "password")
        confirm_password_input = self.browser.find_element(By.ID, "confirm_password")
        password_match_msg = self.browser.find_element(By.ID, "password_match_msg")

        password_input.send_keys("bptaTvji!")
        confirm_password_input.send_keys("bptaTvji")
        time.sleep(0.5)
        self.assertEqual("Passwords do not match!", password_match_msg.text)

    def test_passwords_match(self):
        """Check if passwords match"""
        password_input = self.browser.find_element(By.ID, "password")
        confirm_password_input = self.browser.find_element(By.ID, "confirm_password")
        password_match_msg = self.browser.find_element(By.ID, "password_match_msg")

        password_input.send_keys("Password1!")
        confirm_password_input.send_keys("Password1!")
        time.sleep(0.5)
        self.assertEqual("", password_match_msg.text)

    def test_password_submit_error_messages(self):
        """Check if password check message is empty when both fields are empty"""
        first_name = self.browser.find_element(By.ID, "first_name")
        last_name = self.browser.find_element(By.ID, "last_name")
        email = self.browser.find_element(By.ID, "email")
        password = self.browser.find_element(By.ID, "password")
        confirm_password = self.browser.find_element(By.ID, "confirm_password")
        register_button = self.browser.find_element(By.ID, "register_form_button")

        first_name.send_keys("John")
        last_name.send_keys("Doe")
        email.send_keys("john.doe@example.com")
        password.send_keys("Hayhbjio232")
        confirm_password.send_keys("Hayhbjio232")
        time.sleep(0.5)
        register_button.click()

        alert = self.browser.switch_to.alert
        alert_text = alert.text
        self.assertEqual(
            "There are error messages displayed. Please fix these issues", alert_text
        )
        alert.accept()

    def test_password_submit_correct(self):
        """Check if password check message is empty when both fields are empty"""
        first_name = self.browser.find_element(By.ID, "first_name")
        last_name = self.browser.find_element(By.ID, "last_name")
        email = self.browser.find_element(By.ID, "email")
        password = self.browser.find_element(By.ID, "password")
        confirm_password = self.browser.find_element(By.ID, "confirm_password")
        register_button = self.browser.find_element(By.ID, "register_form_button")

        first_name.send_keys("John")
        last_name.send_keys("Doe")
        email.send_keys("john.doe@example.com")
        password.send_keys("Hayhbjio232!")
        confirm_password.send_keys("Hayhbjio232!")
        time.sleep(0.5)
        register_button.click()

        WebDriverWait(self.browser, 10).until(
            EC.url_changes(f"{self.live_server_url}/register/")
        )

        redirected_url = self.browser.current_url
        self.assertEqual(f"{self.live_server_url}/login/", redirected_url)


class LoginTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        """
        Prequisites for all tests. Only runs once.
        """
        super().setUpClass()
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        cls.browser = webdriver.Chrome(options=chrome_options)
        password_hash = bcrypt.hashpw(
            "TestPassword1!".encode("utf-8"), bcrypt.gensalt()
        )

        cls.user = Users.objects.create(
            email="test@example.com", password_hash=password_hash, user_type="user"
        )

    @classmethod
    def tearDownClass(cls):
        """
        Runs once after all tests.
        """
        cls.browser.quit()
        super().tearDownClass()

    def setUp(self):
        """
        Runs before each test.
        Clear all input fields.
        """
        self.browser.get(f"{self.live_server_url}/login/")

    def test_show_password_button(self):
        """Check if show password button works"""
        password_input = self.browser.find_element(By.ID, "login_password")
        show_password_button = self.browser.find_element(By.ID, "toggle_password")

        password_input.send_keys("Password1!")
        time.sleep(0.5)

        show_password_button.click()
        time.sleep(0.5)
        self.assertEqual("text", password_input.get_attribute("type"))

        show_password_button.click()
        time.sleep(0.5)
        self.assertEqual("password", password_input.get_attribute("type"))

    def test_login_incorrect_email(self):
        """Check if login fails with incorrect email"""
        email_input = self.browser.find_element(By.ID, "email")
        password_input = self.browser.find_element(By.ID, "login_password")
        login_button = self.browser.find_element(By.ID, "login_form_button")
        error_message = self.browser.find_element(By.ID, "login_form_error")
        email_input.send_keys("test@example.com")
        password_input.send_keys("TestPassword2!")
        time.sleep(0.5)

        login_button.click()
        WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element(
                (By.ID, "login_form_error"), "Invalid email or password!"
            )
        )
        self.assertEqual("Invalid email or password!", error_message.text)

    def test_login_correct_auth(self):
        """Check if login succeeds with correct email and password"""
        email_input = self.browser.find_element(By.ID, "email")
        password_input = self.browser.find_element(By.ID, "login_password")
        login_button = self.browser.find_element(By.ID, "login_form_button")
        email_input.send_keys("test@example.com")
        password_input.send_keys("TestPassword1!")
        time.sleep(0.5)

        login_button.click()
        WebDriverWait(self.browser, 10).until(
            EC.url_changes(f"{self.live_server_url}/login/")
        )
        self.assertEqual(f"{self.live_server_url}/", self.browser.current_url)


if __name__ == "__main__":
    unittest.main()
