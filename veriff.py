from typing import Dict
import requests
from pylenium.driver import Pylenium
from pylenium.element import Element


class DocumentType:
    PASSPORT = "PASSPORT"
    DRIVERS_LICENSE = "DRIVERS_LICENSE"
    ID_CARD = "ID_CARD"
    RESIDENCE_PERMIT = "RESIDENCE_PERMIT"


class LaunchVia:
    IN_CONTEXT = "incontext"
    REDIRECT = "redirect"


def create_session(full_name: str, language: str, country: str, doc_type: str) -> str:
    payload = {
        "full_name": full_name,
        "lang": language,
        "document_country": country,
        "document_type": doc_type,
        "additionalData": {"isTest": False},
    }
    response = requests.post("https://demo.saas-3.veriff.me/", json=payload)
    if not response.ok:
        raise ValueError(f"Failed to create session. Status Code: {response.status_code}, Error: {response.text}")
    return response.json().get("sessionToken")


def get_session_config(session_token: str) -> Dict:
    headers = {"Authorization": f"Bearer {session_token}"}
    response = requests.get("https://magic.saas-3.veriff.me/api/v2/sessions", headers=headers)
    if not response.ok:
        raise ValueError(f"Failed to get session config. Status Code: {response.status_code}, Error: {response.text}")
    return response.json()


class VeriffUI:
    def __init__(self, py: Pylenium):
        self.py = py

    def visit(self) -> "VeriffUI":
        self.py.visit("https://demo.saas-3.veriff.me/")
        return self

    def enter_full_name(self, full_name: str) -> Element:
        fullname_field = self.py.get("[name='name']")
        return fullname_field.clear().type(full_name)

    def select_language(self, language: str) -> Element:
        """The dropdown is actually a button element that opens a list under script elements.

        Poor UI design and not accessible. RAISE AS ISSUE!
        """
        dropdown = self.py.get("[name='language']")
        dropdown.click()
        language_options = self.py.find("ul[id='downshift-0-menu'] > li")

        for option in language_options:
            if option.text() == language:
                option.click()
                break
        return dropdown

    def select_country(self, country: str) -> Element:
        country_field = self.py.get("[name='documentCountry']")
        country_field.type(country)
        country_options = self.py.find("ul[id='downshift-1-menu'] > li")
        country_options[0].click()
        return country_field

    def select_document_type(self, document_type: str) -> Element:
        dropdown = self.py.get("[name='documentType']")
        dropdown.click()
        document_options = self.py.find("ul[id='downshift-2-menu'] > li")
        for option in document_options:
            if option.text() == document_type:
                option.click()
                break
        return dropdown

    def select_launch_via(self, launch_via: str) -> Element:
        launch = launch_via.lower()
        if launch in ["incontext", "redirect"]:
            return self.py.get(f"[value='{launch}']").check(allow_selected=True)
        else:
            raise ValueError(f"Invalid launch_via. Must be 'incontext' or 'redirect'")

    def launch_veriff(self) -> "VeriffUI":
        self.py.get("button[type='submit']").click()
        return self

    def launch_veriff_with(
        self, full_name: str, language: str, country: str, document_type: str, launch_via: str
    ) -> "VeriffUI":
        self.enter_full_name(full_name)
        self.select_language(language)
        self.select_country(country)
        self.select_document_type(document_type)
        self.select_launch_via(launch_via)
        return self.launch_veriff()

    def find_QR_code(self, launch_via: str) -> Element:
        if launch_via.lower() == "incontext":
            self.py.switch_to.frame("veriffFrame")
        return self.py.contains("QR")
