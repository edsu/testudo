import testudo

def test_get_deptartments():
    depts = testudo.get_departments()
    assert len(list(depts)) > 0

def test_courses():
    dept = {"id": "MUSC", "name": "Music"}
    courses = testudo.get_courses(dept, '202101')
    assert len(list(courses)) > 0

def test_get_sections():
    sections = testudo.get_sections('MUSC103', '202101')
    assert len(sections) == 3
    s = sections[0]
    assert s['id'] == '0101'
    assert s['seats'] == 14
    assert s['open-seats'] >= 0
    assert s['waitlist'] >= 0
    assert s['days'] == 'TuTh'
    assert s['start'] == '11:00am'
    assert s['end'] == '12:15pm'
    assert s['building'] == ''
    assert s['room'] == 'ONLINE'
    assert s['instructors'] == ['Aleksandra Velgosha']

