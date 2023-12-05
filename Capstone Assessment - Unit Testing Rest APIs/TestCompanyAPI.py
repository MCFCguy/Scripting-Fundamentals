import AccessApi as mws
import pytest
import datetime

#base_url: str = "https://raw.githubusercontent.com/bclipp/"
base_url: str = "https://raw.githubusercontent.com/cengage-ide-content/"
billing_end_point: str = "APItesting/master/getBillingInfo.json"
customer_end_point: str = "APItesting/master/getCustomers.json"
site_end_point: str = "APItesting/master/getSites.json"

# TASK 2
#url_to_test = mws.AccessApi(base_url)

#billing_url = url_to_test.get_end_point(billing_end_point)
#customer_url = url_to_test.get_end_point(customer_end_point)
#site_url = url_to_test.get_end_point(site_end_point)

#billing_status_code = url_to_test.get_status_code(billing_end_point)




# billing
def test_billing_status_code(url:str, end_point:str):
    url_to_test = mws.AccessApi(url)
    status_code = url_to_test.get_status_code(end_point)
    assert status_code == 200

def test_billing_validate_schema():
    url_to_test = mws.AccessApi(base_url)
    billing_url = url_to_test.get_end_point(billing_end_point)
    correct_key_sequence = ['id','FirstName','LastName','city','state','Lang','SSN']
    correct_item_type_sequence = []
    for dictionary in billing_url:
        assert list(dictionary.keys()) == correct_key_sequence
        for i in dictionary.items():
            if i[0] == 'id':
                assert type(i[1]) is int
            else:
                assert type(i[1]) is str

def test_billing_validate_ssn():
    url_to_test = mws.AccessApi(base_url)
    billing_url = url_to_test.get_end_point(billing_end_point)
    for dictionary in billing_url:
        ssn_to_test = dictionary.get('SSN')
        ssn_numerical = "".join(ssn_to_test.split('-'))
        assert ssn_to_test.find('-') == 3
        assert ssn_to_test.rfind('-') == 6
        assert ssn_to_test.count('-') == 2
        assert ssn_numerical.isdecimal() == True
        assert len(ssn_numerical) == 9
    return True

def test_billing_validate_time(url:str, end_point:str):
    url_to_test = mws.AccessApi(url)
    elapsed_time = url_to_test.get_elapsed_time(end_point)
    assert elapsed_time < 1


# customers
def test_customers_status_code():
    url_to_test = mws.AccessApi(base_url)
    status_code = url_to_test.get_status_code(customer_end_point)
    assert status_code == 200

def test_customers_validate_schema():
    url_to_test = mws.AccessApi(base_url)
    customer_url = url_to_test.get_end_point(customer_end_point)
    correct_key_sequence = ['id','first_name','last_name','email','ip_address','address']
    correct_item_type_sequence = []
    for dictionary in customer_url:
        assert list(dictionary.keys()) == correct_key_sequence
        for i in dictionary.items():
            if i[0] == 'id':
                assert type(i[1]) is int
            else:
                assert type(i[1]) is str

def test_customers_validate_ssn():
    url_to_test = mws.AccessApi(base_url)
    customer_url = url_to_test.get_end_point(customer_end_point)
    for dictionary in customer_url:
        ip_to_test = dictionary.get('ip_address')
        ip_numerical = "".join(ip_to_test.split('.'))
        for piece in ip_numerical:
            assert piece.isdecimal() == True
            assert len(piece) <= 3 and len(piece) > 0
    return True

def test_customers_validate_time():
    url_to_test = mws.AccessApi(base_url)
    elapsed_time = url_to_test.get_elapsed_time(customer_end_point)
    assert elapsed_time < 1

# site
def test_site_status_code():
    url_to_test = mws.AccessApi(base_url)
    status_code = url_to_test.get_status_code(site_end_point)
    assert status_code == 200

def test_site_validate_schema():
    url_to_test = mws.AccessApi(base_url)
    site_url = url_to_test.get_end_point(site_end_point)
    correct_key_sequence = ['id','address','ThirdParty','admin']
    correct_item_type_sequence = []
    for dictionary in site_url:
        assert list(dictionary.keys()) == correct_key_sequence
        for i in dictionary.items():
            if i[0] == 'id':
                assert type(i[1]) is int
            else:
                assert type(i[1]) is str

def test_site_validate_ssn():
    url_to_test = mws.AccessApi(base_url)
    site_url = url_to_test.get_end_point(site_end_point)
    for dictionary in site_url:
        address_to_test = dictionary.get('address')
        address_numerical = address_to_test.split(' ')
        piece_count = 0
        for piece in address_numerical:
            if piece_count == 0:
                piece_count += 1
                assert piece.isdecimal() == True
            else:
                piece_count += 1
                assert piece.isalpha() == True 
    return True


def test_site_validate_time():
    url_to_test = mws.AccessApi(base_url)
    elapsed_time = url_to_test.get_elapsed_time(site_end_point)
    assert elapsed_time < 1

# tests
"""
test_billing_status_code(base_url, billing_end_point)
test_billing_validate_schema()
test_billing_validate_ssn()
test_billing_validate_time(base_url, billing_end_point)
"""
# task 3
@pytest.mark.parametrize('base_url', [base_url])
@pytest.mark.parametrize('end_point', [billing_end_point, customer_end_point, site_end_point])

def test_billing_status_code(base_url, end_point):
    url_to_test = mws.AccessApi(base_url)
    for point in end_point:
        status_code = url_to_test.get_status_code(end_point)
        assert status_code == 200

@pytest.mark.parametrize('base_url', [base_url])
@pytest.mark.parametrize('end_point',[billing_end_point,customer_end_point,site_end_point])

def test_billing_validate_time(base_url, end_point):
    url_to_test = mws.AccessApi(base_url)
    for point in end_point:
        elapsed_time = url_to_test.get_elapsed_time(end_point)
        assert elapsed_time < 1




