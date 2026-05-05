from phonebook import Contact, Phonebook
import pytest

@pytest.fixture
def pb():
    phonebook = Phonebook()
    return phonebook

def test_contact_str():
    contact = Contact("John", "1234567")
    assert str(contact) == "John: 1234567"

def test_phonebook_str(pb):
    pb.contacts = [Contact("John", "1234567")]
    assert str(pb) == "John: 1234567"

def test_phonebook_empty_str(pb):
    assert str(pb) == "No contacts found"

def test_add_contact(pb):
    pb.add(Contact("John", "1234567"))
    assert len(pb.contacts) == 1

def test_lookup_contact(pb):
    pb.contacts = [Contact("John", "1234567")]
    result = pb.lookup("john")
    assert result.name == "John"

def test_lookup_missing_contact(pb):
    result = pb.lookup("John")
    assert result == None

def test_delete_contact(pb):
    pb.contacts = [Contact("John", "1234567")]
    pb.delete("john")
    assert len(pb.contacts) == 0

def test_delete_missing_contact(pb):
    pb.delete("john")

def test_valid_name():
    assert Phonebook.valid_name("John O'Brien") == True

def test_invalid_name():
    assert Phonebook.valid_name("John O'Brien23") == False

def test_valid_number():
    assert Phonebook.valid_number("+1 234 567 8901") == True

def test_invalid_number():
    assert Phonebook.valid_number("+61") == False