import testudo

def test_get_deptartments():
    depts = testudo.get_departments()
    assert len(list(depts)) > 0

def test_courses():
    dept = {"id": "MUSC", "name": "Music"}
    courses = testudo.get_courses(dept, '201908')
    assert len(list(courses)) > 0

def test_get_sections():
    sections = testudo.get_sections('MUSC229K', '201908')
    assert len(sections) > 0
    s = sections[1]
    assert s['id'] == 'FC01'
    assert s['seats'] == 10
    assert s['open-seats'] == 8
    assert s['waitlist'] == 0
    assert s['days'] == 'Su'
    assert s['start'] == '7:00pm'
    assert s['end'] == '9:30pm'
    assert s['building'] == 'TBA'
    assert s['room'] == ''
    assert s['instructors'] == ['Ann Kennedy', 'Craig Potter', 'Andrea Brown']


