import pytest
from rest_framework.test import APIClient
from students.models import Student, Course
from model_bakery import baker

@pytest.fixture
def client():
    """Фикстура для API клиента"""
    return APIClient()

@pytest.fixture
def courses_factory():
    '''Фикстура курсов'''
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.fixture
def students_factory():
    '''Фикстура студентов'''
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory

@pytest.mark.django_db
def test_get_first_course(client, courses_factory):
    '''Проверка получения первого курса'''
    cours = courses_factory(_quantity=10)
    first_course = cours[0]
    response = client.get(f'/api/v1/courses/{first_course.id}/') 
      
    assert response.status_code == 200
    data = response.json() 
    assert data['name'] == first_course.name 


@pytest.mark.django_db
def test_list_course(client, courses_factory):
    '''Проверка получения списка курсов'''
    cours = courses_factory(_quantity=10)
    response = client.get(f'/api/v1/courses/') 
    
    assert response.status_code == 200
    data = response.json() 
    assert len(data) == len(cours)
    
    
@pytest.mark.django_db
def test_check_filter_list_course_id(client, courses_factory):
    '''1- проверка фильтрации списка курсов по id
       2- проверка фильтрации списка курсов по name'''
    cours = courses_factory(_quantity=10)
    target_course = cours[3]
    response_id = client.get('/api/v1/courses/', {'id': target_course.id})
    response_name = client.get('/api/v1/courses/', {'name': target_course.name})
    
    assert response_id.status_code == 200
    assert response_name.status_code == 200
    
    data = response_id.json() 
    data = response_name.json() 
    assert data[0]['id'] == target_course.id 
    assert data[0]['name'] == target_course.name 
    

@pytest.mark.django_db
def test_create_course(client):
    '''Тест успешного создания курса: через JSON-данные'''
    course = {'name': 'Нефтегазовое дело'}
    response = client.post('/api/v1/courses/', data=course,
    format='json')
    
    assert response.status_code == 201
    created_course = Course.objects.first()
    assert created_course.name == course['name']
    
@pytest.mark.django_db
def test_update_course(client, courses_factory):
    '''Тест успешного обновления курса:
    сначала через фабрику создаём, потом обновляем JSON-данными;'''
    course = courses_factory(name='Трубоукладчик')
    data_updata = {'name': 'Стропальщик'}
    response = client.patch(f'/api/v1/courses/{course.id}/', data= data_updata,
                            content_type='application/json')
    
    assert response.status_code == 200
    updated_course = Course.objects.get(id=course.id)
    assert updated_course.name == data_updata['name']
    
@pytest.mark.django_db
def test_deletion_course(client, courses_factory):
    '''Тест успешного удаления курса'''
    cours = courses_factory(_quantity=10)
    cours_delete = cours[2]
    
    response = client.delete(f'/api/v1/courses/{cours_delete.id}/')
    
    assert response.status_code == 204
    
    assert not Course.objects.filter(id=cours_delete.id).exists()
